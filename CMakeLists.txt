cmake_minimum_required(VERSION 3.0.2)
project(my_navigation)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib
  move_base_msgs
  std_msgs
  nav_msgs
)

catkin_package()
catkin_install_python(PROGRAMS
  src/task_manager_node.py
  src/qr_reader_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

