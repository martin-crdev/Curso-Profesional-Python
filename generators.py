import time 

def fibo_gen(number):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            if counter <= number:
                counter += 1
                yield n1
            else:
                break
        elif counter == 1:
            if counter<= number:
                counter += 1
                yield n2
            else:
                break
        else:
            if n1 + n2 <= number:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                break


def run():
    num = int(input("Ingresa un numero: "))
    fibonacci = fibo_gen(num)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)

if __name__ == "__main__":
    run()