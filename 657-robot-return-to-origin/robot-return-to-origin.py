class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir = {'U':0, 'D':0, 'L':0, 'R':0}
        for i in moves:
            dir[i]+=1
        return dir['U']==dir['D'] and dir['L']==dir['R']