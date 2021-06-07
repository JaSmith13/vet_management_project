from db.run_sql import run_sql
from models.owner import Owner

#Read all
def select_all():
    owners = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['contact_number'], row['address'], row['email'], row['id'])
        ownerds.append(owner)
    return owners

#Read one
def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        owner = Owner(row['first_name'], row['last_name'], row['contact_number'], row['address'], row['email'], row['id'])
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

#Update