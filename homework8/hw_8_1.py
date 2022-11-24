def to_camel_case(array: str) -> str:
    new_array = array.replace("-"," ").replace("_", " ").split()
    if len(new_array) == 0:
        return "Error"
    return new_array[0] + "".join([x.capitalize() for x in new_array[1:]])
print(to_camel_case("the-stealth-warrior"))