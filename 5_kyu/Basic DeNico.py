'''
Write a function deNico/de_nico() that accepts two parameters:

key/$key - string consists of unique letters and digits
message/$message - string with encoded message
and decodes the message using the key.

First create a numeric key basing on the provided key by assigning each letter 
position in which it is located after setting the letters from key in an 
alphabetical order.

For example, for the key crazy we will get 23154 because of acryz (sorted 
letters from the key).

Let's decode  cseerntiofarmit on   using our crazy key.
1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n   

After using the key:
2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n

Notes

The message is never shorter than the key.
Don't forget to remove trailing whitespace after decoding the message
Examples

deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key" 
'''

def de_nico(key, msg):
    # unsorted key positions correspond to positions of given msg
    # Create columns of the message to match with the sorted key
    # re-construct columns in order of unsorted key

    # crazy


    # crazy --> acryz --> 12345 --> 23154
    # 12345
    # -----
    # cseer
    # ntiof
    # armit
    #  on

    # 23154
    # -----
    # secre
    # tinfo
    # rmati
    # on   
    
    print(f'key = {key}, msg = {msg}')
    
    # create alphabetically sorted key
    key_dict = {}
    for pos,keyChar in enumerate(key.sorted()):
        key_dict[keyChar] = str(pos)
    
    # Get key in numbers 
    newkey = ''
    for item in key:
        newkey = newkey + key_dict[item]
    
    msg_lst = [] # each element represents a column of encrypted message
    for char in msg:
        working = ""
        for letter in key: # each column length corresponds to length of key.
            working = working + char
        msg_lst.append(working)

    ret_lst = [] # Columns sorted to correct order
    for num in newkey:
        ret_lst.append(msg_lst[int(num)])
    
    # read each column into string
    ret = ''
    
