'''
Your task is to write a function that receives as its single argument a string 
that contains numbers delimited by single spaces. Each number has a single 
alphabet letter somewhere within it.

Example : "24z6 1x23 y369 89a 900b"
As shown above, this alphabet letter can appear anywhere within the number. 
You have to extract the letters and sort the numbers according to their 
corresponding letters.

Example : "24z6 1x23 y369 89a 900b" will become 89 900 123 369 246 (ordered 
according to the alphabet letter)
Here comes the difficult part, now you have to do a series of computations on 
the numbers you have extracted.

The sequence of computations are + - * /. Basic math rules do NOT apply, you 
have to do each computation in exactly this order.
This has to work for any size of numbers sent in (after division, go back to 
addition, etc).
In the case of duplicate alphabet letters, you have to arrange them according 
to the number that appeared first in the input string.
Remember to also round the final answer to the nearest integer.

Examples :
"24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299
"24z6 1z23 y369 89z 900b" = 900 + 369 - 246 * 123 / 89 = 1414
"10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60
Good luck and may the CODE be with you!
'''

def do_math(s) :
    import re

    print(f'\nInput string: {s}\n')

    s1 = s.split() # Split s into list
    
    # Iterate through list and add words as tuple to new list
    #   ord(<letter>) as first item
    s_tups = []

    for item in s1:
        
        index = re.search("[a-zA-Z]", item).start()
        s_tups.append((item[index],int(item.replace(item[index], ''))) )
        # print(f'\nWorking on {item}. Index = {index}, tuple = {s_tups[-1]}')
    
    print(f's_tups = {s_tups}')

    # Order touples into list according to tuple[0]
    def sort_crit(e):
        return e[0]
    
    s_tups.sort(key=sort_crit)
    print(f's_tups = {s_tups}')

    # Perform math operations in repeating order + - * /
    
    
    ret = 0
    count = 0
    for num in s_tups:
        if count == 0: # Start with first item
            ret = s_tups[0][1]
            count += 1
        elif count == 1:
            print(f'{ret} + {num[1]} = {ret + num[1]}')
            ret += num[1]
            count += 1
        elif count == 2:
            print(f'{ret} - {num[1]} = {ret - num[1]}')
            ret -= num[1]
            count += 1
        elif count == 3:
            print(f'{ret} * {num[1]} = {ret * num[1]}')
            ret *= num[1]
            count += 1
        elif count == 4:
            print(f'{ret} / {num[1]} = {ret /num[1]}')
            ret /= num[1]
            count = 1
        else:
            print("Something went wrong dude!!!")

    # Return rounded result
    return int(round(ret,0))


# Examples :
print(do_math("24z6 1x23 y369 89a 900b")) # = 89 + 900 - 123 * 369 / 246 = 1299
print(do_math("24z6 1z23 y369 89z 900b")) # = 900 + 369 - 246 * 123 / 89 = 1414
print(do_math("10a 90x 14b 78u 45a 7b 34y")) # = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60