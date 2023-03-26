from plates import is_valid 

def test_is_valid():
    assert is_valid("lash4a") == True
    
    
def test_is_not_valid():
    assert is_valid("lasha504") == False