from pytest import mark
from pytest import fixture



# @mark.param_testcase
# @mark.parametrize("number", [1,0,100,-4])
# def test_firfirst(number):
#     assert number > 0
    
@fixture(params=["apple","banana","peach"])
def fruit(request):
    return request.param

@mark.gaga
def test_fruit(fruit):
    print(f"i'm {fruit}")
