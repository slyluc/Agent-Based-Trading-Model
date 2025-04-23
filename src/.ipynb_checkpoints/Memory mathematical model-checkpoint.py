import numpy as np
import matplotlib.pyplot as plt


def dx_dt(x, y):
    return y * (1 - x) - x * (1 - y)

def dy_dt(x, y):
    return x * (1 - y) - y * (1 - x)


def runge_kutta4(x0, y0, t0, t_final, h):
    t_values = np.arange(t0, t_final, h)
    x_values = np.zeros(len(t_values))
    y_values = np.zeros(len(t_values))
    
    x_values[0], y_values[0] = x0, y0
    
    for i in range(1, len(t_values)):
        t = t_values[i-1]
        x, y = x_values[i-1], y_values[i-1]

        k1_x = h * dx_dt(x, y)
        k1_y = h * dy_dt(x, y)

        k2_x = h * dx_dt(x + 0.5 * k1_x, y + 0.5 * k1_y)
        k2_y = h * dy_dt(x + 0.5 * k1_x, y + 0.5 * k1_y)

        k3_x = h * dx_dt(x + 0.5 * k2_x, y + 0.5 * k2_y)
        k3_y = h * dy_dt(x + 0.5 * k2_x, y + 0.5 * k2_y)

        k4_x = h * dx_dt(x + k3_x, y + k3_y)
        k4_y = h * dy_dt(x + k3_x, y + k3_y)

        x_values[i] = x + (1/6) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        y_values[i] = y + (1/6) * (k1_y + 2*k2_y + 2*k3_y + k4_y)
    
    return t_values, x_values, y_values


x0, y0 = 1, 0.5  
t0, t_final, h = 0, 10, 0.01  


t_vals, x_vals, y_vals = runge_kutta4(x0, y0, t0, t_final, h)


plt.plot(t_vals, x_vals, label='x')
plt.plot(t_vals, y_vals, label='y')
plt.xlabel('Time (t)')
plt.ylabel('Values of x and y')
plt.legend()
plt.title('Mathematical solution')
plt.grid()
plt.show()
