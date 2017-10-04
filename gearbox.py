import wpilib
import ctre
import math

class Gearbox:
    WHEEL_DIAMETER = 6
    WHEEL_CORRECTION = 0

    def __init__(self, motor_controllers):
        self.throttle = 0

        self.master_talon = ctre.CANTalon(motor_controllers[0])
        self.slave_talons = []
        for i in motor_controllers[1:]:
            slave = ctre.CANTalon(i)
            slave.changeControlMode(ctre.CANTalon.ControlMode.Follower)
            slave.set(self.master_talon.getDeviceID())

            self.slave_talons.append(slave)

    def revolutions_to_inches(self, revs):
        return revs * (self.WHEEL_DIAMETER * math.pi) #+ self.WHEEL_CORRECTION

    def inches_to_revolutions(self, inches):
        return inches / (self.WHEEL_DIAMETER * math.pi) #- self.WHEEL_CORRECTION
    
    def rpm_to_inches_per_second(self, rpm):
        return self.revolutions_to_inches(rpm) / 60

    def inches_per_second_to_rpm(self, ips):
        return self.inches_to_revolutions(ips) * 6

    #Talons want velocity data in position change / 10ms
    def rpm_to_native(self, rpm):
        return rpm / 6000

    def set_throttle(self, val):
        self.throttle = val

        self.master_talon.changeControlMode(ctre.CANTalon.ControlMode.PercentVbus)
        self.master_talon.set(val)

    def set_rpm(self, rpm):
        self.master_talon.changeControlMode(ctre.CANTalon.ControlMode.Speed)
        self.master_talon.set(self.rpm_to_native(rpm))

    def set_inches_per_second(self, ips):
        self.set_rpm(self.inches_per_second_to_rpm(ips))