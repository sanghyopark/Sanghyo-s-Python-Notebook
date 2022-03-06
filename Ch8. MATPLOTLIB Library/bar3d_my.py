def bar3d_my(X, Y, Z, wx=None, wy=None, ax=None):
    import matplotlib.pyplot as plt
    import numpy as np
    
    X = np.array(X); Y = np.array(Y)
    dx = X[0][1]-X[0][0]; dy = Y[1][0]-Y[0][0]
    
    if wx == None: wx = dx/2
    if wy == None: wy = dy/2
    wx = min([wx, dx]); wy = min([wy, dy])
    xoffset = wx/2; yoffset = wy/2
    Xpos, Ypos = X-xoffset, Y-yoffset
    xpos = Xpos.ravel(); ypos = Ypos.ravel(); zpos = 0
    Z = np.array(Z)
    wz = Z.ravel()
    
    if ax==None:
        ax = plt.subplot(111, projection='3d')
    ax.bar3d(xpos,ypos,0,wx,wy,wz) #, zsort='avarage')
    plt.show()