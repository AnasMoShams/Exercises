# class stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()
#     def is_empty(self):
#         return len(self.items) == 0
#     def peek(self):
#         return self.items[-1]
#     def size(self):
#         return len(self.items)

# class test:
#     def __init__(self, data):
#         self.stack = stack()
#         self.data = data
    
#     def test(self):
#         braket_map = {")": "(",
#                     "}": "{",
#                     "]": "["}
#         for char in self.data:
#             if char in braket_map:
#                 top_element = self.stack.pop()
#                 if top_element != braket_map[char]:
#                     return False
#             else:
#                 self.stack.push(char)
#         return self.stack.is_empty()


# test_data = test("(){}[]")
# print(test_data.test())
# test_data2 = test("({[})")
# print(test_data2.test())    
# test_data3 = test("({[()]})")
# print(test_data3.test())


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def removeNthFromEnd(self, head, n):
#         dummy = ListNode(0, head)
#         frist = dummy
#         second = dummy
#         for _ in range(n+1):
#             frist = frist.next

#         while frist:
#             frist = frist.next
#             second = second.next
#         second.next= second.next.next

#         return dummy.next


# class Solution(object):
#     def reverse(self, x):
#         rsl = ""
#         if x < 0 :
#             x_str = str(x)[1:]
#             rsl = "-" + x_str[::-1]
#         else:
#             x_str = str(x)
#             rsl = x_str[::-1].lstrip("0")
#         if rsl == "" or rsl == " ":
#             return 0
#         rsl = int(rsl)
#         if rsl < -2**31 or rsl > 2**31 -1 :return 0 
    
#         return rsl


# class Solution(object):
#     def twoSum(self, nums, target):
#        for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[j] + nums[i] == target:
#                 return [i, j]
    
# class Solution(object):
#     def intRoman(self, num):
#         roman_values = {
#             'M': 1000,
#             'CM': 900,
#             'D': 500,
#             'CD': 400,
#             'C': 100,
#             'XC': 90,
#             'L': 50,
#             'XL': 40,
#             'X': 10,
#             'IX': 9,
#             'V': 5,
#             'IV': 4,
#             'I': 1
#         }
#         rsl = ""
#         for key, value in roman_values.items():
#             while num >= value:
#                 rsl += key
#                 num -= value
#         return rsl
    
# p = Solution()
# print(p.intRoman(3749) ) # "MMMDCCXLIX"      


# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, num1, num2):
#         dummy = ListNode()
#         current = dummy
#         carry = 0
#         step = 1
        
#         while num1 or num2 or carry:
#              val1 = num1.val if num1 else 0
#              val2 = num2.val if num2 else 0
        
#              total = val1 + val2 + carry
#              carry = total // 10
#              digit = total % 10
             
#             #  print("#" * 10)
#             #  print("steps ", step)
#             #  print("val 1", val1)
#             #  print("-" *10)
#             #  print("val 2", val2)
#             #  print("carry ", carry)
#             #  print("@" *10)
#             #  print(f"total = {total}")
#             #  print(f"digit to insert = {digit}")
        
#              current.next= ListNode(digit)
#              current = current.next
             
#              if num1 : num1 = num1.next
#              if num2 : num2 = num2.next
#              step += 1

#         return dummy.next
    

# class Stack:
#     def __init__(self):
#         self.item = []

#     def __remove_pattern(self, s, th1, th2, points):
#         stack = []
#         score = 0
#         for char in s :
#             if stack and stack[-1] == th1 and char == th2:
#                 stack.pop()
#                 score += points
#             else:
#                 stack.append(char)
#         return "".join(stack), score
    
#     def max_gain(self, s, x, y):
#         total = 0
#         while True:
#             if x > y:
#                 s, score1= self.__remove_pattern(s, "a", "b", x)
#                 total += score1 
#                 s, score2= self.__remove_pattern(s, "b", "a", y)
#                 total += score2 

#             else:
#                 s, score1 = self.__remove_pattern(s, "b", "a", y)
#                 total += score1  
#                 s, score2 = self.__remove_pattern(s, "a", "b", x)
#                 total += score2 

            
#             if score1 == 0 or score2 == 0:
#                 break
#         return total
# test = Stack()
# s = "aabbaaxybbaabb"
# x, y = 5, 4
# print(test.max_gain(s, x, y))


# # solution of puzzel https://leetcode.com/problems/two-sum/
# by array
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
        
# # sol = Solution()
# # print(sol.twoSum([2,7,11,15], 9))

# # by HashMap
# class Solution(object):
#     def twoSum(self, nums, target):
#         value_index = {}
#         for index, num in enumerate(nums):
#             diff = target - num
#             # print("index", index)
#             # print("num", num)
#             # print("value to index", value_index)
#             if diff in value_index:
#                 return [value_index[diff], index]
#             value_index[num] = index
# sol2 = Solution()
# print(sol2.twoSum([2, 7, 11, 15], 9))


# #solution of puzzel https://leetcode.com/problems/string-to-integer-atoi/description/
# class Solution(object):
#     def myAtoi(self ,s):
#         s = s.strip()
#         rsl = ""
#         sign = 1
#         started = False

#         for i in s:
#             if i == "-" and not started:
#                 sign = -1
#             elif i == "+" and not started:
#                 sign = 1
#                 started = True
#             elif i.isdigit():
#                 rsl += i
#                 started = True
#             elif started :
#                 break
#         if not rsl: return 0
#         result = sign * int(rsl)

#         INT_MAX = 2147483647
#         INT_MIN = -2147483648

#         if result > INT_MAX:
#             return INT_MAX
#         elif result < INT_MIN:
#             return INT_MIN

#         return result


# x = Solution()
# print(x.myAtoi("    _2435")) # 2435

# import re
# class Solution(object):
#     def myAtoi(self, s):
#         s = s.strip()
#         rsl = re.match(r"([+-]?\d+)", s)
#         if not rsl:
#             return 0
#         result = int(rsl.group(1))

#         INT_MAX = 2147483647
#         INT_MIN = -2147483648

#         if result > INT_MAX:
#             return INT_MAX
#         elif result < INT_MIN:
#             return INT_MIN

#         return result


# x = Solution()
# print(x.myAtoi("Word of 9832"))
    

# #Solution of puzzel https://leetcode.com/problems/roman-to-integer/description/
# class Solution(object):
#     def romanToInt(self, s):
#         roman_number = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
#         total = 0
#         prev_value = 0

#         for char in reversed(s):
#             value = roman_number[char]
#             # print("value", value)
#             # print("Prev_value", prev_value)

#             if value < prev_value:
#                 total -= value

#             else:
#                 total += value
#                 prev_value = value
#         return total


# x = Solution()
# print(x.romanToInt("III"))


# # Solution of puzzel https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=problem-list-v2&envId=array
# class Solution(object):
#     def maxProfit(self,prices):
#         current = 0
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 current = max(current, prices[j] - prices[i])

#         return current

#     def maxProfit_2(self,prices):
#         min_price = float("inf")
#         max_profit = 0

#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             profit = price - min_price

#             if profit > max_profit:
#                 max_profit = profit
#         return max_profit


# # Solution of puzzel https://leetcode.com/problems/linked-list-cycle/description/?envType=problem-list-v2&envId=xi4ci4ig
# class Node :
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class Solution(object):
#     def hasCycle(self, head):
#         if not head or not head.next :
#             return False
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#             if slow == fast:
#                 return True
#         return False

# #  Test 
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# solution = Solution()
# print(solution.hasCycle(node1))

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2 
# print(solution.hasCycle(node1))