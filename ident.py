def get_summ(one, two, delimiter='&'):
    string1 = one
    string2 = two
    a = f"{string1}{delimiter}{string2}"
    return a

a = get_summ("Learn", "python") 
print(a)


    
