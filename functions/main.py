# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return 'Hello, ' + name + '!'

greet('Bob')

def add(num1, num2, num3):
    return num1 + num2 + num3

add(5, 3, 2)

def positive(number):
    is_positive = number > 0
    return is_positive

print(positive(2))

def negative(number):
    is_negative = number < 0
    return is_negative

print(negative(0))

