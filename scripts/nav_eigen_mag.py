import numpy as np
import os
import sys

sys.path.append('../build/src/nav_core/.libs/')
sys.path.append('../build/src/nav_eigen_mag/.libs/')
import libnav_core
import libnav_eigen_mag

class filter():
    def __init__(self):
        self.ekf = libnav_eigen_mag.EKF15mag()
        self.name = 'EKF15+Mag'

    def init(self, imu, gps, filterpt=None):
        nav = self.ekf.init(imu, gps)
        return nav

    def update(self, imu, gps, filterpt=None):
        nav = self.ekf.update(imu, gps)
        return nav

    def close(self):
        pass