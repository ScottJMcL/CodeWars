def two_sum(n, t):
    '''
    Write a function that takes an array of numbers (integers for the tests) and 
    a target number. It should find two different items in the array that, when 
    added together, give the target value. The indices of these items should 
    then be returned in a tuple / list (depending on your language) like so: 
    (index1, index2).

    For the purposes of this kata, some tests may have multiple answers; any 
    valid solutions will be accepted.

    The input will always be valid (numbers will be an array of length 2 or 
    greater, and all of the items will be numbers; target will always be the 
    sum of two different items from that array).
    '''
    print(f'numbers = {n} \nTarget = {t}')
    
    for num in n:
        index = n.index(num) + 1
        for num2 in n:
            if num + num2 == t:
                if num == num2 and n.count(num) ==1:
                    continue
                else:
                    print(f'num = {num}, num2 = {num2}')
                    index1 = n.index(num)
                    n.remove(num)
                    index2 = n.index(num2) + 1
                    return (index1, index2)
            else:
                index += 1
