def powerfunction (number, power):
    result = 1
    for i in range(power):
        result *= number
    return result

print(powerfunction(3,3))