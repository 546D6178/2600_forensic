from config import REGRIPPER_PATH
from src.RegRipperHelper import RegRipperHelper
import pytest

class TestRegRipperHelper:
    def test_exec_usbstor(self):
        helper = RegRipperHelper(REGRIPPER_PATH)
        with pytest.raises(RuntimeError):
            helper.exec_usbstor("invalid_filepath")

    def test_exec_mountdev(self):
        helper = RegRipperHelper(REGRIPPER_PATH)
        with pytest.raises(RuntimeError):
            helper.exec_mountdev("invalid_filepath")
    
    def test_exec_mp2(self):
        helper = RegRipperHelper(REGRIPPER_PATH)
        with pytest.raises(RuntimeError):
            helper.exec_mp2("invalid_filepath")
    
    def test_exec_shellbags(self):
        helper = RegRipperHelper(REGRIPPER_PATH)
        with pytest.raises(RuntimeError):
            helper.exec_shellbags("invalid_filepath")