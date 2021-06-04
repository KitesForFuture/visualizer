import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import collections

HEIGHT_GRAPH_HISTORY = 1000

class Plot:

    def __init__(self):
        self.fig = plt.figure()
        ax = plt.subplot(1,2,1, projection='3d')
        self._init_rotation_graph(ax)
        ax = plt.subplot(1,2,2)
        self._init_height_graph(ax)
        plt.show(block=False)
        plt.pause(0.001)

    def _init_rotation_graph(self, ax):
        initial_vectors = np.array([
            # [[x values], [y values], [z values]]
            [[0,1],[0,0],[0,0]],
            [[0,0],[0,1],[0,0]],
            [[0,0],[0,0],[0,1]]
        ])

        self.rotation_lines = [ax.plot(vector[0], vector[1], vector[2])[0] for vector in initial_vectors]

        # Setting the axes properties
        ax.set_xlim3d([-1.0, 1.0])
        ax.set_xlabel('X')
        ax.set_ylim3d([-1.0, 1.0])
        ax.set_ylabel('Y')
        ax.set_zlim3d([-1.0, 1.0])
        ax.set_zlabel('Z')

    def _init_height_graph(self, ax):
        self.height_history = collections.deque([0.0 for i in range(0, HEIGHT_GRAPH_HISTORY)], maxlen=HEIGHT_GRAPH_HISTORY)
        self.height_line = plt.plot(range(0, HEIGHT_GRAPH_HISTORY), self.height_history)[0]
        ax.set_ylim([-2,2])

    def update(self, flydata):
        self._update_rotation([flydata.x_rotation, flydata.y_rotation, flydata.z_rotation])
        self._update_height(flydata.height)
        self.fig.canvas.draw()
        plt.pause(0.001)

    def _update_rotation(self, xyz_vectors):
        for i in range(0,3):
            # NOTE: there is no .set_data() for 3 dim data...
            self.rotation_lines[i].set_data(np.array([0, xyz_vectors[i][0]]), np.array([0, xyz_vectors[i][1]]))
            self.rotation_lines[i].set_3d_properties(np.array([0, xyz_vectors[i][2]]))

    def _update_height(self, height):
        self.height_history.append(height)
        self.height_line.set_ydata(self.height_history)