# print("hello world")
# print("Hello there")
# print("I am", 32, "years old")

# name = input('Enter your name, please: ')
# print(name)

# value = input('Enter a number: ')
# other = input('Enter another: ')

# print(value + other) # gives 34
# print(int(value) + int(other)) # gives 7

# age = input('Please input your age: ')
# print('You will be', int(age) + 1, 'years old next year')

# pi = 3.14159
# r = 10
# print("Circle Area is:", pi*r**2)

# b = 10
# h = 2
# b_str = str(b)
# print("Perimiter is:", b*2 + h*2)
# print("Perimiter in base 6 is:", (int(b_str[0])*6 + int(b_str[1]))*2 + h*2)

# vary = 3.75
# print("Id:", id(vary), "Type: ", type(vary), "Value:", vary)
# vary = vary + 20
# print("Id:", id(vary), "Type: ", type(vary), "Value:", vary)

# listy = []
# print(id(listy), type(listy), listy)
# listy.append(300)
# print(id(listy), type(listy), listy)

# hrs_slept = [6.2, 7, 8, 5, 6.5, 7.1, 8.5]
# mean_slept = sum(hrs_slept) / len(hrs_slept)
# print(hrs_slept)
# print(mean_slept)

# num = 297
# if (num % 3) == 0:
#     print(num, 'is divisible by three')
# else:
#     print(num, "isn't divisible by three")

# print("Two raised to the tenth power is", 2**10)

# def leap(yr):
#     if (yr % 4) == 0 and (yr % 100) != 0:
#         return True
#     elif (yr % 400) == 0:
#         return True
#     else:
#         return False

# years = [1800, 1900, 1903, 2000, 2002, 2018]
# for yr in years:
#     print("Is", yr, "a leap year?", leap(yr))

# What is this... text?
# unicode_snake = "I love to poke the \N{SNAKE}"
# print(unicode_snake)

# slash_t = r'\tText \\'
# print(slash_t)

# Playing with formats
# print("Name: {:-^12}".format("Matej"))
# print("Name: {:-^12}".format("Kathleen"))
# print("Name: {:-^4}".format("Kathleen"))

# some binary and hex conversions
# print("Binary of {0} is: {0:b}".format(12))
# print("Hex of {0} is: {0:X}".format(12))
# print("Unicode of {0} is: {0:c}".format(12))
# print("Decimal of {0} is: {0:n}".format(12))
# print("Octal of {0} is: {0:o}".format(12))
# print("Percentage of {0} is: {0:%}".format(0.05))

# F strings
# name = 'mAtej'
# print(f'My name is {name.capitalize()}')
# print(f'Square root of two: {2**0.5:5.3f}')
# print(f'Square root of two: {2**0.5:4.3f}')
# print(f'Square root of two: {2**0.5:2.3f}')
# print(f'Square root of two: {2**0.5:5.4f}')
# print(f'Square root of two: {2**0.5:5.2f}')

# age = 32
# print(f'{name.capitalize()} is {age}')

# paragraph = """
# 	"Python is a great language!", said {}.
# 	"I don't even remember having thus much fun before."
# """.format(name.capitalize())
# print(paragraph)

# print('At the end there is just \N{GREEK CAPITAL LETTER OMEGA}')
# print('At the end there is just \u03A9')

# item = 'car'
# cost = 13499.99

# print('{:<10} {:>10,.2f}'.format(item, cost))

# print(dir('Matej'))
# print(help('Matej'.find))
# print(help('Matej'.title))

# age = 32
# print(dir(age))
# print(help(age.numerator))

#f_name = 'something_something.txt'
#print('Does it end with txt: {}'.format(f_name.endswith('.txt')))
#print('Does it have a thing: {}'.format(f_name.find('thing')))

#school = 'Pavleka Miskine'
# print(help(str))

#country = 'usa'
#correct_country = country.upper()
# print(correct_country)

# filename = 'hello.py'
# print('Does it end with java? {}'.format(filename.endswith('.java')))
# print('Location of index of py is at: {}'.format(filename.find('py')))
# print('Does it start with world: {}'.format(filename.startswith('world')))
