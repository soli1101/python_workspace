import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.drawType = 1 # 직선, 곡선등 선택할 수 있게 하는 객체 1.직선 2.사각형
        self.initUI()
        
    def initUI(self):
        self.setGeometry(400,100,1000,800)

        # 전체 QBoxLayout으로 생성  
        formbox = QHBoxLayout()  
        self.setLayout(formbox)
        
        # leftbox를 1열, rightbox를 2열에 생성
        leftbox = QVBoxLayout()
        rightbox = QVBoxLayout()
        #--leftbox, rightbox를 상위 상자인 formbox에 담음
        formbox.addLayout(leftbox)
        formbox.addLayout(rightbox)

        #(1) 그룹박스1
        gb1 = QGroupBox("타입") # gb1이라는 그룹박스 생성 
        leftbox.addWidget(gb1)  # leftbox에 gb1 넣기
        box1 = QVBoxLayout()    # box1이라는 QVBox 생성
        gb1.setLayout(box1)     # gb1에 box1 넣기
        
        #--leftbox> gb1> box1> 안의 Radio btn 생성
        self.rbtnLine = QRadioButton("직선",self)
        self.rbtnCurve = QRadioButton("곡선",self)
        self.rbtnRect = QRadioButton("사각형",self)
        self.rbtnEllipse = QRadioButton("타원",self)

        #--RadioSetting: box1에 Radio btn 담기
        box1.addWidget(self.rbtnLine)
        box1.addWidget(self.rbtnCurve)
        box1.addWidget(self.rbtnRect)
        box1.addWidget(self.rbtnEllipse)

        #--RadioSetting: Radio btn에 Signal 주기
        self.rbtnLine.clicked.connect(self.radioBtnClicked)
        self.rbtnCurve.clicked.connect(self.radioBtnClicked)
        self.rbtnRect.clicked.connect(self.radioBtnClicked)
        self.rbtnEllipse.clicked.connect(self.radioBtnClicked)

        #--RadioSetting: Radio btn의 초기값!(줘도 되고 안줘도 됨)
        self.rbtnLine.setChecked(True)
        self.drawType = 1


        #(2) 그룹박스2
        gb2 = QGroupBox("Pen setting") 
        leftbox.addWidget(gb2)

        # label 생성
        label = QLabel("선굵기")
        label2 = QLabel("선색상")

        # combo box 생성&Item추가
        self.combo = QComboBox()
        for i in range(1,21):
            self.combo.addItem(str(i))
        
        # 선색상
        self.pencolor = QColor(0,0,0)
        self.penbtn = QPushButton()
        self.penbtn.setStyleSheet("background-color: rgb(0,0,0)")
        self.penbtn.clicked.connect(self.selectColorDialog)
        
        # 그룹박스2 > Grid에 위젯추가
        grid = QGridLayout()             # Grid 객체 생성
        grid.addWidget(label,0,0)        
        grid.addWidget(label2,1,0)
        grid.addWidget(self.combo,0,1)
        grid.addWidget(self.penbtn,1,1)
        gb2.setLayout(grid) 


        #(3) 그룹박스3
        gb3 = QGroupBox("붓설정")
        leftbox.addWidget(gb3)
        hbox=QHBoxLayout()
        gb3.setLayout(hbox)
        label3 = QLabel("붓색상")
        hbox.addWidget(label3)

        #     붓설정
        self.brushcolor = QColor(100,100,100)
        self.brushbtn = QPushButton()
        self.brushbtn.setStyleSheet('background-color:rgb(100,100,100)')
        hbox.addWidget(self.brushbtn)
        self.brushbtn.clicked.connect(self.selectColorDialog)

        #(4) 그룹박스 4
        gb4 = QGroupBox("File") # 'File' 그룹박스 생성 
        leftbox.addWidget(gb4)  # 그룹박스 왼쪽박스에 담기
        hbox4 = QHBoxLayout()    # 저장이 들어갈 hbox 생성    
        gb4.setLayout(hbox4)     # gb4를 hbox4에 담기
        saveBtn = QPushButton("저장",self) # '저장'이라는 버튼생성 
        hbox4.addWidget(saveBtn)          # hbox4에 saveBtn담기
        saveBtn.clicked.connect(self.save_img) #saveBtn 연결 Signal

        #(5) 그룹박스 5
        gb5 = QGroupBox("지우개")
        leftbox.addWidget(gb5)
        vbox5 = QVBoxLayout()
        gb5.setLayout(vbox5)
        eraseBtn = QPushButton("지우개",self)
        vbox5.addWidget(eraseBtn)
        eraseBtn.clicked.connect(self.erase)
        clearBtn = QPushButton("clear",self)
        vbox5.addWidget(clearBtn)
        clearBtn.clicked.connect(self.clear)
        
        #RightBox 그래픽 뷰 추가
        self.view = CGView(self)      #CGView를 초기화 해 
        rightbox.addWidget(self.view) #rightbox에 view 추가

        self.show()

    # MyApp내에 기능을 가진 함수 모음
    def clear(self):
        self.view.scene.clear()
    
    def erase(self):
        self.drawType = 5
        
    def save_img(self):
        img = QPixmap(self.view.grab(self.view.sceneRect().toRect()))   # toRect()사각형으로 캡쳐를 해와라
        fname = QFileDialog.getSaveFileName(self,"어따가 저장할래?","./")
        print(fname)
        if fname[0]:
            img.save(fname[0]) # save('경로')

    def selectColorDialog(self):
        color = QColorDialog.getColor()

        # 컬러가 Pen 인지 Brush 에서 온건지 sender를 통해 구분 
        who = self.sender()
        if who == self.penbtn:
            self.pencolor = color
            self.penbtn.setStyleSheet("background-color:{}".format(color.name()))
        elif who == self.brushbtn:
            self.brushcolor = color
            self.brushbtn.setStyleSheet("background-color:{}".format(color.name()))

    def radioBtnClicked(self):
        if self.rbtnLine.isChecked():
            self.drawType = 1
        elif self.rbtnCurve.isChecked():
            self.drawType = 3
        elif self.rbtnRect.isChecked():
            self.drawType = 2
        elif self.rbtnEllipse.isChecked():
            self.drawType = 4
        print("선택한 타입은:",self.drawType)

