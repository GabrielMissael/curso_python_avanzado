def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]


def main():
    string: str = input('Introduce una palabra 😄: ')
    if is_palindrome(string):
        print(string, ' = ', string[::-1], '¡Es palindromo! 😯')
    else:
        print(string, ' != ', string[::-1], '¡No es palindromo! 😵')


if __name__ == '__main__':
    main()
