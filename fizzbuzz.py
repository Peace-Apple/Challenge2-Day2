def fizzbuzz(l1,l2):
    len_1=str(len(l1))
    len_2=str(len(l2))
    comb_len = int(len_1 +len_2)
    
    
    if (comb_len%3 == 0):
        return("Fizz")
    elif (comb_len%5 == 0):
        return("Buzz")
    elif (comb_len%5==0 and comb_len%3==0): 
        return("Fizzbuzz")
    else:
        return("comb_len")

print(fizzbuzz([1,2],[1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,33,33]))
