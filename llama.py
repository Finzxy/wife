import requests

llama = "http://localhost:12828/v1/chat/completions" #change ts to your llama-server port. default is 12828 cuz its peak
def ask(text):
    payload={
        "messages": [
            {"role": "system", "content": "you are fin wife"} #you can change ts to give name or make personality (nvm its just example :v)
            {"role": "user", "content": text}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }
    try:
        response=requests.post(
            llama,
            json=payload
        )
        response.raise_for_status()

        data=response.json()
        result=data["choices"][0]["message"]["content"]
        return result

#just for debugging not important things
    except requests.RequestException as e:
        return f"{e}"
    except (KeyError, IndexError, ValueError) as e:
        return f"{e}"
