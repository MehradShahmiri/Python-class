nums=[]
q=input('enter a number')
nums.append(q)
w=input('enter a number')
nums.append(w)
e=input('enter a number')
nums.append(e)
r=input('Do you want to keep last number')
if r=='no':
    nums.remove(e)
print(nums)
