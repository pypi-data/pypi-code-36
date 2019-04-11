# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#This file is a modified version of Tony DiCola's work adapted to the Kervi i2c and sensors api. 


from __future__ import division
import logging
import time
from kervi.hal import I2CSensorDeviceDriver

#BMP085 sensor type
BMP085_TEMPERATURE_SENSOR = 1
BMP085_PRESSURE_SENSOR = 2
BMP085_ALTITUDE_SENSOR = 3

# BMP085 default address.
BMP085_I2CADDR           = 0x77

# Operating Modes
BMP085_ULTRALOWPOWER     = 0
BMP085_STANDARD          = 1
BMP085_HIGHRES           = 2
BMP085_ULTRAHIGHRES      = 3

#private constants
# BMP085 Registers
BMP085_CAL_AC1           = 0xAA  # R   Calibration data (16 bits)
BMP085_CAL_AC2           = 0xAC  # R   Calibration data (16 bits)
BMP085_CAL_AC3           = 0xAE  # R   Calibration data (16 bits)
BMP085_CAL_AC4           = 0xB0  # R   Calibration data (16 bits)
BMP085_CAL_AC5           = 0xB2  # R   Calibration data (16 bits)
BMP085_CAL_AC6           = 0xB4  # R   Calibration data (16 bits)
BMP085_CAL_B1            = 0xB6  # R   Calibration data (16 bits)
BMP085_CAL_B2            = 0xB8  # R   Calibration data (16 bits)
BMP085_CAL_MB            = 0xBA  # R   Calibration data (16 bits)
BMP085_CAL_MC            = 0xBC  # R   Calibration data (16 bits)
BMP085_CAL_MD            = 0xBE  # R   Calibration data (16 bits)
BMP085_CONTROL           = 0xF4
BMP085_TEMPDATA          = 0xF6
BMP085_PRESSUREDATA      = 0xF6

# Commands
BMP085_READTEMPCMD       = 0x2E
BMP085_READPRESSURECMD   = 0x34

