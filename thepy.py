import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Helper function to draw a cube at a given position (x, y, z)
def draw_cube(ax, position, color):
    x, y, z = position
    # Create a cube using the vertices of a unit cube
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], 
                         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    # Translate the vertices to the given position
    vertices = vertices + np.array([x, y, z])
    # Define the 6 faces of the cube
    faces = [[vertices[j] for j in [0, 1, 2, 3]],  # bottom
             [vertices[j] for j in [4, 5, 6, 7]],  # top
             [vertices[j] for j in [0, 1, 5, 4]],  # front
             [vertices[j] for j in [2, 3, 7, 6]],  # back
             [vertices[j] for j in [0, 3, 7, 4]],  # left
             [vertices[j] for j in [1, 2, 6, 5]]]  # right
    # Draw the faces
    ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='r', alpha=.25))

# Create the puzzle pieces
def create_puzzle_pieces(ax):
    # Piece 1: A line of 4 cubes
    piece_1 = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 0)]
    
    # Piece 2: An L-shape with 5 cubes
    piece_2 = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (2, 1, 0), (2, 2, 0)]
    
    # Piece 3: A T-shape with 5 cubes
    piece_3 = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (1, 1, 0), (1, -1, 0)]
    
    # Piece 4: A rectangular block of 6 cubes (2x3)
    piece_4 = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (1, 1, 0), (2, 1, 0)]
    
    # Piece 5: A zigzag shape of 6 cubes
    piece_5 = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (2, 1, 0), (2, 2, 0), (3, 2, 0)]
    
    # Draw each piece in a different color
    colors = ['blue', 'green', 'red', 'yellow', 'purple']
    for i, piece in enumerate([piece_1, piece_2, piece_3, piece_4, piece_5]):
        for cube in piece:
            draw_cube(ax, cube, colors[i])

# Plotting the puzzle pieces
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
create_puzzle_pieces(ax)

# Set the axes properties
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
