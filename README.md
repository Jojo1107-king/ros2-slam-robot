# 🤖 ROS 2 Jazzy SLAM Robot

A four-wheel autonomous mobile robot developed using **ROS 2 Jazzy**, **Gazebo Sim**, **RViz2**, and **SLAM Toolbox**. This project demonstrates robot simulation, real-time mapping (SLAM), and autonomous navigation in a simulated environment.

---

## 🚀 Features

- Four-wheel mobile robot simulation
- Robot visualization using RViz2
- Gazebo Sim integration
- Real-time mapping using SLAM Toolbox
- ROS 2 Jazzy launch system
- Autonomous Navigation using Nav2
- Modular ROS 2 package structure

---

## 🛠️ Technologies Used

- ROS 2 Jazzy
- Ubuntu 24.04 LTS
- Gazebo Sim
- RViz2
- SLAM Toolbox
- Nav2
- URDF
- Python
- Git & GitHub

---

## 📁 Project Structure

```text
slam_robot_ws/
│
├── src/
│   └── slam_robot_description/
│       ├── launch/
│       ├── urdf/
│       ├── worlds/
│       ├── config/
│       └── package.xml
│
├── build/
├── install/
├── log/
└── README.md
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Jojo1107-king/ros2-slam-robot.git
```

Move into the workspace:

```bash
cd ros2-slam-robot
```

Build the workspace:

```bash
colcon build
```

Source the workspace:

```bash
source install/setup.bash
```

---

## ▶️ Running the Project

Launch the simulation:

```bash
ros2 launch slam_robot_description rsp_gazebo.launch.py
```

Start SLAM:

```bash
ros2 launch slam_robot_description slam.launch.py
```

Launch Navigation:

```bash
ros2 launch slam_robot_description navigation.launch.py
```

---

## 📸 Project Demonstration

### Gazebo Simulation

> *(Add a screenshot here)*

### RViz2 Visualization

> *(Add a screenshot here)*

### SLAM Mapping

> *(Add a screenshot here)*

### Autonomous Navigation

> *(Add a screenshot here)*

---

## 📌 Future Improvements

- Obstacle avoidance
- Dynamic path planning
- Camera integration
- LiDAR optimization
- Multi-robot navigation
- Real robot deployment

---

## 📚 Learning Outcomes

Through this project I learned:

- ROS 2 workspace management
- Robot modeling using URDF
- Gazebo simulation
- RViz visualization
- SLAM Toolbox integration
- Navigation2 (Nav2)
- ROS 2 launch system
- Git and GitHub workflow

---

## 👨‍💻 Author

**Jonathan M**

Robotics & Automation Engineering Student

GitHub: https://github.com/Jojo1107-king

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.