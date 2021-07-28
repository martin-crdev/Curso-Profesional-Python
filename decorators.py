from datetime import datetime 

def execution_time(func):
    #*args indica que tome todos los argumentos sin importar el numero que tenga la funcion
    #**kwargs indica que tome todos los parametros nombrados sin importar el numero que tenga la funcion 
    def wrapper(*args, **kwargs): #Esto ayuda a que podamos decorar cualquier funcion
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Pasaron "+ str(time_elapsed.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    #Cuando no nos importa el numero en el que este iterando un for se usa un _ 
    for _ in range(1, 1000000):
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Cesar"):
    print("Hola " + nombre)

def run():
    random_func()
    suma(5, 5)
    saludo("Facundo")

if __name__ == "__main__":
    run()