class BMP085DeviceDriver(I2CSensorDeviceDriver):
    def __init__(self, sensor_type=BMP085_TEMPERATURE_SENSOR, mode=BMP085_STANDARD, address=BMP085_I2CADDR, bus=0):
        I2CSensorDeviceDriver.__init__(self, address, bus)
        # Check that mode is valid.
        if mode not in [BMP085_ULTRALOWPOWER, BMP085_STANDARD, BMP085_HIGHRES, BMP085_ULTRAHIGHRES]:
            raise ValueError('Unexpected mode value {0}.  Set mode to one of BMP085_ULTRALOWPOWER, BMP085_STANDARD, BMP085_HIGHRES, or BMP085_ULTRAHIGHRES'.format(mode))
        self._mode = mode
        self._sensor_type = sensor_type
        self._load_calibration()

    def _load_calibration(self):
        self.cal_AC1 = self.i2c.read_S16BE(BMP085_CAL_AC1)   # INT16
        self.cal_AC2 = self.i2c.read_S16BE(BMP085_CAL_AC2)   # INT16
        self.cal_AC3 = self.i2c.read_S16BE(BMP085_CAL_AC3)   # INT16
        self.cal_AC4 = self.i2c.read_U16BE(BMP085_CAL_AC4)   # UINT16
        self.cal_AC5 = self.i2c.read_U16BE(BMP085_CAL_AC5)   # UINT16
        self.cal_AC6 = self.i2c.read_U16BE(BMP085_CAL_AC6)   # UINT16
        self.cal_B1 = self.i2c.read_S16BE(BMP085_CAL_B1)     # INT16
        self.cal_B2 = self.i2c.read_S16BE(BMP085_CAL_B2)     # INT16
        self.cal_MB = self.i2c.read_S16BE(BMP085_CAL_MB)     # INT16
        self.cal_MC = self.i2c.read_S16BE(BMP085_CAL_MC)     # INT16
        self.cal_MD = self.i2c.read_S16BE(BMP085_CAL_MD)     # INT16
        

    def _load_datasheet_calibration(self):
        # Set calibration from values in the datasheet example.  Useful for debugging the
        # temp and pressure calculation accuracy.
        self.cal_AC1 = 408
        self.cal_AC2 = -72
        self.cal_AC3 = -14383
        self.cal_AC4 = 32741
        self.cal_AC5 = 32757
        self.cal_AC6 = 23153
        self.cal_B1 = 6190
        self.cal_B2 = 4
        self.cal_MB = -32767
        self.cal_MC = -8711
        self.cal_MD = 2868

    def read_raw_temp(self):
        """Reads the raw (uncompensated) temperature from the sensor."""
        self.i2c.write8(BMP085_CONTROL, BMP085_READTEMPCMD)
        time.sleep(0.005)  # Wait 5ms
        raw = self.i2c.read_U16BE(BMP085_TEMPDATA)
        self.logger.debug('Raw temp 0x{0:X} ({1})', raw & 0xFFFF, raw)
        return raw

    def read_raw_pressure(self):
        """Reads the raw (uncompensated) pressure level from the sensor."""
        self.i2c.write8(BMP085_CONTROL, BMP085_READPRESSURECMD + (self._mode << 6))
        if self._mode == BMP085_ULTRALOWPOWER:
            time.sleep(0.005)
        elif self._mode == BMP085_HIGHRES:
            time.sleep(0.014)
        elif self._mode == BMP085_ULTRAHIGHRES:
            time.sleep(0.026)
        else:
            time.sleep(0.008)
        msb = self.i2c.read_U8(BMP085_PRESSUREDATA)
        lsb = self.i2c.read_U8(BMP085_PRESSUREDATA+1)
        xlsb = self.i2c.read_U8(BMP085_PRESSUREDATA+2)
        raw = ((msb << 16) + (lsb << 8) + xlsb) >> (8 - self._mode)
        self.logger.debug('Raw pressure 0x{0:04X} ({1})', raw & 0xFFFF, raw)
        return raw

    def read_temperature(self):
        """Gets the compensated temperature in degrees celsius."""
        UT = self.read_raw_temp()
        # Datasheet value for debugging:
        #UT = 27898
        # Calculations below are taken straight from section 3.5 of the datasheet.
        X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
        X2 = (self.cal_MC << 11) // (X1 + self.cal_MD)
        B5 = X1 + X2
        temp = ((B5 + 8) >> 4) / 10.0
        self.logger.debug('Calibrated temperature {0} C', temp)
        return temp

    def read_pressure(self):
        """Gets the compensated pressure in Pascals."""
        UT = self.read_raw_temp()
        UP = self.read_raw_pressure()
        # Datasheet values for debugging:
        #UT = 27898
        #UP = 23843
        # Calculations below are taken straight from section 3.5 of the datasheet.
        # Calculate true temperature coefficient B5.
        X1 = ((UT - self.cal_AC6) * self.cal_AC5) >> 15
        X2 = (self.cal_MC << 11) // (X1 + self.cal_MD)
        B5 = X1 + X2
        self.logger.debug('B5 = {0}', B5)
        # Pressure Calculations
        B6 = B5 - 4000
        self.logger.debug('B6 = {0}', B6)
        X1 = (self.cal_B2 * (B6 * B6) >> 12) >> 11
        X2 = (self.cal_AC2 * B6) >> 11
        X3 = X1 + X2
        B3 = (((self.cal_AC1 * 4 + X3) << self._mode) + 2) // 4
        self.logger.debug('B3 = {0}', B3)
        X1 = (self.cal_AC3 * B6) >> 13
        X2 = (self.cal_B1 * ((B6 * B6) >> 12)) >> 16
        X3 = ((X1 + X2) + 2) >> 2
        B4 = (self.cal_AC4 * (X3 + 32768)) >> 15
        self.logger.debug('B4 = {0}', B4)
        B7 = (UP - B3) * (50000 >> self._mode)
        self.logger.debug('B7 = {0}', B7)
        if B7 < 0x80000000:
            p = (B7 * 2) // B4
        else:
            p = (B7 // B4) * 2
        X1 = (p >> 8) * (p >> 8)
        X1 = (X1 * 3038) >> 16
        X2 = (-7357 * p) >> 16
        p = p + ((X1 + X2 + 3791) >> 4)
        self.logger.debug('Pressure {0} Pa', p)
        return p/100

    def read_altitude(self, sealevel_pa=101325.0):
        """Calculates the altitude in meters."""
        # Calculation taken straight from section 3.6 of the datasheet.
        pressure = float(self.read_pressure())
        altitude = 44330.0 * (1.0 - pow(pressure / sealevel_pa, (1.0/5.255)))
        self.logger.debug('Altitude {0} m', altitude)
        return altitude

    def read_sealevel_pressure(self, altitude_m=0.0):
        """Calculates the pressure at sealevel when given a known altitude in
        meters. Returns a value in Pascals."""
        pressure = float(self.read_pressure())
        p0 = pressure / pow(1.0 - altitude_m/44330.0, 5.255)
        self.logger.debug('Sealevel pressure {0} Pa', p0)
        return p0

    def read_value(self):
        if self._sensor_type == BMP085_TEMPERATURE_SENSOR:
            return self.read_temperature()
        elif self._sensor_type == BMP085_PRESSURE_SENSOR:
            return self.read_pressure()
        elif self._sensor_type == BMP085_ALTITUDE_SENSOR:
            return self.read_altitude()

    @property
    def type(self):
        if self._sensor_type == BMP085_TEMPERATURE_SENSOR:
            return "temperature"
        elif self._sensor_type == BMP085_PRESSURE_SENSOR:
            return "pressure"
        elif self._sensor_type == BMP085_ALTITUDE_SENSOR:
            return "altitude"

    @property
    def unit(self):
        if self._sensor_type == BMP085_TEMPERATURE_SENSOR:
            return "c"
        elif self._sensor_type == BMP085_PRESSURE_SENSOR:
            return "hPa"
        elif self._sensor_type == BMP085_ALTITUDE_SENSOR:
            return "m"

    @property
    def max(self):
        if self._sensor_type == BMP085_TEMPERATURE_SENSOR:
            return 85
        elif self._sensor_type == BMP085_PRESSURE_SENSOR:
            return 1100
        elif self._sensor_type == BMP085_ALTITUDE_SENSOR:
            return 9000


    @property
    def min(self):
        if self._sensor_type == BMP085_TEMPERATURE_SENSOR:
            return -40
        elif self._sensor_type == BMP085_PRESSURE_SENSOR:
            return 300
        elif self._sensor_type == BMP085_ALTITUDE_SENSOR:
            return -500
