# My Navigation Package

This ROS Noetic package implements autonomous indoor navigation for a TurtleBot3 (Burger) robot within a simulated bookstore environment. The robot navigates sequentially to predefined target stations, utilizing AMCL for localization and `move_base` for path planning.

---

## 📂 Package Structure

The package is structured strictly according to the project requirements:

```text
my_navigation/
├── CMakeLists.txt
├── package.xml
├── README.md
├── config/
│   └── mission.yaml          # Target coordinates (YAML)
├── launch/
│   ├── simülasyon.launch     # Starts Gazebo bookstore environment
│   ├── slam.launch           # Template placeholder for SLAM mapping
│   ├── navigation.launch     # Starts map_server, AMCL, and move_base
│   └── task_manager.launch   # Loads params and triggers autonomous execution
├── maps/
│   ├── map.pgm               # Occupancy grid map image
│   └── map.yaml              # Map metadata configuration
├── world/
│   └── bookstore.world       # 3D bookstore environment file
└── src/
    ├── qr_reader_node.py     # Odometry tracking / verification node
    └── task_manager_node.py  # Actionlib navigation client node
Execution Instructions
To run the complete autonomous simulation, open three separate terminal windows, resource your workspace (source devel/setup.bash), and execute the following commands in order:

1. Launch the Simulation Environment
Spins up Gazebo, loads the bookstore layout, and spawns the TurtleBot3 Burger model.

Bash
export TURTLEBOT3_MODEL=burger
roslaunch my_navigation simülasyon.launch

2. Launch Navigation stack
Loads the map server with the static bookstore map, initializes AMCL localization layers, and configures global/local costmaps for path planning.

Bash
roslaunch my_navigation navigation.launch
Note: Use the 2D Pose Estimate tool in RViz if the initial laser scans need synchronization with the map walls.

3. Launch the Task Manager Sequence
Loads the waypoint parameters from mission.yaml to the ROS parameter server and triggers the navigation client node to drive through all designated targets.

Bash
roslaunch my_navigation task_manager.launch
