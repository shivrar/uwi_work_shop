cmake_minimum_required(VERSION 2.8.3)
project(chatter)

# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  actionlib_msgs
)

## Generate messages in the 'msg' folder
add_message_files(
   FILES
   Num.msg
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
  AddTwoInts.srv
)

## Generate actions in the 'action' folder
add_action_files(
   DIRECTORY action
   FILES
   Talk.action
   Timer.action
)

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   actionlib_msgs
   std_msgs  # Or other packages containing msgs
)


catkin_package(
CATKIN_DEPENDS message_runtime
actionlib_msgs
)


include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

