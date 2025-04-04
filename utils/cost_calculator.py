# cost_calculator.py

from utils.market_api import get_market_price
from config import SHIP_BLUEPRINTS,TYPE_NAMES
from utils.filters import get_type_name

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
            materials_cost[type_id] = {
                "price_per_unit": None,
                "quantity": quantity,
                "total_price": None
            }
            continue  # Skip adding to total cost

        total_price = price_per_unit * quantity
        materials_cost[type_id] = {
            "price_per_unit": price_per_unit,
            "quantity": quantity,
            "total_price": total_price
        }
        total_cost += total_price

    return {
        "ship_name": ship_name,
        "materials": materials_cost,
        "flat_isk_cost": ship["flat_isk_cost"],
        "lp_cost": ship["lp_cost"],
        "manufacturing_cost": ship["manufacturing_cost"],
        "total_cost": total_cost,
        "lp_to_isk_ratio": lp_to_isk_ratio
    }, None
