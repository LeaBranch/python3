from random import randrange

#### search for the max value in the array
def max_elem(s):
	n=len(s)
	max=s[0]
	for i in range(n):
		if(s[i]>max): max=s[i]
	return max


#### search for the min value in the array
def min_elem(s):
	n=len(s)
	min=s[0]
	for i in range(n):
		if(s[i]<min): min=s[i]
	return min


#### bubble sorting
def myBubbleSort(s):
	bubble=0
	n=len(s)
	for j in range(n):
		for i in range(n-1):
			if (s[i]<s[i+1]):
				bubble=s[i]
				s[i]=s[i+1]
				s[i+1]=bubble
	return s


#### array output
def out(s):
	for elem in s:
		print(elem, end=' ')

#### array output
def out2(s):
	for i in range(len(s)):
		print("[ " + str(i+1) + " ] " + s[i])

#### line reverse 
def myReverse(s):
	s[::-1]
	return s


#### line reverse output
def myReverseOut(s):
	myReverse(s)
	print(s)


#### the sum of all elements in array
def mySumAll(s):
	sum=0
	n=len(s)
	for i in range(n):
		sum+=s[i]
	print('sum:', sum)


#### the sum of each elements in array
def mySum1(s, k):
    z=[]
    n=len(s)
    for i in range(n):
        z.append(s[i]+k[i])
    print('')
    out(z)


#### number of '+', '-', '0' elements value
def myElem(s):
    p=0
    m=0
    z=0
    for i in range(len(s)):
	    if(s[i]>0): p+=1
	    if(s[i]<0): m+=1
	    if(s[i]==0): z+=1
    print ("\n+:",p)
    print ("-:", m)
    print ("0:", z)


#### arifmetic midle of '+' elements in array
def myMidSum(s):
	p=0
	q=0
	n=len(s)
	for elem in s:
		if(elem>0):
			q+=elem
			p+=1
		s=q/p
	print("SrArif '+': " '%.3f'%s)


#### the number of even and odd elements in the array
def myChetNechet(s):
	c=0
	n=0
	for i in range(len(s)):
		if(s[i]%2==0): c+=1
		else: n+=1
	print ("chetn:",c)
	print ("nechetn", n)



####
if __name__	=="__main__":
	n=5
	a=[randrange(0,10) for j in range(n)]
	res = max(a)
	#print(res)
