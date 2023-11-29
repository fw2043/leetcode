# 1. get the max of the given number
# 2. Frequencies of dict values

"""
Python：
1. 给一个只包括digital的string，比如“10001”，返回这个string可能对应的最大的数字，11000。
2. 给定一个dictionary，key是书名，value是对应的themes，比如 ｛book1：［theme 1， theme‍‍‌‍‍‌‍‌‍‌‌‌‌‍‌‍‍‍‌ 2，theme3］，book2:［theme 3， theme4]}，返回出现次数最多的theme: theme3
3. 给定一个list of Meetings， e.g. [Meeting(audience=10, starttime=1, endtime=4), Meeting[audience=30, starttime=3, endtime=6), ...],  求max number of audiences who are in meetings at the same time.
4. 给定一个list shelves; [2, 4, 3, 6], value 表示对应层数的shelf 的width，然后给定一个list of books: [3, 1，2], value对应的是书的厚度， 求是否可以把所有的书都放到shelves上， True or False
5. 给定一个dictionary: {1: [2,3, 4], 2: [4, 5]....}, 每一对key-value pair表示某个人给其他人发了friend invite, 比如 user 1 给 user 2，3， 4发了invite，问题： find the users who are N edges away from the customers who didn't recieve any invite.
SQL：
给了四个table： author，customer，book，transaction，围绕这四个table写query，时间久了，问题的顺序有可能不完全对
1. Find customers ‍‌‍‌‌‌‍‌‍‍‌‍‍‌‍‍‌‌‍‌who purchased from the same author with at least two categories and the total sales of these books
2. Rank customers by the sales by who they invited. (这个问题不好理解）
3. For each customer, find the total number of books and total number of unique books they purchased
4. Find authors who have a url starting with "https//" but have no sales over the total number of authors
5. Find top two months with unique customers who made purchases this month and the previous month
"""