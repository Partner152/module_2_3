my_list = [42 , 69 , 322 , 13 , 0 , 99 , -5 , 9 , 8 , 7 , -6 , 5 ]
start_number = 0
while len(my_list)>start_number:
    if my_list[start_number] > 0:
        print(my_list[start_number])
    if my_list[start_number] < 0:
        break
    start_number += 1