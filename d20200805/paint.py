import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(400,100,1000,800)

        # 전체 form 
        formbox = QHBoxLayout()  
        self.setLayout(formbox)
        
        # 좌측 레이아웃
        leftbox = QVBoxLayout()
        rightbox = QVBoxLayout()
        
        # 좌측 #그룹박스Groupbox
        gb = QGroupBox("타입")
        leftbox.addWidget(gb)

        box1 = QVBoxLayout()
        gb.setLayout(box1)

        box1.addWidget(QRadioButton("직선",self))
        box1.addWidget(QRadioButton("곡선",self))
        box1.addWidget(QRadioButton("사각형",self))
        box1.addWidget(QRadioButton("타원",self))

        formbox.addLayout(leftbox)
        formbox.addLayout(rightbox)

        # 그룹박스2
        gb2 = QGroupBox("Pen setting")
        leftbox.addWidget(gb2)

        grid = QGridLayout()
        gb2.setLayout(grid)

        label = QLabel("선굵기")
        grid.addWidget(label,0,0)

        combo = QComboBox()
        grid.addWidget(combo,0,1)

        for i in range(1,21):
            combo.addItem(str(i))

        label2 = QLabel("선색상")
        grid.addWidget(label2,1,0)

        self.pencolor = QColor(0,0,0)
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet("background-color: rgb(0,0,0)")

        grid.addWidget(self.penbtn,1,1)

        # 그룹박스 3
        # 붓 설정
        gb3 = QGroupBox("붓설정")
        leftbox.addWidget(gb3)

        hbox=QHBoxLayout()
        gb3.setLayout(hbox)

        label3 = QLabel("붓색상")
        hbox.addWidget(label3)

        self.brushcolor = QColor(255,255,255)
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet('background-color:rgb(255,255,255)')
        hbox.addWidget(self.brushbtn)

        # 우측 레이아웃 박스에 그래픽 뷰 추가
        self.view = CGView(self)
        rightbox.addWidget(self.view)


        self.show()


# QGraphics 는 시각적 객체의 복잡한 장면을 쉽게 처리할 수 있는 
# 프레임 워크로 구성하는데 사용할 수 있다.

# QGraphicsView, QGraphicsScene, QGraphicsItem

class CGView(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.items = []
        self.start = QPointF()
        self.end = QPointF()


if __name__=="__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())
