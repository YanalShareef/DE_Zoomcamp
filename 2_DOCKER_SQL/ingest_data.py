import os 
import pandas as pd
import pyarrow.parquet as pq
from sqlalchemy import create_engine
import numpy as np
from time import time
import argparse

def main(args):
    
    user = args.user
    password = args.password
    host = args.host 
    port =  args.port 
    databasename = args.databasename
    tablename = args.tablename
    fileurl = args.fileurl
    filename = "output.parquet"

    # download the csv file 
    os.system(f"wget {fileurl} -O {filename}")

    # Read Parquet file into Pandas DataFrame
    trips = pq.read_table(filename)
    data = trips.to_pandas()

    # Create a PostgreSQL engine using the provided arguments
    engine_url = f"postgresql://{user}:{password}@{host}:{port}/{databasename}"
    engine = create_engine(engine_url)

    # Split the DataFrame into 100 chunks
    dfs = np.array_split(data, 100)

    # Create an empty table in the database for the first chunk (replace if exists)
    dfs[0].head(0).to_sql(name=tablename, con=engine, if_exists="replace")

    # Insert each chunk into the database with append mode
    for df in dfs:
        t_start = time()
        df.to_sql(name=tablename, con=engine, if_exists="append")
        t_end = time()
        print("Inserted another chunk..., took %.3f seconds" % (t_end - t_start))

if __name__ == "__main__":
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Ingest parquet file to postgres')

    # Add the desired command line arguments
    parser.add_argument('--user', type=str, help='Postgres user')
    parser.add_argument('--password', type=str, help='Postgres password')
    parser.add_argument('--host', type=str, help='Postgres host')
    parser.add_argument('--port', type=int, help='Postgres port')
    parser.add_argument('--databasename', type=str, help='Postgres database name')
    parser.add_argument('--tablename', type=str, help='Postgres table name')
    parser.add_argument('--fileurl', type=str, help='URL of the Parquet file')

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the main function with the parsed arguments
    main(args)
