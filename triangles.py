def equilateral(sides):
    if 0 not in sides:
        return sides[0] == sides[1] == sides[2]
    return False
    
def isosceles(sides):
    if 0 not in sides:
        if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
            return sides.count(sides[0]) >= 2 or sides.count(sides[1]) >= 2
        
        return False

def scalene(sides):
    if 0 not in sides:
        if sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]:
            return sides.count(sides[0]) == 1 and sides.count(sides[1]) == 1
        return False


