"""
@Title : Lab 1
@author: Efrain Retana
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def circle(center,rad):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_triangles(ax,n,p):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') # Draw triangle
        i1 = [1,2,0,1]
        q = p*(0.5)+ p[i1]*0.5
        draw_triangles(ax,n-1,q)
        
def draw_triangle_grid(ax,n,p):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') # Draw triangle grid
        i1 = [1,2,0,1]
     
        q = p*(0.5)+ p[i1]*0.5
        p1 = np.array([p[0],q[2],q[0],p[0]])
        p2 = np.array([q[2],q[1],p[2],q[2]])
        p3 = np.array([q[0],p[1],q[1],q[0]])
        p4 = np.array([q[0],q[1],q[2],q[0]])
        draw_triangle_grid(ax,n-1,p1)
        draw_triangle_grid(ax,n-1,p2)
        draw_triangle_grid(ax,n-1,p3)
        draw_triangle_grid(ax,n-1,p4)
        
   
def draw_four_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') # plot the main square
        # create a new square for each corner -- represented as p1(bottom left), p2(top left)
        # p3(top right), and p4(top right)
        p1 = np.array([ [p[0][0] - w/4,p[0][1]-w/4],[p[0][0] + w/4,p[0][1]-w/4],[p[0][0] 
        +w/4 ,p[0][1]+w/4],[p[0][0] -w/4 ,p[0][1]+w/4],[p[0][0] - w/4,p[0][1]-w/4]])
        p2 = np.array([ [p[1][0] -w/4 ,p[1][1]-w/4],[p[1][0] +w/4 ,p[1][1]-w/4],[p[1][0] 
        +w/4 ,p[1][1]+w/4],[p[1][0] -w/4 ,p[1][1]+w/4],[p[1][0] -w/4 ,p[1][1]-w/4] ])
        p3 = np.array([ [p[2][0] -w/4 ,p[2][1]-w/4],[p[2][0] +w/4 ,p[2][1]-w/4],[p[2][0] 
        +w/4 ,p[2][1]+w/4],[p[2][0] -w/4 ,p[2][1]+w/4],[p[2][0] -w/4 ,p[2][1]-w/4] ])
        p4 = np.array([ [p[3][0] -w/4 ,p[3][1]-w/4],[p[3][0] +w/4 ,p[3][1]-w/4],[p[3][0] 
        +w/4 ,p[3][1]+w/4],[p[3][0] -w/4 ,p[3][1]+w/4],[p[3][0] -w/4 ,p[3][1]-w/4] ])
        #pass 4 recursive calls on each of the new p squares
        draw_four_squares(ax,n-1,p1,w/2)
        draw_four_squares(ax,n-1,p2,w/2)
        draw_four_squares(ax,n-1,p3,w/2)
        draw_four_squares(ax,n-1,p4,w/2)

        
def draw_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') # Draw squares
        i1 = [1,2,3,0,1]
        q = p*(1-w) + p[i1]*w  
        draw_squares(ax,n-1,q,w)

def draw_four_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color='k')
        draw_four_circles(ax,n-1,[center[0],center[1]+radius],radius/2)
        draw_four_circles(ax,n-1,[center[0],center[1]-radius],radius/2)
        draw_four_circles(ax,n-1,[center[0]+radius,center[1]],radius/2)
        draw_four_circles(ax,n-1,[center[0]-radius,center[1]],radius/2)
        
def drawCircles(center,radius,n,w): #draw a circle recursively
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color='k')
        drawCircles(center,radius *(1-(w)),n-1,w)
        
def draw_branches(ax, n, p, xpos, ypos):#returns the drawing of branches
    if n > 0:
       points = np.zeros((3, 2))
       points[:3] = p #populates the whole array with what p is
       points[0][0] -= xpos #for the left branch
       points[0][1] -= ypos
       points[2][0] += xpos #for the right branch
       points[2][1] -= ypos 
       ax.plot(points[:,0],points[:,1], linewidth=0.5, color='k') 
       draw_branches(ax, n-1, points[0], xpos/2, ypos)
       draw_branches(ax, n-1, points[2], xpos/2, ypos)
        
def draw_trees(ax,n,p,deg,turn_angle,L):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') # Draw tree
        L = L* 3/4
        r_xPos = p[1][0] + L * math.cos(math.radians(deg))
        r_yPos =p[1][1] + L * math.sin(math.radians(deg)) -deg
        p1 = np.array([[p[1][0],p[1][1]],[r_xPos,r_yPos]])
        
        l_xPos = p[1][0] - L * math.cos(math.radians(deg))
        l_yPos =p[1][1] - L * math.sin(math.radians(deg)) 
        p2 = np.array([[p[1][0],p[1][1]],[l_xPos,l_yPos]])
        
        draw_trees(ax,n-1,p1, deg/1.5 ,turn_angle/1.6 ,L)
        draw_trees(ax,n-1,p2,deg/1.5,turn_angle/1.6,L)
        

if __name__ == "__main__":  
    
    plt.close("all") # Close all figures
    
    orig_size = 1000.0
    p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
    print('Points in original square:')
    print(p)
    
#    fig, ax = plt.subplots()
#    draw_squares(ax,6,p,.1)
#    ax.set_aspect(1.0)
#    ax.axis('off') # Uncomment to see coordinates in drawing
#    plt.show()
#    fig.savefig('squaresa.png')
#    
#    fig, ax = plt.subplots()
#    draw_squares(ax,10,p,.2)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('squaresb.png')
#    
#    fig, ax2 = plt.subplots()
#    draw_squares(ax2,5,p,.3)
#    ax2.set_aspect(1.0)
#    ax2.axis('off')
#    plt.show()
#    fig.savefig('squaresc.png')
#   
#    fig, ax = plt.subplots() 
#    draw_four_circles(ax, 2, [0,0], 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('four_circlesa.png')
#    
#    fig, ax = plt.subplots() 
#    draw_four_circles(ax, 3, [0,0], 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('four_circlesb.png')
#    
#    fig, ax = plt.subplots() 
#    draw_four_circles(ax, 4, [0,0], 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('four_circlesc.png')
#   
#    fig, ax = plt.subplots() 
#    drawCircles([0,0],100,3,(1/3))
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('circlesa.png')
#    
#    fig, ax = plt.subplots() 
#    drawCircles([0,0],100,9,(1/6))
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('circlesb.png')
#    
#    fig, ax = plt.subplots() 
#    drawCircles([0,0],100,9,(1/9))
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('circlesc.png')
#
    a = np.array([[0,0],[50,100],[100,0],[0,0]])
#    fig, ax = plt.subplots() 
#    draw_triangles(ax, 3, a)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('trianglesa.png')
#    
#    fig, ax = plt.subplots() 
#    draw_triangles(ax, 6, a)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('trianglesb.png')
#    
#    fig, ax = plt.subplots() 
#    draw_triangles(ax, 9, a)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('trianglesc.png')
#    
    fig, ax = plt.subplots() 
    draw_triangle_grid(ax, 2, a)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('triangleGrida.png')
    
    fig, ax = plt.subplots() 
    draw_triangle_grid(ax, 3, a)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('triangleGridb.png')
    
    fig, ax = plt.subplots() 
    draw_triangle_grid(ax, 4, a)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('triangleGridc.png')
# 
#    squares = np.array([[0,0],[0,100],[100,100],[100,0],[0,0]])
#    fig, ax = plt.subplots() 
#    draw_four_squares(ax, 2, squares, 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('four_squaresa.png')
#    
#    fig, ax = plt.subplots() 
#    draw_four_squares(ax, 3, squares, 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('four_squaresb.png')
#    
#    fig, ax = plt.subplots() 
#    draw_four_squares(ax, 4, squares, 100)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('four_squaresc.png')
#    
#    
#    branches = np.array([[500, 1000]])
#    fig, ax = plt.subplots() #5a, draw_branch method
#    draw_branches(ax, 4, branches, 3, 1)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('branchesa.png')
#    
#    fig, ax = plt.subplots() #5a, draw_branch method
#    draw_branches(ax, 5, branches, 3, 1)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('branchesb.png')
#    
#    fig, ax = plt.subplots() #5a, draw_branch method
#    draw_branches(ax, 6, branches, 3, 1)
#    ax.set_aspect(1.0)
#    ax.axis('off')
#    plt.show()
#    fig.savefig('branchesc.png')
    
    trees = np.array([[0,0],[0,100]])
    fig, ax = plt.subplots() 
    draw_trees(ax, 5, trees,45,45,100)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treesa.png')
    
    
    

