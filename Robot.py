import numpy as np
from math import pi, cos, sin, tan, atan, asin
class Robot:
    def __init__(self,D,L):
        # Variables geometricas del robot
        self.D = D
        self.L = L
        # Variables de control
        self.u1 = 0.0
        self.u2 = 0.0
        # Estado del robot
        self.X = np.array([0.0,0.0,0.0,0.0])
        
    @property
    def Xq_dot(self):
        phi = self.X[2]
        XqDot = self.u1*cos(phi)
        return XqDot
    
    @property
    def Yq_dot(self):
        phi = self.X[2]
        YqDot = self.u1*sin(phi)
        return YqDot
    
    @property
    def Phi_dot(self):
        phi_dot = (1/self.D) * (self.u1 * tan(self.u2))
        return phi_dot
    
    def advance_state(self,dt):
        Psi_dot = (self.u2 - self.X[3])/dt
        X_dot = np.array([self.Xq_dot,self.Yq_dot,self.Phi_dot, Psi_dot])
        
        self.X = self.X + X_dot * dt
        
        return self.X
    
    def set_controls(self,u1,u2):
        self.u1 = u1
        self.u2 = u2
        
    def set_state(self,array):
        self.X = array
        
        
class Controller:
    def __init__(self, x_kp, x_kd, y_kp, y_kd, phi_kp, phi_kd):
        self.x_k_p = x_kp
        self.x_k_d = x_kd
        self.y_k_p = y_kp
        self.y_k_d = y_kd
        self.phi_k_p = phi_kp
        self.phi_k_d = phi_kd
    
    def XY_controller(self,x_target,x_actual,x_dot_target,x_dot_actual,y_target,y_actual,y_dot_target,y_dot_actual,phi_actual):
        x_err = x_target-x_actual
        x_err_dot = x_dot_target-x_dot_actual
        
        p_termx = self.x_k_p*x_err
        d_termx = self.x_k_d*x_err_dot
#         X = p_termx + d_termx
        X = x_dot_target + p_termx + d_termx
        
        y_err = y_target - y_actual
        y_err_dot = y_dot_target - y_dot_actual

        p_termy = self.y_k_p * y_err
        d_termy = self.y_k_d * y_err_dot
#         Y = p_termy +d_termy
        Y = y_dot_target + p_termy +d_termy
        
        phi_commanded = 0.0
        v1 = 0.0
        if (X!=0.0):
            phi_commanded = atan(Y/X)
            if (cos(atan(Y/X)) !=0.0):
                v1 = X/cos(atan(Y/X))
        else:
            print('HOLA')
            pass
        
        return phi_commanded,v1
    
    def Psi_controller(self,phi_target,phi_actual,phi_dot_target, phi_dot_actual,v1,D):
        phi_err = phi_target - phi_actual
        phi_err_dot = phi_dot_target - phi_dot_actual
        p_term = self.phi_k_p * phi_err
        d_term = self.phi_k_d * phi_err_dot
        
        phi_dot =(phi_target - phi_actual)/0.002 + p_term + d_term

        psi = 0.0
        if (v1!=0.0):
            psi = atan((phi_dot*D)/v1)
        else:
            print('HoLA 2')
            pass
        return psi

    
    
        
        
        
        