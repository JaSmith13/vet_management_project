from db.run_sql import run_sql
from models.owner import Owner

#Read all
def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['contact_number'], row['address'], row['email'], row['id'])
        owners.append(owner)
    return owners

#Read one
def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        owner = Owner(result['first_name'], result['last_name'], result['contact_number'], result['address'], result['email'], result['id'])
    return owner

#Delete all
def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

#Delete one
def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#Create
def save(owner):
    sql = "INSERT INTO owners (first_name, last_name, contact_number, address, email) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [owner.first_name, owner.last_name, owner.contact_number, owner.address, owner.email]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id

#Update
def update(owner):
    sql = "UPDATE owners SET (first_name, last_name, contact_number, address, email) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [owner.first_name, owner.last_name, owner.contact_number, owner.address, owner.email, owner.id]
    run_sql(sql, values)
