from matplotlib.colors import Normalize
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
fig.set_facecolor('black')
h = 1e-10
_ = np.linspace(-5, 5, 10*10**2)

def q(x, y):
    return (1*h+1)**(x/h)+np.sin(2*np.pi*5/10*y)

def xx(i):
    return 2*np.cos(2*np.pi/10*i)

def yy(i):
    return 4*np.sin(2*np.pi/10*i)

def dxx(i):
    return (xx(i+h)-xx(i))/h

def dyy(i):
    return (yy(i+h)-yy(i))/h

def simulation(t):
    ax.clear()
    ax.set_facecolor('black')
    ax.xaxis.pane.set(visible=0)
    ax.yaxis.pane.set(visible=0)
    ax.zaxis.pane.set(visible=1)

    ax.xaxis._axinfo['grid'].update(color='black')
    ax.yaxis._axinfo['grid'].update(color='black')
    ax.zaxis._axinfo['grid'].update(color='none')

    ax.set(xlim=[-5, 5], ylim=[-5, 5], zlim=[-5, 5])
    
    ax.plot(xx(_), yy(_), q(xx(_), yy(_)), color='red')
    ax.quiver(0, 0, 0, xx(t), yy(t), q(xx(t), yy(t)), color='white', arrow_length_ratio=0.1)
    Mag = mag = np.sqrt(dxx(_)**2 + dyy(_)**2 + ((q(xx(_+h), yy(_+h))-q(xx(_), yy(_)))/h)**2)
    norm = Normalize(Mag.min(), Mag.max())
    mag = np.sqrt(dxx(t)**2 + dyy(t)**2 + ((q(xx(t+h), yy(t+h))-q(xx(t), yy(t)))/h)**2)
    color = plt.get_cmap('plasma')(norm(mag))
    ax.quiver(xx(t), yy(t), q(xx(t), yy(t)), dxx(t)/mag, dyy(t)/mag, ((q(xx(t+h), yy(t+h))-q(xx(t), yy(t)))/h)/mag, color=color)

ani = FuncAnimation(fig, simulation, frames=np.linspace(-5, 5, 10**2), interval=0, blit=0)

plt.tight_layout()
plt.show()
