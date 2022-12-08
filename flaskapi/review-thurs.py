#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   A simple Flask server to upload and download files"""

# python3 -m pip install flask
from flask import Flask
from flask import redirect

#from flask import request



app = Flask(__name__)

x= "Slappy"

@app.route("/example1/<y>")
def example1(y):
    return f"Hello {y}!"

@app.route("/example2")
def example2():
    return redirect("/example1/Happy")

@app.route("/example3")
def example3():
    print("Hello, world!")
    return "World, hello!"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

