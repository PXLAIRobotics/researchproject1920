import rospy
import sys, signal
import threading
from sensor_msgs.msg import Joy

controller = None

class DuckieDemoController():
    INTERVAL = 0.02 # ms
    DURATION = 2
    STOPPED = False

    def __init__(self):
        rospy.init_node('DuckieDemoController', anonymous=True)
        self.pub = rospy.Publisher("/erna/joy", Joy, queue_size=1)
        self.vx = 1
        self.vy = 0
        self.total = 0

        self.update()

    def update(self):
        self.total = self.total + self.INTERVAL	
        
        if self.total > self.DURATION:
            self.vx = 0

        msg = Joy()
        msg.axes = [0.0, self.vx, 0.0, self.vy, 0.0, 0.0, 0.0, 0.0]
        self.pub.publish(msg)

        if not self.STOPPED:
            threading.Timer(self.INTERVAL, self.update).start()
    
    def stop(self):
        self.total = self.DURATION
        self.STOPPED = True

def on_close(sig, frame):
    print("Shutting down")
    if not controller == None:
        controller.stop()
    sys.exit()

if __name__ == "__main__":
    controller = DuckieDemoController()

    signal.signal(signal.SIGINT, on_close)

    rospy.spin()