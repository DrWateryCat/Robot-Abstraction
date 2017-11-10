from robotpy_ext.autonomous import *
from components import drive

class RPM_TEST(StatefulAutonomous):
    MODE_NAME = "60 rpm test"
    drive_system = drive.Drive

    def initialize(self):
        #self.drive_system.reset()
        pass

    @state(first=True)
    def go(self, initial_call):
        if initial_call:
            self.drive_system.reset()

        self.drive_system.set_left_rpm(60)
        self.drive_system.set_right_rpm(60)