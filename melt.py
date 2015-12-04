import sys

# Read
heights = [int(line) for line in sys.stdin]

# Write 
maxDeac = 0
Deac = 0
min1 = heights[0]
i = 0
while i < len(heights):
	if heights[i] > min1:
		min1 = heights[i]
		
	Deac = heights[i] - min1
	
	if abs(Deac) > maxDeac:
		maxDeac = abs(Deac)
	i += 1
print (maxDeac)

# There is only one loop that is repeating for n elements
# So the running time would be linear time O(n)
