from stl import mesh, Mode

# Specify the path of our stl model

stl_path = "STL Files//mini_car.stl"
stl_model = mesh.Mesh.from_file(stl_path)

vectors = stl_model.vectors
normals = stl_model.normals

print(vectors[0:10])
print(normals[0:10])

stl_model.save("STL Files//mini_car_ASCII.stl", mode=Mode.ASCII)
