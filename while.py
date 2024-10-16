total_sum = 0
last_number = 0
i = 1

while total_sum  <= 10000:
    total_sum += i
    last_number = i
    i += 1
print(last_number)        
print(total_sum)