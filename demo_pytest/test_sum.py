import pytest
import sum

# type 1
def test_sum1():
    assert sum.add(5, 6) == 11
    
 # type 2
@pytest.mark.parametrize('a,b,expected', [(3, 5, 8)])  # () is a tuple
def test_sum(a, b, expected):
    assert sum.add(a, b) == expected
    
    
  # type 3
@pytest.fixture
def get_test_data_sum():
    return[(5, -1, 4)]

def test_sum2(get_test_data_sum):
    for data in get_test_data_sum:
        a = data[0]
        b = data[1]
        expected = data[2]
        assert sum.add(a, b) == expected
        
        
# type 4
def test_sum_type():
    assert type(sum.add(5, 6)) is int
