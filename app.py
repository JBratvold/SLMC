from flask import Flask, render_template
from config import TYPE_NAMES
from blueprints.lpcalculator import lpcalculator_bp
from utils.filters import get_type_name, format_number

app = Flask(__name__)
app.register_blueprint(lpcalculator_bp, url_prefix="/lpcalculator")

@app.template_filter('get_type_name')
def get_type_name_filter(type_id):
    return get_type_name(type_id, TYPE_NAMES)

@app.template_filter('format_number')
def format_number_filter(value, decimals=2):
    return format_number(value, decimals)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/yieldcalculator')
def yieldCalc():
    return render_template('yieldcalculator.html')

if __name__ == '__main__':
    app.run(debug=True)
