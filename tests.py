from myfile import multiply

def test_pass():
    assert multiply([1,2,3]) == 6
    
def test_fail():
    assert multiply([1,2,3,4]) == 24

if __name__ == '__main__':
    test_pass()
    test_fail()
