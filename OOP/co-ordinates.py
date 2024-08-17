'''write oop classes to handle the following scenarios
1. user can create and view 2d coordinates
2.A user can find out the distance between two coordinates 
3.a user can find out the distance of co-ordinate from origin 
4.a user can take it point lies on the given line 
5. user can find the distance of given point and given LINE'''
class coordinates:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def view(self):
        print("({},{})".format(self.x,self.y))

    def distfromO(self):
        print((self.x*self.x+self.y*self.y)**0.5)

    def dist(self,other):
        print(((other.x-self.x)**2+(other.y-self.y)**2)**0.5)
        

x1=int(input("Enter a number: "))
y1=int(input("Enter a number: "))
points1=coordinates(x1,y1)
x2=int(input("Enter a number: "))
y2=int(input("Enter a number: "))
points2=coordinates(x2,y2)

points1.view()
points2.view()
points1.distfromO()
points1.dist(points2)

class line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return ("{}x+{}y+{}=0".format(self.A,self.B,self.C))
    
    def point_on_line(self,point):
        if(self.A*point.x+self.B*point.y+self.C==0):
            print("The point lies on the line")
        else:
            print("The point does not lie on the line")

    def dist_eq_point(self,point):
           print(abs((self.A*point.x+self.B*point.y+self.C)/((self.A*self.A+self.B*self.B)**0.5)))
l1=line(1,1,-2)
print(l1)
l1.point_on_line(points1)
l1.dist_eq_point(points1)

#to find the distance between a line equation and a point

    




    
    