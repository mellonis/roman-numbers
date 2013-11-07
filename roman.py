import re


class Roman(int):
    __digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    __pattern = re.compile("^M*(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")

    def __new__(class_, value):
        try:
            value = int(value)
        except ValueError:
            value = str(value).replace(' ', '').upper()
            if class_.__pattern.match(value) == None or not set(class_.__digits) >= set(value):
                raise ValueError("Error!")
            integers = list(map(class_.__digits.get, value))
            value = sum(-n if n < max(integers[i:]) else n for i, n in enumerate(integers))
            return super(Roman, class_).__new__(class_, value)
        else:
            if value < 0:
                raise ValueError("Error!")
            return super(Roman, class_).__new__(class_, value)


print(Roman('0'))
print(Roman('1'))
print(Roman('MCMXL') + Roman('I'))
#0rIX