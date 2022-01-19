n=int(input())
c=0
k,v=n,n
new=0
while n>0:
	n=n//10
	c+=1
print(c)
while k>0:
	rem=k%10
	new=new+(rem**c)
	k=k//10
print(new)
if v==new:
	print("yes it is armstrong number")
else:
	print("not a armstrong number ")