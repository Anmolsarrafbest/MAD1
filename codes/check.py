import pytest

def square(x):
    sum=0
    for c in range(x):
        sum+=x
        return sum
print(square(5))
@pytest.mark.marker1
def test1():
    assert square(13)==144

@pytest.mark.marker2
def test2():
    assert square(6)==6

@pytest.mark.marker3
def test3():
    assert square(3)==9
