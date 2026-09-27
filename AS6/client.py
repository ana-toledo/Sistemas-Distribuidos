import sys, Ice
import Demo
 
communicator = Ice.initialize(sys.argv)

base = communicator.stringToProxy("SimplePrinter:tcp -h 34.203.80.210 -p 5678")
printer = Demo.PrinterPrx.checkedCast(base)
if not printer:
    raise RuntimeError("Invalid proxy")

print(printer.printString("Hello World!"))
print(printer.reverse("Hello World!"))
print(printer.capitalize("hello world!"))

communicator.destroy()

