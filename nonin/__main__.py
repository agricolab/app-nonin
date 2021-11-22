import argparse
from nonin.device import detect_nonin_devices
from nonin.device import Nonin
from nonin.outlet import Outlet


def scan():
    print("Searching for Nonin Medical Pulse Oximeters")
    try:
        for device in detect_nonin_devices():
            print(device.device)
    except ConnectionError as e:
        print(e)


def run(port=None) -> Outlet:
    """start a Nonin PPG LSL Outlet 
    
    
    Args
    ----
    port : str
        the port at which the Nonin Medical Xpod 3012 LP USB Pulse Oximeter is connected
    """

    nonin = Nonin(port=port)
    outlet = Outlet(nonin)
    outlet.start()
    return outlet


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
        scan()
    else:
        try:
            outlet = run(args.port)
        except ConnectionError as e:
            parser.print_help()
            print("\n", e)


if __name__ == "__main__":
    main()
