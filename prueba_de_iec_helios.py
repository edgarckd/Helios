from iec62056_21.client import Iec6205621Client

client = Iec6205621Client.with_serial_transport(port='/dev/ttyUSB0')
client.connect()
print(client.standard_readout())
