def deep_equals(a, b):
    # Handle primitive types
    if a == b:
        return True
    
    # Handle arrays
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if not deep_equals(a[i], b[i]):
                return False
        return True
    
    # Handle objects
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a.keys()) != set(b.keys()):
            return False
        for key in a.keys():
            if not deep_equals(a[key], b[key]):
                return False
        return True
    
    # Handle NaN
    if a != a and b != b:
        return True
    
    # Handle other cases (None, etc.)
    return False

# Primitive types
print(deep_equals(1, 1)) # True
print(deep_equals('hello', 'hello')) # True
print(deep_equals(True, False)) # False
print(deep_equals(None, None)) # True
print(deep_equals(float('nan'), float('nan'))) # True

# Arrays
print(deep_equals([1, 2, 3], [1, 2, 3])) # True
print(deep_equals([1, 2, 3], [1, 2, '3'])) # False
print(deep_equals([1, {'a': 2, 'b': 3}], [1, {'b': 3, 'a': 2}])) # True

# Objects
print(deep_equals({'a': 1, 'b': 2}, {'a': 1, 'b': 2})) # True
print(deep_equals({'a': 1, 'b': 2}, {'a': 1, 'b': 3})) # False
print(deep_equals({'a': 1, 'b': {'c': 2}}, {'a': 1, 'b': {'c': 2}})) # True

# Other types
print(deep_equals(lambda x: x, lambda x: x)) # False
print(deep_equals(None, [])) # False
