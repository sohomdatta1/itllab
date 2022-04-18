class String_man:
    def __init__(self) -> None:
        self.str=""
    def get_string(self):
        self.str = input("Enter string: ")
    def to_upper(self):
        for i in range(0, len(self.str)):
            if ord(self.str[i]) >= 0x61 and ord(self.str[i]) <= 0x7a:
                self.str = self.str[:i] + chr(ord(self.str[i]) - 0x20) + self.str[i+1:]
    def print_string(self):
        print(self.str)
a = String_man()
a.get_string()
a.to_upper()
a.print_string()