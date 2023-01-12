from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def calculator():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = float(request.form["num1"])
    operator = request.form["operator"]
    num2 = float(request.form["num2"])

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "Invalid operator."
    
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
