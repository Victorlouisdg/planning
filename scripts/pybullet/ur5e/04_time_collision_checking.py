from typing import List
import pybullet as p
import time
import planning
import numpy as np
from termcolor import cprint
import pybullet_planning as pp
from pybullet_planning import wait_for_user

# Adapted from pybullet_demo.py in pybullet_planning

physicsClient = p.connect(p.DIRECT)
robot = p.loadURDF(planning.ur5e, useFixedBase=True)

joint_angles_start = np.deg2rad([0, -90, 0, -90, 0, 0])

ik_joints = pp.get_movable_joints(robot)
ik_joint_names = pp.get_joint_names(robot, ik_joints)

link_names = [(link, pp.get_link_name(robot, link)) for link in pp.get_all_links(robot)]
cprint("link_names: {}".format(link_names), "yellow")

pp.set_joint_positions(robot, ik_joints, joint_angles_start)

# Setting up the collision checking
robot_self_collision_disabled_link_names = [
    ("base_link", "shoulder_link"),
    ("shoulder_link", "upper_arm_link"),
    ("upper_arm_link", "forearm_link"),
    ("forearm_link", "wrist_1_link"),
    ("wrist_1_link", "wrist_2_link"),
    ("wrist_2_link", "wrist_3_link"),
    ("wrist_1_link", "wrist_3_link"),
]

# This function converts the link names to link indices
self_collision_links = pp.get_disabled_collisions(robot, robot_self_collision_disabled_link_names)


collision_fn = pp.get_collision_fn(
    robot, ik_joints, obstacles=[], attachments=[], self_collisions=True, disabled_collisions=self_collision_links
)


cprint("self_collision_links disabled: {}".format(self_collision_links), "yellow")

start_time = time.time()

for i in range(10000):
    random_joints = np.random.uniform(-np.pi, np.pi, len(ik_joints))
    collision_fn(random_joints)

end_time = time.time()
cprint(f"Time elapsed: {end_time - start_time:.2f} seconds.", "yellow")

p.disconnect()
