def multiplicar(fator1, fator2):
    if type(fator1) == str:
        fator1 = float(fator1)

    if type(fator2) == str:
        fator2 = float(fator2)
    produto = fator1 * fator2

    if type(fator1) == str:
        print(type(produto))
        return str(produto)


    if type(fator1) == int:
        print(type(produto))
        return int(produto)



    if type(fator1) == float:
        print(type(produto))
        return float(produto)



numero1 = input("Entre com o primeiro valor : ")
numero2 = input("Entre com o segundo valor : ")
produto = multiplicar(10, 10.5)
if type(produto) == str:
    print("Resultado...: "+produto)
if type(produto) == int or type(produto)== float:
    print("Resultado...: ", produto)
