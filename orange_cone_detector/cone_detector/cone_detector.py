#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

class ConeDetector(Node):
    def __init__(self):
        super().__init__('cone_detector')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/camera/image_raw',          # change if your topic differs
            self.image_callback,          # now this exists
            10
        )

    def image_callback(self, msg):       # ← indented four spaces
        frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        hsv   = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # orange cone HSV range
        lower_orange = np.array([10, 100, 100])
        upper_orange = np.array([25, 255, 255])

        mask = cv2.inRange(hsv, lower_orange, upper_orange)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 500:
                continue

            approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = h / float(w)

            perimeter = cv2.arcLength(cnt, True)
            if perimeter == 0:
                continue
            circularity = 4 * np.pi * (area / (perimeter ** 2))

            # taper check (bottom wider than top)
            mask_shape = np.zeros(mask.shape, dtype=np.uint8)
            cv2.drawContours(mask_shape, [cnt], -1, 255, -1)
            top_width    = np.count_nonzero(mask_shape[y])
            bottom_width = np.count_nonzero(mask_shape[y + h - 1])
            taper_ratio  = bottom_width / (top_width + 1e-5)

            if (len(approx) >= 3 and
                aspect_ratio > 1.2 and
                circularity < 0.6 and
                taper_ratio  > 1.4):
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
                cv2.putText(frame, "Cone", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("Cone Detection", frame)
        cv2.imshow("Mask", mask)
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    node = ConeDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()





