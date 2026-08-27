from pytest import mark
from pytest import fixture


@mark.fixture_smoke
def test_cart_firstTestcase(cart_secondTestcase):
    assert 1 + 2 == 3
    print("1순위")
    
@fixture()
def cart_secondTestcase():
    assert [1,2] == [1,2]
    print("0순위")
    yield
    print("2순위")

@mark.fixture_smoke
def test_cart_thirdTestcase():
    assert "i am" == "i am"
    print("마지막")