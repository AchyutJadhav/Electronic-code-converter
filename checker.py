from codeconverter import CodeConverter

code = CodeConverter()


class Checker:
    def __init__(self):
        self.number = None

    def is_octal(self, number):
        self.number = str(number)

        for i in number:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7":
                continue

            else:
                return False

        return True

    @staticmethod
    def is_binary(number):

        for i in number:
            if i == "0" or i == "1":
                continue

            else:
                return False

        return True

    def is_hexadecimal(self, number):

        self.number = str(number)

        for i in number:
            if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" \
                    or i == "9" or i == "a" or i == "b" or i == "c" or i == "d" or i == "e" or i == "f" or i == "A" \
                    or i == "B" or i == "C" or i == "D" or i == "E" or i == "F":
                continue

            else:
                return False

        return True

    def is_bcd(self, number):
        self.number = str(number)
        if len(self.number) % 4 == 0:
            for i in range(0, len(self.number) , 3):
                a = ""
                for j in range(i, i + 4):
                    a = a + number[j]

                print(a)
                binary = code.binary_to_decimal(a)
                print(binary)

                if int(binary) > 9:
                    return False
                else:
                    return True

        else:
            return False
