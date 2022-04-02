cmake_minimum_required(VERSION 2.8.3)

project(ares_description)

find_package(catkin REQUIRED COMPONENTS
  urdf
  xacro
  gazebo_plugins
  gazebo_ros
  gazebo_ros_control
  roscpp
  rospy
  controller_manager
  message_generation
  std_msgs
  sensor_msgs
)

catkin_package(
	CATKIN_DEPENDS urdf xacro
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
