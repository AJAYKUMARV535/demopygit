class Solution:
	def combinations(n,r):
		result = [ ]
		def Backtrack(start , comb):
			if len(comb) == r:	
				result.append(comb.copy( ))
				return
			for i in range(1,n+1):
				comb.append(i)
				for i in range(1, n+1):
					Backtrack(i+1, comb)
				comb.pop()
		Backtrack(1, [ ])		
		print(result)
		print(len(result))
for i in range(5):
	Solution.combinations(4,i)
	print("__"*150)
			