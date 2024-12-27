from src.math_operation import add,sub
def testadd():
    assert add(2,3)==5
    assert add(4,1)==5
    assert add(4,0)==4
    assert add(-1,1)==0

def testsub():
    assert sub(3,2)==1
    assert sub(4,1)==3
    assert sub(4,0)==4
    assert sub(-1,1)==-2