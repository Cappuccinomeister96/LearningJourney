from langchain_openai import ChatOpenAI

def main():
    # 1) LLM-Objekt erstellen (ChatGPT)
    llm = ChatOpenAI(model="gpt-5")  # oder ein anderes verfügbares Modell

    # 2) Einen einfachen Prompt senden
    response = llm.invoke("Sag in einem Satz, was du bist.")

    # 3) Antwort ausgeben
    print(response)

if __name__ == "__main__":
    main()
