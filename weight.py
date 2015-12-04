import sys

class Interval:
	def __init__ (self, line):
		splitLine = line.split()
		self.start = int(splitLine[0])
		self.finish = int(splitLine[1])
		self.value = int(splitLine[2])
	def __str__ (self):
		return str(self.start)+' '+str(self.finish)+' '+str(self.value)
		
def compute_previous_intervals(WIS):
    # extract start and finish times
    start = [i.start for i in WIS]
    finish = [i.finish for i in WIS]

    a = []
    for j in xrange(len(WIS)):
        i = bisect.bisect_right(finish, start[j]) - 1  # rightmost interval f_i <= s_j
        a.append(i)
    return a
	
def schedule_weighted_intervals(WIS):
	WIS.sort(lambda x, y: x.finish - y.finish)  # f_1 <= f_2 <= .. <= f_n
	a = compute_previous_intervals(WIS)
	OPT = collections.defaultdict(int)
	OPT[-1] = 0
	OPT[0] = 0
    for j in xrange(1, len(I)):
        OPT[j] = max(I[j].weight + OPT[p[j]], OPT[j - 1])
	O = []
    
	def compute_solution(j):
        if j >= 0:  # will halt on OPT[-1]
            if WIS[j].weight + OPT[p[j]] > OPT[j - 1]:
                O.append(WIS[j])
                compute_solution(p[j])
            else:
                compute_solution(j - 1)
    compute_solution(len(WIS) - 1)
	
	return O
	
if __name__ == '__main__':
    WIS = []
	WIS.append(Interval("0" , "2", "1"))
	WIS.append(Interval("0" , "3", "5"))
	WIS.append(Interval("2" , "3", "2"))
	WIS.append(Interval("3" , "6", "10"))
	O = schedule_weighted_intervals(I)
    print O
