# Dado uma string de expressão x.
# Verifique se os pares e a ordem de ‘{’ , ‘}’ , ‘(’ , ‘)’ , ‘[’ , ‘]’ estão corretos.
# Por exemplo, a função deve retornar:
# ‘True’ para exp = “[()]{}{()()}” e
# ‘False’ para exp = “[(])”.

from stack import Stack

def is_balanced(expression):
    """
    Verifica se a expressão possui parênteses balanceados.
    Usa a pilha implementada em stack.py.
    """
    pilha = Stack()
    #------- COLOQUE SEU CÓDIGO AQUI -------
    correspondencia = {")": "(", "]": "[", "}":"{"}
    i = 0
    while i < len(expression):
        if expression[i] in ['(', '[', '{']:
            pilha.push(expression[i])
        elif expression[i] in [')', ']', '}']:
            if pilha.is_empty():
                return False
            elif correspondencia[expression[i]] == pilha.peek():
                pilha.pop()
            else:
                return False
        i += 1
    
    return pilha.is_empty()

    #---------------------------------------


# Teste
print(is_balanced("[{}(2+2)]{}")) #Esperado True
print(is_balanced("[{}(2+2))]{}")) #Esperado False
print(is_balanced("[{}])")) #Esperado False
