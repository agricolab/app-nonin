import argparse
from nonin.device import detect_nonin_devices


def run(port=None):
    from nonin.device import Nonin
    from nonin.outlet import Outlet

    nonin = Nonin(port=port)
    outlet = Outlet(nonin)
    outlet.start()


def main():
    parser = argparse.ArgumentParser(
        description="Stream Nonin Medical Xpod 3012 LP USB Pulse Oximeter"
    )
    parser.add_argument(
        "--scan", action="store_true", help="report the available devices"
    )
    parser.add_argument("--port", default=None, help="which port to use")
    args = parser.parse_args()

    if args.scan:

        print("Nonin Medical Pulse Oximeter found at")
        for device in detect_nonin_devices():
            print(device.device)

    else:
        run(args.port)


if __name__ == "__main__":
    main()
