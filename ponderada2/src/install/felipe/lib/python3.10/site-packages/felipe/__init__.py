#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from time import sleep
from turtlesim.srv import SetPen

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 1000)
        self.cor = SetPen.Request()
        self.twist_msg_ = Twist()
        self.move_sem_loop()
    
    def cor_caneta(self, r, g ,b, w):
        self.clientcolor_ = self.create_client(SetPen, 'turtle1/set_pen')
        self.cor.r = r  
        self.cor.g = g
        self.cor.b = b      
        self.cor.width = w        

        self.future = self.clientcolor_.call_async(self.cor)

    def move_sem_loop(self):
        turns = 0
        self.cor_caneta(255,255,0,3)
        sleep(1)
        while (turns<=31):
            self.twist_msg_.linear.x = 0.1
            self.twist_msg_.angular.z = 2.3
            self.publisher_.publish(self.twist_msg_)
            sleep(1)
            self.twist_msg_.linear.x = 0.3
            self.twist_msg_.angular.z = 0.0
            self.publisher_.publish(self.twist_msg_)
            sleep(1)
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = -2.5
            self.publisher_.publish(self.twist_msg_)
            sleep(1)
            self.twist_msg_.linear.x = 0.3
            self.twist_msg_.angular.z = 0.0
            self.publisher_.publish(self.twist_msg_)
            sleep(1)
            turns+=1

def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
