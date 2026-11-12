from llama import ask

def main():
    while True:
        prompt = input("me: ")
        if prompt == ("exit"):
            break

        result = ask(prompt)
        print("wife:",result)

main()
