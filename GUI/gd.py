# import numpy as np
# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111)

# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# line, = ax.plot(t, s, lw=2)

# ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )

# ax.set_ylim(-2, 2)
# plt.show()
# import numpy as np
# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_subplot(111, polar=True)
# r = np.arange(0, 1, 0.001)
# theta = 2*2*np.pi*r
# line, = ax.plot(theta, r, color='#ee8d18', lw=3)

# ind = 800
# thisr, thistheta = r[ind], theta[ind]
# ax.plot([thistheta], [thisr], 'o')
# ax.annotate('a polar annotation',
#             xy=(thistheta, thisr),  # theta, radius
#             xytext=(0.05, 0.05),    # fraction, fraction
#             textcoords='figure fraction',
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             horizontalalignment='left',
#             verticalalignment='bottom',
#             )
# plt.show()
# from matplotlib.patches import Ellipse, Circle
# import matplotlib.pyplot as plt
# from matplotlib.lines import Line2D
# fig = plt.figure()
# line1 = Line2D(
#     [0, 1], [0, 1], transform=fig.transFigure, figure=fig, color="r")
# line2 = Line2D(
#     [0, 1], [1, 0], transform=fig.transFigure, figure=fig, color="g")
# fig.lines.extend([line1, line2])
# # fig.show()
# plt.savefig('D:/youget/1.png')
# plt.show()

# 画圆

from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
fig = plt.figure()
ax = fig.add_subplot(111)

line1 = Line2D(
    [0, 1], [0, 1], transform=fig.transFigure, figure=fig, color="r")
line2 = Line2D(
    [0, 1], [1, 0], transform=fig.transFigure, figure=fig, color="g")
fig.lines.extend([line1, line2])

#ell1 = Ellipse(xy=(0.0, 0.0), width=4, height=8, angle=30.0, facecolor='yellow', alpha=0.3)
cir1 = Circle(xy=(4, 4), radius=2, alpha=0.5)
# ax.add_patch(ell1)
ax.add_patch(cir1)

x, y = 0, 0
ax.plot(x, y, 'ro')

# plt.axis('scaled')

# changes limits of x or y axis so that equal increments of x and y have
# the same length
plt.axis('equal')

plt.show()

# from math import pi
# from numpy import cos, sin
# from matplotlib import pyplot as plt

# if __name__ == '__main__':
#     '''plot data margin'''
#     angles_circle = [i*pi/180 for i in range(0, 360)]  # i先转换成double
#     # angles_circle = [i/np.pi for i in np.arange(0,360)]             # <=>
#     # angles_circle = [i/180*pi for i in np.arange(0,360)]    X
#     x = cos(angles_circle)
#     y = sin(angles_circle)
#     plt.plot(x, y, 'r')

#     plt.axis('equal')
#     plt.axis('scaled')
#     plt.show()
