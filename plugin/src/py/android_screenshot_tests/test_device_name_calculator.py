# Copyright (c) Facebook, Inc. and its affiliates.
import subprocess
import sys
import unittest

from .device_name_calculator import DeviceNameCalculator

if sys.version_info >= (3,):
    from unittest.mock import *
else:
    from mock import *


class TestDeviceNameCalculator(unittest.TestCase):

    def test_API_19_GP_XXHDPI_1080x1920_arm64_v8a_esES(self):
        def mock_data(parameters):
            if 'ro.build.version.sdk' in parameters:
                return '19'
            elif 'com.google.android.gms' in parameters:
                return 'package:/data/app/com.google.android.gms-pHwJaHhvXiRvuTo2Qxdbww==/base.apk'
            elif 'window' in parameters:
                return 'init=1080x1920 420dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731'
            elif 'ro.product.cpu.abi' in parameters:
                return 'arm64-v8a'
            elif 'persist.sys.locale' in parameters:
                return 'es-ES'
            return None

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator.name()

        assert result == "API_19_GP_XXHDPI_1080x1920_arm64-v8a_es-ES"

    def test_API_23_NO_GP_XXHDPI_1080x1920_arm64_v8a_esES(self):
        def mock_data(parameters):
            if 'ro.build.version.sdk' in parameters:
                return '23'
            elif 'com.google.android.gms' in parameters:
                return None
            elif 'window' in parameters:
                return 'init=1080x1920 420dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731'
            elif 'ro.product.cpu.abi' in parameters:
                return 'arm64-v8a'
            elif 'persist.sys.locale' in parameters:
                return 'es-ES'
            return None

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator.name()

        assert result == "API_23_NO_GP_XXHDPI_1080x1920_arm64-v8a_es-ES"

    def test_API_25_NO_GP_XXHDPI_1080x1920_x86_esES(self):
        def mock_data(parameters):
            if 'ro.build.version.sdk' in parameters:
                return '25'
            elif 'com.google.android.gms' in parameters:
                return None
            elif 'window' in parameters:
                return 'init=1080x1920 420dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731'
            elif 'ro.product.cpu.abi' in parameters:
                return 'x86'
            elif 'persist.sys.locale' in parameters:
                return None
            elif 'ro.product.locale' in parameters:
                return 'es-ES'
            return None

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator.name()

        assert result == "API_25_NO_GP_XXHDPI_1080x1920_x86_es-ES"

    def test_density_10_to_LDPI(self):
        def mock_data(parameters):
            return '''
            WINDOW MANAGER DISPLAY CONTENTS (dumpsys window displays)
              Display: mDisplayId=0
                init=1080x1920 10dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731
                deferred=false mLayoutNeeded=false mTouchExcludeRegion=SkRegion((0,0,1080,1920))
            '''

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator._screen_density_text()

        assert result == "LDPI"

    def test_density_140_to_MDPI(self):
        def mock_data(parameters):
            return '''
            WINDOW MANAGER DISPLAY CONTENTS (dumpsys window displays)
              Display: mDisplayId=0
                init=1080x1920 140dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731
                deferred=false mLayoutNeeded=false mTouchExcludeRegion=SkRegion((0,0,1080,1920))
            '''

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator._screen_density_text()

        assert result == "MDPI"

    def test_density_200_to_HDPI(self):
        def mock_data(parameters):
            return '''
            WINDOW MANAGER DISPLAY CONTENTS (dumpsys window displays)
              Display: mDisplayId=0
                init=1080x1920 200dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731
                deferred=false mLayoutNeeded=false mTouchExcludeRegion=SkRegion((0,0,1080,1920))
            '''

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator._screen_density_text()

        assert result == "HDPI"

    def test_density_250_to_XHDPI(self):
        def mock_data(parameters):
            return '''
            WINDOW MANAGER DISPLAY CONTENTS (dumpsys window displays)
              Display: mDisplayId=0
                init=1080x1920 250dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731
                deferred=false mLayoutNeeded=false mTouchExcludeRegion=SkRegion((0,0,1080,1920))
            '''

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator._screen_density_text()

        assert result == "XHDPI"

    def test_density_340_to_XXHDPI(self):
        def mock_data(parameters):
            return '''
            WINDOW MANAGER DISPLAY CONTENTS (dumpsys window displays)
              Display: mDisplayId=0
                init=1080x1920 340dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731
                deferred=false mLayoutNeeded=false mTouchExcludeRegion=SkRegion((0,0,1080,1920))
            '''

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator._screen_density_text()

        assert result == "XXHDPI"

    def test_density_500_to_XXXHDPI(self):
        def mock_data(parameters):
            return '''
            WINDOW MANAGER DISPLAY CONTENTS (dumpsys window displays)
              Display: mDisplayId=0
                init=1080x1920 500dpi cur=1080x1920 app=1080x1794 rng=1080x1017-1794x1731
                deferred=false mLayoutNeeded=false mTouchExcludeRegion=SkRegion((0,0,1080,1920))
            '''

        adb_executor = MagicMock()
        adb_executor.execute.side_effect = mock_data

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator._screen_density_text()

        assert result == "XXXHDPI"

    def test_absent_gms_gracefully_handled(self):
        adb_executor = MagicMock()
        adb_executor.execute.side_effect = subprocess.CalledProcessError(
            returncode=1,
            cmd=["irrelevant"]
        )

        device_calculator = DeviceNameCalculator(adb_executor)

        result = device_calculator._has_play_services()

        assert not result
