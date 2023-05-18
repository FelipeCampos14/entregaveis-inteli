import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
import math

# Inputando as coordenadas para ir
coord_x = float(input("para que coordenada x quer ir? "))
coord_y = float(input("para que coordenada y quer ir? "))
# Definindo um intervalo para evitar que o robô fiquei travado, indo e voltando no ponto
dist_segura = 0.05

class GazeboRoda(Node):
    def __init__(self):
        super().__init__("node_gazebo")
        # Publisher para movimentar, no tópico 'cmd_vel
        self.cmd_vel_publish = self.create_publisher(Twist, '/cmd_vel', 10)
        # Subscriber para obter a posição, no tópico 'odom
        self.odom2 = self.create_subscription(Odometry, '/odom', self.odometria, 10)

    def odometria(self, msg, vel_msg:Twist): 
        # Acertando as posições e ângulos
        x = float(msg.pose.pose.position.x)
        y = float(msg.pose.pose.position.y)
        ang = msg.pose.pose.orientation
        # Tranformando coordenadas atuais em ângulo de euler 
        _, _, theta = euler_from_quaternion([ang.x, ang.y, ang.z, ang.w])
        dif_ang_x = coord_x - x
        dif_ang_y = coord_y - y
        # Usando arco tangente para ter a posição desejada em ângulo de euler também
        angulo = math.atan2(dif_ang_y, dif_ang_x)
        # Calcula a diferença entre os ângulo atual e desejado
        dif_ang_total = theta - angulo
        # Primeiro acerta o ângulo
        if abs(dif_ang_total) > 0.1:
            vel_msg.angular.z = 0.2
            vel_msg.linear.x = 0.0
        # Depois se movimentar na direção definida
        elif abs(coord_x - x) > dist_segura and abs(coord_y - y) > dist_segura:
            vel_msg.linear.x = 0.2
            vel_msg.angular.z = 0.0
        # Quanod chega no local, para
        else:
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.0
        # Publisher da posição e print das posições apenas para acompanhamento
        self.cmd_vel_publish.publish(vel_msg)
        self.get_logger().info(f"x={round(x, 2)},y={round(y, 2)}, dif_ang_total={abs(round(dif_ang_total, 2))}")

def main(args=None):
    rclpy.init(args=args)
    node = GazeboRoda()
    rclpy.spin(node)
    rclpy.shutdown