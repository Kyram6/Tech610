#1.
def is_even(number):
    return number % 2 == 0

#2.
def get_initials(name):
    words = name.split()
    result = ""
    for word in words:
        result = result + word[0].upper()
    return result

# 3
def find_longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

#4
def filter_even_numbers(numbers):
    result = []

    for n in numbers:
        if n % 2 == 0:
            result.append(n)
    return result

# 5. count vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count = count +1
    return count

# 6. count words
def count_words(sentence):
    words = sentence.lower().split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

    return counts

# 7. most common item

# 8. palindrome

# 9. mask email address

# 10.discount
def calculate_discount(price, discount_percent):
    discount = price * discount_percent / 100
    return price - discount

#11. grade scores
def grade_score(score):
    if score >= 90:
        return "A*"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >=60:
        return "C"
    elif score >=50:
        return "D"
    else:
        return "F"

#12. calculate total cost of shopping basket
def calculate_total_basket(items):
    total = 0
    for items in items:
        price = items[0]
        quantity = items[1]
        total = total + (price * quantity)

    return total

#13. passes and fails
def count_passes_and_fails(scores):
    passes = 0
    fails = 0

    for score in scores:
        if score >= 50:
            passes = passes +1
        else:
            fails = fails + 1

    return {"pass": passes, "fail":fails}

#14. filter odd numbers
def filter_odd_numbers(numbers):
    result = []

    for n in numbers:
        if n % 2 !=0:
            result.append(n)
    return result


#15. shortest words
def find_shortest_word(words):
    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word

    return shortest