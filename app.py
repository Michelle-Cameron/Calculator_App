from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def add(x, y):
    return round(x + y, 3)

def subtract(x, y):
    return round(x - y, 3)

def multiply(x, y):
    return round(x * y, 3)

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return round(x / y, 3)

@app.route('/')
def index():
    return render_template('calculator_ui.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']

    if operation == 'add':
        result = add(num1, num2)
    elif operation == 'subtract':
        result = subtract(num1, num2)
    elif operation == 'multiply':
        result = multiply(num1, num2)
    elif operation == 'divide':
        result = divide(num1, num2)
    else:
        result = "Invalid operation."

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
