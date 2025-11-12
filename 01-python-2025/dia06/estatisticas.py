def soma(a:float, b:float, *args)->float: #Args são argumento que não são os obrigatórios (a e b) e ele serve pra quando não sabemos quantos parâmetros iremos passar pra função
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args) + 2)

a = float(input('Entre com o valor de A: '))
b = float(input('Entre com o valor de B: '))
c = float(input('Entre com o valor de C: '))

print('Média = ', media(a, b, c))