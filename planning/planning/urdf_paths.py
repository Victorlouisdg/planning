import os

def robot_path(name: str) -> str:
    filepath = os.path.realpath(__file__)
    resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(filepath))), "resources")
    _robot_path = os.path.join(resources_path, "robots", f"{name}", f"{name}.urdf")
    return _robot_path

ur5e = robot_path("ur5e")