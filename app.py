from llama import ask
from kitten import speaking
import subprocess

def main():
    while True:
        prompt = input("me: ")
        if prompt == ("exit"):
            break

        result = ask(prompt)
        print("wife:",result)

        speaking(result)
        subprocess.run(["pw-play", "output.mp3"], check=True)
main()
