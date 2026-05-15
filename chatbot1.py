import re

def responde(entrada):

    # procura palavras como ola, oi ou olá
    if re.search(r'\b(ola|oi|olá)\b', entrada):
        return 'Olá, como posso ajudar?'

    # procura palavras relacionadas à comida
    elif re.search(r'\b(comida|fome)\b', entrada):
        return 'Você está com fome? 🍔'

    else:
        return 'Desculpa, não entendi sua pergunta'


print("Bem-vindo ao chatbot! Digite 'sair' para encerrar")


while True:
    user_input = input('Você: ').lower()

    if user_input == 'sair':
        print('Chatbot: Até mais!')
        break

    resposta = responde(user_input)

    print(f'Chatbot: {resposta}')