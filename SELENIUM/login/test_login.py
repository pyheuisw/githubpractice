from pytest import mark

def test_login_firstTestcase():
    assert 1 + 2 == 3
    
@mark.fixture_smoke
def test_login_secondTestcase():
    assert [1,2] == [1,2,3]
    print("0순위")

def test_login_thirdTestcase():
    assert "i am" == "i am QAMilestone"

