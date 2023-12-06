class String:
    def __init__(self, value):
        self.value = str(value)

    def get_length(self):
        return len(self.value)

    def reverse(self):
        return self.value[::-1]

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.value if char in vowels)

    def to_uppercase(self):
        return self.value.upper()

    def has_substring(self, substring):
        return substring in self.value

my_string = String("Hello, World!")
print("Original String:", my_string.value)
print("Length:", my_string.get_length())
print("Reversed:", my_string.reverse())
print("Vowel Count:", my_string.count_vowels())
print("Uppercase:", my_string.to_uppercase())
print("Contains 'World':", my_string.has_substring("World"))

