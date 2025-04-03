# lpcalculator.py (Inside a "blueprints" folder)

from flask import Blueprint, render_template, request, jsonify
from utils.cost_calculator import calculate_total_cost
from config import SHIP_BLUEPRINTS

lpcalculator_bp = Blueprint('lpcalculator', __name__)

@lpcalculator_bp.route("/", methods=["GET", "POST"])
def lpCalc():
    if request.method == "POST":
        # Get the user-defined LP to ISK ratio from the form
        lp_to_isk_ratio = float(request.form.get("lp_to_isk_ratio", 1000))
        ship_name = request.form.get("ship", "Gila")  # Default to Gila
        
        # Calculate the total cost using the user-defined LP to ISK ratio
        cost_data, error = calculate_total_cost(ship_name, lp_to_isk_ratio)
        if error:
            return jsonify({'error': error}), 400
        
        return render_template("result.html", **cost_data)
    
    return render_template("lpcalculator.html", ships=SHIP_BLUEPRINTS)
