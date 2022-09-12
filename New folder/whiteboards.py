
# Find Even numbers
# Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.
# Example:
# Input: [2, 7, 10, 11, 12]
# Output: [2, 10, 12]

# def evenNum(x):
#     even = []
#     for num in x:
#         if num % 2 == 0:
#             even.append(num)           
#         else:
#             continue     
#     return even
            

# print(evenNum([2, 7, 10, 11, 12]))


# def evenNum2(x):
#     for odd in x:
#         if odd % 2 != 0:
#             x.remove(odd)
#         else: 
#             continue

#     return x

# print(evenNum2([3,3,3,3]))


# Electric Company
# Create a function that given a list which represents street lights given as a parameter(l_street), determine if an outage has occurred. A street with a total number of “F” greater than or equal to 2 returns “Outage”, anything below returns “Power”
# Example Input: [ ""T’, ""F’, ""F’, ""F’ ]
# Example Output: “Outage”
# def power(x):
#     count = 0
#     while True:
#         if "F" in x:
#             count += 1 
#             if count >= 2:
#                 return "outage"
#             else:
#                 return 'No Outage'
#         else:
#             return "No Outage"


# print(power(['T', 'T', 'F', 'F']))


# def power1(x):
#     if x.count('F') >= 2:
#         return 'Outage'
#     else:
#         return 'No Outage'

# print(power1(['F', 'T', "F", "T"]))

# Square(n) sum
# Create a function that given a list of integers squares each number passed into it and then sums the results together.
# Example Input: [1, 2, 2]
# Example Output: 9 
# Explanation: 1^2 + 2^2 + 2^2 = 9
# Explanation: 3^2 + 4^2 + 5^2 = 50
# Example Output: 50

# def square(x):
#     new = []
#     for y in x:
#         z= y **2        
#         new.append(z)
#     new = sum(new)
#     return new

# print(square([3, 4, 5]))

# Find Smallest Number - (Without min)
# Create a function that given a list of numbers (non-sorted) find the lowest number in the list and return it.
# Example Input: [50,30,4,2,11,0]
# Example Output: 0
# Example Input 2: [40,3,4,2]
# Example Output 2: 2


# Given a number (n) and an array of numbers (num_list) as 
# input to a function, return True if the number is greater than 
# the middle number of the array. Return False if the number is less
# than the middle number of the array.
# Example Input: n = 6, array = [3,5,8, 10]
# Example Output: True
# Example Input: n = 105, array = [10,30,44,22,100]
# Example Output: True    
        



# Max consecutive Nums:

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
 
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#  The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


# def maxNum(alist):
#     newlist = [1]
#     for i in range(len(alist)-1):
#         count = 1
#         if alist[i] == 1 and alist[i+1] == 1:
#             count += 1

#         elif alist[i] != 1:
#             newlist.append(count)
#             continue

#     return newlist
# print(maxNum([1,1,0,1,1,1]))   


# def maxNums(alist):
#     while True:




# Move Zeros
# Given an array nums, write a function to move all 0's to the end of it while
#  maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]
# Example Output: [11,2,3,4,0,0]

# def moveNum(alist):
#     new_list = []
#     for num in alist:
#         if num != 0:
#             alist.append(num)
#             alist.append(0)
            
    
#     return alist
# print(moveNum([0,0,11,2,3,4]))


# How many even digits?
# Given an array of integers, return how many of them contain an even number of digits.
# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).
# 345 contains 3 digits (odd number of digits).
# 2 contains 1 digit (odd number of digits).
# 6 contains 1 digit (odd number of digits).
# 7896 contains 4 digits (even number of digits).
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1
# Explanation:
# Only 1771 contains an even number of digits.


# def runFun(alist):
#     count = 0
#     for x in alist:
#         x = str(x)
#         if len(x) % 2 == 0:
#             count +=1
#     return count

# print(runFun([555,901,482,1771]))


# find Single Number
# Given a non-empty array of integers nums, every element appears twice 
# except for one. Find that single one.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1

# def runFun(alist):
#     for num in alist:
#         if alist.count(num) == 1:
#             return num


# print(runFun([2,2,1]))

# Minimum Index Sum of Two Lists
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have 
# a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. 
# If there is a choice tie between answers, output all of them with no order requirement. You
#  could assume there always exists an answer.
 
# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
# Example 3:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
# Example 4:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
# Example 5:
# Input: list1 = ["KFC"], list2 = ["KFC"]
# Output: ["KFC"]

# find whatevr they have in common and put it in a list

