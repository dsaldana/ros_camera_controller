#!/usr/bin/env python
import roslib
roslib.load_manifest('camera_controller')

import rospy

from ar_track_alvar.msg import AlvarMarkers
from geometry_msgs.msg import PoseStamped

# base_publisher = None

def marker_callback(marker_info):
	global base_publisher

	if base_publisher == None:
		return

	for marker in marker_info.markers:
		if marker.id == 0:
			base_publisher.publish( marker.pose )

if __name__ == '__main__':
	global base_publisher
	base_publisher = None

	# Init note
	rospy.init_node('pose_remap')

	# Get robot name
	robotName = rospy.get_param('~robot_name', 'mobile_base')

	# Subscribe to pose marker topic
	rospy.Subscriber("/ar_pose_marker", AlvarMarkers, marker_callback)

	# The redirect topic
	base_publisher = rospy.Publisher("/" + robotName + "/pose", PoseStamped)

	# Wait
	rospy.spin()
