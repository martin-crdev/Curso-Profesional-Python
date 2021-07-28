import time

class FiboIter():

    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        
        if self.counter == 0:
            if self.counter <= self.max:
                self.counter += 1
                return self.n1
            else:
                raise StopIteration
        elif self.counter == 1:
            if self.counter <= self.max:
                self.counter += 1
                return self.n2
            else:
                raise StopIteration
        else:
            if self.n1 + self.n2 <= self.max:
                self.aux = self.n1 + self.n2
                #self.n1 = self.n2
                #self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration

def run():
    x = int(input("Ingresa un numero: "))
    fibonacci = FiboIter(x)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)

if __name__ == "__main__":
    run()