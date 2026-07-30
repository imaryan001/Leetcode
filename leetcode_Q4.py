class sloution:
    def findmediansortedarray(self,num1,num2):
        merged = sorted(num1+num2)

        
        total = len(merged)

        if total%2 == 0:
            return (merged[total//2])
        else:
            middle1 =merged[total//2-1]
            middle2 =merged[total//2]
            return (float(middle1)+float(middle2))/2.0
