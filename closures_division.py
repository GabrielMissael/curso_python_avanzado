def make_division_by(n: float):
    assert type(n) == float or type(n) == int, "Debes ingresar un número"

    def divisor(x: float) -> float:
        assert type(x) == float or type(x) == int, "Debes ingresar un número"
        return x/n

    return divisor

def main():
    division_3 = make_division_by(3)
    print(division_3(18))

    division_5 = make_division_by(5)
    print(division_5(100))

    division_18 = make_division_by(18)
    print(division_18(54))


if __name__=='__main__':
    main()