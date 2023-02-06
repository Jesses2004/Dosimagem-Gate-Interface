import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import csv
import glob
from SimpleITK import ReadImage, GetArrayFromImage
sys.path.append("C:\Usuarios\Usuario\Documents\GateInfo\gate_monitor.git")
from gate_monitor.gate_uncertainty.errors import MissingSegMhdFileError, MissingSegMhdColorTableFileError, NumberOfUncertaintyFilesError
from gate_monitor.search import find_dirs

class MyApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # Create widgets
        self.simulation_time_button = QtWidgets.QPushButton("Calculate Simulation Time")
        self.uncertainty_button = QtWidgets.QPushButton("Calculate Uncertainty")

        # Create layout and add widgets
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.simulation_time_button,0,0)
        layout.addWidget(self.uncertainty_button,1,0)
        # Set layout to the main window
        self.setLayout(layout)

        # Connect buttons to callback functions
        self.simulation_time_button.clicked.connect(self.calculate_simulation_time)
        self.uncertainty_button.clicked.connect(self.calculate_uncertainty)

        # Set main window properties
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("My App")

    def calculate_simulation_time(self):
        result = estimate_simulation_time(path)
        print("Simulation time: ", result)

    def calculate_uncertainty(self):
        result = calculate_dose_uncertainty(path)
        print("Uncertainty: ", result)

def read_mhd_file(path, verbose=False):
    """Reads a MHD file and returns its matrix representation."""
    img = ReadImage(path)
    matrix = GetArrayFromImage(img)
    if verbose:
        print("(z,y,x)=", matrix.shape)
