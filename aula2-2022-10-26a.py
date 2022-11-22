# comando input(): quero permitir que o usuário digite algo...

nome = input("Digite seu nome: ")
# pede a idade do usuário "Qual a sua idade"
idade = int(input("Digite sua idade: "))

# comando de saida... exibir na tela
print(f"Boa noite, seu nome é {nome}")
# exiba "Sua idade é..."
print("Sua idade é {}".format(idade))

# e se eu quisesse mostrar o dobro da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Já pode beber ou dirigir"
if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode beber ou dirigir")
else:
  print("Você é xóvem ainda")

#E se eu quisesse perguntar o gênero (M = masculino e F = feminino)
#Mostre (... e você também precisa/precisou prestar o serviço militar obrigatório)
genero = input("Informe o gênero M=Masculino, F=Feminino, O=Outros: ")
if idade>=18 and genero == "M":
  print("... e você também precisa/precisou prestar o serviço militar obrigatório")
print("vai ser executada de qualquer jeito")