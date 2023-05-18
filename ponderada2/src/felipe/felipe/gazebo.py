import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from time import sleep
import math

coord_x = float(input("para que coordenada x quer ir? "))
coord_y = float(input("para que coordenada y quer ir? "))
dist_segura = 0.05

class GazeboRoda(Node):
    def __init__(self):
        super().__init__("node_gazebo")
        self.cmd_vel_publish = self.create_publisher(Twist, "/cmd_vel", 10)
        self.odom2 = self.create_subscription(Odometry, '/odom', self.odometria, 10)
        self.x = 0
        self.get_logger().info("rodano")

    def odometria(self, msg): 
        # acertando as posições e ângulos
        x = float(msg.pose.pose.position.x)
        y = float(msg.pose.pose.position.y)
        ang = msg.pose.pose.orientation
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        
        dif_ang_x = coord_x - x
        dif_ang_y = coord_y - y

        angulo = math.atan2(dif_ang_y, dif_ang_x)

        dif_ang_total = theta - angulo
        vel_msg = Twist()

        if abs(dif_ang_total) > 0.1:
            vel_msg.angular.z = 0.2
            vel_msg.linear.x = 0.0
        elif abs(coord_x - x) > dist_segura and abs(coord_y - y) > dist_segura:
            vel_msg.linear.x = 0.2
            vel_msg.angular.z = 0.0
        else:
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.0
        
        self.cmd_vel_publish.publish(vel_msg)
        self.get_logger().info(f"x={round(x, 2)},y={round(y, 2)}, dif_ang_total={abs(round(dif_ang_total, 2))}")

def main(args=None):
    rclpy.init(args=args)
    node = GazeboRoda()
    rclpy.spin(node)
    rclpy.shutdown