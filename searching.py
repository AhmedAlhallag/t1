class Searching:
    def __init__(self):
        self.string = None
        self.sub = None

    def set_string_sub(self, string, sub):
        self.string = string
        self.sub = sub

    def subString(self):
        for i in range(len(self.string)-len(self.sub)+1):
            match = True
            for j in range(len(self.sub)):
                if self.string[i+j] != self.sub[j]:
                    match = False
                    break

            if match:
                return True
        return False


# Driver
# s = "bannk"
# sub = "ana"
# s1 = Searching(s, sub)

# print(s1.subString())
