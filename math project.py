import numpy as np

#row1=input("Enter the elements of Row 1 separated by spaces ").split()
#row2=input("Enter the elements of Row 2 separated by spaces ").split()
#row3=input("Enter the elements of Row 3 separated by spaces ").split()

#data=[]
#data.append(row1)
#data.append(row2)
#data.append(row3)

#matrix=np.array(data)
#print("This is the matrix",matrix)

theta_x=int(input("Enter the value of angle x in degrees"))
theta_y=int(input("Enter the value of angle y in degrees"))
theta_z=int(input("Enter the value of angle z in degrees"))

def rotation(theta_x,theta_y,theta_z):
    Rx=np.array([[1,0,0],
         [0,np.cos(np.radians(theta_x)),-np.sin(np.radians(theta_x))],
         [0,np.sin(np.radians(theta_x)),np.cos(np.radians(theta_x))]])

    Ry=np.array([[np.cos(np.radians(theta_y)),0,np.sin(np.radians(theta_y))],
         [0,1,0],
         [-np.sin(np.radians(theta_y)),0,np.cos(np.radians(theta_y))]])

    Rz=np.array([[np.cos(np.radians(theta_z)),-np.sin(np.radians(theta_z)),0],
         [np.sin(np.radians(theta_z)),np.cos(np.radians(theta_z)),0],
         [0,0,1]])

    #A=np.zeros((3,3))

    #for i in range(3):
        #for j in range(3):
         #   for k in range(3):
          #      A[i][j]+=Rx[i][k] *Ry[k][j]

    #result=np.zeros((3,3))

    #for i in range(3):
     #   for j in range(3):
      #      for k in range(3):
       #         result[i][j]+=A[i][k]*Rz[k][j]

    #print(result)
    R=Rx @ Ry @ Rz
    return (np.round(R,3))


rotation(theta_x,theta_y,theta_z)

