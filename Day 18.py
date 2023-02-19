from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/hello2")
def hello_world2():
    return "<h2>Hello, World! Heading 2</h2>"

@app.route("/hello3")
def hello_world3():
    return "<h3>Hello, World! Heading 3</h3>" 

@app.route("/test")
def test_function():
    a = 4.5*6.3
    return f"This is my test function, Output = {round(a,2)}"   

@app.route('/input_url')
def request_input():
    data = request.args.get('x')
    return f"This is my input data {data}"

@app.route('/square_url')
def square():
    num = request.args.get('i')
    num = float(num)
    return f"Square of given number {num} is : {round(num**2,4)}"

if __name__=="__main__":
    app.run(host="0.0.0.0")
