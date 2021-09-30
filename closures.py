def make_repeater_of(n: int):
    assert type(n) == int, "Repetidor funciona con números enteros 😶"
    def repeater(string: str) -> str:
        assert type(string) == str, "Solo puedes utilizar cadenas de texto 😄"
        return n*string
    return repeater

def main():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hey '))

    repeat_10 = make_repeater_of(10)
    print(repeat_10('Platzi '))

if __name__=='__main__':
    main()