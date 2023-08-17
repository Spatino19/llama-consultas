
from langchain.agents import AgentExecutor
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.agents import *
from langchain.llms import OpenAI
from langchain import OpenAI, SQLDatabase

import os
import openai
from custom_table_info import custom_table_info


class ChatGPTIntegration():
    _name = 'chatgpt.integration'
    _description = 'ChatGPT Integration'
    __api_key = os.environ["OPENAI_API_KEY"]
    
    TRAINING_OPTIONS = [('question', 'By Question'), ('file', 'By File')]

    # responses_questions = '' #respuesta
    # question_user = ''  #Pregunta Prueba
    # responses = '' #responses
    # responses_db = '' #Responses DB
    # question_querys = ''  #Pregunta Base de Datos
    responses_query = '' #Respuesta base de datos
    
    def __init__(self, question_querys) -> None:
        self.question_querys = question_querys
        self.generate_query()

    # @api.model
    # def _get_chat_integration(self):
    #     return ChatGPTIntegration(self.api_key)


    def process_message(self):
        # import pdb
        # pdb.set_trace()
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.question_user,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
            api_key=self.__api_key
        )
        self.responses_questions = response.choices[0].text.strip()

    # @api.multi
    def generate_query(self):

        db = SQLDatabase.from_uri(os.environ["DATABASE_URI"], include_tables=['biofeeder_production', 'shrimps_farm', 'shrimps_pond', 'route_production_line_pro'], custom_table_info=custom_table_info)
        
        llm = OpenAI(model_name="gpt-3.5-turbo",openai_api_key=self.__api_key)
        toolkit = SQLDatabaseToolkit(db=db, llm=llm)
        # agent = OpenAI(model_name="gpt-3.5-turbo")
        agent_executor = create_sql_agent(
            llm=OpenAI(temperature=0, openai_api_key=self.__api_key),
            toolkit=toolkit,
            verbose=True
        )
        # db_chain = SQLDatabaseChain.from_llm(llm, db,return_intermediate_steps=True)
        # result = db_chain(self.question_querys)
        result = agent_executor.run(self.question_querys)
        ""
        # steps = result.get("intermediate_steps")
        
        print(result)
        
def main():
    ChatGPTIntegration("") #Insertar pregunta query para q busque en base de datso
    
if __name__ == '__main__':
    main()
    
    