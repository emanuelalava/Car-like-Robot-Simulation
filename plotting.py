from matplotlib import pyplot as plt
import matplotlib.pylab as pylab
def plotting(x,y,x_path,y_path,t):
    pylab.rcParams['figure.figsize'] = 20, 40
    plt.figure()
    plt.subplot(311)
    plt.plot(t[1:],x,linestyle='-',marker='.',color='red')
    plt.plot(t,x_path,linestyle='-',color='blue')
    plt.ylabel('$x$ [$m$]').set_fontsize(20)
    plt.xlabel('$time$ [$s$]').set_fontsize(20)
    plt.legend(['X Planned','X response'],fontsize = 14)
    plt.title('Respuesta del robot en el Eje x',fontsize = 24)
    
    plt.figure()
    plt.subplot(312)
    plt.plot(t[1:],y,linestyle='-',marker='.',color='yellow')
    plt.plot(t,y_path,linestyle='-',color='green')
    plt.ylabel('$y$ [$m$]').set_fontsize(20)
    plt.xlabel('$time$ [$s$]').set_fontsize(20)
    plt.legend(['Y Planned','Y response'],fontsize = 14)
    plt.title('Respuesta del robot en el Eje Y',fontsize = 24)

    plt.figure()
    plt.subplot(313)
    plt.plot(x_path,y_path,linestyle='-',color='black')
    plt.plot(x,y,linestyle='-',marker='.',color='red')
    plt.ylabel('$Y$ [$m$]').set_fontsize(20)
    plt.xlabel('$X$ [$m$]').set_fontsize(20)
#     plt.axis('equal')
    plt.legend(['XY Planned','XY response'],fontsize = 14)
    plt.title('Respuesta del robot en el plano de movimiento',fontsize = 24)

    plt.ylim(-6,6)
    plt.show()