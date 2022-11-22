contador = 1

#Exibir de 1 até 10 repetidamente
while(contador <= 10):
  print(contador)
  contador = contador+1 #contador += 1

#Laço for (Python for = for each)
fruta = "morango"
print(fruta)

#Lista
frutas = ["morango", "abacaxi", "manga"]
#Mostra todas
print(frutas)
#Quero exibir apenas a 3a. fruta, não esquecer que o Python começa do número 0
print(frutas[2])

#Exibir quantas frutas tem na minha lista
print(len(frutas))  #lenght = tamanho

#Quero incluir uma fruta nova
frutas.append("laranja")

print(len(frutas)) 
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("Exemplo das frutas com 'while'... ")

frutas.append("uva")

i=0 #(i de index)
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1