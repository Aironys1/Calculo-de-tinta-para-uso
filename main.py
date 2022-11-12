from calculadora import Calculadora
calc = Calculadora()

mensagem = 'Fim da execução'

largura: float   = float (input('Qual a largura do cômodo? '))
profundidade: float  = float (input('Qual a profundidade do cômodo? '))
altura:float  = 2.9

calc.area_paredes: float = 2 * (largura + profundidade) * altura

print ("A area das paredes é: ", calc.area_paredes)

calc.area_teto: float = largura * profundidade

print(
    'A área do teto é:',
    calc.area_teto
)

print(
    'A litragem de tinta necessária é:',
    (calc.area_paredes + calc.area_teto) / 10    # Rendimento da tinta = 10 litros
)

print(mensagem)

