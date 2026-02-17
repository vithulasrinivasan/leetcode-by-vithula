class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        valid=[]
        for i in range(12):
            for j in range(60):
                temp=bin(i)+bin(j)
                if temp.count("1")==turnedOn:
                    time= "%d:%02d"% (i,j)
                    valid.append(time)
        return valid
        