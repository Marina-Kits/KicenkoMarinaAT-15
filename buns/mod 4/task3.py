def euclid_algorithm(a,b):
    if a == b:
        return a
    if a<b:
        return euclid_algorithm(a,b-a)
    return euclid_algorithm(a-b,b)
print(euclid_algorithm(7975,2585))
print(euclid_algorithm(2585,7975))