#Funçao lambda são funções anonimas. 

# soma_lambda = lambda num1 , num2: num1 + num2
# soma = soma_lambda(5,7)
# print(soma)

#Função lambdas também podem realizar uma condição.

par_impar = lambda num : 'é par ' if num%2 == 0 else 'é impar'

result = par_impar(5)

print(result)