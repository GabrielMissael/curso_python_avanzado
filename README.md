# Notas del Curso profesional de Python 馃悕

- Instructor: Facundo Garc铆a Martoni
- Link al curso: [Curso profesional de Python](https://platzi.com/clases/python-profesional/)

## Introducci贸n

### 驴C贸mo funciona Python?

Tenemos una clasificaci贸n de los lenguajes de programaci贸n:

- **Compilado:** En C++, por ejemplo, el c贸digo pasa directamente, mediante el compilador, a lenguaje binario. Se comunica directamente con la computadora a trav茅s de la compilaci贸n. 馃
- **Interpretados:** Python es interpretado, por lo que no se pasa a c贸digo maquina, si no que se pasa a un estado intermedio en bytecode, que es un lenguaje de m谩s bajo nivel que puede ser le铆do por un interprete, por una m谩quina virtual, que puede funcionar en diferentes SO. 馃

Algunas preguntas frecuentes:

- Los lenguajes interpretados son normalmente m谩s lentos. "C cuando se debe, Python cuando se puede". 馃憖 Pero no es realmente importante en la mayor铆a de las aplicaciones.
- El **garbage collector** es una secci贸n especial de Python, el cual se encarga de tomar los objetos y variables que no est谩n en uso y las elimina. 馃Щ
- La carpeta `__pycache__` contiene el bytecode que es le铆do por la maquina virtual, y funciona como una especie de recuperaci贸n.

### C贸mo organizar las carpetas de tus proyectos

Es importante comprender dos conceptos:

- **M贸dulo**: Es cualquier archivo de Python. Generalmente, contiene c贸digo que puedes reutilizar 馃槂.
- **Paquete**:  Un paquete es una carpeta que contiene un conjunto de m贸dulos. Siempre posee el archivo `__init__.py` (*dander init.py*). Estos m贸dulos est谩n relacionados.

Un orden com煤n de proyectos:

```python
- exploracion_espacial_proyecto.
    - README
    - .gitignore
    - venv
    - exploraci贸n espacial
        - __init__.py
        - nave.py
        - destino.py
        - tests.py
```

Sin embargo, en cada proyecto puede ser diferente dependiendo de lo que se est茅 haciendo, ya que, por ejemplo, podr铆as usar alg煤n *framework.*馃く

## Static typing

### 驴Qu茅 son los tipados?

Tenemos tipos de datos primitivos (arreglos, n煤meros, strings, booleanos, etc). La manera en que un lenguaje trata a los tipos es el tipado. Tenemos 4 clasificaciones:

- Est谩tico: Son los que levantan los errores de tipo en tiempo de compilaci贸n. Esto es, si al estar programando tenemos un error de tipo, entonces el lenguaje nos avisa antes de que se ejecute (mientras compila). 馃槸 (C/C++)
- Din谩mico: Opuesto al est谩tico, levantan los errores de tipo en el tiempo de compilaci贸n, es decir, el error sale mientras el programa se ejecuta en esa l铆nea donde est谩 el error. 馃洃 (Python)
- Fuerte: Son los que tratan con mas severidad a los datos de diferente tipo. 馃槧 (Python)
- D茅bil: Son mas relajados con datos de diferente tipo. 馃 (Javascript)

### Tipado est谩tico en Python

- Podemos convertir a Python a un lenguaje de tipado est谩tico 馃く. Para eso, usamos Static Typing, y es muy sencillo, solo debemos a帽adir una sintaxis adicional, en la cual declaramos variables con su tipo.

    ```python
    a: int = 5
    b: str = 'Hola'
    c: bool = True
    
    print(a, b, c)
    ```

    Esto funciona desde Python 3.6 馃憖. Para hacerlo con funciones (con sus variables y con lo que retorna la funci贸n):

    ```python
    def suma(a: int, b: int) -> int:
     return a + b
    
    print(suma(1, 2))
    ```

    Si le pasamos strings a la funci贸n `suma`, si funcionar谩 y nos va a regresar las strings sumadas, para evitar esto, debemos a帽adir un m贸dulo.

- Podemos hacer tipado en estructuras de datos. Para definir que una variable es de un tipo (de una estructura de datos), desde la versi贸n 3.9, podemos hacerlo con las palabras claves de ese tipo. Antes de la versi贸n 3.9, es con:

    ```python
    from typing import Dict, List
    
    positives: List[int] = [1, 2, 3, 4, 5]
    
    users: Dict[str, int] = {
     'argentina': 1,
     'mexico': 34,
     'colombia': 45
    }
    
    countries: List[Dict[str, str]] = [
     {
      'name':'Argentina'
      'people':'45000'
     },
     {
      'name':'M茅xico'
      'people':'900000'
     },
     {
      'name':'Colombia'
      'people':'9999999'
     }
    ]
    ```

- Podemos hacer lo mismo con las tuplas:

    ```python
    from typing import Tuple
    
    numbers: Tuple[int, float, int] = (1, 0.5, 1)
    ```

- Podemos *definir* nuestros propios tipos de variable y usarlas:

    ```python
    from typing import Tuple, Dict, List
    
    CoordinateType = List[Dict[str, Tuple[int, int]]]
    
    coordinates: CoordinateType = [
     {
      'coord1': (1, 2),
      'coord2': (3, 5)
     },
     {
      'coord1': (0, 1),
      'coord2': (2, 5)
     }
    ]
    ```

- Para que Python considere este tipado est谩tico y no se salte, es con el m贸dulo `mypy` que nos detiene cuando hay errores de tipado 馃憖.

### Practicando el tipado est谩tico

- Para checar que el c贸digo respeta el tipado que especificamos, debemos correrlo con `mypy <nombre>.py --check-untyped-defs` 馃憖. El m贸dulo mypy nos arroja errores de tipado, por ejemplo:

    ```markdown
    palindrome.py:9: error: Argument 1 to "is_palindrome" has incompatible type "int"; expected "str"
    Found 1 error in 1 file (checked 1 source file)
    ```

- Soluci贸n al reto:

    ```python
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
    ```

## Conceptos avanzados de funciones

### Scope: alcance de las variables

- Una variable solo est谩 disponible dentro de la regi贸n donde fue creada 馃.
- **Local scope**: Regi贸n que se corresponde al 谩mbito de una funci贸n:

    ```python
    # Local scope
    def my_func():
     y = 5
     print(y)
    my_func()
    # 5
    ```

    En este caso, la variable `y` no puede ser le铆da fuera de la funci贸n.

- **Global scope**: Variables que tienen alcance en todo nuestro programa. 馃寧

    ```python
    # Global scope
    y = 5
    def my_func():
     print(y)
    
    def my_other_func():
     print(y)
    
    my_func()
    my_other_func()
    # 5 # 5
    ```

- Podemos tener dos variables que se llaman igual, pero dado a que una es global y otra es local, son objetos diferentes. En la funci贸n, se le da **prioridad a la variable m谩s local**. 馃

### Closures

- **Nested functions**: Las funciones anidadas son simplemente funciones creadas dentro de otra funci贸n. Podemos hacer return de una funci贸n creada dentro de otra funci贸n 馃樀 y luego guardar esas funciones en variables que podemos utilizar.

    ```python
    def main():
     a = 1
     def nested():
      print(a)
     return nested
    
    my_func = main()
    my_func()
    # 1
    ```

- Eso anterior es un closure 馃く y es b谩sicamente cuando una variable de un scope superior es recordada por una funci贸n de scope inferior (aunque luego se elimine la de scope superior).

    ```python
    def main():
     a = 1
     def nested():
      print(a)
     return nested
    
    my_func = main()
    my_func()
    # 1
    del(main)
    my_func()
    # 1
    ```

- Reglas para encontrar un closure: 馃敟
  - Debemos tener una nested function.
  - La nested function debe referenciar un valor de un scope superior.
  - La funci贸n que envuelve a la nested function debe retornarla tambi茅n.
- Ejemplo de closures para crear funciones:

    ```python
    def make_multiplier(x):
     def multiplier(n):
      return x*n
     return multiplier
    
    times10 = make_multiplier(10)
    times4 = make_multiplier(4)
    
    print(times10(3)) # 30
    print(times4(5)) #20
    print(times10(times4(2))) # 80
    ```

- Los closure aparecen en dos casos particulares: cuando tenemos una clase corta (con un solo m茅todo), los usamos para que sean elegantes. El segundo caso, es cuando usamos decoradores 馃憖

### Programando closures

- Soluci贸n al reto:

    ```python
    def make_division_by(n: float):
        assert type(n) == float or type(n) == int, "Debes ingresar un n煤mero"
    
        def divisor(x: float) -> float:
            assert type(x) == float or type(x) == int, "Debes ingresar un n煤mero"
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
    ```

## Estructuras de datos avanzadas

### Decoradores

- Es el concepto m谩s avanzado de funciones 馃樀. Un decorador es un closure especial, con una funci贸n adicional.
- Un decorador es una funci贸n que recibe como par谩metro otra funci贸n, le a帽ade cosas, y retorna una funci贸n diferente. Le da superpoderes a una funci贸n 馃Ω鈥嶁檧锔?.

    ```python
    def decorador(func):
     def envoltura():
      print('Esto se a帽ade a mi funci贸n original')
      return envoltura
    
    def saludo():
     print('Hola!')
    
    saludo() # Hola!
    saludo = decorador(saludo)
    saludo() # Esto se a帽ade a mi funci贸n original. Hola!
    ```

- Esto, a ser un patr贸n muy com煤n, hay una manera mas pythonica de hacerlo, con az煤car sint谩ctica. Esto es cuando tenemos un c贸digo que est谩 embellecido para que sea m谩s f谩cil de entender. (*Sugar sintax*). Ser铆a algo as铆:

    ```python
    def decorador(func):
     def envoltura():
      print('Esto se a帽ade a mi funci贸n original')
      return envoltura
    
    @decorador
    def saludo():
     print('Hola!')
    
    saludo() # Esto se a帽ade a mi funci贸n original. Hola!
    ```

- Otro ejemplo:

    ```python
    def mayusculas(func):
     def envoltura(texto):
      return func(texto).upper()
     return envoltura
    
    @mayusculas
    def mensaje(nombre):
     return f'{nombre} recibiste un mensaje'
    
    print(mensaje('Cesar'))
    ```

### Iteradores

- Un iterator es una estructura de datos para guardar datos infinitos 馃く. Para entenderlo, primero debemos saber que un **iterable** es todo aquel objeto que puedo recorrer en un ciclo (lista, strings, etc). Un iterable es divisible.
- Cuando hacemos un ciclo, Python internamente no est谩 recorriendo a ese iterable, si no m谩s bien ese iterable se convierte internamente en un iterador, que si puede ser recorrido. 馃
- Para crear un iterador:

    ```python
    # Creando un iterador
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)  # Se recibe un iterable
    
    # Iterando un iterador
    print(next(my_iter))
    # Cuando no quedan datos, la excepci贸n StopIteration es elevada
    ```

- Para que no se rompa el c贸digo, hacemos manejo de errores: 馃

    ```python
    # Creando un iterador
    my_list = [1, 2, 3, 4, 5]
    my_iter = iter(my_list)
    
    # Iterando un iterador
    while True: 
     try: 
      element = next(my_iter)
      print(element)
     except StopIteration:
      break
    ```

    Esta es una manera eficiente de extraer todos los elementos de un iterable. De hecho, esta es la manera en la que funciona un ciclo for, es la az煤car sintaxis de este c贸digo anterior 馃槏. El ciclo for en si mismo no existe.

- 驴C贸mo construyo un iterador?. Una opci贸n es castear desde un iterable. Para hacerlo desde cero, debemos usar el protocolo de los iteradores que contiene dos clases importantes `__iter__` y `__next__`:

    ```python
    class EvenNumbers:
     """Calse que implementa un iterador de todos los
       n煤meros pares, o los n煤meros pares hasta un m谩ximo"""
     def __init__(self, max = None):
      self.max = max
    
     def __iter__(self):
      self.num = 0
      return self
    
     def __next__(self):
      if not self.max or self.num <= self.max:
       result = self.num
       self.num += 2
       return self
      else:
       raise StopIteration
    ```

- Las ventajas de usar iteradores: Nos ahorra recursos computacionales y de memoria, ya que tenemos una funci贸n matem谩tica de como obtener los siguientes elementos, sin necesidad de guardarlos todos 馃憖.

### La sucesi贸n de Fibonacci

- Una sucesi贸n matem谩tica famosa es la sucesi贸n de Fibonacci 馃. Se define c贸mo:

    $$x_0 = 0 \\ x_1 =1 \\ x_i = x_{i-1} + x_{i-2} \ \ \ \ \ \ i>2$$

- Soluci贸n al reto:

    ```python
    import time
    
    class FiboIter():
    
        def __init__(self, max = None):
            self.max = max
    
        def __iter__(self):
            self.n1 = 0
            self.n2 = 1
            self.counter = 0
            return self
    
        def __next__(self):
            if not self.max or self.counter < self.max:
    
                if self.counter == 0:
                    self.counter += 1
                    return self.n1
                elif self.counter == 1:
                    self.counter += 1
                    return self.n2
                else:
                    n1 = self.n2
                    self.n1, self.n2 = n1, self.n1 + self.n2
                    self.counter += 1
                    return self.n2
            else:
                raise StopIteration
    
    if __name__=='__main__':
    
        fibonacci = FiboIter(max = 10)
        for element in fibonacci:
            print(element)
            time.sleep(0.5)
    ```

### Generadores

- Los iteradores tienen sugar syntax 馃挅. Son llamados **generadores**, los cuales son funciones que guardan un estado 馃.
- Los generadores son funciones: 馃敟

    ```python
    def my_gen():
     """Un ejemplo de generadores"""
     print("Hello world!")
     n = 0
     yield n 
     
     print("Hello heaven!")
     n = 1
     yield n
    
     print("Hello hell!")
     n = 2
     yield n
    
    # Lo instanciamos
    a = my_gen()
    print(next(a)) # Hello world!
    print(next(a)) # Hello heaven!
    print(next(a)) # Hello hell!
    print(next(a)) # StopIteration
    ```

- `yield` este keyword es an谩loga al `return`, pero no termina la funci贸n, le pone pausa. La siguiente ejecuci贸n, corre despu茅s de este punto 馃憖.
- Generator expression. 馃く Se trae un elemento a la vez, y no ocupa toda la memoria 馃槸.

    ```python
    my_list = [0, 1, 2, 3, 4, 5, 6]
    
    my_second_list = [x*2 for x in my_list] # List comprehension
    my_second_gen = (x*2 for x in my_list) # Generator expression
    ```

- La ventaja de los generadores es que es m谩s f谩cil de escribir que un iterador, y tiene las mismas ventajas que este 煤ltimo. 馃挄

### Mejorando nuestra sucesi贸n de Fibonacci

- Soluci贸n al reto:

    ```python
    import time
    
    def fibo_gen(max = None):
        n1, n2 = 0, 1
        counter = 0
    
        while not max or counter <= max:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield n2
    
    if __name__ == '__main__':
        fibonacci = fibo_gen(10)
        for element in fibonacci:
            print(element)
            time.sleep(0.5)
    ```

### Sets

- Los sets, o conjuntos, son una colecci贸n desordenada de elementos 煤nicos e inmutables. 鉁?
- Tuplas, strings, n煤meros, True, False, etc son sets. 馃く
- Para crear un set:

    ```python
    my_set = {3, 4, 5}
    print(my_set) # {3, 4, 5}
    
    my_set2 = {"Hola", 23.3, False, True}
    print(my_set2) # {False, True, "Hola", 23.3}
    
    my_set3 = {3, 3, 2}
    print(my_set3) # {3, 2}
    
    my_set4 = {[1, 2, 3], 4} # ERROR!!!
    
    empty_set = {} # Esto es dict por defecto
    print(type(empty_set)) # <class 'dict'>
    
    empty_set = set()
    print(type(empty_set)) # <class 'set'>
    ```

- Para hacer casting a sets usamos `set()`. Esto elimina los repetidos de una lista o tupla y los hace set.
- Para a帽adir elementos a un set, usamos `my_set.add(<elemento inmutable>)`. Para a帽adir varios elementos, hacemos `my_set.update(<lista>, <tupla>)`.
- Para borrar elementos de un set, usamos `my_set.remove(<elemento>)` pero debemos estar seguro de que el set contiene ese elemento. Si no sabemos si existe el elemento `my_set.discard(<elemento?>)`. 馃憖
- Para borrar un elemento aleatorio, usamos `my_set.pop()`. Para borrar todo usamos `my_set.clear()`.

### Operaciones con sets

Podemos operaro con set:

- Uni贸n: La uni贸n de dos conjuntos es el resultado de combinar todos los elementos, sin repetir馃憖. Para hacer esto, usamos el pipe operator `my_set3 = my_set1 | my_set2`.
- Intersecci贸n: Nos quedamos solamente con los elementos que ambos sets tienen en com煤n. Para hacer esto, hacemos `my_set3 = my_set1 & my_set2`. 馃く
- Diferencia: Tomar dos set, y de uno quitar todos los elementos que contiene el otro. Para hacer esto, hacemos `my_set3 = my_set1 - my_set2`. Es importante notar que `my_set1 - my_set2 != my_set2 - my_set1`.
- Diferencia sim茅trica: Es lo contrario a la intersecci贸n. Nos quedamos con los elementos que no se comparten, esto es hace c贸mo `my_set3 = my_set1 ^ my_set2`.

Tambi茅n podemos usar los m茅todos para que sea m谩s explicito, que son:

```python
set1.union(set2)
set1.symmetric_difference(set2)
set1.difference(set2)
set1.intersection(set2)
```

Ejemplo con sets:

```python
def main():
    set1 = {1, 2, 3.5, True, "Juan", "Mar铆a"}
    set2 = {0, 2, 3.1, False, "Juan", "Missael"}

    print(f"set1 = {set1}")
    print(f"set2 = {set2}")

    # union
    print(f"set1 + set2 = {set1 | set2}")

    # difference
    print(f"set2 - set1 = {set2 - set1}")
    print(f"set1 - set2 = {set1.difference(set2)}")

    # symmetric difference
    print(f"set1 ^ set2 = {set1 ^ set2}")

    # intersection
    print(f"set1 & set2 = {set1 & set2}")

if __name__=='__main__':
    main()
```

El output:

```markdown
set1 = {1, 2, 3.5, 'Mar铆a', 'Juan'}
set2 = {0, 2, 3.1, 'Missael', 'Juan'}
set1 + set2 = {0, 1, 2, 3.5, 3.1, 'Missael', 'Mar铆a', 'Juan'}
set2 - set1 = {0, 'Missael', 3.1}
set1 - set2 = {1, 'Mar铆a', 3.5}
set1 ^ set2 = {0, 1, 3.1, 'Missael', 3.5, 'Mar铆a'}
set1 & set2 = {2, 'Juan'}
```

## Bonus

### Manejo de fechas

- Cuando hagamos aplicaciones o proyectos, es importante conocer como manejar fechas en Python. Podemos hacerlo con Python con el m贸dulo `datetime` que viene ya en el core de Python.
- Ejemplo sencillo 馃憖

    ```python
    import datetime
    
    # Tiempo en d铆as, horas y segundos
    my_time = datetime.datetime.now()
    print(my_time)
    
    # Siguiendo el estandar
    utc_time = datetime.datetime.utcnow()
    print(utc_time)
    
    # Para solo la fecha actual
    my_day = datetime.date.today()
    ```

- Podemos acceder tambi茅n al d铆a, a帽o y mes con `my_day.year`, `my_day.month`, y `my_day.day`
- Debemos considerar el formateo de fechas, ya que no en todas las partes del mundo se escribe de la misma manera. Para especificar el formato de la fecha, tenemos la tabla de c贸digo de formato.

- Ejemplo de formato:

    ```python
    from datetime import datetime
    my_datetime = datetime.now()
    print(my_datetime)
    
    my_str = my_datetime.strftime('Fecha : %d/%m/%Y')
    my_str2 = my_datetime.strftime('Estamos en el a帽o %Y')
    ```

- Tabla de formato completa:

    [datetime - Basic date and time types - Python 3.9.7 documentation](https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes)

### Time zones

- En cada pa铆s, la hora es diferente. Para trabajar distintas zonas horarias, debemos usar un m贸dulo especial `pytz` que debemos instalar porque no viene instalada.
