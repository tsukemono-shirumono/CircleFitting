import numpy as np
import math

def circFit(xs,ys,calc_err=True):#https://imagingsolution.blog.fc2.com/blog-entry-16.html
   M=np.empty([3,3])
   M[0,0]=np.sum(xs**2)
   M[0,1]=M[1,0]=np.sum(xs*ys)
   M[0,2]=M[2,0]=np.sum(xs)
   M[1,1]=np.sum(ys**2)
   M[1,2]=M[2,1]=np.sum(ys)
   M[2,2]=len(xs)

   V=np.empty(3)
   V[0]=-np.sum(xs**3+xs*ys**2)
   V[1]=-np.sum(xs**2*ys+ys**3)
   V[2]=-np.sum(xs**2+ys**2)
   try:
       A,B,C=np.linalg.inv(M) @ V
   except:#det(M)=0
       print("error:直線上に点がのってる")
       if calc_err==True:
           return None,None,None,None
       else:
           return None,None,None

   x_c=-0.5*A
   y_c=-0.5*B
   r=math.sqrt(x_c**2+y_c**2-C)

   if calc_err==True:
       rs=np.sqrt((xs-x_c)**2+(ys-y_c)**2)
       err=np.average((rs-r)**2)
       return x_c,y_c,r,err
   else:
       return x_c,y_c,r
