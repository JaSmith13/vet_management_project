from db.run_sql import run_sql
from models.vet import Vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['qualifications'], row['contact_number'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        vet = Vet(result['first_name'], result['last_name'], result['qualifications'], result['contact_number'], result['id'])
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)