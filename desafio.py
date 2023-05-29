def area (largura, comprimento):
    total = largura * comprimento 
    return total 

largura =  float(input("qual largura do terreno :"))
comprimento =  float(input("qual o comprimento do terreno :"))

resultado = area(largura, comprimento)

print("a area do terreno", area (largura,comprimento),"metros quadrado")
