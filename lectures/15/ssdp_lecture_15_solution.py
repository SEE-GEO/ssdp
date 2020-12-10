import numpy as np
import matplotlib.pyplot as plt
import pyvista as pv

dx = 5e3
dy = 5e3
dz = 250
z_scaling = 5

################################################################################
# Surface data
################################################################################

# Loading the data.
elevation = np.load("elevation.npy")

# Create a mesh.
surface = pv.UniformGrid((elevation.shape[0], elevation.shape[1], 1),
                         (dx / 2.0, dy / 2.0, dz))
surface.point_arrays["elevation_scaled"] = z_scaling * elevation.ravel("F")
surface.point_arrays["elevation"] = elevation.ravel("F")
surface_warped = surface.warp_by_scalar("elevation_scaled")

# Add the texture
surface_warped.texture_map_to_plane(inplace=True)
texture = np.load("texture.npy")
texture = pv.numpy_to_texture(np.flipud(texture))

################################################################################
# Volume data
################################################################################

precipitation = np.load("precipitation.npy")[:, :, :]
nx, ny, nz = precipitation.shape
volume = pv.UniformGrid((nx + 1, ny + 1, nz + 1),
                        (dx, dy, dz * z_scaling))
volume.cell_arrays["Rain rate [mm/h]"] = np.minimum(precipitation.ravel("F"), 8.0)

plotter = pv.Plotter()
plotter.add_volume(volume)
plotter.add_mesh(surface_warped, texture=texture, specular=1)
plotter.show()

