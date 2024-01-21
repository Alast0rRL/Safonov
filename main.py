import openai
from config import config
import os
#from api import answer

openai.api_key = config['api_key']

#if config['proxy'] != '':
#  os.environ['http_proxy'] = 'http://' + config['proxy']
#  os.environ['https_proxy'] = 'http://' + config['proxy']


def answer(history):
    response = openai.ChatCompletion.create(
        model=config.get('model', 'gpt-3.5-turbo'),  # используйте значение по умолчанию, если ключ 'model' отсутствует
        messages=history,
        temperature=config.get('temperature', 0.7),  # используйте значение по умолчанию, если ключ 'temperature' отсутствует
    )

    return response['choices'][0]['message']['content']



history = [
    {"content": "You're a helpful assistant", "role": "system"}
]

while True:
    prompt = input('>>> ')
    history.append({"content": prompt, "role": "user"})
    chat_answer = ""  # Предварительное определение переменной
    try:
        chat_answer = answer(history)
        print(chat_answer)
    except openai.error.AuthenticationError as e:
        print(f"Authentication Error: {e}")
        # Дополнительные действия, например, запрос нового ключа или прекращение выполнения программы
    except Exception as e:
        print(f"Error during OpenAI request: {e}")
        history.pop(1)
        history.pop(1)
        chat_answer = answer(history)
    history.append({"content": chat_answer, "role": "assistant"})