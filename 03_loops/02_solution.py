n = 10
sum_even = 0

for i in range(n+1):
    if i%2 == 0:
        print(i)
        sum_even += i
        

print("Total Sum is ", sum_even)