# def findCom(list1, list2):
#     new_list1 = []
#     new_list = {}
#     min = float('inf')
#     for item in list1:
#         for items in list2:
#             if item == items:
#                 new_list1.append(item)
#     for i in new_list1:
#         x =list1.index(i) + list2.index(i)
#         new_list[i]=x
#     for x in new_list.values():
#         if x < min:
#             min = x
#     return [k for k,v in new_list.items() if v == min ]
        
        

        
        
# print(findCom(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))
        


# def valid_braces(string):
#     new_dict = {}
#     for s in string:
#         new_dict[s]= 1
#     test_val = list(new_dict.values())[0]
  
#     for ele in new_dict:   
#         if new_dict[ele] != test_val:
#             return False 
#         else:
#             return True
            
# valid_braces("{}[]()")


# def divisors(n):
#     x= list(range(1,n))
#     new_list = []
#     for i in range(len(x)):
#         if x[i]* x[i-1] == n:
#             new_list.append(i)
#     s = len(new_list)
#     return s
# print(divisors(12))

# def open_or_senior(data):
#     new_list = []
#     for nums in data:
#         print(nums)
#         if nums[0] >= 55 and nums[1] > 7:
#             new_list.append("Senior")
#         else:
#             new_list.append("Open")
#     return new_list
# print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))

# def find_short(s):
#     s = s.split()
#     new_dict = {}
#     for i in s:
#         x= len(i)
#         new_dict[i] = x
#     temp = min(new_dict.values())
   
#     return temp

# print(find_short("bitcoin take over the world maybe who knows perhaps"))

# def sum_mix(arr):
#     new =[]
#     for num in arr:
#         num = int(num)
#         new.append(num)
#         x = sum(new)
#     return x

# print(sum_mix([9, 3, '7', '3']))


# def switch_it_up(number):
#     if number == 1:
#         return "One"
#     elif number == 2:
#         return "Two"
#     elif number == 3:
#         return "Three"
#     elif number == 4:
#         return "Four"
#     elif number == 5:
#         return "Five"
#     elif number == 6:
#         return "Six"
#     elif number == 7:
#         return "Seven"
#     elif number == 8:
#         return "Eight"
#     elif number == 9:
#         return "Nine"
    

# def expression_matter(a, b, c):
#     nlist = []
#     x = a*(b+c)
#     nlist.append(x)
#     y = a*b*c
#     nlist.append(y)
#     z = a+b*c
#     nlist.append(z)
#     w = (a+b)*c
#     nlist.append(w)
#     a = max(nlist)
#     print(nlist)
#     return a


# print(expression_matter(1, 1, 1))

# def reverse_words(text):
#     s = text.split()
#     for i in s:
#         i = sorted(i, reverse=True)            not done
#         x = ''.join(i)
#     return f'"{x}"'

# print(reverse_words('The quick brown fox jumps over the lazy dog.'))


# Find Difference in a String
# You are given two strings s and t.
# String t is generated by random shuffling string s 
# and then add one more letter at a random position.
# Return the letter that was added to t.
# Example 1:
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# Example 2:
# Input: s = "", t = "y"
# Output: "y"
# Example 3:
# Input: s = "a", t = "aa"
# Output: "a"
# Example 4:
# Input: s = "ae", t = "aea"
# Output: "a"
# def findLast(s, y):
#     dict1 = {}
#     dict2 = {}
#     for f in s:
#         dict1[f]=1
#     print(dict1)


# print(findLast("abcd","abcde"))


# def differences(s,t):
#     new = set()
#     for l in t:
#         if t.count(l) != s.count(l):
#             new.add(l)
#     return new
# print(differences("aaba","adaba"))

# def is_isogram(string):
#     new_dict = {}
#     for s in string:
#         new_dict[s]= 0
#         print(new_dict)
#         if s in new_dict:
#             new_dict[s] += 1
#     x = new_dict.values()
#     for y in x:
#         if y >= 2:
#             return False
#         else:
#             return True
       

# print(is_isogram("helo"))


# def human_years_cat_years_dog_years(human_years):
#     y=24
#     z=24
#     if human_years == 1:
#         return [1, 15, 15]
#     elif human_years == 2:
#         return [2, 24, 24]
#     elif human_years >= 3:
#         return [human_years, (((human_years-2)*4)+y), (((human_years-2)*5)+z)]
 
 
# print(human_years_cat_years_dog_years(10))

# def pythagorean_triple(integers):
#     x = max(integers)
#     y= min(integers)
#     a=integers.remove(x)
#     b=integers.remove(y)
#     z = integers[0]
#     if x**2 == (y**2)+(z**2):
#         return 1
#     else:
#         return 0
# print(pythagorean_triple([5,4,2]))

