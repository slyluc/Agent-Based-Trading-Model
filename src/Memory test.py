import numpy as np
import matplotlib.pyplot as plt

t_max = 200
N=2
M=50


x = np.ones(M)
y = np.zeros(M)

def trade(X,Y):
    X_hist = np.zeros((t_max+1,M))
    Y_hist = np.zeros((t_max+1,M))
    memory_index_x = 0
    memory_index_y = 0
    
    for t in range(t_max):
        X_hist[t] = X
        Y_hist[t] = Y
        prod_x_want = np.random.choice(X)
        prod_y_want = np.random.choice(Y)
        '''
        memory_index_x = np.random.randint(M)
        X[memory_index_x] = prod_y_want
        

        memory_index_y = np.random.randint(M)
        Y[memory_index_y] = prod_x_want
        '''
        
        X[memory_index_x] = prod_y_want
        memory_index_x = (memory_index_x + 1) % M


        Y[memory_index_y] = prod_x_want
        memory_index_y = (memory_index_y + 1) % M
        

    X_hist[-1] = X
    Y_hist[-1] = Y

    return X_hist, Y_hist

A1,A2 = trade(x,y)

A1 = np.mean(A1,axis = 1)
A2 = np.mean(A2,axis = 1)

c=2

if c == 2:
    Data = np.zeros((1000,2, t_max+1))
    for i in range(1000):
        x = np.ones(M)
        y = np.zeros(M)
        A1,A2 = trade(x,y)

        A1 = np.mean(A1,axis = 1)
        A2 = np.mean(A2,axis = 1)

        Data[i, 0, :] = A1  # Store A1 in first row of Data[i]
        Data[i, 1, :] = A2  # Store A2 in second row of Data[i]

    AVG_DATA1 = np.mean(Data[:,0],axis=0)
    AVG_DATA2 = np.mean(Data[:,1],axis=0)
    print(AVG_DATA2.shape)

    plt.plot(Data[3,0],color = "green",alpha = 0.5, label = "Agent 1 - singular run")
    plt.plot(Data[3,1],color = "red",alpha = 0.5, label = "Agent 2 - singular run")
    plt.plot(AVG_DATA1, label = "Agent 1 - 1000 run average")
    plt.plot(AVG_DATA2, label = "Agent 2 - 1000 run average")
else:
    plt.plot(A1, label = "x")
    plt.plot(A2, label = "y")


plt.xlabel('Time (t)')
plt.ylabel(r'$\rho$')
plt.title('Simulation solution')
plt.legend()
plt.show()


