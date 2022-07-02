from collections import defaultdict
from heapq import nlargest
def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s) - 1
    i = 0
    while i < n:
        s[n], s[i] = s[i], s[n]
        i += 1
        n -= 1
    return s

def validate(ip):
    adr = ip.split('.')

    if len(adr) != 4:
        return False
    for slice in adr:
        if not slice.isdigit():
            return False
        if int(slice) < 0 or int(slcie) > 255:
            return False
    return True






# if __name__ == "__main__":
    key_value = {}
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    list = sorted(key_value.items(), key=lambda item: item[1])
    print(list)
    # for i in d:
    #    print(key_value[i])
    print(key_value.items())

# for a list array=[['D'],['A','B'],['A','C'],['C','A']] find the number of followers
# Ans
# D=0
# A=2
# c=1
    friends = [['D'],['A','B'],['A','C'],['C','A']]
    hashset = {}
    for f in friends:
        if len(f) == 1 and f[0] not in hashset:
            hashset[f[0]] = 0
        elif len(f) == 2:
            hashset[f[0]] = hashset.get(f[0], 0) + 1

    print(hashset)

    # Replace None with previous element from List, there was some challenges
    # [1,4,None,None,3]
# find the index of
    state = 'missisipi'
    res = []
    for i, s in enumerate(state):
        if s == 's':
            res.append(i)
    print(res)
# Uncommon words from two sentences
    A = "Geeks for Geeks"
    B = "Learning from Geeks for Geeks"

    alist = set(A.split(' '))
    blist = set(B.split(' '))
    res = []
    for l in blist:
        if l not in alist:
            res.append(l)
    print(res)

# Given a ´dictionary, print the key for nth highest value present in the dict.
# Group Similar items to Dictionary Values List
# input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
# Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
    test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
    dict = defaultdict(list)
    for i in test_list:
        if i not in dict:
            dict[i] = [i]
        else:
            dict[i].append(i)
    print(dict)
# Group Similar keys in dictionary
# initializing Dictionary
    test_dict = {'gfg1' : 1, 'is1' : 2, 'best1' : 3,
                'gfg2' : 9, 'is2' : 8, 'best2' : 7,
                'gfg3' : 10, 'is3' : 5, 'best3' : 6}

















