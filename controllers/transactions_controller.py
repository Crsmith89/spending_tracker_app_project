from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.transaction import Transaction

import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository


transactions_blueprint = Blueprint("transactions", __name__)

# get transactions
@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions = transactions)

# New transactions
@transactions_blueprint.route("/transactions/new")
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants = merchants, tags = tags)

# create - Post
@transactions_blueprint.route("/transactions", methods=["POST"])
def create_transaction():
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    amount = int(request.form["amount"])
    date = request.form["date"]
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    new_transaction = Transaction(merchant, amount, date, tag)
    transaction_repository.save(new_transaction)
    return redirect("/transactions")

# show - get
@transactions_blueprint.route("/transactions/<id>")
def show_transaction(id):
    transaction = transaction_repository.select(id)
    return render_template("transactions/show.html", transaction = transaction)

# edit
@transactions_blueprint.route("/transactions/<id>/edit")
def edit_transaction(id):
    transaction = transaction_repository.select(id)
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/edit.html", transaction = transaction, merchants = merchants, tags = tags)

# update
@transactions_blueprint.route("/transactions/<id>", methods=["POST"])
def update_transaction(id):
    merchant_id = request.form["merchant_id"]
    merchant = merchant_repository.select(merchant_id)
    amount = request.form["amount"]
    date = request.form["date"]
    tag_id = request.form["tag_id"]
    tag = tag_repository.select(tag_id)
    transaction = Transaction(merchant, amount, date, tag, id)
    transaction_repository.update(transaction)
    return redirect("/transactions")

# delete
@transactions_blueprint.route("/transactions/<id>/delete", methods=["POST"])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect("/tranactions")