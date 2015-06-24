#!usr/local/bin/python3


# a "void function" does not return anything
# if there is no return called (conditional is not met) then python returns 
# the value "None"
def add(a, b):
    return a + b
    print("hello")  # this is an example of dead code - it will not run after the return statement
    if a < 100:
        return a + b
    elif a > 200:
        return a - b
    print("add was called", a, b)

add(1, 2)

# without capturing the return value in a variable, the return value will get 
# discarded
sum = add(90, 2)
print(sum)

exit()

completions = 180
attempts = 