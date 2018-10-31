
import func as f

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


resultado1 = str(f.imc(peso,altura))
resultado2 = f.classeImc(sexo,peso,altura)

print('O seu IMC é:', resultado1[0:5])
print('A sua classificação é:', resultado2)
