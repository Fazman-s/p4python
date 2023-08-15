def valid(ipad):

	
	ipad = ipad.split(".")
	
	
	for i in ipad:
		if (len(i) > 3 or int(i) < 0 or int(i) > 255):
			return False
		if len(i) > 1 and int(i) == 0:
			return False
		if (len(i) > 1 and int(i) != 0 and
			i[0] == '0'):
			return False
			
	return True


def answer(s):
	
	sz = len(s)

	
	if sz > 12:
		return []
	snew = s
	list = []

	
	for i in range(1, sz - 2):
		for j in range(i + 1, sz - 1):
			for k in range(j + 1, sz):
				snew = snew[:k] + "." + snew[k:]
				snew = snew[:j] + "." + snew[j:]
				snew = snew[:i] + "." + snew[i:]
								
				if valid(snew):
					list.append(snew)
					
				snew = s
				
	return list

		
p= input().strip()
print(answer(p))

"""or

def isvalid(s, i, j, level, temp, result):
 
    if (i == (j + 1) and level == 5):
        result.append(temp[1:])
 

    k = i
    while(k < i + 3 and k <= j):
         
        address = s[i: k + 1]
 
        if ((s[i] == '0' and len(address) > 1) or int(address) > 255):
            return
 
        isvalid(s, k + 1, j, level + 1, temp + '.' + address, result)   
 
        k += 1
 
s = input().strip()
n = len(s)
ans = []
isvalid(s, 0, n - 1, 1, "", ans)
for s in ans:
    print(s)

    
"""