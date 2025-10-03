squares = [x**2 for x in range(1, 11)]
print(squares)

even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print(even_numbers)

words = ['python', 'Java', 'c++', 'Rust', 'go']
upper_long_words = [word.upper() for word in words if len(word) > 3]
print(upper_long_words)