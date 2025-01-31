def my_function(x):
    if x == 0:
        return 0
    elif x < 0:
        return 0  # Handle negative inputs
    else:
        return x + my_function(x - 1)

print(my_function(5))
print(my_function(-3)) #test for negative input
print(my_function(1000)) #test for a large number