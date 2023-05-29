nota1 = float(input("informe a nota1:"))
nota2 = float(input("informe a nota2:"))
nota3 = float(input("informe a nota3:"))

media = (nota1 + nota2 + nota3) /3 

print("sua media foi: {:.2f}".format(media)) 

if media >= 6:
    print("aprovado")
elif media > 5:
    print("recuperaçao:")
else:
    print("reprovado:")


