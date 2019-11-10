from morse.builder import *

robot = ATRV('robot')
#robot.translate(x=-7.8, y=4.5, z=0.75)
robot.translate(z=0.0)
robot.add_stream('socket')
robot.add_service('socket')
robot.add_interface('socket')
motion = Waypoint()
#motion = MotionVW()
#motion.translate(z=0.3)
robot.append(motion)
motion.add_stream('socket')
motion.add_service('socket')
motion.add_interface('socket')



table = PassiveObject('props/furnitures','IKEA_cupboard_BILLY_2')
#table.setgraspable()
table.translate(x=0.65, y=0.65, z=0.0)
table.rotate(z=2.355)

#vtape= PassiveObject("props/objects", "BlackVideotape")
#vtape.setgraspable()
#milk.properties(Label = "My milk")
#vtape.translate(0.0, 0.8, 0.8)
#vtape.rotate(z= -1.57)

#milk= PassiveObject("props/kitchen_objects", "Milk")
#milk.setgraspable()
#milk.properties(Label = "My milk")
#milk.translate(0.0, 0.8, 0.8)
#milk.rotate(z= -1.57)

#cornflakes = PassiveObject("props/kitchen_objects", "Cornflakes")
#cornflakes.properties(Object = True, Label = "My cornflakes", Graspable = True)
#cornflakes.setgraspable()
#cornflakes.translate(0.23, 0.0, 0.83)
#cornflakes.rotate(z= -1.57)



arm = KukaLWR()
robot.append(arm)
arm.translate(z=0.7)
arm.rotate(z= 1.57)
arm.add_stream('socket')
arm.add_service('socket')
arm.add_interface('socket')
arm_pose = Pose()
arm.append(arm_pose)
arm_pose.add_stream('socket')
arm_pose.add_service('socket')
arm_pose.add_interface('socket')
arm_pose.translate(z=1.18)



#armpose = ArmaturePose()
#arm.append(armpose)
#armpose.add_service('socket')
#armpose.add_stream('socket')
#armpose.add_interface('socket')


gripper = Gripper()
#gripper = Gripper('gripper')
arm.append(gripper)
#gripper.translate(x=0.38, y=0.69, z=0.37)
gripper.translate(z=1.18)
#gripper.properties(Angle = 0.0, Distance=0.0)
gripper.add_service('socket')
gripper.add_stream('socket')
gripper.add_interface('socket')


human = Human()
pose = Pose()
#humanposture = HumanPosture()
human.append(pose)
#humanposture.add_stream('socket')
#humanposture.add_service('socket')
#humanposture.add_interface('socket')
pose.add_stream('socket')
pose.add_service('socket')
pose.add_interface('socket')
#humanmotion = Waypoint()
#humanmotion.properties(ControlType="Position")
#human.append(humanmotion)
#humanmotion.add_stream('socket')
#humanmotion.add_service('socket')
#humanmotion.add_interface('socket')
human.disable_keyboard_control()
human.add_stream('socket')
human.add_service('socket')
human.add_interface('socket')

human.translate(x=1.1, y=0.1, z=0.0)
human.rotate(z= 2.355)


#human.armature.add_stream('pocolibs')

env = Environment('indoors-1/indoor-1')
env.set_camera_location([5, -5, 6])
env.set_camera_rotation([1.0470, 0, 0.7854])
