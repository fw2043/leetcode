from collections import Counter
import math
def checkMagine(magine, note):
    a = (Counter(note) - Counter(magine))
    print(a)
    print(Counter(note) & Counter(magine))
    if a == {}:
        return True
    else: return False

def check_notes(magine, notes):
    for note in notes:
        if note not in magine:
            return False
    return True

def socksCheck(my_array):
    res = 0
    # convert to dict
    dict = {}
    for i in my_array:
        dict[i] = dict.get(i, 0) + 1
    print(dict)
    # check pairs
    for value in dict.values():
        res += value // 2
    return res

def move0end(my_list):
    for i in my_list:
        if i == 0:
            # remove the first value in the list
            my_list.remove(0)
            my_list.append(0)
            print(my_list)
    return my_list

def fillNone(my_list):
    if my_list is None:
        return my_list

    if my_list[0] is None:
        my_list[0] = 0

    for i in range(1, len(my_list)):
        if my_list[i] is None:
            my_list[i] = my_list[i-1]

    return my_list

def deleteRecurring(my_List):
    if len(my_List) <= 1:
        return my_List
    new = ''
    # res = []
    for char in my_List:
        if char not in new:
            new += char
    #         res.append(i)
    # return ''.join(res)
    return new

def calculateAvg(sentence):
    if len(sentence) == 0:
        return 0
    # what if the character is '?."!;
    for p in "!?'.,;":
        sentence = sentence.replace(p, "")

    words = sentence.split() # split functio, by default is whitespace
    return round(sum(len(word) for word in words) / len(words), 2)

def isMonotonic(list):
    if all(list[i] <= list[i+1] for i in range(len(list)-1)) or all(list[i] >= list[i+1] for i in range(len(list)-1)):
        return True
    return False

def rotation(list, d):
    d = d % len(list)
    n = len(list)
    list = list[d: n] + list[:d]
    return list

def isValidBraces(string):
    braces = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for char in string:
        if char in braces:
            stack.append(char)
        elif stack and char == braces[stack[-1]]:
            stack.pop()

    return stack == []

def maxCapacity(price_list, money):
    price_list = sorted(price_list)
    max_cnt, total_cnt = 0, 0
    for price in price_list:
        money = money - price
        if money < 0:
            max_cnt = total_cnt # max_cnt equal to the total_cnt we got from the last iteration
            break
        else: total_cnt += 1
    return max_cnt

def avg_length(list1):

    if list1 is None or len(list1) == 0:
        print('empty list')
    else:
        # sum = 0
        # for item in list1:
        #     sum += item
        # avg = round(sum/len(list1), 2)
        avg = round(sum(i for i in list1) / len(list1),2)
        print(avg)

def findNthSale(book_sale):
    book_sale.sort(key=lambda x: (-x[1], x[0]))
    print(book_sale)
    for i, val in enumerate(book_sale):
        if i == n -1 :
            print(val)

def findExtension(titles):
    # first sort the list
    titles.sort(key=lambda a: len(a))
    dict = {}
    for book in titles:
        if book.split()[0] not in dict:
            dict[book.split()[0]] = [book]
        else:
            dict[book.split()[0]].append(book)
    print(dict)
    res = []
    # the first value in the list would be the prefix
    for value in dict.values():
        res += value[1:]
    print(res)

def validate(ip):
    adr = ip.split('.')

    if len(adr) != 4:
        return False
    for slice in adr:
        if not slice.isdigit():
            return False
        if int(slice) < 0 or int(slice) > 255:
            return False
    return True


def isPerfectSquare(x):
    # if x >= 0,
    if (x >= 0):
        sr = int(math.sqrt(x))
        # sqrt function returns floating value so we have to convert it into integer
        # return boolean T/F
        return (sr * sr) == x
    return False






if __name__ == "__main__":

