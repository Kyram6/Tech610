print('Hello World')

def shout(thing_to_shout):
    loud_thing = thing_to_shout.upper()
    print(loud_thing)

shout('hello')

def triple_and_halve_minus_one(num):
    num_tripled = num * 3
    halved = num_tripled / 2
    result = halved - 1
    return result


res = triple_and_halve_minus_one(10)
print(res)

def add (a,b):
    return a + b
print(add(1,2))

def subtract (a,b):
    return a - b
print(subtract(3,2))

def multiply(a, b):
    return a * b
print(multiply(5,4))

def divide(a, b):
    return a / b
print(divide(10,5))

# weight in stones from pounds
def pounds_to_stones(pounds):
    return pounds / 14
print(pounds_to_stones((150)))
#10.7 st

# weight in stones from pounds
def stones_to_pounds(stones):
    return stones * 14
print(stones_to_pounds(10.7))
#149.79

# celcius to farenheit
def cel_to_fa(celcius):
    return (celcius * 1.8) + 32
print(cel_to_fa(20))
#68

# farenheit to celcius
def fa_to_cel(farenheit):
    return(farenheit - 32) / 1.8
print(fa_to_cel(68))
#20

#weight in pounds from stones and pounds (named parameters)
def stones_and_pounds_to_pounds(*, stones=0, pounds=0):
    return (stones * 14) + pounds
print(stones_and_pounds_to_pounds(stones=10,pounds=5))
#145

# testing
import unittest
def pounds_to_stones(pounds):
    return pounds / 14
def stones_to_pounds(stones):
    return stones * 14
def cel_to_fa(celcius):
    return (celcius * 1.8) + 32
def fa_to_cel(farenheit):
    return(farenheit - 32) / 1.8

class TestConverters(unittest.TestCase):

    #pounds to stones
    def test_pounds_to_stones(self):
        self.assertEqual(pounds_to_stones(14), 1)
        self.assertEqual(pounds_to_stones(28), 2)

    def test_stones_to_pounds(self):
        self.assertEqual(stones_to_pounds(5),70)

    def test_cel_to_fa(self):
        self.assertEqual(cel_to_fa(2),35.6)
if __name__ == "__main__":
    unittest.main()

def test_stones_to_pounds():
    result = stones_to_pounds(10)
    expected = 140
    assert result == expected


