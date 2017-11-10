import wpilib
from wpilib import SmartDashboard
import gearbox

from config import Config
from robotpy_ext.common_drivers import navx

class Drive:
    class __DriveStateEnum:
        THROTTLE = 0
        RPM = 1
        PATH_FOLLOWING = 2

    def setup(self):
        self.left_gearbox = gearbox.Gearbox(Config.LEFT_GEARBOX, Config.LEFT_GEARBOX_PID, reversed=True)
        self.right_gearbox = gearbox.Gearbox(Config.RIGHT_GEARBOX, Config.RIGHT_GEARBOX_PID)

        self.navx = navx.AHRS.create_spi()

        self.left_value = 0
        self.right_value = 0

        self.current_state = self.__DriveStateEnum.THROTTLE

    def set_left_right(self, drive_data):
        self.left_value = drive_data[0]
        self.right_value = drive_data[1]

        self.current_state = self.__DriveStateEnum.THROTTLE

    def set_left_rpm(self, rpm):
        self.left_value = rpm

        self.current_state = self.__DriveStateEnum.RPM

    def set_right_rpm(self, rpm):
        self.right_value = rpm

        self.current_state = self.__DriveStateEnum.RPM

    def reset(self):
        #self.left_gearbox.reset()
        #self.right_gearbox.reset()
        pass

    def execute(self):
        if self.current_state is self.__DriveStateEnum.THROTTLE:
            self.left_gearbox.set_throttle(self.left_value)
            self.right_gearbox.set_throttle(self.right_value)
        elif self.current_state is self.__DriveStateEnum.RPM:
            self.left_gearbox.set_rpm(self.left_value)
            self.right_gearbox.set_rpm(self.right_value)

        SmartDashboard.putNumber('Left Value', self.left_value)
        SmartDashboard.putNumber('Right Value', self.right_value)
        
        SmartDashboard.putNumber('Left Set', self.left_gearbox.master_talon.getSetpoint())
        SmartDashboard.putNumber('Right Set', self.right_gearbox.master_talon.getSetpoint())

        SmartDashboard.putNumber('Left Encoder', self.left_gearbox.master_talon.getEncVelocity())
        SmartDashboard.putNumber('Right Encoder', self.right_gearbox.master_talon.getEncVelocity())

        SmartDashboard.putNumber('Right', self.right_gearbox.master_talon.getSpeed())

        SmartDashboard.putString('Current Drive Mode', 'Throttle' if self.current_state is self.__DriveStateEnum.THROTTLE else 'RPM')

    