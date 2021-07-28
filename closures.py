#Function de scope superior
def make_repeater_of(n):
    #Nested function de scope inferior
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater #Retornamos la nested function para poder aplicar un closure

def run():
    #Indicamos que repeat_5 inicie la funcion make_repeater con 5 y retorna a nuestra nested function
    repeat_5 = make_repeater_of(5)
    #Ahora repeat_5 inicia la funcion repeater recordando la variable de la funcion de scope superior(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Platzi"))

if __name__ == "__main__":
    run()