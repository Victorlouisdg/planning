from typing import List
import pybullet as p
import time
import planning
import numpy as np


physicsClient = p.connect(p.GUI)
robot_id = p.loadURDF(planning.ur5e, useFixedBase=True)

joint_angles = np.deg2rad([0, -90, 0, -90, 0, 0])

revolute_joints = planning.pybullet_utils.get_revolute_joints(robot_id)

planning.pybullet_utils.set_joint_angles(robot_id, revolute_joints, joint_angles)

dt = 0.001
p.setTimeStep(dt)

durations_seconds = 60
steps = int(durations_seconds / dt)

for i in range (steps):
    p.stepSimulation()
    time.sleep(dt)
    if i % 3000 == 0:
        random_joints = np.random.uniform(-np.pi, np.pi, len(revolute_joints))
        planning.pybullet_utils.set_joint_angles(robot_id, revolute_joints, random_joints)

p.disconnect()
