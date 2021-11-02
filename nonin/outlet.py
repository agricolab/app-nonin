from pylsl import StreamOutlet, local_clock, StreamInfo
from socket import gethostname
import threading


def create_stream_outlet():
    info = StreamInfo(
        name="Nonin 3012 LP USB",
        type="PPG",
        channel_count=1,
        nominal_srate=75,
        channel_format="float32",
        source_id="Nonin3012LPUSB_" + str(gethostname()),
    )

    names = ["PPG"]
    units = ["au"]
    types = ["PPG"]

    channels = info.desc().append_child("channels")
    for c, u, t in zip(names, units, types):
        channels.append_child("channel").append_child_value(
            "label", c
        ).append_child_value("unit", u).append_child_value("type", t)
    stream = StreamOutlet(info, chunk_size=0, max_buffered=1)
    print("Creating", info.as_xml())
    return stream


class Outlet(threading.Thread):
    def __init__(self, nonin):
        threading.Thread.__init__(self)
        self.nonin = nonin

    def run(self):
        self.is_running = True
        nonin = self.nonin
        stream = create_stream_outlet()

        t0 = None

        def print_log(t0, data, dt=[], cnt=[0]):
            t1 = local_clock()
            if t0 is not None:
                cnt[0] += 1
                dt.append(t1 - t0)
                if len(dt) > 100:
                    dt = dt[-100:]
                Fs = len(dt) / sum(dt)
                ppg = data["PPG"]
                print(
                    f"#{int(cnt[0]):5} with {ppg:3.0f} at {t1:4.2f} approx Fs = {Fs:4.2f}"
                )
            return t1

        while self.is_running:  # publish
            data = nonin.read()
            t0 = print_log(t0, data)
            stream.push_sample([data["PPG"]])


def main():
    from nonin.device import Nonin

    nonin = Nonin("/dev/ttyUSB0")
    outlet = Outlet(nonin)
    outlet.start()


if __name__ == "__main__":
    main()
