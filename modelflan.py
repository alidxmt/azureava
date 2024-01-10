from langchain.llms import HuggingFacePipeline
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM
# from langchain import LLMChain
from langchain.chains import LLMChain

from langchain.prompts import prompt,PromptTemplate

import asyncio
import websockets

import numpy as np
import pandas as pd 

df = pd.read_csv('first_interview.csv') 
questions = df['question']

model_id = 'google/flan-t5-large'
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,max_length = 100
)

local_llm = HuggingFacePipeline(pipeline=pipe)
print(local_llm('what is the capital of Iran?'))


async def calculate(websocket, path):
    async for message in websocket:
        try:
            is_in_que = 'no'
            result = ''
            for a_question in questions:
                print('process:',is_in_que)
                check_sim_messages = f"are these two expressions similar: ({message}) and ({a_question})."
                is_in_que = local_llm(check_sim_messages)
                if is_in_que=='yes':
                    print('is it',(is_in_que=='yes'))
                    result = list(df[df['question']==a_question]['answer'])[0]
                    break
            
            print('after loop, is it',(is_in_que=='yes'))

            if is_in_que != 'yes':
                result = local_llm(message)
            print('done:',is_in_que)
            
            # result = local_llm(message)

            await websocket.send(str(result))
        except ValueError:
            await websocket.send("Invalid input. Please enter a valid number.")

start_server = websockets.serve(calculate, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
