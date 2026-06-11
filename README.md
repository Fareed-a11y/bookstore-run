# my_navigation

## Project Structure

```text
my_navigation/
├── CMakeLists.txt
├── package.xml
├── README.md
├── config/
│   └── mission.yaml          # Target coordinates (YAML)
├── launch/
│   ├── simulation.launch     # Starts Gazebo bookstore environment
│   ├── slam.launch           # Template placeholder for SLAM mapping
│   ├── navigation.launch     # Starts map_server, AMCL, and move_base
│   └── task_manager.launch   # Loads parameters and triggers autonomous execution
├── maps/
│   ├── map.pgm               # Occupancy grid map image
│   └── map.yaml              # Map metadata configuration
├── world/
│   └── bookstore.world       # 3D bookstore environment file
└── src/
    ├── qr_reader_node.py     # Odometry tracking / verification node
    └── task_manager_node.py  # Actionlib navigation client node
```

---

## Execution Instructions

To run the complete autonomous navigation simulation, open **three separate terminal windows**, source your workspace in each terminal, and execute the following commands in order:

```bash
source devel/setup.bash
```

### 1. Launch the Simulation Environment

Starts Gazebo, loads the bookstore environment, and spawns the TurtleBot3 Burger model.

```bash
export TURTLEBOT3_MODEL=burger
roslaunch my_navigation simulation.launch
```

### 2. Launch the Navigation Stack

Loads the static bookstore map, initializes AMCL localization, and configures the global and local costmaps used for path planning.

```bash
roslaunch my_navigation navigation.launch
```

> **Note:** If the robot's laser scans are not properly aligned with the map, use the **2D Pose Estimate** tool in RViz to initialize localization, or kill the rviz and relaunch navigation.

### 3. Launch the Task Manager

Loads waypoint parameters from `mission.yaml` into the ROS parameter server and starts the navigation client responsible for visiting all target locations.

```bash
roslaunch my_navigation task_manager.launch
```

---

## Overview

This package provides an autonomous navigation workflow for a TurtleBot3 operating in a bookstore environment. The system combines:

* Gazebo simulation
* AMCL-based localization
* ROS Navigation Stack (`move_base`)
* YAML-configured mission waypoints
* Actionlib-based task execution

The robot autonomously navigates through predefined target locations specified in `config/mission.yaml`.
