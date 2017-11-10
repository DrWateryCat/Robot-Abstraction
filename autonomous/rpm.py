from robotpy_ext.autonomous import *
from components import drive

class RPM(StatefulAutonomous):
    MODE_NAME = "RPM"
    drive_system = drive.Drive

    def initialize(self):
        #self.drive_system.reset()
        pass

    @timed_state(duration=3, next_state='second_stage', first=True)
    def first_stage(self, tm, state_tm, initial_call):
        self.drive_system.set_left_rpm(60)
        self.drive_system.set_right_rpm(60)

    @timed_state(duration=3, next_state='stop')
    def second_stage(self, tm, state_tm, initial_call):
        self.drive_system.set_left_rpm(120)
        self.drive_system.set_right_rpm(120)

    @state
    def stop(self, tm, state_tm, initial_call):
        self.drive_system.set_left_right((0, 0))
