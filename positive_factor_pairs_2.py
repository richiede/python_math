# Update positive fator pairs
# Takes a number "num" and finds all positive factor pairs

final_list = []

num = 124

for i in range(1, num+1):
    if num % i == 0:
        temp_list = sorted([int(num/i), int(i)])
        if temp_list not in final_list:
            final_list.append(temp_list)
    return(final_list)
