from flask import Flask, render_template, request, jsonify
import requests
import locale

app = Flask(__name__)

# Set the locale to use commas as the thousands separator
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# System ID's
JITA_SYSTEM_ID = 30000142

# Mineral IDs
Tritanium = 34
Pyerite = 35
Mexallon = 36
Isogen = 37
Nocxium = 38
Zydrine = 39
Megacyte = 40
# Pyroxeres = 1224

# Component ID's
AutoIntegrityPreservationSeal = 57478
LifeSupportBackupUnit = 57486
DreadGuristasCrystalTag = 17244
CaldariCU1NexusChip = 17646


# Ship Blueprints
SHIP_BLUEPRINTS = {
    "Caracal Navy Issue (ISK)": {
        "materials": {Tritanium: 540_000,
                      Pyerite: 180_000, 
                      Mexallon: 36_000,
                      Isogen: 10_000,
                      Nocxium: 1_500,
                      Zydrine: 1_000,
                      Megacyte: 500,
                      AutoIntegrityPreservationSeal: 50,
                      LifeSupportBackupUnit: 25},
        "flat_isk_cost": 5_000_000,
        "lp_cost": 18_000,
        "manufacturing_cost": 1_800_000,
    },
    "Caracal Navy Issue (Tags)": {
        "materials": {Tritanium: 540_000,
                      Pyerite: 180_000, 
                      Mexallon: 36_000,
                      Isogen: 10_000,
                      Nocxium: 1_500,
                      Zydrine: 1_000,
                      Megacyte: 500,
                      DreadGuristasCrystalTag: 1,
                      AutoIntegrityPreservationSeal: 50,
                      LifeSupportBackupUnit: 25},
        "flat_isk_cost": 0,
        "lp_cost": 18_000,
        "manufacturing_cost": 1_800_000,
    },
    "Caracal Navy Issue (Chips)": {
        "materials": {Tritanium: 540_000,
                      Pyerite: 180_000, 
                      Mexallon: 36_000,
                      Isogen: 10_000,
                      Nocxium: 1_500,
                      Zydrine: 1_000,
                      Megacyte: 500,
                      CaldariCU1NexusChip: 4,
                      AutoIntegrityPreservationSeal: 50,
                      LifeSupportBackupUnit: 25},
        "flat_isk_cost": 0,
        "lp_cost": 18_000,
        "manufacturing_cost": 1_800_000,
    },
}

def get_market_price(type_id):
    """Fetches the lowest Jita market price for a material."""
    url = f'https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id={type_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        orders = response.json()

        # Find the cheapest price in Jita
        jita_orders = [order for order in orders if order['system_id'] == JITA_SYSTEM_ID]
        return min((order['price'] for order in jita_orders), default=None)

    except requests.exceptions.RequestException:
        return None  # If API fails, return None

def calculate_total_cost(ship_name, lp_to_isk_ratio):
    """Calculates total cost for a ship, including materials and fixed costs."""
    ship = SHIP_BLUEPRINTS.get(ship_name)
    if not ship:
        return None, "Invalid ship name"

    total_cost = ship["flat_isk_cost"] + ship["lp_cost"] * lp_to_isk_ratio + ship["manufacturing_cost"]
    materials_cost = {}

    for type_id, quantity in ship["materials"].items():
        price_per_unit = get_market_price(type_id)
        if price_per_unit is None:
            return None, f"Failed to get price for material {type_id}"

        total_price = price_per_unit * quantity
        materials_cost[type_id] = {"price_per_unit": price_per_unit, "quantity": quantity, "total_price": total_price}
        total_cost += total_price

    return {
        "ship_name": ship_name,
        "materials": materials_cost,
        "flat_isk_cost": ship["flat_isk_cost"],
        "lp_cost": ship["lp_cost"],
        "manufacturing_cost": ship["manufacturing_cost"],
        "total_cost": total_cost,
        "lp_to_isk_ratio": lp_to_isk_ratio  # Add LP conversion ratio to data
    }, None

# Define a custom filter to format numbers with commas and decimals
@app.template_filter('format_number')
def format_number(value, decimals=2):
    try:
        return f"{value:,.{decimals}f}"  # This adds commas and formats the number with given decimals
    except ValueError:
        return value  # If the value isn't a number, return it as-is

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the user-defined LP to ISK ratio from the form
        lp_to_isk_ratio = float(request.form.get("lp_to_isk_ratio", 1000))
        ship_name = request.form.get("ship", "Gila")  # Default to Gila
        
        # Calculate the total cost using the user-defined LP to ISK ratio
        cost_data, error = calculate_total_cost(ship_name, lp_to_isk_ratio)
        if error:
            return jsonify({'error': error}), 400
        
        return render_template("result.html", **cost_data)
    
    return render_template("index.html", ships=SHIP_BLUEPRINTS)

if __name__ == "__main__":
    app.run(debug=False)
