import os
import json
from flask import Blueprint, render_template
import requests

fwtracker_bp = Blueprint('fwtracker', __name__)

FACTION_IDS = [500001, 500004]
FACTION_NAMES = {
    500001: "Caldari State",
    500004: "Gallente Federation"
}

def classification_rank(classification):
    if classification == "Frontline":
        return 0
    elif classification == "Command Ops":
        return 1
    elif classification == "Rearguard":
        return 2
    else:
        return 3  # unknown or fallback




def load_stargate_map():
    try:
        file_path = os.path.join(os.path.dirname(__file__), '../data', 'fw_stargate_map.json')
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Stargate map file not found at {file_path}")
        return {}

@fwtracker_bp.route('/fwtracker')
def fwtracker():
    fw_systems_url = 'https://esi.evetech.net/latest/fw/systems/?datasource=tranquility'
    response = requests.get(fw_systems_url)
    if response.status_code != 200:
        return render_template('fwtracker.html', systems=[], error='Failed to fetch data from ESI API.')

    systems_data = response.json()

    filtered_systems = [
        system for system in systems_data
        if system.get('occupier_faction_id') in FACTION_IDS
    ]
    system_ids = [system['solar_system_id'] for system in filtered_systems]

    names_url = 'https://esi.evetech.net/latest/universe/names/'
    names_response = requests.post(names_url, json=system_ids)
    if names_response.status_code != 200:
        return render_template('fwtracker.html', systems=[], error='Failed to fetch system names.')

    names_data = names_response.json()
    id_to_name = {str(entry['id']): entry['name'] for entry in names_data}
    system_occupiers = {
        str(system['solar_system_id']): system['occupier_faction_id']
        for system in filtered_systems
    }

    stargate_map = load_stargate_map()

    # First pass to find frontline systems
    frontline_systems = set()
    for system in filtered_systems:
        system_id = str(system['solar_system_id'])
        occupier = system['occupier_faction_id']
        connected_ids = stargate_map.get(system_id, [])

        for conn_id in connected_ids:
            conn_id_str = str(conn_id)
            conn_occupier = system_occupiers.get(conn_id_str)
            if conn_occupier and conn_occupier != occupier:
                frontline_systems.add(system_id)
                break

    # Second pass to classify all systems
    systems = []
    for system in filtered_systems:
        system_id = str(system['solar_system_id'])
        occupier = system['occupier_faction_id']
        solar_system_name = id_to_name.get(system_id, 'Unknown')
        contested_percent = (system.get('victory_points', 0) / system.get('victory_points_threshold', 1)) * 100
        connected_ids = stargate_map.get(system_id, [])

        # Determine classification
        if system_id in frontline_systems:
            classification = "Frontline"
        else:
            connected_frontline_same = False
            connected_frontline_opposite = False
            connected_command_same = False

            for conn_id in connected_ids:
                conn_id_str = str(conn_id)
                conn_occupier = system_occupiers.get(conn_id_str)
                if not conn_occupier:
                    continue

                # Is connected to a frontline?
                if conn_id_str in frontline_systems:
                    if conn_occupier == occupier:
                        connected_frontline_same = True
                    else:
                        connected_frontline_opposite = True

            if connected_frontline_opposite:
                classification = "Unknown"  # Shouldn't happen, fallback
            elif connected_frontline_same:
                classification = "Command Ops"
            else:
                # Check for connection to command ops of same faction
                for conn_id in connected_ids:
                    conn_id_str = str(conn_id)
                    conn_occupier = system_occupiers.get(conn_id_str)
                    if not conn_occupier:
                        continue

                    if conn_id_str not in frontline_systems:
                        # Check if this system is a command ops
                        for inner_id in stargate_map.get(conn_id_str, []):
                            inner_id_str = str(inner_id)
                            if inner_id_str in frontline_systems and system_occupiers.get(inner_id_str) == conn_occupier:
                                if conn_occupier == occupier:
                                    connected_command_same = True

                if connected_command_same:
                    classification = "Rearguard"
                else:
                    classification = "Rearguard"

        systems.append({
            'solar_system_name': solar_system_name,
            'contested_percent': round(contested_percent, 2),
            'occupier_faction': FACTION_NAMES.get(occupier, 'Unknown'),
            'classification': classification
        })

        systems.sort(key=lambda x: classification_rank(x['classification']))

    return render_template('fwtracker.html', systems=systems)
