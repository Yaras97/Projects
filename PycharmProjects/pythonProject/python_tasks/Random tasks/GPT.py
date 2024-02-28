import g4f

def gpt_requests(messages: str) -> str:
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )
    for message in response:
        print(message, flush=True, end='')
    return response


messages = []
while True:
    messages.append({'role': 'user', 'content': input()})
    messages.append({'role': 'assistant', 'content': gpt_requests(messages=messages)})