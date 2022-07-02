"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person
if there is some common email to both accounts. Note that even if two accounts have the same name,
they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely
have the same name.

After merging the accounts, return the accounts in the following format:
the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
Example 1:
Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.

"""
# DSU (disjoint set union)
# there is no index to build a list for the disjoint set, so we need a dict: use email as key and inialize itself as parent/root
# to get the name of the emails: we need another dict to map email to name,: johnsmith@mail.com: John
# don't need to rank by root
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if x == parents[x]:
                return x
            parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                parents[rooty] = rootx

        parents = {}  # to store the list: key:value == email: parent, initialize the key and value are email themselves
        emailToName = {}  # to map the emails and account name

        for acnt in accounts:
            name = acnt[0]
            for email in acnt[1:]:
                parents[email] = email
                emailToName[email] = name

        # for emails in same acnt, they are connected, need to union
        for acnt in accounts:

            email1 = acnt[1]
            for email2 in acnt[2:]:
                union(email1, email2)

        groups = defaultdict(list)

        for email in parents:
            r = find(email)
            groups[r].append(email)

        ans = []
        for key in groups:
            ans.append([emailToName[key]] + sorted(groups[key]))
        return ans




