from stack import Stack


main_stack = Stack()
delete_stack = Stack()



def enqueue(data):
    main_stack.push(data)

def dequeue():
    while not main_stack.is_empty():
        delete_stack.push(main_stack.pop())

    removed = delete_stack.pop()
    print("EStou aquiiiii")
    while not delete_stack.is_empty():
        main_stack.push(delete_stack.pop())

    return removed

def is_empty():
    """Verifica se a fila está vazia."""
    return main_stack.is_empty()

print(is_empty())

enqueue("Cebola")
enqueue("Salada")

print(is_empty())

dequeue()




