"""Fee Calculator API"""

from flask import Flask, jsonify

from feecalculator import FeeCalculator, LoanApplication

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Hello world handler"""
    return "/fee/12/1500 > 70"


@app.route("/fee/<term>/<loan>")
def fee_calculator(term, loan) -> dict:
    """fee calculator handler"""
    term, loan = int(term), int(loan)
    application = LoanApplication(term, loan)
    calculator = FeeCalculator(application)
    fee = calculator.calculate()
    output = {"fee": fee, "loan": loan, "term": term}
    return jsonify(output)
