"""
You have a browser of one tab where you start on the homepage and you can visit another url,
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x,
  you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history.
  If you can only forward x steps in the history and steps > x,
  you will forward only x steps. Return the current url after forwarding in history at most steps.


Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
"""
"""
Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.
"""
# Because we have to forward, so can't use one stack, when we go back to pop from stack, we might need to forward later,
# so have to use another stack to store the ones being popped(back)
# when we visit a new one which is not in history, we have to reset another stack to be empty
# when we backward, have to keep len(hist) > 1
# Two stacks:
class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = []
        self.future = []
        self.hist.append(homepage)

    def visit(self, url: str) -> None:
        # when we visit a new url, set future to []
        self.hist.append(url)
        self.future = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.hist) > 1:
            self.future.append(self.hist.pop())
            steps -= 1
        return self.hist[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.future) > 0:
            self.hist.append(self.future.pop())
            steps -= 1
        return self.hist[-1]

# Can we improve it by using one stack?
#

class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.cur = 0  # the current index/position

    def visit(self, url: str) -> None:
        # Visits url from the current page.
        #  It clears up all the forward history
        # hist = [a, b,c,d,e], forward to c, then cur = 2, hist = [a,b,c]
        while self.hist and len(self.hist) - 1 > self.cur:
            self.hist.pop()

        self.hist.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        # steps > x, you will return only x steps
        self.cur -= min(self.cur, steps)
        return self.hist[self.cur]

    def forward(self, steps: int) -> str:
        # If you can only forward x steps in the history and steps > x, y
        self.cur += steps
        self.cur = min(self.cur, len(self.hist) - 1)
        return self.hist[self.cur]


