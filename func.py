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

