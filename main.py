# Scenario
# You are about to create a multifunction device (MFD) that can scan and print documents;
# - the system consists of a scanner and a printer;
# - your task is to create blueprints for it and deliver the implementations;
# - create an abstract class representing a scanner that enforces the following methods:
# - scan_document – returns a string indicating that the document has been scanned;
# - get_scanner_status – returns information about the scanner (max. resolution, serial number)

# Create an abstract class representing a printer that enforces the following methods:
# - print_document – returns a string indicating that the document has been printed;
# - get_printer_status – returns information about the printer (max. resolution, serial number)

# Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
# - MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
# - MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
# - MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.

# Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.

################################################################################################################################################
import abc
import random


class scanner_bp(abc.ABC):

    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class printer_bp(abc.ABC):

    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(scanner_bp, printer_bp):
    def __init__(self):
        self.SN = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789", k=12))
        self.maxRes = "600 DPI"

    def scan_document(self):
        return "File scanned"

    def get_scanner_status(self):
        return f"Max Resolution: {self.maxRes} \nSerial Number: {self.SN}"

    def print_document(self, file: str = "document.txt"):
        return f"Document {file} has been printed"

    def get_printer_status(self):
        return f"Max resolution: {self.maxRes} \nSerial Number: {self.SN}"


class MFD2(scanner_bp, printer_bp):
    def __init__(self):
        self.SN = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789", k=12))
        self.maxRes = "1800 DPI"
        self.printHistory = ""

    def scan_document(self):
        return "File scanned"

    def get_scanner_status(self):
        return f"Max Resolution: {self.maxRes} \nSerial Number: {self.SN}"

    def print_document(self, file: str = "document.txt"):
        self.printHistory += f"- Document {file} printed\n"
        return f"Document {file} has been printed"

    def get_printer_status(self):
        return f"Max resolution: {self.maxRes} \nSerial Number: {self.SN}"

    def print_operation_history(self):
        return f"Print history:\n" + self.printHistory


class MFD3(scanner_bp, printer_bp):
    def __init__(self):
        self.SN = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789", k=12))
        self.maxRes = "4800 DPI"
        self.printHistory = ""
        self.FaxN = "".join(random.choices("123456789", k=9))

    def scan_document(self):
        return "File scanned"

    def get_scanner_status(self):
        return f"Max Resolution: {self.maxRes} \nSerial Number: {self.SN}"

    def print_document(self, file: str = "document.txt"):
        self.printHistory += f"- Document {file} printed\n"
        return f"Document {file} has been printed"

    def print_operation_history(self):
        return f"Print history:\n" + self.printHistory

    def get_printer_status(self):
        return f"Max resolution: {self.maxRes} \nSerial Number: {self.SN}"

    def sendFax(self, faxN):
        return f"Fax sended to {faxN}"

    def getFax(self):
        return "Fax received"


dis1 = MFD1()

print(dis1.scan_document())
print(dis1.get_scanner_status())

print(dis1.print_document("file1.txt"))
print(dis1.print_document("file3.txt"))
print(dis1.print_document("file7.txt"))
print(dis1.get_printer_status())

print(f"Dispositive 1 Serial Number: {dis1.SN}")

print("---------------------------------------------------------------------")

dis2 = MFD2()

print(dis2.scan_document())
print(dis2.get_scanner_status())

print(dis2.print_document("file1.txt"))
print(dis2.print_document("file3.txt"))
print(dis2.print_document("file7.txt"))
print(dis2.print_operation_history())
print(dis2.get_printer_status())

print(f"Dispositive 2 Serial Number: {dis2.SN}")

print("---------------------------------------------------------------------")

dis3 = MFD3()

print(dis3.scan_document())
print(dis3.get_scanner_status())

print(dis3.print_document("file1.txt"))
print(dis3.print_document("file3.txt"))
print(dis3.print_document("file7.txt"))
print(dis3.print_operation_history())
print(dis3.get_printer_status())

print(dis3.sendFax("9854515"))
print(dis3.getFax())
print(f"Dispositive 3 Fax Number: {dis3.FaxN}")

print(f"Dispositive 3 Serial Number: {dis3.SN}")
