from datetime import date, datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        r = func(*args, **kwargs)
        final_time = datetime.now()
        time_elapse = final_time-initial_time
        print("Pasaron " + str(time_elapse.total_seconds()) + " segundos")
        return r
    return wrapper


def main():

    @execution_time
    def random_func():
        for _ in range(1, 10 ** 7):
            pass

    random_func()

    @execution_time
    def suma(a: int, b: int) -> int:
        return a + b

    print(suma(5, 6))

    @execution_time
    def saludo(nombre = 'Cesar'):
        print('Hola '+nombre)

    saludo('Missael')
if __name__ == '__main__':
    main()
