import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setGeometry(400,200,600,400)
        self.qIcon = QIcon("./img/notepad.png")
        self.setWindowIcon(self.qIcon)
        self.setWindowTitle("제목 없음 - windows 메모장")
        
        # 파일열기 만들기
        openFile = QAction(QIcon("./img/openfile.png"),"OPEN",self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("파일 열기")
        openFile.triggered.connect(self.showDialog)

        # 새파일 만들기
        newFile = QAction(QIcon("./img/newFile.png"),"NEW",self)
        newFile.setShortcut("Ctrl+N")
        newFile.setStatusTip("새로운 파일 만들기")
        newFile.triggered.connect(self.newFile)

        # 파일저장하기 만들기
        saveFile = QAction(QIcon("./img/saveFile.png"),"SAVE",self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip("파일 저장하기")
        saveFile.triggered.connect(self.saveDialog)

        # 종료하기 만들기
        exitFile = QAction(QIcon("./img/exit.png"),"QUIT",self)
        exitFile.setShortcut("Ctrl+x")
        exitFile.setStatusTip("종료하기")
        exitFile.triggered.connect(QCoreApplication.instance().quit)
        
        # 종료하기 만들기
        fontMenu = QAction(QIcon("./img/merong2.png"),"글꼴서식",self)
        fontMenu.setShortcut("Ctrl+f")
        fontMenu.setStatusTip("글꼴")
        fontMenu.triggered.connect(self.changeFont)
        
        # 메뉴바 생성하기
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False) # 기존 메뉴바 말고
        fileMenu = menuBar.addMenu("&File") # 새로 생성하기
        fileMenu.addAction(openFile)
        fileMenu.addAction(newFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitFile)
        
        formMenu= menuBar.addMenu("&서식")
        formMenu.addAction(fontMenu)

        self.show()

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,'open file','./')
        print("show dialog 함수 호출됨")
        print(fname)
        if fname[0]:
            f = open(fname[0],'r',encoding="utf-8")
            with f:
                data = f.read()
                self.textEdit.setText(data)
                name = fname[0].split("/")
                print(name[-1].split(".")[0])
                self.setWindowTitle(name[-1].split('.')[0]+" - Windows 메모장")

    def saveDialog(self):
        # 저장창을 띄우기
        file = QFileDialog.getSaveFileName(self,'save file','./')
        print(file)
        # print(self.textEdit.toPlainText())
        with open(file[0], "w") as file:
            file.write(self.textEdit.toPlainText())

    def newFile(self):
        txt = self.textEdit.toPlainText()
        if len(txt) != 0:
            rep = QMessageBox.question(self,"메모장","변경내용을 제목 없음에 저장하시겠습니까?",QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            if rep == QMessageBox.Yes:
                self.saveDialog()
            self.textEdit.setText(" ") # 기존에 있는 텍스트를 초기화

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my = MyApp()
    sys.exit(app.exec_())