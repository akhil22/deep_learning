#!/usr/bin/python
#scores = [3.0, 1.0, 0.2]
import numpy as np
import matplotlib.pyplot as plt
def softmax(x):
    return np.exp(x)/np.sum(np.exp(x),axis= 0)
def main():
    x = np.arange(-2.0, 6.0, 0.1)
    scores = np.vstack([x, np.ones_like(x), 0.2*np.ones_like(x)])
    print scores
    print softmax(scores)
    plt.plot(x,softmax(scores).T, linewidth = 2)
    plt.show()
if __name__=='__main__':
    main()

