a_list = [1,2,3,4,5]
for index, elem in enumerate(a_list):
    if (index+1 < len(a_list) and index - 1 >= 0):
        prev_el = str(a_list[index-1])
        curr_el = str(elem)
        next_el = str(a_list[index+1])
        print(prev_el, curr_el, next_el)
