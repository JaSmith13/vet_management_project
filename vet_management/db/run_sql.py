import psycopg2
import psycopg2.extras

def run_sql(sql, values = None):
    results = []
    connection = None
    try:
        connection = psycopg2.connect("dbname = 'vet_manager'")
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(sql, values)
        connection.commit()
        results = cursor.fetchall()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
    return results