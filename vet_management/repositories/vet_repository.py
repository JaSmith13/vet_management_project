from db.run_sql import run_sql
from models.vet import Vet

#Read all
def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['qualifications'], row['contact_number'], row['id'])
        vets.append(vet)
    return vets

#Read one
def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        vet = Vet(result['first_name'], result['last_name'], result['qualifications'], result['contact_number'], result['id'])
    return vet

#Delete all
def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

#Delete one
def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#Create
def save(vet):
    sql = "INSERT INTO vets (first_name, last_name, qualifications, contact_number) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [vet.first_name, vet.last_name, vet.qualifications, vet.contact_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id

#Update
# def update(vet):