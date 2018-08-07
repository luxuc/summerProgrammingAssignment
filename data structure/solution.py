import copy

class Guard(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        self.cost = e - s 
        
def addHours(answer):
    finalHour = 0
    for ele in answer:
        if ele != None:
            hour = ele.end - ele.start
            finalHour += hour
    return finalHour
        
def merge(intervals):
    merged_intervals = []
    
    intervals.sort(key=lambda x: x.start, reverse=False)
    intervals_cp = copy.deepcopy(intervals)
    for i in range(len(intervals)-1):
        if intervals[i].end >= intervals[i+1].start:    # need to merge
            
            #---------------
            #print ("start: %d end: %d" %(intervals[i+1].start, intervals[i+1].end))
            #print ("start: %d end: %d" %(intervals_cp[i+1].start, intervals_cp[i+1].end))
            #print "cost0: %d" %intervals_cp[i+1].cost
            #---------------
            
            # modify costs
            help_cover = min(intervals[i].end, intervals[i+1].end) - intervals[i+1].start
            intervals_cp[i+1].cost -= help_cover
            
            #---------------
            #print "cost1: %d" %intervals_cp[i+1].cost
            #---------------

            # merge intervals
            intervals[i + 1].start = intervals[i].start
            intervals[i+1].end = max(intervals[i].end, intervals[i+1].end)
            intervals[i] = None
            
    # add intervals to merged_intervals
    for ele in intervals:
        if ele:
            merged_intervals.append(ele)   
    
    intervals_cp.sort(key=lambda x: x.end, reverse=True)
    # sort from latest end to earliest end
    for i in range(len(intervals_cp) - 1):
        if intervals_cp[i].start <= intervals_cp[i + 1].end:  # need to merge
            # modify costs
            help_cover = intervals_cp[i+1].end - max(intervals_cp[i+1].start, intervals_cp[i].start)
            
            #---------------
            #print ("start: %d end: %d" %(intervals_cp[i+1].start, intervals_cp[i+1].end))            
            #print "cost3: %d" %intervals_cp[i+1].cost
            #---------------
            
            intervals_cp[i+1].cost -= help_cover
            intervals_cp[i+1].cost = max(intervals_cp[i + 1].cost, 0)
            if intervals_cp[i+1].cost == 0:
                return addHours(merged_intervals)
            
            #---------------
            #print "cost4: %d" %intervals_cp[i+1].cost
            #---------------

            # merge intervals
            intervals_cp[i + 1].start = min(intervals_cp[i+1].start, intervals_cp[i].start)
            intervals_cp[i + 1].end = intervals_cp[i].end
    
    # find minimum cost
    for i in range(len(intervals_cp)):
        if i == 0:
            min_cost = intervals_cp[i].cost
        else:
            if intervals_cp[i].cost < min_cost:
                min_cost = intervals_cp[i].cost
    finalHour = addHours(merged_intervals)
    return finalHour - min_cost

if __name__=='__main__':
    # reading file
    inputFileName = "10.in"
    fo = open(inputFileName, "r")
    print "Filename: ", fo.name
    
    guardList = []
    guardNumber = fo.readline()
    for i in range(int(guardNumber)):
        rawTime = fo.readline()
        times = rawTime.strip().split(" ")
        guard = Guard(int(times[0]), int(times[1]))
        guardList.append(guard)
    fo.close()  
    
    answer = merge(guardList)
    print "final hour: %d" %answer
    
    # outputing file
    index = inputFileName.split(".")[0]
    fileName = index + ".out"
    output = open(fileName, "w")
    print "Result has been saved in file: ", output.name
    output.write( str(answer) )
    output.close()    