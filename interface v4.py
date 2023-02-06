import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("MyApp")

layout = QVBoxLayout()
window.setLayout(layout)

simulation_time_button = QPushButton("Calculate Simulation Time")
simulation_time_input = QLineEdit()
simulation_time_input.setPlaceholderText("Enter path to simulation time file")
layout.addWidget(simulation_time_input)
layout.addWidget(simulation_time_button)

def calculate_simulation_time():
    try:
        path = simulation_time_input.text()
        times = all_times(path)
        total_time = 0
        for time in times.values():
            total_time += time.estimate_time_h
        print("Simulation time:", total_time)
    except:
        print("An error occurred. Please check the path and try again.")

simulation_time_button.clicked.connect(calculate_simulation_time)

window.show()
sys.exit(app.exec_())
