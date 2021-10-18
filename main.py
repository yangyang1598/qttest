import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("qt_test.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class DialogClass(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.count=0
        self.num1=0
        self.num2 = 0
        self.num3=0
        self.n1=[]
        self.n2=[]
        self.n3=[]
        self.action = []
        self.btn_1.clicked.connect(self.run_btn_1)
        self.btn_2.clicked.connect(self.run_btn_2)
        self.btn_3.clicked.connect(self.run_btn_3)
        self.btn_clear.clicked.connect(self.run_btn_clear)
        self.btn_undo.clicked.connect(self.run_btn_undo)
        self.btn_1.setStyleSheet('QPushButton {color: blue;}')
        self.btn_2.setStyleSheet('QPushButton {color: red;}')
        self.btn_3.setStyleSheet('QPushButton {color: Green;}')


    def run_btn_1(self):
        self.action.append('Blue')
        self.n1 += [self.num1]
        self.count += 1
        self.num1+=1
        self.label.setText("Total Count: %02d" % self.count)
        self.label_2.setText("%02d"%self.num1)


    def run_btn_2(self):
        self.action.append('Red')
        self.n2 += [self.num2]
        self.count += 1
        self.num2+=1
        self.label.setText("Total Count: %02d"%self.count)
        self.label_3.setText("%02d" % self.num2)

    def run_btn_3(self):
        self.action.append('Green')
        self.n3 += [self.num3]
        self.count += 1
        self.num3+=1
        self.label.setText("Total Count: %02d"%self.count)
        self.label_4.setText("%02d" % self.num3)

    def run_btn_clear(self):
        self.label.setText("Total Count: 0")
        self.count=0
        self.action = []
        self.num1=0
        self.num2=0
        self.num3=0
        self.label_2.setText("%02d" % self.num1)
        self.label_3.setText("%02d" % self.num2)
        self.label_4.setText("%02d" % self.num3)


    def run_btn_undo(self):

        if len(self.action) != 0:
            last_action = self.action.pop()
        else:
            return

        if last_action == 'Blue':
            self.count -= 1
            if len(self.n1) != 0:
                b = self.n1.pop()
                self.label_2.setText("%02d" % b)
                self.num1 = b
            else:
                return

        if last_action == 'Red':
            self.count -= 1
            if len(self.n2) != 0:
                x = self.n2.pop()
                self.label_3.setText("%02d" % x)
                self.num2 = x
            else:
                return

        if last_action == 'Green':
            self.count -= 1
            if len(self.n3) != 0:
                a = self.n3.pop()
                self.label_4.setText("%02d" % a)
                self.num3 = a
            else:
                return
        self.label.setText("Total Count :%02d" %self.count)








if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # DialogClass의 인스턴스 생성
    myDialog = DialogClass()

    # 프로그램 화면을 보여주는 코드
    myDialog.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()