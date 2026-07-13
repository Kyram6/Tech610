from TDD.tdd import *

#1. check even number
def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even (4) is True

#2. get intials
def test_get_intials():
    assert get_initials("Kyram T Ngoma") == "KTN"

# 3. find longest word
def test_find_longest_word():
    assert find_longest_word(["dog", "lion", "supercalifragilistic"]) == "supercalifragilistic"

# 4. filter even number
def test_filter_even_numbers():
    assert filter_even_numbers([1,2,3,4,5,6,7]) == [2,4,6]

# 5. count vowels
def test_count_vowels():
    assert count_vowels("AEIOU") == 5
    assert count_vowels("water") == 2

# 6. count words
def test_count_words():
    assert count_words("the crazy crazy cat") == {
        "the": 1,
        "crazy": 2,
        "cat":1
    }
# 7. most common item
def test_common_item():
    assert most_common_item(["lemon", "ham", "bacon", "lemon"]) == "lemon"

def test_common_item():
    assert most_common_item([1,4,3,3,3,6,7]) == 3

# 8. palindrome
def test_is_palindrome():
    assert is_palindrome("rotor") is True
    assert is_palindrome("bed") is False

# 9. mask email address

# 10.discount
def test_calculate_discount():
    assert calculate_discount(100,10) == 90
    assert calculate_discount(100,30) == 70

#11. grade scores
def test_grade_score():
    assert grade_score(90) == "A*"
    assert grade_score(60) == "C"

#12. calculate total cost of shopping basket
def test_calculate_total_basket():
    assert calculate_total_basket([(10,1), (2,5)]) == 20

#13. passes and fails
def test_count_passes_and_fails():
    assert count_passes_and_fails([30,70,20]) == {"pass":1, "fail":2}

#14. filter odd numbers
def test_filter_odd_numbers():
    assert filter_odd_numbers({1,2,3,4,5,6}) == [1,3,5]

#15. shortest words
def test_find_shortest_word():
    assert find_shortest_word(["dog", "lion", "as"]) == "as"
