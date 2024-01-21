import numpy as np
from stl import mesh, Mode

# Define the vertices of the 3D triangle

vertices = np.array([
    [0, 0, 0],           # Vertex O (index 0)
    [1, 0, 0],           # Vertex A (index 1)
    [0.5, 0.87, 0],      # Vertex B (index 2)
    [0.5, 0.29, 0.82]    # Vertex C (index 3)
])


# Define the faces (triangles) with vertex indices

faces = np.array([
    [0, 1, 3],  # Triangle OAC
    [1, 2, 3],  # Triangle ABC
    [0, 2, 3],  # Triangle OBC
    [0, 1, 2]   # Triangle OAB
])

# Create the mesh

my_mesh = mesh.Mesh(np.zeros(np.shape(faces)[0], dtype=mesh.Mesh.dtype))
print(my_mesh)

# Create the mesh
for i, face in enumerate(faces):
    for j in range(3):
        my_mesh.vectors[i][j] = vertices[face[j]]

print(my_mesh.vectors)

# Save the mesh to an ASCII STL file

my_mesh.save('STL Files//tetrahedron_ASCII.stl', mode=Mode.ASCII)
my_mesh.save('STL Files//tetrahedron_BINARY.stl', mode=Mode.BINARY)
