import os
import sys

from script import TextPredictor

# Get the absolute path of the current script file
script_path = os.path.abspath(__file__)

# Get the root directory by going up one level from the script directory
project_root = os.path.dirname(os.path.dirname(script_path))

sys.path.insert(0, project_root)
sys.path.insert(0, os.getcwd())  # Add the current directory as well

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDoubleSpinBox, QFormLayout, QGroupBox, \
    QVBoxLayout, QSplitter, QWidget, QLabel, QFrame, QSizePolicy
from PyQt5.QtCore import Qt, QCoreApplication, QThread, pyqtSignal
from PyQt5.QtGui import QFont

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # HighDPI support

QApplication.setFont(QFont('Arial', 12))


class Thread(QThread):
    generateFinished = pyqtSignal(str)

    def __init__(self, n_arr, pred):
        super(Thread, self).__init__()
        self.__n_arr = n_arr
        self.__pred = pred

    def run(self):
        try:
            result = 'Positive' if self.__pred.predict_text(self.__n_arr) else 'Negative'
            self.generateFinished.emit(result)
        except Exception as e:
            raise Exception(e)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__min = 0
        self.__max = 1000
        model_path = 'result.pt'
        self.__pred = TextPredictor(model_path)

    def __initUi(self):
        self.setWindowTitle('PyQt Text Classification from Number')

        self.__PregnanciesSpinBox = QDoubleSpinBox()
        self.__GlucoseSpinBox = QDoubleSpinBox()
        self.__BloodPressureSpinBox = QDoubleSpinBox()
        self.__SkinThicknessSpinBox = QDoubleSpinBox()
        self.__InsulinSpinBox = QDoubleSpinBox()
        self.__BMISpinBox = QDoubleSpinBox()
        self.__DiabetesPedigreeFunctionSpinBox = QDoubleSpinBox()
        self.__AgeSpinBox = QDoubleSpinBox()

        self.__PregnanciesSpinBox.setRange(self.__min, self.__max)
        self.__GlucoseSpinBox.setRange(self.__min, self.__max)
        self.__BloodPressureSpinBox.setRange(self.__min, self.__max)
        self.__SkinThicknessSpinBox.setRange(self.__min, self.__max)
        self.__InsulinSpinBox.setRange(self.__min, self.__max)
        self.__BMISpinBox.setRange(self.__min, self.__max)
        self.__DiabetesPedigreeFunctionSpinBox.setRange(self.__min, self.__max)
        self.__AgeSpinBox.setRange(self.__min, self.__max)

        self.__PregnanciesSpinBox.valueChanged.connect(self.__valueChanged)
        self.__PregnanciesSpinBox.setValue(9.0)

        self.__GlucoseSpinBox.valueChanged.connect(self.__valueChanged)
        self.__GlucoseSpinBox.setValue(164.0)

        self.__BloodPressureSpinBox.valueChanged.connect(self.__valueChanged)
        self.__BloodPressureSpinBox.setValue(84.0)

        self.__SkinThicknessSpinBox.valueChanged.connect(self.__valueChanged)
        self.__SkinThicknessSpinBox.setValue(21.0)

        self.__InsulinSpinBox.valueChanged.connect(self.__valueChanged)
        self.__InsulinSpinBox.setValue(0.0)

        self.__BMISpinBox.valueChanged.connect(self.__valueChanged)
        self.__BMISpinBox.setValue(30.8)

        self.__DiabetesPedigreeFunctionSpinBox.valueChanged.connect(self.__valueChanged)
        self.__DiabetesPedigreeFunctionSpinBox.setValue(0.831)

        self.__AgeSpinBox.valueChanged.connect(self.__valueChanged)
        self.__AgeSpinBox.setValue(32.0)

        paramGrpBox = QGroupBox('Parameter')
        lay = QFormLayout()
        lay.addRow('Pregnancies', self.__PregnanciesSpinBox)
        lay.addRow('Glucose', self.__GlucoseSpinBox)
        lay.addRow('BloodPressure', self.__BloodPressureSpinBox)
        lay.addRow('SkinThickness', self.__SkinThicknessSpinBox)
        lay.addRow('Insulin', self.__InsulinSpinBox)
        lay.addRow('BMI', self.__BMISpinBox)
        lay.addRow('DiabetesPedigreeFunction', self.__DiabetesPedigreeFunctionSpinBox)
        lay.addRow('Age', self.__AgeSpinBox)
        paramGrpBox.setLayout(lay)

        btn = QPushButton('Run')
        btn.clicked.connect(self.__run)

        lay = QVBoxLayout()
        lay.addWidget(paramGrpBox)
        lay.addWidget(btn)

        leftWidget = QWidget()
        leftWidget.setLayout(lay)

        rightWidgetTopLbl = QLabel('Result')
        rightWidgetTopLbl.setAlignment(Qt.AlignCenter)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)

        self.__resultLbl = QLabel()
        self.__resultLbl.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.__resultLbl.setFont(QFont('Arial', 24, QFont.Bold))
        self.__resultLbl.setAlignment(Qt.AlignCenter)

        lay = QVBoxLayout()
        lay.addWidget(rightWidgetTopLbl)
        lay.addWidget(sep)
        lay.addWidget(self.__resultLbl)
        lay.setAlignment(Qt.AlignTop)

        rightWidget = QWidget()
        rightWidget.setLayout(lay)

        splitter = QSplitter()
        splitter.addWidget(leftWidget)
        splitter.addWidget(rightWidget)
        splitter.setHandleWidth(1)
        splitter.setChildrenCollapsible(False)
        splitter.setSizes([500, 500])
        splitter.setStyleSheet(
            "QSplitterHandle {background-color: lightgray;}")
        splitter.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        topLbl = QLabel('AI that diagnoses diabetes based on given values')
        topLbl.setFont(QFont('Arial', 14, QFont.Bold))
        topLbl.setAlignment(Qt.AlignCenter)

        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)

        lay = QVBoxLayout()
        lay.addWidget(topLbl)
        lay.addWidget(sep)
        lay.addWidget(splitter)
        lay.setAlignment(Qt.AlignTop)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.setCentralWidget(mainWidget)

    def __valueChanged(self, v):
        sender = self.sender()
        if sender == self.__PregnanciesSpinBox:
            print(f'PregnanciesSpinBox value has changed to {v}')
        if sender == self.__GlucoseSpinBox:
            print(f'GlucoseSpinBox value has changed to {v}')
        if sender == self.__BloodPressureSpinBox:
            print(f'BloodPressureSpinBox value has changed to {v}')
        if sender == self.__SkinThicknessSpinBox:
            print(f'SkinThicknessSpinBox value has changed to {v}')
        if sender == self.__InsulinSpinBox:
            print(f'InsulinSpinBox value has changed to {v}')
        if sender == self.__BMISpinBox:
            print(f'BMISpinBox value has changed to {v}')
        if sender == self.__DiabetesPedigreeFunctionSpinBox:
            print(f'DiabetesPedigreeFunctionSpinBox value has changed to {v}')
        if sender == self.__AgeSpinBox:
            print(f'AgeSpinBox value has changed to {v}')

    def __run(self):
        n_arr = [self.__PregnanciesSpinBox.value(),
        self.__GlucoseSpinBox.value(),
        self.__BloodPressureSpinBox.value(),
        self.__SkinThicknessSpinBox.value(),
        self.__InsulinSpinBox.value(),
        self.__BMISpinBox.value(),
        self.__DiabetesPedigreeFunctionSpinBox.value(),
        self.__AgeSpinBox.value()]

        self.__t = Thread(n_arr, self.__pred)
        self.__t.started.connect(self.__started)
        self.__t.generateFinished.connect(self.__generateFinished)
        self.__t.finished.connect(self.__finished)
        self.__t.start()

    def __started(self):
        print('started')

    def __generateFinished(self, v):
        self.__resultLbl.setText(v)

    def __finished(self):
        print('finished')


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())