
def add_numbers(start, end):
    c =0
    for number in range(start, end+1):
        #print(number)
        c=c+number
    return c



test1=add_numbers(1,5)
print(test1)
def add_numbers2(start, end):
    c =0
    for number in range(start, end+1,2):
        print(number)
        c=c+number
    return c
