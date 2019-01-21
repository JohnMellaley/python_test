"""def is_even(number):
    return number%2==0
    
def number_of_evens(numbers):
    evens = sum([1 for n in numbers if is_even(n)])
    return False if evens == 0 else is_even(evens)"""


def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection,item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)

def test_in_between(lower,higher,item):
    assert item >= lower and item <= higher, "{0} is not between {1} and {2}".format(item, lower, higher)
    
#test_are_equal(number_of_evens([1,2,4,9,6]), False)
#test_are_equal(number_of_evens([1,2,4,9]), True)
#test_is_in([5,4,3,2,1],6)
#test_is_in([5,4,3,2,1],1)
#test_not_in([5,4,3,2,1],6)
#test_not_in([5,4,3,2,1],1)
#test_not_equal(4,3)
# test_not_equal(2,2)

#test_in_between(1,5,3)
#test_in_between(1,5,6)