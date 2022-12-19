def get_equal(array: str) -> bool:
    if array.lower().count("x") == array.lower().count("y"):
        return True
    else:
        return False

print(get_equal("xxoo"))