class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        i=0
        res=0
        while(i<len(seats)):
            res+=abs(students[i]-seats[i])
            i+=1
        return res