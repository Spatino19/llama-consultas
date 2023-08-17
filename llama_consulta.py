from llama_index import SQLDatabase
from llama_index.response.schema import RESPONSE_TYPE
from llama_index.indices.struct_store.sql_query import NLSQLTableQueryEngine
from sqlalchemy import create_engine
from conteo_tokens import num_tokens_from_string
import openai
import os

def consulta(query_str: str, mostrar_tokens = False) -> RESPONSE_TYPE:
    openai.api_key = os.environ["OPENAI_API_KEY"]

    if mostrar_tokens: print("Tokens:", num_tokens_from_string(query_str))

    engine = create_engine(os.environ["DATABASE_URI"])
    sql_database = SQLDatabase(engine, include_tables=['shrimps_farm'])
    query_engine = NLSQLTableQueryEngine(sql_database=sql_database, tables=['shrimps_farm','shrimps_pond'],)

    return query_engine.query(query_str)

def main():
    texto = input("Ingresa pregunta para consulta:\n")
    response = consulta(texto, mostrar_tokens=True)
    print(response.metadata)
    print(response)
    

if __name__ == '__main__':
    main()