# def odd_or_even(arr):
#     list1 = []
#     for num in arr:
#         if num%2==0:
#             continue
#         elif num%2!=0:
#             list1.append(num)
#     for a in list1:
#         if a%2!=0:
#             return False
#         else:
#             return True


# Sum w/o High/Low
# Sum all the numbers of a given list except the highest and 
# the lowest element ( by value, not by index! ).
# The highest or lowest element respectively is a single 
# element at each edge, even if there are more than one with the same value.
# Mind the input validation.
# Example
# [ 6, 2, 1, 8, 10 ] => 16
# [1, 1, 11, 2, 3 ] => 6
# Input validation
# If an empty value is given instead of an array, or the given array is an empty 
# list or a list with only 1 element, return 0.


# def addMost(alist):
#     alist.sort()
#     alist.pop()
#     alist.remove(alist[0])
    
#     x =sum(alist)
#     return x
# print(addMost([ 6, 2, 1, 8, 10 ]))

# Count Palindromes
# GIven a list of strings, count the number of palindromes that occur
#  inside of the list (a palindrome is a word that is spelled the same backwards and forward).

# Example input: [‘dog’, ‘racecar’, ‘wildebeest’]
# Output: 1
# # Explanation: ‘racecar’ is the only palindrome in the list
# import math

# def ans(alist):
#     count =0

#     x= len(alist)
#     for a in alist:
#         x= len(a)*.5
#         x= math.floor(x)
#         print(x)
#         print(a[x+1:])
#         print(a[-x:])
#         if a[x+1:] == a[-x:]:
            
#             count+=1
#         else:
#             continue
#     return count
# print(ans(['dog', 'racecar', 'wildebeest']))

# def generate_hashtag(s):
#     if s == '':
#         return False
#     elif len(s) > 140:
#         return False
#     new=[]
#     x = s.split()

#     for l in x:
#         l = l.lower()
#         l = l.title()
#         new.append(l)
#     new[0]= '#'+new[0]
#     new_s = ''.join(new)
#     return new_s

# print(generate_hashtag('codewars is nice'))


# def narcissistic( value ):
#     alist = []
#     value = str(value)
#     length = len(value)

#     for num in value:
#         num = int(num)
#         new = num**length
#         alist.append(new)
#     if sum(alist) == int(value):
#         return True
#     else:
#         return False
# print(narcissistic(153))

# def square_sum(numbers):
#     new_list = []
#     for num in numbers:
#         x =num**2
#         new_list.append(x)
#     answer = sum(new_list)
#     return answer

# def likes(names):
#     end = "likes this"
#     sums = len(names)
#     if len(names) == 0:
#         return 'no one likes this'
#     elif len(names) == 2:
#         return f'{names[0]} and {names[1]} {end}'
#     elif len(names) == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} {end}'
#     elif len(names) > 3:
#         return f'{names[0]}, {names[1]} and {sums - 2 } others like this'

# def amount_of_pages(summary):
#     count = 0
#     x =[]
#     alist = range(1,summary+1)
#     for num in alist:
#         x.append(num)
#     for nums in x:
#         d = len(str(nums))
#         count +=  d
#     return count
    

# print(amount_of_pages(25))



# def amount_of_pages(summary):
#     count = 0
#     x =[]
#     alist = range(1,summary)
#     for num in alist:
#         x.append(num)
#     for nums in x:
#         d = len(str(nums))
#     return count
    
# def solution(s):
#     s = list(s)
#     if len(s) == 0:
#         return []
#     alist = []
#     slist = []
#     if len(s)%2 != 0:
#         slist.append(s[-1] + '_')
#         for i in range(len(s)-1):
#             alist.append(s[i] + s[i+1])
#     for i in range(0, len(alist)):
#         if i % 2:
#             slist.append(alist[i])
#     x = slist.pop(0)
#     slist.append(x)
#     return slist

# print(solution('asdfadsf'))


# def increment_string(strng):
#     new_list = []
#     for s in strng:
#         new_list.append(s)
#     if new_list[-1].isnumeric() == False:
#         new_list.append(str(1))
#     for i in range(len(s)-1):
#         if s[i].isnumeric() == True:
#             if s[i+1] == '9':
#                 z = s.pop(s[i+1])
#                 z = int(z)+1
#                 x= int(s[i]) + 1
                
# print(increment_string('foobar001'))


# elif new_list[-1].isnumeric() == True:
#         x = new_list.pop()
#         x = int(x) + 1
#         new_list.append(str(x))
#         new_list = "".join(new_list)
#         return new_list


# The question asks the following: Write a function that takes an integer flight_length
#  (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean
#  indicating whether there are two numbers in movie_lengths whose sum equals flight_length.
# movie_lengths1=[20, 30, 110, 40, 50] #true
# movie_lengths2=[80, 110, 40]  #false
# flight_length=160


