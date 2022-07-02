# 1. how to parse json file and return the depth of the file:
def depth(x):
    if type(x) is dict and x:
        return 1 + max(depth(x[a]) for a in x)
    if type(x) is list and x:
        return 1 + max(depth(a) for a in x)
    return 0

# https://towardsdatascience.com/how-to-best-work-with-json-in-python-2c8989ff0390
# Example 1: Loading JSON to Python dictionary