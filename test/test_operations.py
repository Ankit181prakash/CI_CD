from src.operations import add,sub
def test_add():
    assert add(3,4)==7
    assert add(5,3)==8
    assert add(8,8)==16
    
    
    
def test_sub():
    assert sub(3,3)==0
    assert sub(3,2)==1
    assert sub(7,8)==-1
    