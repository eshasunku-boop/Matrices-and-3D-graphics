import numpy as np
import matplotlib.pyplot as plt


# Step 1-4: rotation matrix 
def rotation(theta_x, theta_y, theta_z):
    """Return the 3x3 rotation matrix R = Rx @ Ry @ Rz."""
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(theta_x), -np.sin(theta_x)],
                   [0, np.sin(theta_x),  np.cos(theta_x)]])

    Ry = np.array([[ np.cos(theta_y), 0, -np.sin(theta_y)],
                   [ 0,               1,  0],
                   [ np.sin(theta_y), 0,  np.cos(theta_y)]])

    Rz = np.array([[np.cos(theta_z), -np.sin(theta_z), 0],
                   [np.sin(theta_z),  np.cos(theta_z), 0],
                   [0, 0, 1]])

    return Rx @ Ry @ Rz


# Projection matrix (drops one coordinate) 
def projection(drop="z"):
    """Return a 3x3 matrix that flattens points by dropping x, y or z."""
    P = np.eye(3)
    i = {"x": 0, "y": 1, "z": 2}[drop]
    P[i, i] = 0
    return P


# Step 5: cube vertices and adjacency matrix 
Vertices = np.array([[ 1,  1,  1],
                     [-1,  1,  1],
                     [ 1, -1,  1],
                     [ 1,  1, -1],
                     [-1, -1,  1],
                     [-1,  1, -1],
                     [ 1, -1, -1],
                     [-1, -1, -1]])

Edges = np.zeros((8, 8))
for a, b in [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 4),
             (2, 6), (3, 5), (3, 6), (4, 7), (5, 7), (6, 7)]:
    Edges[a, b] = 1
Edges = Edges + Edges.T  # make symmetric


# Step 6-7: rotate the vertices 
rotmat = rotation(np.pi / 3, np.pi / 4, np.pi / 6)
VertRot = Vertices @ rotmat.T      # rows are vertices, hence the transpose


# Sanity checks 
# necesary??
print("R is orthogonal:      ", np.allclose(rotmat.T @ rotmat, np.eye(3)))
print("det(R) = 1:           ", np.isclose(np.linalg.det(rotmat), 1))
print("det(P) = 0 (no inverse):", np.isclose(np.linalg.det(projection("z")), 0))


# Step 8-9: draw the projections 
def draw_cube(drop, title):
    """Project VertRot by dropping one coordinate, then draw the edges."""
    P = projection(drop)
    VertProj = VertRot @ P.T
    cols = [c for c in range(3) if c != {"x": 0, "y": 1, "z": 2}[drop]]

    plt.figure()
    plt.axis("equal")
    for j in range(8):
        for k in range(j + 1, 8):        
            if Edges[j, k] == 1:
                plt.plot([VertProj[j, cols[0]], VertProj[k, cols[0]]],
                         [VertProj[j, cols[1]], VertProj[k, cols[1]]], "b-")
    plt.title(title)
    plt.grid()


draw_cube("z", "Rotated cube, z dropped (step 8)")
draw_cube("y", "Rotated cube, y dropped (step 9)")
plt.show()
