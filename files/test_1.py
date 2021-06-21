# article refered https://www.postgresqltutorial.com/postgresql-python/connect/     https://www.postgresqltutorial.com/postgresql-python/

import psycopg2
from config import config
from main_prog import main_program



# conn = psycopg2.connect(
#     host="localhost",
#     database="testdummy",
#     user="sam",
#     password="sam123")

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()       # read connection parameters

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()     # create a cursor
        ################################################################################################################
        #       EVERY CODE COMES HERE       #

        main_program(cur)

        #       EVERY CODE ENDS HERE        #
        ################################################################################################################

        conn.commit()  # commit the changes for database
        cur.close()     # close the communication with the PostgreSQL

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
