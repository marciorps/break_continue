# # continue, ignorar/pular
# for numero in range(100):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         continue

#break, para interromper a iteração
# for numero in range(100):
#     if numero % 2 == 0:
#         print(numero)
#     else:
#         break


#desafio1
## Use a operação nescessária(break ou continue) para que a seguinte condição aconteça
    ##*ao chegar ao estilo "Rap" o mesmo não deve ser impresso na tela
# estilos = ['hip-hop', 'rock', 'rap', 'pop']

# for estilo in estilos:
#     if estilo != 'rap':
#         print(estilo)
#     else:
#         continue

#desafio2
## Use a operação nescessária(break ou continue) para que a seguinte condição aconteça:
## *Ao chegar em estilo "rock" a execução deve ser enterrompida estilos

estilos = ['hip-hop', 'rock', 'rap', 'pop']

for estilo in estilos:
    if estilo != 'rock':
        print(estilo)
    else:
        break