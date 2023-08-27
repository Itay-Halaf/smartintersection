import sys
import paho.mqtt.client as mqtt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import requests
import json



APILINK = "localhost"
PORTNUM = "8002"
url = f"http://{APILINK}:{PORTNUM}/crossroads/create"

class CrossroadStateModifier(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.name=''
        self.light='Red'
        self.longitude= None
        self.latitude= None

    def initUI(self):
        self.setWindowTitle('Set Crossroad')
        self.setGeometry(1800, 900, 300, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        
        self.name_bar = QLineEdit(self)
        self.name_bar.setPlaceholderText("Crossroad Name...")
        layout.addWidget(self.name_bar)

        self.latitude_bar = QLineEdit(self)
        self.latitude_bar.setPlaceholderText("Latitude")
        layout.addWidget(self.latitude_bar)
        
        self.longitude_bar = QLineEdit(self)
        self.longitude_bar.setPlaceholderText("Longitude")
        layout.addWidget(self.longitude_bar)
        
        self.light_bar = QLineEdit(self)
        self.light_bar.setPlaceholderText("Crossroad Light")
        layout.addWidget(self.light_bar)

        self.set_crossroad_button = QPushButton('Set', self)
        self.set_crossroad_button.clicked.connect(self.create)
        layout.addWidget(self.set_crossroad_button)
        
        central_widget.setLayout(layout)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'dragPos'):
            newPos = self.mapToGlobal(event.pos())
            diff = newPos - self.dragPos
            self.move(self.pos() + diff)
            self.dragPos = newPos

    def create(self):
        dict_body = {'name': self.name_bar.text(),'latitude':float(self.latitude_bar.text()),'longitude':float(self.longitude_bar.text()),'light':self.light_bar.text()}
        print(json.dumps(dict_body))
        response = requests.post(url=url,json=dict_body, allow_redirects=False)
        try:
            response.raise_for_status()
        except Exception as e:
            print(f"Error occurred: {e}")
            return




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CrossroadStateModifier()
    window.show()
    sys.exit(app.exec_())
# formLayot=QFormLayout()
# formLayot.addRow("Host",self.eHostInput )
# formLayot.addRow("Port",self.ePort )
# formLayot.addRow("Client ID", self.eClientID)



