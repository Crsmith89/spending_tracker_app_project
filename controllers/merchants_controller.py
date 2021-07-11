from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import merchant_repository 
from models.merchant import Merchant

merchants_blueprint = Blueprint("merchants", __name__)

# get merchants
@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants = merchants)

    