import psycopg
import db_configs

# Connect to an existing database
with psycopg.connect(
    dbname=db_configs.tide_db_name, 
    user=db_configs.tide_db_user, 
    password=db_configs.tide_db_password) as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM nations")
        cur.fetchone()
        # will return (1, 100, "abc'def")

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        for record in cur:
            print(record)

        # Make the changes to the database persistent
        conn.commit()