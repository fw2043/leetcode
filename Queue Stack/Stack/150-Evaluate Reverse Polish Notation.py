"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.



Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
# tokens = ["4","13","5","/","+"]
# (4 + (13 / 5)) = 6
# go through each token, put the elements to stack if it is not an operator
# if it is an operator, pop twice, but need to decide which one is first: 13/5
# the resulst above has to be put back to the stack
# if the token is an operator, then calculte the values (2 + 1) = 3, put 3 to the list, then 3,3,* ==> 9
# need to pop and push---> stack
import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        # ["4","13","5","/","+"]
        for token in tokens:

            if token not in "+-/*":
                stack.append(int(token))
                continue
            # [4, 12,5]
            number_2 = stack.pop()  # 5
            number_1 = stack.pop()  # 13---->13/5 not 5/13

            result = 0
            if token == "+":
                result = number_1 + number_2
            elif token == "-":
                result = number_1 - number_2
            elif token == "*":
                result = number_1 * number_2
            else:
                result = int(number_1 / number_2)

            stack.append(result)

        return stack.pop()

# Similar problem
# Prefix to Postfix Conversion
"""
 Prefix: An expression is called the prefix expression if the operator appears in the expression 
 before the operands. Simply of the form (operator operand1 operand2). 
Example : *+AB-CD (Infix : (A+B) * (C-D) )

Postfix: An expression is called the postfix expression if the operator appears in the expression 
after the operands. Simply of the form (operand1 operand2 operator). 
Example : AB+CD-* (Infix : (A+B * (C-D) )
Given a Prefix expression, convert it into a Postfix expression. 
Conversion of Prefix expression directly to Postfix without going through the process of 
converting them first to Infix and then to Postfix is much better in terms of computation and better understanding the expression (Computers evaluate using Postfix expression). 

Examples: 

Input :  Prefix :  *+AB-CD
Output : Postfix : AB+CD-*
Explanation : Prefix to Infix :  (A+B) * (C-D)
              Infix to Postfix :  AB+CD-*

Input :  Prefix :  *-A/BC-/AKL
Output : Postfix : ABC/-AK/L-*
Explanation : Prefix to Infix :  (A-(B/C))*((A/K)-L)
              Infix to Postfix : ABC/-AK/L-* 
 """


def postfix(s):
    stack = []
    s = s[::-1]

    operators = set(['+', '-', '*', '/', '^'])
    for i in s:

        # if token is operator
        if i in operators:

            # pop 2 elements from stack
            a = stack.pop()
            b = stack.pop()

            # concatenate them as operand1 +
            # operand2 + operator
            temp = a + b + i
            stack.append(temp)

        # else if operand
        else:
            stack.append(i)

    return stack
