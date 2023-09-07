def fibonnaci_series(usr_num):
    first_num = 1
    second_num = 1
    fibo_list = []
    fibo_list.append(first_num)
    fibo_list.append(second_num)
    count = 0
    while(count<usr_num):
        curr_num = first_num + second_num
        first_num = second_num
        second_num = curr_num
        fibo_list.append(curr_num)
        count+=1
    
    print("Fibonaci series - ", fibo_list)


num = int(input("Enter the number of fibo - "))

fibonnaci_series(num)