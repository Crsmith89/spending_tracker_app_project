from controllers.transactions_controller import transactions
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

# Get merchants new 
@merchants_blueprint.route("/merchants/new")
def merchant():
    return render_template("merchants/new.html")  

# Create - POST
@merchants_blueprint.route("/merchants", methods=["POST"])
def create_merchant():
    name = request.form["name"]
    location = request.form["location"]
    new_merchant = Merchant(name, location)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")

# show - get
@merchants_blueprint.route("/merchants/<id>", methods=['GET'])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    transactions = merchant_repository.transactions(id)
    return render_template("merchants/show.html", merchant = merchant, transactions = transactions)


# edit
@merchants_blueprint.route("/merchants/<id>/edit", methods=['GET'])
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant=merchant)

# update
@merchants_blueprint.route("/merchants/<id>", methods=["POST"])
def update_merchant(id):
    name = request.form["name"]
    location = request.form["location"]
    merchant = Merchant(name, location, id)
    merchant_repository.update(merchant)
    return redirect("/merchants")

# delete
@merchants_blueprint.route("/merchants/<id>/delete", methods=['POST'])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")