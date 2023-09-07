from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def start():
    return "NeimanBot Started Successfully"

os.system("python3 -m TelethonNeiman")
app.run(port=5000)
