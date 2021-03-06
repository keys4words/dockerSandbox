import os


DEV_DB = 'sqlite:///market.sqlite'

pg_user = os.environ.get("POSTGRES_USER")
pg_pass = os.environ.get("POSTGRES_PASSWORD")
pg_db = os.environ.get("POSTGRES_DB")
pg_host = 'db'
pg_port = 5432

PROD_DB = f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'