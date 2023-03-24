import openai
import pandas as pd
from transformers import pipeline

# Defina suas credenciais da OpenAI API
openai.api_key = "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"

# Carregue seu arquivo CSV em um DataFrame do pandas
df = pd.read_csv("Data.csv")

# Carregue o modelo de linguagem da Hugging Face para responder perguntas
model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Defina uma função que recebe uma pergunta como entrada e retorna a resposta correspondente
def responder_pergunta():
    while True:
        # Solicite que o usuário digite uma pergunta
        pergunta = input("Digite sua pergunta (ou digite 'sair' para sair): ")
        # Verifique se o usuário quer sair
        if pergunta.lower() == "sair":
            print("Até a próxima!")
            break
        # Use o modelo de linguagem para responder à pergunta
        resposta = model(question=pergunta, context=df["Texto"].to_list(), max_answer_length=500)["answer"]
        # Encontre o link correspondente na coluna "links" do DataFrame
        link = df.loc[df['Texto'] == resposta, 'links'].values[0]
        # Imprima a resposta e o link correspondente
        print("Resposta: ", resposta)
        print("Link: ", link)
