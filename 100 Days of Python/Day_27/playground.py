def add(*numbers):
    total = 0
    for n in numbers:
        total+=n
    return total

print(add(1,2,3,4))

def math(**kwargs):
    print(kwargs["num"])
    print(kwargs["ass"])

print(math(num = 24, ass=2123))