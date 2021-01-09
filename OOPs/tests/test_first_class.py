import pytest
from ..oop.firstclass import Dog


class Test_Dog:
    @pytest.mark.parametrize("name,age", [("miller", 6), ("lucy", 5)])
    def test_1(self, name, age):
        new_Dog = Dog(name, age)
        assert new_Dog.name == name
        assert new_Dog.age == age
