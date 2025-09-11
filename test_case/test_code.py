# pytest keyword is ( Assert ) 
# using for automation test and realtime to rise pull request in github to merge our code only test cases are passed

from code_logic import divide

def test_divide_regular():
    assert divide(6,2) == 3.0 # -------> to fixed ,if output is 3.0 test passed ,else failed
                                # using  -------> Assert <-------- keyword
test_divide_regular()