# def ans(alist, m_length):
#     for i in range(len(alist)-1):
#         x = m_length - alist[i]
#         alist.remove(alist[i])
#         if x in alist:
#             return True
#     return False
        

# print(ans([80, 110, 40], 160))
# Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

# def ans(alist):
#     new_list=[]
#     for i in range(len(alist)):
#         num = alist[0] + alist[i]
#         new_list.append(num)
#     return new_list

# print(ans([3,1,2,10,1]))


# Shuffle the Array

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
 
# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

# Example 2:
# Input: nums = [1,2,3,4,4,3,2,1], n = 4
# Output: [1,4,2,3,3,2,4,1]

# Example 3:
# Input: nums = [1,1,2,2], n = 2
# Output: [1,2,1,2]
# Constraints:
# ●	1 <= n <= 500
# ●	nums.length == 2n
# ●	1 <= nums[i] <= 10^3





# make into a string
# split where given index
# first half is x 2nd half is y
# append to new list w format x1 y1 x2 y2 etc
# turn back into int


# def ans(alist, n):
#     new_list = []
#     xs = alist[:n]
#     ys = alist[n:]
#     for i in range(len(xs)):
#         new_list.append(xs[i])
#         new_list.append(ys[i])
#     return new_list
        

# print(ans([1,1,2,2], 2))


# First Unique Character in a String
# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1


# def ans(word):
#     for i in range(len(word)):
#         if word.count(word[i]) == 1:
#             return [i]
#         else:
#             return -1
# print(ans("aabb"))


# def ans(word):
#     a = {}
#     for i in range(len(word)):
#         a[word[i]]=1
#         if 
# print(ans("loveleetcode"))



# import urlparse



# def domain_name(url):
#     new = url.split('.')
#     if  '/' not in new[1]:
#         return new[1]
#     ans = new[0].split('/')
#     return ans[-1]
    
# print(domain_name("http://github.com/carbonfive/raygun" ))

# def first_non_repeating_letter(string):
#     count_dict = {}
#     for letter in string:
#         count_dict[letter] = count_dict.get(letter,0) +1
#     for i in range(len(s)):
#         if count_dict[string[i]] == 1:
#             return string[i]


# def score(dice):
#     count = 0
    
#     for num in dice:
#         if num == 1:
#             if dice.count(num) == 3:
#                 count += 1000
#             elif dice.count(num) > 3:
#                 count += 1000 + (dice.count(num)-3 * 100)
#             elif dice.count(num) == 1:
#                 count += 100
#         if num == 2:
#             if dice.count(num) == 3:
#                 count += 200
#                 dice = [*set(dice)]
                
#             else:
#                 count += 0
#         if num == 3:
#             if dice.count(num) == 3:
#                 count += 300
#                 dice = [*set(dice)]
#             else:
#                 count += 0
#         if num == 4:
#             if dice.count(num) == 3:
#                 count += 400
#                 dice = [*set(dice)]
#             else:
#                 count += 0
#         if num == 5:
#             if dice.count(num) == 3:
#                 count += 500
#                 dice = [*set(dice)]
#             elif dice.count(num) == 1:
#                 count += 50
#             else:
#                 count += 0
#         if num == 6:
#             if dice.count(num) == 3:
#                 count += 600
#                 dice = [*set(dice)]
#             else:
#                 count += 0
#     return count

# print(score([1, 1, 1, 1, 1]))


# def nines(n):
#     count = 0
#     for num in range(0,n+1):
#         num = str(num)
#         for nu in num:
#             if '9' in nu:
#                 count +=1

#     return count

# print(nines(45))


# def ascend_descend(length, minimum, maximum):
#     ans = ''
#     while len(ans) <= length:
#         for num in range(minimum,maximum+1):
#             ans= ans + str(num)
#             for nums in range(maximum,minimum):
#                 ans = ans + str(nums)
#     return ans

# print(ascend_descend(5, 1, 3))

# def ans(w1, w2):
#     x = len(w2)
#     new = w1[-1:]
#     print(new)
#     if w2 == new:
#         return True
#     else:
#         return False

# print(ans('abc', 'bc'))


# def remove_parentheses(s):
#     f = s.split(s[2],2)
#     return f

# print(remove_parentheses("abcdef"))

def dig_pow(n, p):
    ans = 0
    a = p
    for num in str(n):
        ans += int(num)**a
        a += 1
        print(ans)
    new = ans/n
    if new.is_integer() == True:
        return new
    else:
        return -1
        
print(dig_pow(46288, 3))