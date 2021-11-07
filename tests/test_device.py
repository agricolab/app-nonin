def test__read_frame(mockNonin):
    nonin = mockNonin()
    frame = nonin.read_frame()
    assert frame == b"\x98c\x00\xfc\x01"
    frame = nonin.read_frame()
    assert frame == b"\x01\x98c\x7f\x01"


def test_read(mockNonin):
    nonin = mockNonin()
    state = {
        "PPG": 99,
        "Frame Sync": 0,
        "Perfusion Amplitude": 0,
        "Sensor Alarm": 1,
        "Out Of Track": 1,
        "Artifact - short term": 0,
        "Sensor disconnect": 0,
    }
    assert nonin.read() == state
