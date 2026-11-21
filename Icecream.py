import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
from AboutWindow import AboutWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.about_window = AboutWindow()

        self.temperatures = []
        self.revenues = []

        self.initUI()
        self.draw_temp_graph()

    def initUI(self):
        self.setWindowTitle("Ice Cream Revenue Analysis")
        self.setGeometry(100, 100, 760, 620)

        with open("IcecreamStyle.qss", "r") as f:
            self.setStyleSheet(f.read())

        self.load_button = QPushButton("Load File", self)
        self.load_button.setGeometry(30, 20, 150, 40)
        self.load_button.clicked.connect(self.load_file)

        self.about_button = QPushButton("About", self)
        self.about_button.setGeometry(580, 20, 150, 40)
        self.about_button.clicked.connect(self.about_clicked)

        self.fig, self.ax = plt.subplots(1, 1)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.canvas.setGeometry(30, 120, 700, 470)

        self.toolbar = NavigationToolbar(self.canvas, self)
        self.toolbar.setGeometry(30, 75, 700, 40)

    def about_clicked(self):
        self.about_window.show()

    def draw_temp_graph(self):
        self.ax.clear()
        self.ax.set_title("Load Ice Cream.csv to view data")
        self.ax.set_xlabel("Temperature")
        self.ax.set_ylabel("Revenue")
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)
        self.canvas.draw()

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Ice Cream File", "", "CSV Files (*.csv)")
        if file_path != "":
            self.temperatures = []
            self.revenues = []

            with open(file_path, "r") as f:
                header = f.readline()
                for line in f:
                    line = line.strip()
                    if line != "":
                        parts = line.split(",")
                        temp = float(parts[0])
                        rev = float(parts[1])
                        self.temperatures.append(temp)
                        self.revenues.append(rev)

            self.plot_graph()

    def plot_graph(self):
        self.ax.clear()

        coefficients = np.polyfit(self.temperatures, self.revenues, 1)

        line_function = np.poly1d(coefficients)
        line_x = np.linspace(min(self.temperatures), max(self.temperatures), 100)
        line_y = line_function(line_x)

        self.ax.scatter(self.temperatures, self.revenues, label='Data', s=1, color='blue')
        self.ax.plot(line_x, line_y, color='red', label='Trend Line')
        self.ax.text(2, 800,
                     f'y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}',
                     color='red')

        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.ax.set_title('Ice Cream Revenue vs. Outside Temperature')
        self.ax.set_xlabel('Temperature')
        self.ax.set_ylabel('Revenue')
        self.ax.legend()

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()