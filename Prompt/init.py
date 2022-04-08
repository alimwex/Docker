import requests
from flask import Flask, request, jsonify, render_template
from Variables import *
from AccountService import *
from update_account_status import *
#from activate_template_account import *
#from update_parent_account import *

app = Flask(__name__)

@app.route("/healthz")
def healthz():
  return "Account Python Service is up and running."

@app.route("/")
def hello_world():
  return "Hello! The account service container is up and running."

@app.route("/update_account_status", methods=['POST'])
def app_udpate_account_status():
    return update_account_status()

# @app.route("/activate_template_account", methods=['POST'])
# def app_activate_template_account():
#     return activate_template_account()

# @app.route("/update_parent_account", methods=['POST'])
# def app_update_parent_account():
#     return update_parent_account()

# @app.route("/Create_Account", methods=['POST'])
# def app_Create_Account():
#     return Create_Account()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

# @app.route("/url")
# def sblurl():
#   return SBL_PWD
# @app.route("/update_account", methods=['POST'])
# def app_update_account():
#     return update_account()
