def greet(name:str):
    print("Hello", name +'.')
greet("Giang")
def square(i:int):
    print("Your number square is: ", i*i)
square (2)
def max_of_two(x, y:int): # type: ignore
    if x>y:
         print("The bigger number is: ", x) # type: ignore
    else:
        print("The bigger number is: ", y)
max_of_two(2, 4)