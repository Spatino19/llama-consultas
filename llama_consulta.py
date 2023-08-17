from llama_index import SQLDatabase
from llama_index.indices.struct_store.sql_query import NLSQLTableQueryEngine
import openai
import os

from sqlalchemy import create_engine

openai.api_key = os.environ["OPENAI_API_KEY"]

engine = create_engine(os.environ["DATABASE_URI"])

sql_database = SQLDatabase(engine, include_tables=['shrimps_farm'])

query_engine = NLSQLTableQueryEngine(sql_database=sql_database, tables=['shrimps_farm','shrimps_pond'],)
query_str = "Cual es el tamaño de la piscina P01 de la camaronera Biosuper"
response = query_engine.query(query_str)

print(response.metadata)

print(response)
