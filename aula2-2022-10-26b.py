#Pede o nome do aluno e sua nota (de 0 a 10) e se ele tirou nota 10, mostra "{nome}, você é top demais..."

nome = input("Informe seu nome: ")
nota = float(input("Digite sua nota: "))

if (nota == 10):
  print(f"{nome}, você é top demais!")
elif ("nota >= 6 and < 10"):
  print(f"{nome}, bom trabalho, mas não foi o suficiente.")
  
else: #é sempre automaticamente o que as duas condições acima não trabalham
  print("Buh, tente novamente!")