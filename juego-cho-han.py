import random
def guess():
    menu = """
     escribe -par- si crees que los dados arrojan un numero par
     escribe -impar- si crees que los dados arrojan un numero impar 
                """
    print(menu)

def logic():
 
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    suma =  n1 + n2
    resto = suma%2    
    guess()
    adivina = input('es par o impar? ')
    if  resto == 0 and adivina == 'par':
        print(f'el numero es {suma} es par  ¡ganaste!')
        return True
    elif resto !=0 and adivina == 'impar':
        print(f'el numero es {suma} es imar  ¡ganaste!')
        return True
    
    else:
        print(f'perdio el numero era {suma}')
        return False
def game():
    billetera = 10
    while billetera > 0:
        try:
            apuesta = int(input('¿cuanto deseas apostar? '))
            if logic() == True:
                billetera+=apuesta
            else:
                billetera-=apuesta
                
        except ValueError:
            print('error')
        print(f'ahora tienes {billetera}')

if __name__ == "__main__":
    game()

        
    
