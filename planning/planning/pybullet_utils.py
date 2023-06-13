from typing import List
import pybullet as p


def get_revolute_joints(robot_id: int) -> List[int]:
    """Finds all revolute joints of a robot. URDFs often contain many fixed joints that we don't really need.

    Args:
        robot_id: The robot's pybullet id.

    Returns:
        A list of joint indices that are revolute joints.
    """
    n_joints = p.getNumJoints(robot_id)
    revolute_joints = []
    for i in range(n_joints):
        joint_info = p.getJointInfo(robot_id, i)
        joint_type = joint_info[2]
        if joint_type == p.JOINT_REVOLUTE:
            revolute_joints.append(i)
    return revolute_joints


def set_joint_angles(robot_id:int, joints: List[int], angles: List[float]) -> None:
    """Sets the joint angles of a robot.

    Args:
        robot_id: The robot's pybullet id.
        joints: A list of joint indices.
        angles: A list of joint angles in radians.
    """
    for joint_index, joint_angle in zip(joints, angles):
        p.resetJointState(robot_id, joint_index, joint_angle)