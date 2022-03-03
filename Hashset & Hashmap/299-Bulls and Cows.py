"""
You are playing the Bulls and Cows game with your friend.
You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess,
you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position.
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows.
Note that both secret and guess may contain duplicate digits.


Example 1:

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"
Example 2:

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.


Constraints:

1 <= secret.length, guess.length <= 1000
secret.length == guess.length
secret and guess consist of digits only.
"""
# confirm if the lengths are same? Yes
# how to store and return the result: return "{}A{}B".format(bulls, cows)
# example 2: Input: secret = "1123", guess = "0111", Output: "1A1B"
# both the total number of each unique number and the position matter
# so two dictionaries
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        d1 = {}
        d2 = {}

        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
            else:  # only store elememts except bulls, so later it's easy to find the intersection
                d1[secret[i]] = d1.get(secret[i], 0) + 1
                d2[guess[i]] = d2.get(guess[i], 0) + 1

        for n in d1:
            if n in d2:
                cows += min(d1[n], d2[n])

        return "{}A{}B".format(bulls, cows)





