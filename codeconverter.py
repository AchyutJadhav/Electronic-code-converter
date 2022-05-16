class CodeConverter:

    def __init__(self):
        self.bcd_no = None
        self.gray_code = None
        self.gray = None
        self.prev = None
        self.curr = None
        self.binary = None
        self.excess_3_code = None
        self.get_no = None
        self.get = None
        self.no = None
        self.hex_number_as_list = None
        self.octal_number_as_list = None
        self.hex_number = None
        self.decimal_no = None
        self.decimal_number = None
        self.b = None
        self.binary_number_as_list = None
        self.binary_number = None
        self.a = None
        self.hex_number_as_reversed = None

    def decimal_to_binary(self, decimal_number):
        self.hex_number_as_reversed = []
        while decimal_number != 0:
            self.a = decimal_number % 2
            decimal_number = int(decimal_number / 2)
            self.hex_number_as_reversed.append(str(self.a))

        self.hex_number_as_reversed.reverse()
        self.binary_number = "".join(self.hex_number_as_reversed)

        return self.binary_number

    def binary_to_decimal(self, binary_number):
        self.binary_number_as_list = [int(i) for i in str(binary_number)]
        self.binary_number_as_list.reverse()

        self.decimal_no = 0

        for i in range(len(self.binary_number_as_list)):
            self.a = self.binary_number_as_list[i]
            self.b = self.a * (2 ** i)
            self.decimal_no += self.b

        return self.decimal_no

    def decimal_to_octal(self, decimal_number):
        self.decimal_number = decimal_number
        self.hex_number_as_reversed = []
        while self.decimal_number != 0:
            a = self.decimal_number % 8
            self.decimal_number = int(self.decimal_number / 8)
            self.hex_number_as_reversed.append(str(a))

        self.hex_number_as_reversed.reverse()
        self.hex_number = "".join(self.hex_number_as_reversed)

        return self.hex_number

    def octal_to_decimal(self, octal_number):
        self.hex_number = octal_number
        self.octal_number_as_list = [int(i) for i in str(self.hex_number)]
        self.octal_number_as_list.reverse()

        self.decimal_no = 0

        for i in range(len(self.octal_number_as_list)):
            self.a = self.octal_number_as_list[i]
            self.b = self.a * (8 ** i)
            self.decimal_no += self.b

        return self.decimal_no

    def decimal_to_hex(self, decimal_number):
        self.decimal_number = decimal_number
        self.hex_number_as_reversed = []
        while self.decimal_number != 0:
            self.a = self.decimal_number % 16
            self.decimal_number = int(self.decimal_number / 16)

            if self.a < 10:
                self.hex_number_as_reversed.append(str(self.a))
            elif self.a == 10:
                self.hex_number_as_reversed.append("A")
            elif self.a == 11:
                self.hex_number_as_reversed.append("B")
            elif self.a == 12:
                self.hex_number_as_reversed.append("C")
            elif self.a == 13:
                self.hex_number_as_reversed.append("D")
            elif self.a == 14:
                self.hex_number_as_reversed.append("E")
            elif self.a == 15:
                self.hex_number_as_reversed.append("F")

        self.hex_number_as_reversed.reverse()
        self.hex_number = "".join(self.hex_number_as_reversed)

        return self.hex_number

    def hex_to_decimal(self, hex_number):
        self.hex_number = hex_number
        self.hex_number_as_list = [i for i in str(self.hex_number)]
        self.hex_number_as_list.reverse()

        self.decimal_no = 0
        for i in range(len(self.hex_number_as_list)):
            self.a = self.hex_number_as_list[i]
            if self.a.isdigit():
                self.b = int(self.a) * (16 ** i)
            elif self.a == "A" or self.a == "a":
                self.b = 10 * (16 ** i)
            elif self.a == "B" or self.a == "b":
                self.b = 11 * (16 ** i)
            elif self.a == "C" or self.a == "c":
                self.b = 12 * (16 ** i)
            elif self.a == "D" or self.a == "d":
                self.b = 13 * (16 ** i)
            elif self.a == "E" or self.a == "e":
                self.b = 14 * (16 ** i)
            elif self.a == "F" or self.a == "f":
                self.b = 15 * (16 ** i)
            self.decimal_no += int(self.b)
        return self.decimal_no

    def decimal_to_excess(self, decimal_no):
        self.decimal_no = str(decimal_no)
        self.get_no = ""
        for i in self.decimal_no:
            self.no = int(i) + 3
            self.get = str(self.decimal_to_binary(self.no))

            if len(self.get) == 1:
                self.get = "000" + self.get

            elif len(self.get) == 2:
                self.get = "00" + self.get

            elif len(self.get) == 3:
                self.get = "0" + self.get

            self.get_no = self.get_no + self.get

        return int(self.get_no)

    def excess_to_decimal(self, excess_3_code):
        self.excess_3_code = str(excess_3_code)
        self.get = ""

        for i in range(0, len(self.excess_3_code) - 3, 4):
            self.no = ""
            for j in range(i, i + 4):
                self.no = self.no + self.excess_3_code[j]

            self.get = self.get + str(self.binary_to_decimal(int(self.no)) - 3)

        return int(self.get)

    def decimal_to_gray(self, decimal):
        self.binary = str(self.decimal_to_binary(decimal))
        self.gray = ""

        for i in range(len(self.binary)):
            if i == 0:
                self.gray = self.gray + self.binary[0]

            else:
                self.prev = self.binary[i - 1]
                self.curr = self.binary[i]

                if (self.prev == "0" and self.curr == "0") or (self.prev == "1" and self.curr == "1"):
                    self.gray = self.gray + "0"

                elif (self.prev == "1" and self.curr == "0") or (self.prev == "0" and self.curr == "1"):
                    self.gray = self.gray + "1"
        return int(self.gray)

    def gray_to_decimal(self, gray_code):
        self.gray_code = str(gray_code)
        self.binary = ""

        for i in range(len(self.gray_code)):
            if i == 0:
                self.binary = self.binary + self.gray_code[0]

            else:
                self.prev = self.binary[i - 1]
                self.curr = self.gray_code[i]

                if (self.prev == "0" and self.curr == "0") or (self.prev == "1" and self.curr == "1"):
                    self.binary = self.binary + "0"

                elif (self.prev == "1" and self.curr == "0") or (self.prev == "0" and self.curr == "1"):
                    self.binary = self.binary + "1"

        self.decimal_no = int(self.binary_to_decimal(self.binary))

        return self.decimal_no

    def decimal_to_bcd(self, decimal_no):
        self.decimal_no = str(decimal_no)
        self.get_no = ""
        for i in self.decimal_no:
            self.no = int(i)
            self.get = str(self.decimal_to_binary(self.no))

            if len(self.get) == 1:
                self.get = "000" + self.get

            elif len(self.get) == 2:
                self.get = "00" + self.get

            elif len(self.get) == 3:
                self.get = "0" + self.get

            self.get_no = self.get_no + self.get

        return self.get_no

    def bcd_to_decimal(self, bcd_no):
        self.bcd_no = str(bcd_no)
        self.get = ""

        for i in range(0, len(self.bcd_no) - 3, 4):
            self.no = ""
            for j in range(i, i + 4):
                self.no = self.no + bcd_no[j]

            self.get = self.get + str(self.binary_to_decimal(int(self.no)))

        return int(self.get)

    def from_decimal(self, type_of_number, type_of_number2, number):
        if type_of_number == "Decimal" and type_of_number2 == "Decimal":
            return number

        elif type_of_number == "Decimal" and type_of_number2 == "Binary":
            number = int(number)
            answer = self.decimal_to_binary(number)
            return answer

        elif type_of_number == "Decimal" and type_of_number2 == "Octal":
            number = int(number)
            answer = self.decimal_to_octal(number)
            return answer

        elif type_of_number == "Decimal" and type_of_number2 == "Hexadecimal":
            number = int(number)
            answer = self.decimal_to_hex(number)
            return answer

        elif type_of_number == "Decimal" and type_of_number2 == "Hexadecimal":
            number = int(number)
            answer = self.decimal_to_hex(number)
            return answer

        elif type_of_number == "Decimal" and type_of_number2 == "Excess 3":
            number = int(number)
            answer = self.decimal_to_excess(number)
            return answer

        elif type_of_number == "Decimal" and type_of_number2 == "Gray":
            number = int(number)
            answer = self.decimal_to_gray(number)
            return answer

        elif type_of_number == "Decimal" and type_of_number2 == "BCD":
            answer = self.decimal_to_bcd(number)
            return answer

    def from_octal(self, type_of_number, type_of_number2, number):
        if type_of_number == "Octal" and type_of_number2 == "Octal":
            return number

        elif type_of_number == "Octal" and type_of_number2 == "Decimal":
            answer = self.octal_to_decimal(number)
            return answer

        elif type_of_number == "Octal" and type_of_number2 == "Binary":
            number = int(number)
            number2 = self.octal_to_decimal(number)
            answer = self.decimal_to_binary(number2)
            return answer

        elif type_of_number == "Octal" and type_of_number2 == "Hexadecimal":
            number = int(number)
            number2 = self.octal_to_decimal(number)
            answer = self.decimal_to_hex(number2)
            return answer

        elif type_of_number == "Octal" and type_of_number2 == "Excess 3":
            number = int(number)
            number2 = self.octal_to_decimal(number)
            answer = self.decimal_to_excess(number2)
            return answer

        elif type_of_number == "Octal" and type_of_number2 == "Gray":
            number = int(number)
            number2 = self.octal_to_decimal(number)
            answer = self.decimal_to_gray(number2)
            return answer

        elif type_of_number == "Octal" and type_of_number2 == "BCD":
            number = int(number)
            number2 = self.octal_to_decimal(number)
            answer = self.decimal_to_bcd(number2)
            return answer

    def from_binary(self, type_of_number, type_of_number2, number):
        if type_of_number == "Binary" and type_of_number2 == "Binary":
            return number

        elif type_of_number == "Binary" and type_of_number2 == "Decimal":
            number = int(number)
            answer = self.binary_to_decimal(number)
            return answer

        elif type_of_number == "Binary" and type_of_number2 == "Octal":
            number = int(number)
            number2 = self.binary_to_decimal(number)
            answer = self.decimal_to_octal(number2)
            return answer

        elif type_of_number == "Binary" and type_of_number2 == "Hexadecimal":
            number = int(number)
            number2 = self.binary_to_decimal(number)
            answer = self.decimal_to_hex(number2)
            return answer

        elif type_of_number == "Binary" and type_of_number2 == "Hexadecimal":
            number = int(number)
            number2 = self.binary_to_decimal(number)
            answer = self.decimal_to_hex(number2)
            return answer

        elif type_of_number == "Binary" and type_of_number2 == "Excess 3":
            number = int(number)
            number2 = self.binary_to_decimal(number)
            answer = self.decimal_to_excess(number2)
            return answer

        elif type_of_number == "Binary" and type_of_number2 == "Gray":
            number = int(number)
            number2 = self.binary_to_decimal(number)
            answer = self.decimal_to_gray(number2)
            return answer

        elif type_of_number == "Binary" and type_of_number2 == "BCD":
            number = int(number)
            number2 = self.binary_to_decimal(number)
            answer = self.decimal_to_bcd(number2)
            return answer

    def from_hexadecimal(self, type_of_number, type_of_number2, number):
        if type_of_number == "Hexadecimal" and type_of_number2 == "Hexadecimal":
            return number

        elif type_of_number == "Hexadecimal" and type_of_number2 == "Decimal":
            answer = self.hex_to_decimal(number)
            return answer

        elif type_of_number == "Hexadecimal" and type_of_number2 == "Binary":
            number2 = self.hex_to_decimal(number)
            answer = self.decimal_to_binary(number2)
            return answer

        elif type_of_number == "Hexadecimal" and type_of_number2 == "Octal":
            number2 = self.hex_to_decimal(number)
            answer = self.decimal_to_octal(number2)
            return answer

        elif type_of_number == "Hexadecimal" and type_of_number2 == "Excess 3":
            number2 = self.hex_to_decimal(number)
            answer = self.decimal_to_excess(number2)
            return answer

        elif type_of_number == "Hexadecimal" and type_of_number2 == "Gray":
            number2 = self.hex_to_decimal(number)
            answer = self.decimal_to_gray(number2)
            return answer

        elif type_of_number == "Hexadecimal" and type_of_number2 == "Gray":
            number2 = self.hex_to_decimal(number)
            answer = self.decimal_to_bcd(number2)
            return answer

    def from_excess(self, type_of_number, type_of_number2, number):
        if type_of_number == "Excess 3" and type_of_number2 == "Excess 3":
            return number

        elif type_of_number == "Excess 3" and type_of_number2 == "Decimal":
            answer = self.excess_to_decimal(number)
            return answer

        elif type_of_number == "Excess 3" and type_of_number2 == "Binary":
            number2 = self.excess_to_decimal(number)
            answer = self.decimal_to_binary(number2)
            return answer

        elif type_of_number == "Excess 3" and type_of_number2 == "Octal":
            number2 = self.excess_to_decimal(number)
            answer = self.decimal_to_octal(number2)
            return answer

        elif type_of_number == "Excess 3" and type_of_number2 == "Hexadecimal":
            number2 = self.excess_to_decimal(number)
            answer = self.decimal_to_hex(number2)
            return answer

        elif type_of_number == "Excess 3" and type_of_number2 == "Gray":
            number2 = self.excess_to_decimal(number)
            answer = self.decimal_to_gray(number2)
            return answer

    def from_gray(self, type_of_number, type_of_number2, number):
        if type_of_number == "Gray" and type_of_number2 == "Gray":
            return number

        elif type_of_number == "Gray" and type_of_number2 == "Decimal":
            answer = self.gray_to_decimal(number)
            return answer

        elif type_of_number == "Gray" and type_of_number2 == "Binary":
            number2 = self.gray_to_decimal(number)
            answer = self.decimal_to_binary(number2)
            return answer

        elif type_of_number == "Gray" and type_of_number2 == "Octal":
            number2 = self.gray_to_decimal(number)
            answer = self.decimal_to_octal(number2)
            return answer

        elif type_of_number == "Gray" and type_of_number2 == "Hexadecimal":
            number2 = self.gray_to_decimal(number)
            answer = self.decimal_to_hex(number2)
            return answer

        elif type_of_number == "Gray" and type_of_number2 == "Excess 3":
            number2 = self.gray_to_decimal(number)
            answer = self.decimal_to_excess(number2)
            return answer

        elif type_of_number == "Gray" and type_of_number2 == "BCD":
            number2 = self.gray_to_decimal(number)
            answer = self.decimal_to_bcd(number2)
            return answer

    def from_bcd(self, type_of_number, type_of_number2, number):
        if type_of_number == "BCD" and type_of_number2 == "BCD":
            return number

        elif type_of_number == "BCD" and type_of_number2 == "Decimal":
            answer = self.bcd_to_decimal(number)
            return answer

        elif type_of_number == "BCD" and type_of_number2 == "Binary":
            number2 = self.bcd_to_decimal(number)
            answer = self.decimal_to_binary(number2)
            return answer

        elif type_of_number == "BCD" and type_of_number2 == "Octal":
            number2 = self.bcd_to_decimal(number)
            answer = self.decimal_to_octal(number2)
            return answer

        elif type_of_number == "BCD" and type_of_number2 == "Hexadecimal":
            number2 = self.bcd_to_decimal(number)
            answer = self.decimal_to_hex(number2)
            return answer

        elif type_of_number == "BCD" and type_of_number2 == "Excess 3":
            number2 = self.bcd_to_decimal(number)
            answer = self.decimal_to_excess(number2)
            return answer

        elif type_of_number == "BCD" and type_of_number2 == "Gray":
            number2 = self.bcd_to_decimal(number)
            answer = self.decimal_to_gray(number2)
            return answer
