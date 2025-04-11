
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h2>Simple Calculator</h2>
    <form method="post" action="/calculate">
      <input name="a" placeholder="First number">
      <input name="b" placeholder="Second number">
      <select name="operation">
        <option value="add">+</option>
        <option value="subtract">-</option>
        <option value="multiply">*</option>
        <option value="divide">/</option>
      </select>
      <button type="submit">Calculate</button>
    </form>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        a = float(request.form['a'])
        b = float(request.form['b'])
        op = request.form['operation']

        if op == 'add':
            result = a + b
        elif op == 'subtract':
            result = a - b
        elif op == 'multiply':
            result = a * b
        elif op == 'divide':
            result = a / b
        else:
            return "Invalid operation"

        return f"<h2>Result: {result}</h2><a href='/'>Back</a>"
    except Exception as e:
        return f"<h2>Error: {e}</h2><a href='/'>Back</a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
