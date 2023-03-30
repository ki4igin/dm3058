import pyvisa as visa
import datetime
from time import sleep


def main():
    rm = visa.ResourceManager()
    devices_id = rm.list_resources()

    for string in devices_id:
        if "DM3" in string:
            dmm_resources = string
            print(f"DM3058 address: {dmm_resources}")
            dmm = rm.open_resource(dmm_resources)
            break
    else:
        print("DM3058 not found, list found devices:")
        print("\n".join(devices_id))
        dmm = TestDM()

    print('Instrument ID (IDN:) = ', dmm.query('*IDN?'))
    for x in range(0, 172800):
        rawStr = dmm.query(":MEASure:VOLTage:DC?")
        iStr = rawStr
        rawStr = rawStr.replace("\n", "")
        iStr = iStr.replace("\n", "")
        iStr = iStr.replace("#9000000015", "")

        iFlt = float(iStr)
        t = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-5]
        print(f"{t} | {iFlt:15} | {rawStr.rjust(15)}")
        sleep(.5)


class TestDM:
    def query(self, command: str) -> str:
        match command:
            case "*IDN?":
                return "TestDM"
            case ":MEASure:VOLTage:DC?":
                return "0"
            case _:
                return "?"


if __name__ == "__main__":
    main()
