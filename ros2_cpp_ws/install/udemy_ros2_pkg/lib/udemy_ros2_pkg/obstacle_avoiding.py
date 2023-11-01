#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from threading import Lock

class ObstacleAvoidingBot(Node):
    def __init__(self):
        super().__init__('Go_to_position_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 40)
        self.subscription = self.create_subscription(LaserScan, '/scan', self.get_scan_values, 40)
        self.linear_vel = 0.22
        self.regions = {'A1': [], 'A2': [], 'A3': [], 'A4': [], 'A5': [], 'A6': [], 'A7': [], 'A8': []}
        self.velocity = Twist()
        self.lock = Lock()

    def get_scan_values(self, scan_data):
        if len(scan_data.ranges) != 360:
            self.get_logger().warn("Unexpected number of data points in scan!")
            return
        
        with self.lock:
            self.regions = {
                'A1': min(min(scan_data.ranges[0:45]), 100),
                'A2': min(min(scan_data.ranges[45:90]), 100),
                'A3': min(min(scan_data.ranges[90:135]), 100),
                'A4': min(min(scan_data.ranges[135:180]), 100),
                'A5': min(min(scan_data.ranges[180:225]), 100),
                'A6': min(min(scan_data.ranges[225:270]), 100),
                'A7': min(min(scan_data.ranges[270:315]), 100),
                'A8': min(min(scan_data.ranges[315:359]), 100),
            }
            
            self.send_cmd_vel()

        # Print regions (outside the lock to avoid potential delays)
        print(self.regions['A1'], " / ", ... , self.regions['A8'])

    def send_cmd_vel(self):
        with self.lock:
            self.velocity.linear.x = self.linear_vel
            # ... [rest of the logic for setting velocities]
            self.publisher.publish(self.velocity)

def main(args=None):
    rclpy.init(args=args)
    oab = ObstacleAvoidingBot()
    rclpy.spin(oab)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


# #!/usr/bin/env python3

# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import LaserScan
# from geometry_msgs.msg import Twist


# class ObstacleAvoidingBot(Node):
#     def __init__(self):
#         super().__init__('Go_to_position_node') ## Name of the node
#         # publicher
#         self.publisher = self.create_publisher(Twist, '/cmd_vel', 40)
#         # subscriber
#         self.subscription=self.create_subscription(LaserScan,'/scan',self.get_scan_values,40)
#         ## periodic publisher call
#         #timer_period = 0.1;self.timer = self.create_timer(timer_period, self.send_cmd_vel)
#         ## Initializing Global values
#         ## given a value for VELOCITY
#         self.linear_vel = 0.22
#         ## Making dictionary to divide the area of laser acN
#         self.regions= {'A1': [],'A2': [],'A3': [],'A4': [],'A5': [],'A6': [],'A7': [],'A8': []}
#         ## Creating a message object to fit new velocities and publish them
#         self.velocity=Twist() 

# ## Subscriber Callback function
#     def get_scan_values(self,scan_data):
#         ## We have 360 data points and we dividing them in 8 regions
#         ## We say if there is something in the region get the smallest value
#         self.regions = {
#             'A1':  min(min(scan_data.ranges[0:45])  , 100),
#             'A2':  min(min(scan_data.ranges[45:90])  , 100),
#             'A3':  min(min(scan_data.ranges[90:135])  , 100),
#             'A4':  min(min(scan_data.ranges[135:180])  , 100),
#             'A5':  min(min(scan_data.ranges[180:225])  , 100),
#             'A6':  min(min(scan_data.ranges[225:270])  , 100),
#             'A7':  min(min(scan_data.ranges[270:315])  , 100),
#             'A8':  min(min(scan_data.ranges[315:359])  , 100),
#         }
#         self.send_cmd_vel()
        
#         print(self.regions['A1']," / ", self.regions['A2']," / ",
#         self.regions['A3']," / ", self.regions['A4']," / ",
#         self.regions['A5']," / ", self.regions['A6']," / ",
#         self.regions['A7']," / ", self.regions['A8'])
       
        
        
#     ## Callback Publisher of velocities call every 0.2 seconds
#     def send_cmd_vel(self):
#         ##Angular and linear velocities are set into object self.velocity
#         ## setting the linear velocity to be fixed and robot will keep on moving
#         self.velocity.linear.x=self.linear_vel
#         ## cases to make the robot change its angular velocity
#         if(self.regions["A8"] > 4 and self.regions["A5"] > 4 and self.regions["A2"] > 4 ):
#             self.velocity.angular.z=0.0 # condition in which area is total clear
#             #print("forword")
#         elif(self.regions["A8"] > 4 and self.regions["A5"] > 4 and self.regions["A2"] < 4 ):
#             self.velocity.angular.z=1.57 # object on right, taking left
#             #print("left")
#         elif(self.regions["A8"] < 4 and self.regions["A5"] > 4 and self.regions["A2"] > 4 ):
#             self.velocity.angular.z=-1.57 # object on left, taking right
#             #print("right")
#         elif(self.regions["A8"] < 4 and self.regions["A5"] < 4 and self.regions["A2"] < 4 ):
#             self.velocity.angular.z=2.9 # object on ahead take full turn
#             self.velocity.linear.x=-self.linear_vel
#             #
#         else: ## add more code later
#             print("some other conditions are required to be programmed")

#         ## lets publish the complete velocity
#         self.publisher.publish(self.velocity)


# def main(args=None):
#     rclpy.init(args=args)
#     oab=ObstacleAvoidingBot()
#     rclpy.spin(oab)
#     rclpy.shutdown()

# if __name__ == '__main__':
#     main()