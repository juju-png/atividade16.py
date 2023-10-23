# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.

idoso,gestante,cadeirante=str(input("você é idoso? sim ou não.")),str(input("você é gestante? sim ou não.")),str(input("você é cadeirante? sim ou não."))
if idoso=="sim" or gestante=="sim" or cadeirante=="sim":
    print("fila preferencial")
else: 
    print("não preferencial")