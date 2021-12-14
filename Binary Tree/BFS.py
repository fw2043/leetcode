#### BFS(Breath First Search)

##############################
# For Tree
#################################################
"""
不需要分层遍历
"""

from collections import deque
def level_order_tree(root, result):
    if not root:
        return

    # initialize queue:
    queue = deque([root])

    while queue:
        node = queue.popleft()
        # do something
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


"""
需要分层遍历
"""


def loevel_order_tree(root):
    if not root:
        return
    q = deque([root])
    while q:
        new_q = []
        for node in q:
            # DO something with this layer nodes............
            if node.left:
                new_q.append(node.left)
            if node.right:
                new_q.append(node.right)

        q = new_q
    return xxxx

##############################
# For Graph
#################################################

"""
不需要分层遍历
"""
def bfs_graph(root):
    if not root:
        return
    # queue和seen为一对好基友，同时出现
    queue = deque([root])
    # seen避免图遍历过程中重复访问的情况，导致无法跳出循环
    seen = set([root])

    while queue:
        head = queue.popleft()
        # do something with the head nodes
        # add head's neighbors into queue list:
        for neighbor in head.negihbors:
            if neighbor not in seen:
                queue.append(neighbor)
                seen.add(neighbor)

    return xxxx

"""
需要分层遍历
"""
def bsf_graph(root):
    if not root:
        return
    queue = [root]
    seen = set([root])
    while queue:
        new_queue = []
        for node in queue:
            # do somethins with the node
            for neighbor in node.neighbors:
                if neighbor not in seen:
                    new_queue.append(neighbor)
                    seen.add(neighbor)
    return xxx






























