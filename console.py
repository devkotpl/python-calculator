class Console:
    def writeLine(self, text: str):
        print(text)

    def readLine(self, prompt):
        return input(prompt)

    def read_number_from_console(self, prompt):
        return int(input(prompt))