
from PyQt5 import QtCore, QtWidgets, QtWidgets, QtNetwork

class Client(QtWidgets.QDialog):     #클라이언트라는 클래스 생성
    # def __init__(self, parent=None):
    #     super(Client, self).__init__(parent)

    #     self.main_text = QtWidgets.QTextEdit(self)
    #     self.main_text.setReadOnly(True)
    #     self.send_box = QtWidgets.QLineEdit(self)
    #     self.send_button = QtWidgets.QPushButton("Send", self)
        # self.browse_btn = QtWidgets.QPushButton("Browse", self)
        
        # EVENT FOR SEND BUTTON
        # self.send_button.clicked.connect(self.sendData)

        # self.server_ip = QtWidgets.QLineEdit(self)
        # self.server_ip.setPlaceholderText("IP address")
        # self.port_address = QtWidgets.QLineEdit(self)
        # self.port_address.setPlaceholderText("port")
        # self.userName = QtWidgets.QLineEdit(self)
        # self.userName.setPlaceholderText("username")

        # self.connectButton = QtWidgets.QPushButton("Connect",self)
        
        #Connect Button EVENT
        # self.connectButton.clicked.connect(self.connection)
        # self.connectButton.setDefault(True)

        self.setGeometry(400,50,500,600)
        self.main_text.setGeometry(25,50,450,400)
        self.send_box.setGeometry(25,470,450,40)
        self.send_button.setGeometry(385,520,90,30)
        self.browse_btn.setGeometry(25,520,100,30)
        self.server_ip.setGeometry(150,10,130,25)
        self.port_address.setGeometry(300,10,70,25)
        self.connectButton.setGeometry(385,10,90,25)
        self.userName.setGeometry(25,10,120,25)


        #NetworkInput
        self.socket = QtNetwork.QTcpSocket(self)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)

    def closeEvent(self, event):
        self.socket.disconnectFromHost()

    def connection(self):
        self.socket.connectToHost(self.server_ip.text(), int(self.port_address.text()))
        if self.socket.waitForConnected(1000):
            self.user = self.userName.text()
            self.send("login %s" % self.user)
            self.connectButton.setEnabled(False)
            self.send_button.setDefault(True)
            self.send_box.setFocus()
            #self.setWindowTitle("<%s>" % self.user)


    def readData(self):
        message = self.socket.readLine().data().decode("utf-8")
        self.main_text.append(message)

    def send(self, message):
        self.socket.write(message.encode("utf-8"))

    def sendData(self):
        message = "say %s" % (self.send_box.text())
        self.send(message)
        self.send_box.clear()
        self.send_box.setFocus()

    def displayError(self):
        QtWidgets.QMessageBox.information(self, "Connection", "Connection error")


if __name__ == "__main__":
      import sys
      app = QtWidgets.QApplication(sys.argv)
      client = Client()
      sys.exit(client.exec_())