# 1. Sherlock Holmes is solving a case, and he is trying to find out if a Ransom Note belongs to a magazine
    magine1 = ['apgo', 'cim', 'w', 'lxvt', 'bg', 'elo']
    note1 = ['elo', 'bg', 'cim', 'uuiui']
    # is note1 in magine1: no
    magine2 = ['give', 'me', 'one', 'grand', 'today']
    note2 = ['give', 'one', 'today', 'today']
    # is note2 in magine2: yes
    # print(checkMagine(magine1, note1))
    # print(checkMagine(magine2, note2))
    print(check_notes(magine1, note1))
    print(check_notes(magine2, note2))

#2. Help the Merchant to count the number of pair of socks
    my_array1 = [10, 20, 20, 10, 10, 30, 50, 10, 20, 20]
    my_array2 = [10, 20, 20, 30, 50, 10, 20, 20]
    print(socksCheck(my_array1))
    print(socksCheck(my_array2))

#3. Stacking up empty boxes: Amazon workers are trying to stack up empty boxes at the end
    arr1 = [1,0,2,0,2,7,0,12,15]
    result = [1,2,2,7,12,15,0,0,0]
    print(move0end(arr1))

#4. Factory workers fill in missing time entries
    my_array = [1,2,3, None, 4,5, None, 6, None, 7, None, 8,9, None, None]
    res = [1,2,3,3,4,5,5,6,6,7,7,8,9,9,9]
    print(fillNone(my_array))

#5. Given a string as your input, delete any recurring character, and return the new string.
    state = 'mississippi'
    output = 'misp'
    # what if find the index of s:
    res_index = []
    for i,s in enumerate(state):
        if s == 's':
            res_index.append(i)
    print(res_index)

    # set does not have an order
    print(''.join(set(state)))
    # check the list:
    print(deleteRecurring(state))

#6. Essay Exam Competition: Average Word Length in a statement
    my_statement = 'Hello, Python is my favorite programming language of all the other languages'
    avg = 5.33
    print(calculateAvg(my_statement))

#7. Analyze if a stock price has always gone up or always gone down
# determine if a given array is monotimoc array or not?
    list1 = [100, 90, 80, 70, 60, 60,50, 40,40]
    result = True
    list2 = [100, 90, 80, 100, 60, 60]
    result = False
    list3 = [20, 30 ,40 ,40, 60, 80]
    list4 = [20, 40, 40, 30, 50]
    print(isMonotonic(list1))
    print(isMonotonic(list2))
    print(isMonotonic(list3))
    print(isMonotonic(list4))

#8. Write a Python Program to rotate the elements given in a list to the left
    list = [1,2,3,4,5,6,7,8,9,10]
    # rotate the element '3' to their left in a cyclic way tp come up with the output:
    output = [4,5,6,7,8,9,10,1,2,3]
    print(rotation(list, 3))

#9. Grammarly type words and statements checking algo
    # assume only contain characters and '(', ")', "{" or "}, '[], ']'
    string1 = '()'
    string2 = '[{{]'
    string3 = '[{{}}]'
    print(isValidBraces(string1))
    print(isValidBraces(string2))
    print(isValidBraces(string3))

#10. The BOY in the TOY store
# a boy in a toy store, how many maxium number of toys will he be able to buy if he has 80 dollars
    toy_price = [1, 12, 5, 111, 200, 1000, 10]
    print(maxCapacity(toy_price, 80))

#11. Average List
    list1 = [1, 2, 3, 4, 5]
    avg_length(list1)

#12. The Nth highest sale book: given the list of tuple[(price, sale)], and an integer, return book with Nth highest sale
# If more than one, only return the one with lower price
# tuples
    book_sale = [(40, 8), (10, 15), (15, 8), (50, 7), (30, 12), (20, 12)]
    n = 3
    print(book_sale)
    findNthSale(book_sale)
# dictionary
    price_sale = {40: 8, 10: 15, 15: 8, 50: 7, 30: 12, 20: 12}
    # price_sale.items() will be tuple
    list = sorted(price_sale.items(), key=lambda item: (-item[1], item[0]))
    print(list)
    for i, val in enumerate(list):
        if i == n:
            print(val)
            print(val[0])