'''-------------------------------------------'''

class CGView(QGraphicsView):       # QGraphoicsView의 속성받기
    def __init__(self, parent):    
        super().__init__(parent)
        self.scene = QGraphicsScene() # QGraphics로 Scene 생성
        self.setScene(self.scene)     # setScene으로 설정 

        self.items = []            # 마우스 이동경로 저장 리스트
        self.start = QPointF()     # 마우스가 시작 start x,y좌표
        self.end = QPointF()       # 마우스가 끝난 end x,y좌표
    
    def moveEvent(self,e):
        rect = QRectF(self.rect()) 
        rect.adjust(0,0,-3,-3)     # 창크기가 변동되지 않도록 설정
        self.scene.setSceneRect(rect)

    def mousePressEvent(self,e):
        if e.button() == Qt.LeftButton:
            self.start = e.pos()    # 시작점 지정
            self.end = e.pos()      # 끝점 지정

    def mouseMoveEvent(self,e):
        self.end = e.pos()  # 마우스가 이동할 때를 end 포인트로 줌
        pen = QPen(self.parent().pencolor, self.parent().combo.currentIndex()) # 펜 생성!

        # Scene에 그려진 이전 선을 제거
        if len(self.items) > 0 :
            self.scene.removeItem(self.items[-1])
            del(self.items[-1])

        # 현재 선을 추가
            # line = QlineF(x1,y1,x2,y2)
            # self.scene.addLine(라인객체, 팬종류)
        if self.parent().drawType == 1:
            line = QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            self.items.append(self.scene.addLine(line, pen))

        elif self.parent().drawType == 2 :
            # 사각형 그리기
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start, self.end)
            self.items.append(self.scene.addRect(rect,pen,brush))

        elif self.parent().drawType ==3 :
            line = QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            self.scene.addLine(line,pen)
            # 끝점을 다시 시작점으로 
            self.start = e.pos()
        
        elif self.parent().drawType == 4 :
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start,self.end)
            self.items.append(self.scene.addEllipse(rect,pen,brush))

        elif self.parent().drawType ==5 :
            eraser = QPen(Qt.white,10)
            line = QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            self.scene.addLine(line,eraser)
            self.start = e.pos()


    def mouseReleaseEvent(self,e):
        self.end = e.pos()
        pen = QPen(self.parent().pencolor,self.parent().combo.currentIndex())

        if self.parent().drawType == 1 :
            line = QLineF(self.start.x(),self.start.y(),self.end.x(),self.end.y())
            self.scene.addLine(line,pen)

        elif self.parent().drawType == 2:
            brush = QBrush(self.parent().brushcolor)
            rect = QRectF(self.start, self.end)
            self.scene.addRect(rect,pen,brush)
            
        elif self.parent().drawType == 4 :
            brush = QBrush(self.parent().brushcolor)
            coordinate = QRectF(self.start,self.end)
            self.scene.addEllipse(coordinate,pen,brush)
    
if __name__=="__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())