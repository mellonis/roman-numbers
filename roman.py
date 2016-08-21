import re

class Roman(int):
    __digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    __pattern = re.compile("^M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")

    def __new__(cls, value):
        try:
            value = int(value)
        except ValueError:
            value = str(value).replace(' ', '').upper()
            if cls.__pattern.match(value) == None or not set(cls.__digits) >= set(value):
                raise ValueError("Error!")
            integers = list(map(cls.__digits.get, value))
            value = sum(-n if n < max(integers[i:]) else n for i, n in enumerate(integers))
            return super(Roman, cls).__new__(cls, value)
        else:
            if value < 0:
                raise ValueError("Error!")
            return super(Roman, cls).__new__(cls, value)
