def imc(peso,altura):
    imc = peso / (altura*altura)
    return imc

def classeImc(sexo,peso,altura):
    valorImc = imc(peso,altura)

    if sexo == 'm':
        if valorImc < 20.7:
            return "Abaixo do peso"
        elif valorImc >= 20.7 and valorImc < 26.4:
            return "Peso normal"
        elif valorImc >= 26.4 and valorImc < 27.8:
            return "Marginalmente acima do peso"
        elif valorImc >= 27.8 and valorImc < 31.1:
            return "Acima do peso ideal"
        elif valorImc >= 31.1:
            return "Obesidade"
        else:
            return "Erro de cálculo. Entre em contato com o administrador"

    if sexo == 'f':
        if valorImc < 19.1:
            return "Abaixo do peso"
        elif valorImc >= 19.1 and valorImc < 25.8:
            return "Peso normal"
        elif valorImc >= 25.8 and valorImc < 27.3:
            return "Marginalmente acima do peso"
        elif valorImc >= 27.3 and valorImc < 32.3:
            return "Acima do peso ideal"
        elif valorImc >= 32.3:
            return "Obesidade"
        else:
            return "Erro de cálculo. Entre em contato com o administrador"

print('Vamos calcular seu IMC?')

validSexo = False
while validSexo == False:
    sexo = input('Digite seu sexo (M ou F): ').lower()
    if sexo != 'm' and sexo != 'f':
        print('Sexo inválido. Digite M ou F.')
    else:
        validSexo = True
        print('\n')
        
validPeso = False
while validPeso == False:
    peso = input('Digite seu peso (ex. 68.5): ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 350:
            print('Peso inválido. O número tem que ser maior que 0 e menor 350.')
        else:
            validPeso = True
            print('\n')
    except:
        print("Peso inválido. Use apenas números e separe decimais com '.'.")

validAltura = False
while validAltura == False:
    altura = input('Digite sua altura em metros (ex. 1.70): ')
    try:
        altura = float(altura)
        if altura <= 0 or altura > 3:
            print('Altura inválida. O número tem que ser maior que o e menor que 3.')
        else:
            validAltura = True
            print('\n')
    except:
        print("Altura inválida. Use apenas números e separe decimais com '.'.")


resultado1 = str(imc(peso,altura))
resultado2 = classeImc(sexo,peso,altura)

print('O seu IMC é:', resultado1[0:5])
print('A sua classificação é:', resultado2)
