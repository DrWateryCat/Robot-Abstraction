import magicbot
import wpilib

from components import drive

class Robot(magicbot.MagicRobot):
    drive_system = drive.Drive
    def createObjects(self):
        self.left_joystick = wpilib.Joystick(0)
        self.right_joystick = wpilib.Joystick(1)

    def teleopPeriodic(self):
        data = (self.left_joystick.getRawAxis(1), self.right_joystick.getRawAxis(1))

        self.drive_system.set_left_right(data)

if __name__ == '__main__':
    wpilib.run(Robot)