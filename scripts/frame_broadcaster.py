#!/usr/bin/env python
import roslib
roslib.load_manifest('camera_controller')

import rospy
import tf

if __name__ == '__main__':
	rospy.init_node('frame_broadcaster')

	br = tf.TransformBroadcaster()
	rate = rospy.Rate(10.0)

	target_frame = rospy.get_param("~target_frame")

	while not rospy.is_shutdown():

		br.sendTransform((0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 1.0), rospy.Time.now(), target_frame, "world")

		rate.sleep()
