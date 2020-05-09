class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        size=len(coordinates)
        slope=0
        slope1=0
        diff=0
        diff1=0
        flag=0
        x1=coordinates[0][0]
        y1=coordinates[0][1]
        x2=coordinates[1][0]
        y2=coordinates[1][1]
        diff=y2-y1
        diff1=x2-x1
        if diff1==0:
            slope=999999
        else:
            slope=diff//diff1
        for i in range(size-1):
            x1=coordinates[i][0]
            y1=coordinates[i][1]
            x2=coordinates[i+1][0]
            y2=coordinates[i+1][1]
            diff=y2-y1
            diff1=x2-x1
            if diff1==0:
                slope1=999999
            else:
                slope1=diff//diff1
            if slope!=slope1:
                flag=1
            else:
                slope=slope1
        if flag==1:
            return False
        else:
            return True
            
            