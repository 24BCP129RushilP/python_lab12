class String:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value
        return self

    def toLower(self):
        self.value = self.value.lower()

    def toUpper(self):
        self.value = self.value.upper()

    def __str__(self):
        return self.value

# Example usage
s1 = String("Hello")
s2 = String(" World")
s1 += s2
print("Concatenated String:", s1)
s1.toLower()
print("Lowercase String:", s1)
s1.toUpper()
print("Uppercase String:", s1)