#13. find the extension books, given the list of book titles, return the list of titles having prefix in the list:
    titles = ["Python 2nd edition", "Python", "Python in a nutshell", "Green Book", "Green Book 3th editon",
              "Green Book new version"]
    findExtension(titles)

#14. find freienship
# for a list array=[['D'],['A','B'],['A','C'],['C','A']] find the number of followers
# Ans
# D=0
# A=2
# c=1
    friends = [['D'], ['A', 'B'], ['A', 'C'], ['C', 'A']]
    hashmap = {}
    for f in friends:
        if len(f) == 0:
            hashmap[f[0]] = 0
        elif len(f) == 2:
            hashmap[f[0]] = hashmap.get(f[0], 0) + 1
    print(hashmap)

#15. Validate IP address
    print(validate('127.0.0.b'))

#16. check if a number is perfect square:
    x = 2502
    if (isPerfectSquare(x)):
        print("Yes")

#17. parse nested json
history = {'messages': [{'_id': '9nZFEADadMtFwEpbR',
'rid': 'GENERAL',
'msg': 'TEST ?',
'ts': '2021-02-16T12:28:47.634Z',
'u': {'_id': 'GudgiP3Am5xgThidg',
'username': 'admin'}, 'mentions': [],
'channels': [],
'_updatedAt': '2021-02-16T12:28:47.655Z'}],
'success': True}

import json
#  conversion to JSON done by dumps() function
x = json.dumps(history)
# print(x)
# json.loads()
jsonDict = json.loads(x)
print(jsonDict['messages'][0]['_id'])

# # 18. Given a list of timestamps in sequential order,
# # return a list of lists grouped by week (7 days) using the first timestamp as the starting point.
# # for example:
# # input = ['2019-01-01','2019-01-02','2019-01-08', '2019-02-01','2019-02-05']
# # output = [['2019-01-01', '2019-01-02'],['2019-01-08'],['2019-02-01', '2019-02-05']]
# from collections import defaultdict
# from datetime import datetime as dt
#
# idx = 0
# dic = defaultdict(list)
# # initialize curr
# curr = input[0]
# for i in input:
#     if ( dt.strptime(i, '%Y-%m-%d') -  dt.strptime(curr, '%Y-%m-%d')).days < 7 :
#          dic[idx].append(i)
#     else:
#         # update curr
#         curr = i
#         idx += 1
#         dic[idx].append(i)
# print(dic.values())

# 18. I have 2 strings, each containing a decimal number, and we can assume they have the same precision.
#https://stackoverflow.com/questions/57426963/adding-2-decimal-numbers-in-strings-retaining-precision
from decimal import *
# str1 = "0.16107000"
# str2 = "0.00000270"
str1 = "-70.00000000"
str2 = "0.00131251"
total =  Decimal(str1) + Decimal(str2)
print("Total is " + str(total))


# 19.
orbit_list = ['OCM)B', 'B)C', 'E9(FG)', '(TYY)']
res = {}
for s in orbit_list:
    for char in s:
        if char in '()':
            res[char] = res.get(char, 0) + 1

print(res)

# 20.  find second maximum value in Dictionary
new_dict = {"google":12, "amazon":9, "flipkart":4, "gfg":13, "netflix":10}
max = max(new_dict.values())

# iterate through the dictionary
max2 = 0
for v in new_dict.values():
    if (v > max2 and v < max):
        max2 = v

# print the second largest value
print(max2)
# set()
# sorted()
print(sorted(set((new_dict.values())))[-2])

# Write a Python program to print Fibonacci Series
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

for i in range(2,5):
  print(F(i))

#  Write a Python program to print a list in reverse
li = [21,1,3,4,5,6,7,8,9,19,34,36,48,50,51]
print(li[::-1])


# split the strings into words without using split method:
s = 'my dog is so cute'
lst = []
word = ''
for char in s:
    if char == " ":
        lst.append(word)
        word = ''

    else:
        word += char

if word:
    lst.append(word)
print(lst)
