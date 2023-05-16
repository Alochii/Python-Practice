#dividing by zero exception:
try : 
    attempt = 10/0
    print(int(input("put your number here")))
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
except : 
    print("some random ass error")