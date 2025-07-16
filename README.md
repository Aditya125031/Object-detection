# 🤖 Mclaren – ROS 2 Differential Drive Robot Simulation

Welcome to **Mclaren_p1**, a simulated 4-wheeled differential drive robot developed using **ROS 2** and **Gazebo**. This package is ideal for exploring basic robot mobility, sensor integration, teleoperation, and obstacle detection using LiDAR.

---

## 📦 Package: `mclaren_robo`

### 🔧 Features
- 🛞 **4-Wheel Differential Drive**  
- 🔍 **10 Hz LiDAR Sensor**  
- 🎥 **30 Hz RGB Camera**  
- 🎮 **Keyboard Teleoperation** (via `teleop_twist_keyboard` and XTerm)  
- 🚨 **Wall Detection System**: Stops robot within 0.5 meters of a wall  
- 🧭 **RViz2 Visualization**  
- 🌍 **Custom Gazebo World** with lighting, gravity, and obstacles

## 📦 Package: `orange_cone_detector`
- Node that detects the orange color and also detects the shape



## 🧪 How to Use

# 🚀 How to Run the `mclaren_robo` ROS 2 Package

This guide walks you through setting up and launching the **mclaren_robo* ROS 2 package simulation.

---

## 📦 1. Clone the Repository

Navigate to the `src/` folder of your ROS 2 workspace and clone the repo:

```bash
git clone https://github.com/Aditya125031/Object-detection.git
```

## 🔧 2. Build the Workspace

Navigate to the root of your workspace and build the packages using `colcon`:

```bash
colcon build
```
## ✅ 3. Source the Workspace

Source the workspace to overlay your ROS 2 environment:

```bash
source install/setup.bash
```

## 🚀 4. Launch the Simulation

To start the complete simulation with **Gazebo**, **RViz2**, and control interfaces, run:

```bash
ros2 launch mclaren_robo mclaren_p1_launch.py
```

### 🎯 5. Run the Cone Detector

In a **new terminal window**:

1. Navigate to the root of your ROS 2 workspace.
2. Source the workspace again:

   ```bash
   source install/setup.bash
   ```
3.Run the detector node
  ```bash
  ros2 run orange_cone detector cone_detector.py
  ```
## 🧪 Troubleshooting Tips

### ❌If launch fails, make sure the workspace is sourced:

```
source install/setup.bash
```

### If using a new terminal, re-source your workspace before running launch or nodes.

## Improvements you can make

> ⚠️ **Note:**  
> The cone detector currently relies on color filtering and shape heuristics, so it **may occasionally mistake other objects** (like orange cylinders) for cones.  
> Integration with a depth camera was considered to improve accuracy, but couldn't be finalized in this version.
