def divisor(num):
    lst_divisors = [i for i in range(1,num) if num%i==0]
    return lst_divisors


find_divisors = int(input("Enter the number to find its divisors - "))

print(divisor(find_divisors))