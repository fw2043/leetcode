"""
You are given a list of airline tickets where tickets[i] = [fromi, toi]
represent the departure and the arrival airports of one flight.
Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus,
the itinerary must begin with "JFK". If there are multiple valid itineraries,
you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.


Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.


Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""
# confirm that all the value in the list are [depart, to]: tickets[i].length == 2
# consist of uppercase English letters.
# fromi != toi
# You must use all the tickets once and only once.
# return the itinerary that has the smallest lexical order when read as a single string if there are multiple valid itineraries
# All of the tickets belong to a man who departs from "JFK",
# DFS, start from "JFK" until length(path) == length(tickets) + 1

# adjacency list
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # sort tickets so that later the value in the hashmap will be sorted
        tickets.sort()
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            # dfs search the neighbors and pop it out after visit it
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                # if have not found the solution then continue to search,
                # backtracking the decision above, add them back and pop the result
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs('JFK')
        return res
