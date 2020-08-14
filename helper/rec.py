from helper.point import point
class rec:
    def __init__(self,x,y,w,h):
        # ctor for rec that stores a rec as 4 points
        self.points = {}
        self.points["up_left"] = point(x,y)
        self.points["up_right"] = point(x,y+w)
        self.points["down_left"] = point(x+h,y)
        self.points["down_right"] = point(x+h,y+w)
