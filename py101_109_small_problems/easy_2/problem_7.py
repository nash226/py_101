def xor(arg1, arg2):
    
    if arg1 and not arg2:
        return True
    elif not arg1 and arg2:
        return True
    elif not arg1 and not arg2:
        return False
    else:
        return False





print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)