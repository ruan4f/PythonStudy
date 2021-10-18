#!/usr/bin/python
import psycopg2
from config import config

def query(queryString):
    """ Connect to the PostgreSQL database server """
    results = None
    connection = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(**params)
		
        # create a curso
        cursor = connection.cursor()
        
	# execute a statement
        cursor.execute(queryString)
        connection.commit()
        results = cursor.fetchall()
    
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection closed.')

    return results

if __name__ == '__main__':
    query()