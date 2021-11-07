from pytest import fixture


class Stream:
    streama = b"\x01\x98c\x7f\x01"
    streamb = b"\x98c\x00\xfc\x01"
    flip = True

    def return_until(self, expected=b"\x01"):
        self.flip = not self.flip
        if self.flip:
            return self.streama
        else:
            return self.streamb


@fixture(scope="function")
def mockNonin(monkeypatch):
    from nonin.device import Nonin
    from unittest.mock import Mock

    def __init__(self, *args, protocol=2, **kwargs):
        self.port = "/dev/ttyMock"
        self.manufacturer = "Nonin Medical"
        self.product = "Pulse Oximeter"
        self.serial_number = "FT502JGB"
        print("Found", self)
        if protocol is not 2:
            raise NotImplementedError("Only protocol 2 is supported")
        self.packet_count = 0
        self.frame_count = 0

    serial = Mock()
    serial.read_until = Stream().return_until
    Nonin.serial = serial
    monkeypatch.setattr(Nonin, "__init__", __init__)

    yield Nonin
