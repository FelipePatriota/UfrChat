import openai  

openai.api_key = "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"

model_engine = "text-davinci-003"

while True:
    print (50*"-")
    prompt = input("Digite o texto: ")
    print('.')
    print('..')
    print('...')
    print('processando...')
    print(50*"-")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        temperature=0.9,
        max_tokens=1024

    )
    print (50*"-")
    response = completion.choices[0].text
    print(response)
    print (50*"-")
    print (50*"-")
    saida = input("Deseja continuar? (S/N): ")
    if saida == "N":
        break




