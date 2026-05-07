from flask import Flask, render_template
import requests


from config import (
    COMMON_SERVICES,
    PASSWORD_RESET,
    LAB_ENVIRONMENTS,
    PROD_ENVIRONMENTS
)

app = Flask(__name__)

for env in LAB_ENVIRONMENTS:
    env["services"].sort(key=lambda x: x["name"])

for env in PROD_ENVIRONMENTS:
    env["services"].sort(key=lambda x: x["name"])


COMMON_ENVIRONMENTS = [
    {"name": "Common Services", "services": COMMON_SERVICES},
    {"name": "Password Reset", "services": PASSWORD_RESET},
]


@app.route('/')
def home():
    return render_template('dashboard.html', env_type='Common', environments=COMMON_ENVIRONMENTS)

@app.route('/lab')
def lab():
    return render_template('dashboard.html', env_type='LAB', environments=LAB_ENVIRONMENTS)

@app.route('/prod')
def prod():
    return render_template('dashboard.html', env_type='PROD', environments=PROD_ENVIRONMENTS)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
