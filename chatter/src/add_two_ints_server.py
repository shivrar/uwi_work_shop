#!/usr/bin/env python

from chatter.srv import *
import rospy


def handle_add_two_ints(req):
    print "Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b))
    return AddTwoIntsResponse(req.a + req.b)
# the response is auto generated from catkin_make


def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
# the service initialisation accepts the service name we're advertising,
# then type and finally the callback 
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add two ints from chatter"
    rospy.spin()


if __name__ == "__main__":
    add_two_ints_server()
