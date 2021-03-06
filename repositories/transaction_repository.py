from db.run_sql import run_sql
from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

# CRUD 

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, amount, date, tag_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.merchant.id, transaction.amount, transaction.date, transaction.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id 

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row["merchant_id"])
        tag = tag_repository.select(row["tag_id"])
        transaction = Transaction(merchant, row["amount"], row["date"], tag, row["id"])
        transactions.append(transaction)
    return transactions

def select(id):
    sql = "SELECT * FROM transactions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = merchant_repository.select(result["merchant_id"])
    tag = tag_repository.select(result["tag_id"])
    transaction = Transaction(merchant, result["amount"], result["date"], tag, result["id"])
    return transaction 

def delete_all():
    sql = "DELETE FROM transactions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM transactions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(transaction):
    sql = "UPDATE transactions SET (merchant_id, amount, date, tag_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [transaction.merchant.id, transaction.amount, transaction.date, transaction.tag.id, transaction.id]
    run_sql(sql, values)