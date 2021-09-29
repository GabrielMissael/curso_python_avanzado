def is_prime(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def main():
    # print(is_prime('Hola'))
    print(is_prime(5))


if __name__=='__main__':
    main()