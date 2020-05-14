import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """Run the copy table quries in the sql_quries.py"""
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """Run the insert table quries functions in the sql_quries.py"""
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Copy staging tables to DWH and insert values to new tables"""
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    
    # Connect to dwh
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    # Load/Copy staging tables
    load_staging_tables(cur, conn)
    print ("finish loading staging tables")
    # Insert the new tables
    insert_tables(cur, conn)
    print ('finish inserting tables')

    conn.close()


if __name__ == "__main__":
    main()