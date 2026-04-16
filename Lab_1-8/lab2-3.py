def is_prime(number:int):
    i=1
    j=0
    while i<=number:
        if number%i==0:
            j=j+1
        i=i+1
    if j==2:
        print("True")
    else:
        print("False")
is_prime(1)