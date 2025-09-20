import asyncio
from aiohttp import ClientSession
import uuid
from dotenv import load_dotenv 
import os

load_dotenv()

MAIN_PROMPT = """
Ты крутой решатель задач по программированию. Я тебе отправляю задачу, а ты в ответ должен мне прислать код ее решения и
ничего больше. Вот условие задачи:

"""

async def get_authorization_token(session: ClientSession):
    url = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
    token = os.getenv('GIGACHAT_AUTHORIZATION_KEY') 
    if token == None:
        print("Authorization token not found")
        return
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': str(uuid.uuid4()),
        'Authorization': 'Basic ' + token
    }

    params = {'scope': 'GIGACHAT_API_PERS'}

    async with session.post(url, headers=headers, data=params, ssl=False) as response:
        if response.status == 200:
            data = await response.json()
            return data.get('access_token')
        else:
            print("Failed to retrieve access token")
            return None

async def ask_llm(session: ClientSession, token: str, prompt: str) -> str | None:
    url = 'https://gigachat.devices.sberbank.ru/api/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    data = {
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": MAIN_PROMPT + prompt
            }
        ],
        "stream": False,
        "repetition_penalty": 1
    }

    async with session.post(url, headers=headers, json=data, ssl=False) as response:
        if response.status == 200:
            responseModel = await response.json()
            try:
                return responseModel["choices"][0]["message"]["content"]
            except (KeyError, IndexError, TypeError):
                print("Malformed response from LLM API:", responseModel)
                return None
        else:
            print("Failed to get response from LLM")

async def main():
    async with ClientSession() as session:
        token = await get_authorization_token(session)
        if token:
            print("Authorization token retrieved successfully")
        else:
            print("Failed to retrieve authorization token")
            return

        while True:
            prompt = input("You: ")
            if prompt.lower() == "exit":
                break
            response = await ask_llm(session, token, prompt)
            if response:
                print("LLM:", response)
            else:
                print("Failed to get response from LLM")

asyncio.run(main())