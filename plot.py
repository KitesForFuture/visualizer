import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3


class Plot:

    def __init__(self):

        # Attaching 3D axis to the figure
        self.fig = plt.figure()
        ax = p3.Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(ax)

        initial_vectors = np.array([
            # [[x values], [y values], [z values]]
            [[0,1],[0,0],[0,0]],
            [[0,0],[0,1],[0,0]],
            [[0,0],[0,0],[0,1]]
        ])

        self.lines = [ax.plot(vector[0], vector[1], vector[2])[0] for vector in initial_vectors]

        # Setting the axes properties
        ax.set_xlim3d([-1.0, 1.0])
        ax.set_xlabel('X')
        ax.set_ylim3d([-1.0, 1.0])
        ax.set_ylabel('Y')
        ax.set_zlim3d([-1.0, 1.0])
        ax.set_zlabel('Z')

        plt.show(block=False)
        plt.pause(0.001)

    def update(self, xyz_vectors):
        for i in range(0,3):
            # NOTE: there is no .set_data() for 3 dim data...
            self.lines[i].set_data(np.array([0, xyz_vectors[i][0]]), np.array([0, xyz_vectors[i][1]]))
            self.lines[i].set_3d_properties(np.array([0, xyz_vectors[i][2]]))
        self.fig.canvas.draw()
        plt.pause(0.001)
