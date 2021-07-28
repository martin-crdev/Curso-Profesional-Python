def is_prime(number: int) -> bool:
    if number % 2 != 0:
        return True 
    return False

def run():
    print(is_prime(10))

if __name__ == "__main__":
    run()