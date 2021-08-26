
def create_phone_number(n):
    first = n.copy()
    first = first[0:3]
    mid = n.copy()
    mid = mid[3:6]
    end = n.copy()
    end = end[6:11]
    first = map(str, first)    
    first = ''.join(first)
    mid = map(str, mid)    
    mid=''.join(mid)
    end = map(str, end)    
    end = ''.join(end)
    fin = (f"({first}) {mid}-{end}")
    print(type(fin))
    print (fin)
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])#, "(123) 456-7890")
create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])#, "(111) 111-1111")
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])#, "(123) 456-7890")
create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])#, "(023) 056-0890")
create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])#, "(000) 000-0000")