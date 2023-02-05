import serial

c = serial.Serial(port="/dev/ttyUSB0",timeout=0,baudrate=9600)
c.write("/?1!\015\012".encode(encoding="ascii"))
print(c.read().decode(encoding="ascii"))
input()
# C = "/?1!\051".encode(encoding="ascii")
# print(C)
# print(C.decode(encoding="ascii"))