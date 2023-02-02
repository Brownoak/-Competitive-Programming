'''
You are given 2 arrays representing the stock prices of a big tech company for 2 consecutive weeks, week1 and week2. 
A price is called k-repeating if the stock was sold for that price for k weeks consecutive weeks.

Example: week1 = [4,9,5], week2 = [9,4,9,8,4]
Output: [4,9]
Example: week1 = [2,2], week2 = [2,2,2]
Output: [2,2]
    
Prices 4 and 9 are 2-repeating because the stock has been sold for price 4 and price 9 in both weeks.
Return all 2-repeating prices. A price must appear in your result array as many times as it appears in its minimum appearance. 

"Are you there?"
"can I continue"?
"yeah, sure"
weekOne = {4: 1, 9: 1, 5: 1}
weekTwo = {9: 2, 4 : 2, 8 : 1}
[4, 9]

week1 = [4,9,5], {4: 1, 9 : 1, 5 : 1}
week2 = [9,4,9,8,4] {9 : 2, 4 : 2, 8 : 1}
tmp = [4, 9]
'''

d1={}
d1[5] = 1
d2={}
temp=[]

for i in range(len(week1)):
    if week1[i] not in d1:
        d1[week1[i]]= 1
    else:
        d1[week1[i]] += 1
        
for j in range(len(week2)):
    if week2[i] not in d2:
        d2[week2[i]]= 1
    else:
        d2[week2[i]] += 1 
        
for (elt,freq) in d1:
    x=freq
    if elt in d2:
        x= min(x, d2[elt])
    for j in range(x):
        temp.append(elt)
        



