from db.run_sql import run_sql
from models.merchant import Merchant
from models.transaction import Transaction

# CRUD functions

def save(merchant):
    sql = "INSERT INTO merchants (name, location) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, merchant.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    merchant.id = id
    return merchant 

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row["name"], row["location"], row["id"])
        merchants.append(merchant)
    return merchants

def select(id):
    sql = "SELECT * FROM merchants WHERE ID = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    merchant = Merchant(result["name"], result["location"])
    return merchant

def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM merchants WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(merchant):
    sql = "UPDATE merchants SET (name, location) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.location, merchant.id]
    run_sql(sql, values)


