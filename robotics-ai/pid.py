import math

class PIDController():
    def __init__(self, kp: float, ki: float, kd: float):
        """
        Initializes PID controller
        
        :param kp: Description
        :type kp: float
        :param ki: Description
        :type ki: float
        :param kd: Description
        :type kd: float
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.errors = []


    def forward(self, set_point, curr_point, eps=1e-8):
        """
        computes the corrective control input
        
        :param self: Description
        :param set_point: Target value
        :param curr_point: Measured value
        """
        error = set_point - curr_point
        self.errors.append(error)
        
        integral = sum(self.errors[-self.dt:])
        derivative = (self.errors[-1] - self.errors[-2]) / (self.dt + eps)

        output = self.kp * error + self.ki * integral + self.kd * derivative
        return derivative
