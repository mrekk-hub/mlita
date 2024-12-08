import string


class SyntaxAnalyzer:
    def __init__(self, input_string):
        self.__index = -1
        self.__string = input_string
        self.ch = ''
        self.read()

    def read(self):
        if self.__index + 1 < len(self.__string):
            self.__index += 1
            self.ch = self.__string[self.__index]
        else:
            self.ch = "success"

    def error(self, message):
        raise ValueError(f"Error: {message}")

    def pcz(self):
        if self.ch in string.ascii_lowercase:
            self.read()
            self.pb1()
        elif self.ch == '(':
            self.read()
            self.pcz()
            if self.ch == ')':
                self.read()
                self.pkr()
            else:
                self.error("Missing closing parenthesis ')'")
        elif self.ch == '[':
            self.read()
            self.pcz()
            if self.ch == ']':
                self.read()
                self.pkv()
            else:
                self.error("Missing closing bracket ']'")
        else:
            self.error("Unexpected character in pcz()")

    def pb1(self):
        if self.ch in string.ascii_lowercase:
            self.read()
            self.pb2()
        elif self.ch == '(':
            self.read()
            self.pcz()
            if self.ch == ')':
                self.read()
                self.pkr()
            else:
                self.error("Missing closing parenthesis ')'")
        elif self.ch == '[':
            self.read()
            self.pcz()
            if self.ch == ']':
                self.read()
                self.pkv()
            else:
                self.error("Missing closing bracket ']'")
        elif self.ch in "+-/":
            self.read()
            self.ps()
        else:
            self.error("Unexpected character in pb1()")

    def pb2(self):
        while self.ch in string.ascii_lowercase:
            self.read()
        if self.ch == '(':
            self.read()
            self.pcz()
            if self.ch == ')':
                self.read()
                self.pkr()
            else:
                self.error("Missing closing parenthesis ')'")
        elif self.ch == '[':
            self.read()
            self.pcz()
            if self.ch == ']':
                self.read()
                self.pkv()
            else:
                self.error("Missing closing bracket ']'")
        elif self.ch in "+-/":
            self.read()
            self.ps()

    def ps(self):
        if self.ch in string.ascii_lowercase:
            self.read()
            self.pb2()
        elif self.ch == '(':
            self.read()
            self.pcz()
            if self.ch == ')':
                self.read()
                self.pkr()
            else:
                self.error("Missing closing parenthesis ')'")
        elif self.ch == '[':
            self.read()
            self.pcz()
            if self.ch == ']':
                self.read()
                self.pkv()
            else:
                self.error("Missing closing bracket ']'")

    def pkr(self):
        if self.ch == '[':
            self.read()
            self.pcz()
            if self.ch == ']':
                self.read()
                self.pkv()
        elif self.ch in "+-/":
            self.read()
            if self.ch == '[':
                self.read()
                self.pcz()
                if self.ch == ']':
                    self.read()
                    self.pkv()
            else:
                self.error("Expected '[' after operator in pkr()")

    def pkv(self):
        if self.ch == '(':
            self.read()
            self.pcz()
            if self.ch == ')':
                self.read()
                self.pkr()
            else:
                self.error("Missing closing parenthesis ')' in pkv()")
        elif self.ch in "+-/":
            self.read()
            if self.ch == '(':
                self.read()
                self.pcz()
                if self.ch == ')':
                    self.read()
                    self.pkr()
                else:
                    self.error("Missing closing parenthesis ')' in pkv()")

    def main(self):
        try:
            self.pcz()
        except ValueError as e:
            print(f"Result: ERROR ({e})")
        else:
            if self.ch == "success":
                print("Result: OK")


if __name__ == "__main__":
    while True:
        try:
            syntax_analyzer = SyntaxAnalyzer(input("Insert string: "))
            syntax_analyzer.main()
        except KeyboardInterrupt:
            break
