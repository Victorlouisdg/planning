import pybullet as p
import time
import planning

physicsClient = p.connect(p.GUI)
robot_id = p.loadURDF(planning.ur5e, useFixedBase=True)

for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()
