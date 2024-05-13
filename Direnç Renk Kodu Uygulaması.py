from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys


class StyleOfComboBoxDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)
        colors = {
            "Siyah": QColor("black"),
            "Kahverengi": QColor("brown"),
            "Kırmızı": QColor("red"),
            "Turuncu": QColor("orange"),
            "Sarı": QColor("yellow"),
            "Yeşil": QColor("green"),
            "Mavi": QColor("blue"),
            "Mor": QColor("purple"),
            "Gri": QColor("grey"),
            "Beyaz": QColor("white"),
            "Altın": QColor("gold"),
            "Gümüş": QColor("silver")

        }
        background_color = colors.get(index.data(), Qt.GlobalColor.black)
        option.backgroundBrush = background_color 
        option.displayAlignment = Qt.AlignmentFlag.AlignCenter

class GUI_Main_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        self.LabelForBackgroundImage = QLabel(self)
        self.LabelForResistanceBase = QLabel(self) 
        self.LabelForResistanceBaseLeft = QLabel(self) 
        self.LabelForResistanceBaseRight = QLabel(self) 
        self.LabelForResistanceColorOne = QLabel(self) 
        self.LabelForResistanceColorTwo= QLabel(self) 
        self.LabelForResistanceColorThree= QLabel(self) 
        self.LabelForResistanceColorFour = QLabel(self) 
        self.LabelForResistanceColorFive = QLabel(self) 
        self.LabelForCoverOfCalculationArea = QLabel(self) 
        self.LabelForOptionForThreeBand = QLabel("3-Bant Direnç Hesaplayıcı",self) 
        self.LabelForOptionForFourBand = QLabel("4-Bant Direnç Hesaplayıcı",self) 
        self.LabelForOptionForFiveBand = QLabel("5-Bant Direnç Hesaplayıcı",self) 
        self.LabelForBandOne = QLabel("1.Bant (1.Sayı)",self) 
        self.LabelForBandTwo = QLabel("2.Bant (2.Sayı)",self) 
        self.LabelForBandThree = QLabel("3.Bant (Çarpan)",self) 
        self.LabelForBandFour = QLabel("4.Bant",self) 
        self.LabelForBandFive = QLabel("5.Bant",self) 
        self.ComboBoxForColorOne = QComboBox(self)
        self.ComboBoxForColorTwo = QComboBox(self)
        self.ComboBoxForColorThree = QComboBox(self)
        self.ComboBoxForColorFour = QComboBox(self)
        self.ComboBoxForColorFive = QComboBox(self)
        self.PushButtonForCalculation = QPushButton("Hesapla",self) 
        self.LineEditForResultedValue = QLineEdit("1kΩ ±20%",self) 

        self.LabelForBackgroundImage.setGeometry(0,0,800,800)
        self.PathToBackgroundImage = QPixmap("C:/Users/ugury/Masaüstü/Python PyQt6 Applications/Direnç Renk Kodu Uygulaması/background-image.jpg")
        self.LabelForBackgroundImage.setScaledContents(True)
        self.LabelForBackgroundImage.setPixmap(self.PathToBackgroundImage)

        self.LabelForResistanceBase.setGeometry(200,550,400,80)
        self.LabelForResistanceBase.setStyleSheet("background-color:#ffe6b3;border-radius:10px;border:1px solid black;")
        self.ShadowForResistanceBase = QGraphicsDropShadowEffect(self)
        self.ShadowForResistanceBase.setBlurRadius(40)
        self.ShadowForResistanceBase.setColor(QColor("black"))
        self.ShadowForResistanceBase.setOffset(0,0)
        self.LabelForResistanceBase.setGraphicsEffect(self.ShadowForResistanceBase)
        self.LabelForResistanceBaseLeft.setGeometry(70,585,130,10)
        self.LabelForResistanceBaseLeft.setStyleSheet("background-color:#cccccc;border-left:2px solid black;border-top:1px solid grey;border-bottom:1px solid grey;")
        self.ShadowForResistanceBaseLeft = QGraphicsDropShadowEffect(self)
        self.ShadowForResistanceBaseLeft.setBlurRadius(20)
        self.ShadowForResistanceBaseLeft.setColor(QColor("black"))
        self.ShadowForResistanceBaseLeft.setOffset(0,0)
        self.LabelForResistanceBaseLeft.setGraphicsEffect(self.ShadowForResistanceBaseLeft)
        self.LabelForResistanceBaseRight.setGeometry(600,585,130,10)
        self.LabelForResistanceBaseRight.setStyleSheet("background-color:#cccccc;border-right:2px solid black;border-top:1px solid grey;border-bottom:1px solid grey;")
        self.ShadowForResistanceBaseRight = QGraphicsDropShadowEffect(self)
        self.ShadowForResistanceBaseRight.setBlurRadius(20)
        self.ShadowForResistanceBaseRight.setColor(QColor("black"))
        self.ShadowForResistanceBaseRight.setOffset(0,0)
        self.LabelForResistanceBaseRight.setGraphicsEffect(self.ShadowForResistanceBaseRight)
        self.LabelForResistanceColorOne.setGeometry(250,550,30,80)
        self.LabelForResistanceColorOne.setStyleSheet("background-color:brown;border:1px solid black;")
        self.LabelForResistanceColorTwo.setGeometry(300,550,30,80)
        self.LabelForResistanceColorTwo.setStyleSheet("background-color:black;border:1px solid black;")
        self.LabelForResistanceColorThree.setGeometry(350,550,30,80)
        self.LabelForResistanceColorThree.setStyleSheet("background-color:green;border:1px solid black;")
        self.LabelForResistanceColorFour.setGeometry(400,550,30,80)
        self.LabelForResistanceColorFour.setStyleSheet("background-color:red;border:1px solid black;")
        self.LabelForResistanceColorFive.setGeometry(500,550,30,80)
        self.LabelForResistanceColorFive.setStyleSheet("background-color:red;border:1px solid black;")
        self.LabelForResistanceColorOne.show()
        self.LabelForResistanceColorTwo.show()
        self.LabelForResistanceColorThree.hide()
        self.LabelForResistanceColorFour.hide()
        self.LabelForResistanceColorFive.show()

        self.LabelForCoverOfCalculationArea.setGeometry(55,50,700,400)
        self.LabelForCoverOfCalculationArea.setStyleSheet("border-radius:10px;background-color:rgba(255,255,255,0.4);")
        self.LabelForOptionForThreeBand.setGeometry(95,80,200,40)
        self.LabelForOptionForThreeBand.setStyleSheet("QLabel{background-color:#3385ff;color:white;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
        self.LabelForOptionForThreeBand.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelForOptionForThreeBand.setCursor(Qt.CursorShape.PointingHandCursor)
        self.LabelForOptionForFourBand.setGeometry(305,80,200,40)
        self.LabelForOptionForFourBand.setStyleSheet("QLabel{background-color:orange;color:black;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
        self.LabelForOptionForFourBand.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelForOptionForFourBand.setCursor(Qt.CursorShape.PointingHandCursor)
        self.LabelForOptionForFiveBand.setGeometry(515,80,200,40)
        self.LabelForOptionForFiveBand.setStyleSheet("QLabel{background-color:orange;color:black;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
        self.LabelForOptionForFiveBand.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelForOptionForFiveBand.setCursor(Qt.CursorShape.PointingHandCursor)

        self.LabelForBandOne.setStyleSheet("border:1px solid black;color:white;font-size:16px;background-color:#ff0066;border-radius:5px;")
        self.LabelForBandOne.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelForBandTwo.setStyleSheet("border:1px solid black;color:white;font-size:16px;background-color:#ff0066;border-radius:5px;")
        self.LabelForBandTwo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelForBandThree.setStyleSheet("border:1px solid black;color:white;font-size:16px;background-color:#ff0066;border-radius:5px;")
        self.LabelForBandThree.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelForBandFour.setStyleSheet("border:1px solid black;color:white;font-size:16px;background-color:#ff0066;border-radius:5px;")
        self.LabelForBandFour.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LabelForBandFive.setStyleSheet("border:1px solid black;color:white;font-size:16px;background-color:#ff0066;border-radius:5px;")
        self.LabelForBandFive.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.ComboBoxForColorOne.setMaxVisibleItems(13)
        self.ComboBoxForColorOne.setGeometry(95,200,205,40)
        self.ComboBoxForColorOne.setEditable(False)
        self.DelegateOne = StyleOfComboBoxDelegate(self.ComboBoxForColorOne)
        self.ComboBoxForColorOne.setItemDelegate(self.DelegateOne)
        self.ComboBoxForColorOne.addItems(["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz"])
        self.ComboBoxForColorOne.setCurrentIndex(1)
        self.ComboBoxForColorOne.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: brown;
        font-size:16px;
        border-radius:8px;
        padding-left:60px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
        self.ComboBoxForColorTwo.setMaxVisibleItems(13)
        self.ComboBoxForColorTwo.setGeometry(302,200,205,40)
        self.ComboBoxForColorTwo.setEditable(False)
        self.DelegateTwo = StyleOfComboBoxDelegate(self.ComboBoxForColorTwo)
        self.ComboBoxForColorTwo.setItemDelegate(self.DelegateTwo)
        self.ComboBoxForColorTwo.addItems(["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz"])
        self.ComboBoxForColorTwo.setCurrentIndex(0)
        self.ComboBoxForColorTwo.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: black;
        font-size:16px;
        border-radius:8px;
        padding-left:75px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
        self.ComboBoxForColorThree.setMaxVisibleItems(13)
        self.ComboBoxForColorThree.setGeometry(510,200,205,40)
        self.ComboBoxForColorThree.setEditable(False)
        self.DelegateThree = StyleOfComboBoxDelegate(self.ComboBoxForColorThree)
        self.ComboBoxForColorThree.setItemDelegate(self.DelegateThree)
        self.ComboBoxForColorThree.addItems(["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz","Altın","Gümüş"])
        self.ComboBoxForColorThree.setCurrentIndex(2)
        self.ComboBoxForColorThree.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: red;
        font-size:16px;
        border-radius:8px;
        padding-left:70px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
        self.ComboBoxForColorFour.setMaxVisibleItems(13)
        self.ComboBoxForColorFour.setGeometry(472,200,122,40)
        self.ComboBoxForColorFour.setEditable(False)
        self.DelegateFour = StyleOfComboBoxDelegate(self.ComboBoxForColorFour)
        self.ComboBoxForColorFour.setItemDelegate(self.DelegateFour)
        self.ComboBoxForColorFour.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: black;
        font-size:16px;
        border-radius:8px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
        self.ComboBoxForColorFive.setMaxVisibleItems(13)
        self.ComboBoxForColorFive.setGeometry(597,200,122,40)
        self.ComboBoxForColorFive.setEditable(False)
        self.DelegateFive = StyleOfComboBoxDelegate(self.ComboBoxForColorFive)
        self.ComboBoxForColorFive.setItemDelegate(self.DelegateFive)
        self.ComboBoxForColorFive.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: black;
        font-size:16px;
        border-radius:8px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
        def UpdateTheColor(ComboBox):
             SelectedColor = str()
             SelectedColorsTextColor = "white"
             WidthOfComboBox = ComboBox.geometry().width()
             PaddingForColor = int()
             ConvertedPaddingValue = int()
             if ComboBox.currentText() == "Siyah":
                  SelectedColor = "black"
                  PaddingForColor = 75
             if ComboBox.currentText() == "Kahverengi":
                  SelectedColor = "brown"
                  PaddingForColor = 60
             if ComboBox.currentText() == "Kırmızı":
                  SelectedColor = "red"
                  PaddingForColor = 70
             if ComboBox.currentText() == "Turuncu":
                  SelectedColor = "orange"
                  PaddingForColor = 70
             if ComboBox.currentText() == "Sarı":
                  SelectedColorsTextColor = "black"
                  SelectedColor = "yellow"
                  PaddingForColor = 85
             if ComboBox.currentText() == "Yeşil":
                  SelectedColor = "green"
                  PaddingForColor = 85
             if ComboBox.currentText() == "Mavi":
                  SelectedColor = "blue"
                  PaddingForColor = 85
             if ComboBox.currentText() == "Mor":
                  SelectedColor = "purple"
                  PaddingForColor = 85
             if ComboBox.currentText() == "Gri":
                  SelectedColor = "grey"
                  PaddingForColor = 85
             if ComboBox.currentText() == "Beyaz":
                  SelectedColorsTextColor = "black"
                  SelectedColor = "white"
                  PaddingForColor = 80
             if ComboBox.currentText() == "Altın":
                  SelectedColor = "gold"   
                  PaddingForColor = 80
             if ComboBox.currentText() == "Gümüş":
                  SelectedColor = "silver"      
                  PaddingForColor = 75
             if WidthOfComboBox == 205:
                   ConvertedPaddingValue = int(PaddingForColor-0)
             if WidthOfComboBox == 153:
                   ConvertedPaddingValue = int(PaddingForColor-25)
             if WidthOfComboBox == 122:
                   ConvertedPaddingValue = int(PaddingForColor-38)
             ComboBox.setStyleSheet("""
            QComboBox {
                border: 1px solid black;
                background-color: %s;
                color:%s;
                border-radius:8px;
                padding-left:%spx;
                font-size:16px;
            }
           QComboBox QAbstractItemView {
                background-color:transparent;
                selection-background-color: white;
                color:#e6e6e6;
                border:none;
             }
            QComboBox::down-arrow {
                image: none;
            }
            QComboBox::drop-down {
                border: none;
            }
        """ % (QColor(SelectedColor).name(),SelectedColorsTextColor,ConvertedPaddingValue))
        self.ComboBoxForColorOne.currentTextChanged.connect(lambda : UpdateTheColor(self.ComboBoxForColorOne) )
        self.ComboBoxForColorTwo.currentTextChanged.connect(lambda : UpdateTheColor(self.ComboBoxForColorTwo) )
        self.ComboBoxForColorThree.currentTextChanged.connect(lambda : UpdateTheColor(self.ComboBoxForColorThree) )
        self.ComboBoxForColorFour.currentTextChanged.connect(lambda : UpdateTheColor(self.ComboBoxForColorFour) )
        self.ComboBoxForColorFive.currentTextChanged.connect(lambda : UpdateTheColor(self.ComboBoxForColorFive) )


        def ChangeResistanceColor():
             Colors = {"Siyah":"black","Kahverengi":"brown","Kırmızı":"red","Turuncu":"orange","Sarı":"yellow","Yeşil":"green","Mavi":"blue","Mor":"purple","Gri":"grey","Beyaz":"white","Altın":"gold","Gümüş":"silver"}
             ComboBoxOne = self.ComboBoxForColorOne.isHidden()
             ComboBoxTwo = self.ComboBoxForColorTwo.isHidden()
             ComboBoxThree = self.ComboBoxForColorThree.isHidden()
             ComboBoxFour = self.ComboBoxForColorFour.isHidden()
             ComboBoxFive = self.ComboBoxForColorFive.isHidden()
             if ComboBoxOne == False and ComboBoxTwo == False and ComboBoxThree == False:
                   ColorForOne = self.ComboBoxForColorOne.currentText()
                   ColorForTwo= self.ComboBoxForColorTwo.currentText()
                   ColorForThree = self.ComboBoxForColorThree.currentText()
                   if ColorForOne in Colors and ColorForTwo in Colors and ColorForThree in Colors:
                         RealColorOne = Colors[ColorForOne]
                         RealColorTwo = Colors[ColorForTwo]
                         RealColorThree = Colors[ColorForThree]
                         self.LabelForResistanceColorOne.setStyleSheet(f"background-color:{RealColorOne};border:1px solid black")
                         self.LabelForResistanceColorTwo.setStyleSheet(f"background-color:{RealColorTwo};border:1px solid black")
                         self.LabelForResistanceColorFive.setStyleSheet(f"background-color:{RealColorThree};border:1px solid black")
             if ComboBoxOne == False and ComboBoxTwo == False and ComboBoxThree == False and ComboBoxFour == False:
                   ColorForOne = self.ComboBoxForColorOne.currentText()
                   ColorForTwo= self.ComboBoxForColorTwo.currentText()
                   ColorForThree = self.ComboBoxForColorThree.currentText()
                   ColorForFour = self.ComboBoxForColorFour.currentText()
                   if ColorForOne in Colors and ColorForTwo in Colors and ColorForThree in Colors and ColorForFour in Colors:
                         RealColorOne = Colors[ColorForOne]
                         RealColorTwo = Colors[ColorForTwo]
                         RealColorThree = Colors[ColorForThree]
                         RealColorFour = Colors[ColorForFour]
                         self.LabelForResistanceColorOne.setStyleSheet(f"background-color:{RealColorOne};border:1px solid black")
                         self.LabelForResistanceColorTwo.setStyleSheet(f"background-color:{RealColorTwo};border:1px solid black")
                         self.LabelForResistanceColorThree.setStyleSheet(f"background-color:{RealColorThree};border:1px solid black")
                         self.LabelForResistanceColorFive.setStyleSheet(f"background-color:{RealColorFour};border:1px solid black")
             if ComboBoxOne == False and ComboBoxTwo == False and ComboBoxThree == False and ComboBoxFour == False and ComboBoxFive == False:
                   ColorForOne = self.ComboBoxForColorOne.currentText()
                   ColorForTwo= self.ComboBoxForColorTwo.currentText()
                   ColorForThree = self.ComboBoxForColorThree.currentText()
                   ColorForFour = self.ComboBoxForColorFour.currentText()
                   ColorForFive = self.ComboBoxForColorFive.currentText()
                   if ColorForOne in Colors and ColorForTwo in Colors and ColorForThree in Colors and ColorForFour in Colors and ColorForFive in Colors:
                         RealColorOne = Colors[ColorForOne]
                         RealColorTwo = Colors[ColorForTwo]
                         RealColorThree = Colors[ColorForThree]
                         RealColorFour = Colors[ColorForFour]
                         RealColorFive = Colors[ColorForFive]
                         self.LabelForResistanceColorOne.setStyleSheet(f"background-color:{RealColorOne};border:1px solid black")
                         self.LabelForResistanceColorTwo.setStyleSheet(f"background-color:{RealColorTwo};border:1px solid black")
                         self.LabelForResistanceColorThree.setStyleSheet(f"background-color:{RealColorThree};border:1px solid black")
                         self.LabelForResistanceColorFour.setStyleSheet(f"background-color:{RealColorFour};border:1px solid black")         
                         self.LabelForResistanceColorFive.setStyleSheet(f"background-color:{RealColorFive};border:1px solid black")               
        self.ComboBoxForColorOne.currentTextChanged.connect(ChangeResistanceColor)
        self.ComboBoxForColorTwo.currentTextChanged.connect(ChangeResistanceColor)
        self.ComboBoxForColorThree.currentTextChanged.connect(ChangeResistanceColor)
        self.ComboBoxForColorFour.currentTextChanged.connect(ChangeResistanceColor)
        self.ComboBoxForColorFive.currentTextChanged.connect(ChangeResistanceColor)

        self.LabelForBandOne.setGeometry(95,140,205,40)
        self.LabelForBandTwo.setGeometry(302,140,205,40)
        self.LabelForBandThree.setGeometry(510,140,205,40) 
        self.ComboBoxForColorFour.hide()
        self.ComboBoxForColorFive.hide()
        self.LabelForBandFour.hide()
        self.LabelForBandFive.hide() 
        def ThreeColorOption(event):
              self.LabelForResistanceColorOne.show()
              self.LabelForResistanceColorTwo.show()
              self.LabelForResistanceColorThree.hide()
              self.LabelForResistanceColorFour.hide()
              self.LabelForResistanceColorFive.show()
              self.LabelForResistanceColorOne.setStyleSheet("background-color:brown;border:1px solid black;")
              self.LabelForResistanceColorTwo.setStyleSheet("background-color:black;border:1px solid black;")
              self.LabelForResistanceColorFive.setStyleSheet("background-color:red;border:1px solid black;")
              self.LineEditForResultedValue.setText("1kΩ ±20%")
              self.LabelForBandOne.setText("1.Bant (1.Sayı)")
              self.LabelForBandTwo.setText("2.Bant (2.Sayı)")
              self.LabelForBandThree.setText("3.Bant (Çarpan)")
              self.LabelForBandFour.setText("4.Bant")
              self.LabelForBandFive.setText("5.Bant")
              self.LabelForBandOne.setGeometry(95,140,205,40)
              self.LabelForBandTwo.setGeometry(302,140,205,40)
              self.LabelForBandThree.setGeometry(510,140,205,40)     
              self.LabelForOptionForThreeBand.setStyleSheet("QLabel{background-color:#3385ff;color:white;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
              self.LabelForOptionForFourBand.setStyleSheet("QLabel{background-color:orange;color:black;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
              self.LabelForOptionForFiveBand.setStyleSheet("QLabel{background-color:orange;color:black;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
              self.ComboBoxForColorOne.setGeometry(95,200,205,40)
              self.ComboBoxForColorTwo.setGeometry(302,200,205,40)
              self.ComboBoxForColorThree.setGeometry(510,200,205,40)
              self.ComboBoxForColorFour.hide()
              self.ComboBoxForColorFive.hide()
              self.LabelForBandFour.hide()
              self.LabelForBandFive.hide()
              self.ComboBoxForColorOne.setCurrentIndex(1)
              self.ComboBoxForColorOne.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: brown;
        font-size:16px;
        border-radius:8px;
        padding-left:55px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
              self.ComboBoxForColorTwo.clear()
              self.ComboBoxForColorTwo.addItems(["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz"])
              self.ComboBoxForColorTwo.setCurrentIndex(0)
              self.ComboBoxForColorTwo.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: black;
        font-size:16px;
        border-radius:8px;
        padding-left:75px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
              self.ComboBoxForColorThree.clear()
              self.ComboBoxForColorThree.addItems(["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Altın","Gümüş"])
              self.ComboBoxForColorThree.setCurrentIndex(2)
              self.ComboBoxForColorThree.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: red;
        font-size:16px;
        border-radius:8px;
        padding-left:70px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
        def FourColorOption(event):
               self.LabelForResistanceColorOne.show()
               self.LabelForResistanceColorTwo.show()
               self.LabelForResistanceColorThree.show()
               self.LabelForResistanceColorFour.hide()
               self.LabelForResistanceColorFive.show()
               self.LabelForResistanceColorOne.setStyleSheet("background-color:brown;border:1px solid black;")
               self.LabelForResistanceColorTwo.setStyleSheet("background-color:black;border:1px solid black;")
               self.LabelForResistanceColorThree.setStyleSheet("background-color:silver;border:1px solid black;")     
               self.LabelForResistanceColorFive.setStyleSheet("background-color:gold;border:1px solid black;")     
               self.LineEditForResultedValue.setText("0.1Ω ±5%")
               self.LabelForBandOne.setText("1.Bant (1.Sayı)")
               self.LabelForBandTwo.setText("2.Bant (2.Sayı)")
               self.LabelForBandThree.setText("3.Bant (Çarpan)")
               self.LabelForBandFour.setText("4.Bant (Tolerans)")
               self.LabelForBandFive.setText("5.Bant")
               self.LabelForBandOne.setGeometry(95,140,153,40)
               self.LabelForBandTwo.setGeometry(252,140,153,40)
               self.LabelForBandThree.setGeometry(408,140,153,40)
               self.LabelForBandFour.setGeometry(565,140,153,40)
               self.LabelForOptionForThreeBand.setStyleSheet("QLabel{background-color:orange;color:black;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
               self.LabelForOptionForFourBand.setStyleSheet("QLabel{background-color:#3385ff;color:white;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
               self.LabelForOptionForFiveBand.setStyleSheet("QLabel{background-color:orange;color:black;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}") 
               self.ComboBoxForColorOne.setGeometry(95,200,153,40)
               self.ComboBoxForColorTwo.setGeometry(252,200,153,40)
               self.ComboBoxForColorThree.setGeometry(408,200,153,40)
               self.ComboBoxForColorFour.setGeometry(565,200,153,40)
               self.ComboBoxForColorFour.show()
               self.ComboBoxForColorFive.hide()
               self.LabelForBandFour.show()
               self.LabelForBandFive.hide()
               self.ComboBoxForColorOne.setCurrentIndex(1)
               self.ComboBoxForColorTwo.setCurrentIndex(0)
               self.ComboBoxForColorFour.clear()
               self.ComboBoxForColorFour.addItems(["Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Altın","Gümüş"])
               self.ComboBoxForColorFour.setCurrentIndex(8)
               self.ComboBoxForColorThree.clear()
               self.ComboBoxForColorThree.addItems(["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz","Altın","Gümüş"])
               self.ComboBoxForColorThree.setCurrentIndex(11)
               self.ComboBoxForColorOne.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: brown;
        font-size:16px;
        border-radius:8px;
        padding-left:35px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
               self.ComboBoxForColorTwo.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: black;
        font-size:16px;
        border-radius:8px;
        padding-left:50px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
               self.ComboBoxForColorThree.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: silver;
        font-size:16px;
        border-radius:8px;
        padding-left:50px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
               self.ComboBoxForColorFour.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: gold;
        font-size:16px;
        border-radius:8px;
        padding-left:55px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
        def FiveColorOption(event):
                self.LabelForResistanceColorOne.show()
                self.LabelForResistanceColorTwo.show()
                self.LabelForResistanceColorThree.show()
                self.LabelForResistanceColorFour.show()
                self.LabelForResistanceColorFive.show()
                self.LabelForResistanceColorOne.setStyleSheet("background-color:brown;border:1px solid black;")
                self.LabelForResistanceColorTwo.setStyleSheet("background-color:black;border:1px solid black;")
                self.LabelForResistanceColorThree.setStyleSheet("background-color:green;border:1px solid black;")     
                self.LabelForResistanceColorFour.setStyleSheet("background-color:red;border:1px solid black;")    
                self.LabelForResistanceColorFive.setStyleSheet("background-color:gold;border:1px solid black;")   
                self.LineEditForResultedValue.setText("10.5kΩ ±5%")
                self.LabelForBandOne.setText("1.Bant (1.Sayı)")
                self.LabelForBandTwo.setText("2.Bant (2.Sayı)")
                self.LabelForBandThree.setText("3.Bant (3.Sayı)")
                self.LabelForBandFour.setText("4.Bant (Çarpan)")
                self.LabelForBandFive.setText("5.Bant (Tolerans)")
                self.LabelForBandOne.setGeometry(95,140,122,40)
                self.LabelForBandTwo.setGeometry(220,140,122,40)
                self.LabelForBandThree.setGeometry(346,140,122,40)
                self.LabelForBandFour.setGeometry(472,140,122,40)
                self.LabelForBandFive.setGeometry(597,140,122,40)
                self.LabelForOptionForThreeBand.setStyleSheet("QLabel{background-color:orange;color:black;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
                self.LabelForOptionForFourBand.setStyleSheet("QLabel{background-color:orange;color:black;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
                self.LabelForOptionForFiveBand.setStyleSheet("QLabel{background-color:#3385ff;color:white;border-radius:8px;border:1px solid blue;font-size:15px;font-family:Century Gothic;}QLabel:hover {background-color:#3385ff;color:white;border:1px solid black;}")
                self.ComboBoxForColorOne.setGeometry(95,200,122,40)
                self.ComboBoxForColorTwo.setGeometry(220,200,122,40)
                self.ComboBoxForColorThree.setGeometry(346,200,122,40)
                self.ComboBoxForColorFour.setGeometry(472,200,122,40)
                self.ComboBoxForColorFive.setGeometry(597,200,122,40)
                self.ComboBoxForColorFour.show()
                self.ComboBoxForColorFive.show()
                self.LabelForBandFour.show()
                self.LabelForBandFive.show()
                self.ComboBoxForColorOne.setCurrentIndex(1)
                self.ComboBoxForColorTwo.setCurrentIndex(0)
                self.ComboBoxForColorThree.clear()
                self.ComboBoxForColorThree.addItems(["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz"])       
                self.ComboBoxForColorThree.setCurrentIndex(5) 
                self.ComboBoxForColorFour.clear()
                self.ComboBoxForColorFour.addItems(["Siyah","Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Beyaz","Altın","Gümüş"])
                self.ComboBoxForColorFour.setCurrentIndex(2)
                self.ComboBoxForColorFive.clear()
                self.ComboBoxForColorFive.addItems(["Kahverengi","Kırmızı","Turuncu","Sarı","Yeşil","Mavi","Mor","Gri","Altın","Gümüş"])
                self.ComboBoxForColorFive.setCurrentIndex(8)
                self.ComboBoxForColorOne.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: brown;
        font-size:16px;
        border-radius:8px;
        padding-left:22px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
                self.ComboBoxForColorTwo.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: black;
        font-size:16px;
        border-radius:8px;
        padding-left:37px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
                self.ComboBoxForColorThree.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: green;
        font-size:16px;
        border-radius:8px;
        padding-left:47px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
                self.ComboBoxForColorFour.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: red;
        font-size:16px;
        border-radius:8px;
        padding-left:32px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
                self.ComboBoxForColorFive.setStyleSheet("""
    QComboBox {
        border: 1px solid black;
        background-color: gold;
        font-size:16px;
        border-radius:8px;
        padding-left:42px;
    }
    QComboBox QAbstractItemView {
        background-color:transparent;
        selection-background-color: white;
        color:#e6e6e6;
        border:none;
    }
    QComboBox::down-arrow {
        image: none;
    }
    QComboBox::drop-down {
        border: none;
    }                                             
""")
        self.LabelForOptionForThreeBand.mousePressEvent = ThreeColorOption
        self.LabelForOptionForFourBand.mousePressEvent = FourColorOption
        self.LabelForOptionForFiveBand.mousePressEvent = FiveColorOption

        self.PushButtonForCalculation.setGeometry(90,360,300,50)
        self.PushButtonForCalculation.setStyleSheet("QPushButton {background-color:purple;color:white;border-radius:8px;font-size:17px;border:1px solid orange;}QPushButton:hover {background-color:#cc99ff;color:black;border:2px solid #b36b00;}")
        self.ShadowForCalculationButton = QGraphicsDropShadowEffect(self)
        self.ShadowForCalculationButton.setBlurRadius(20)
        self.ShadowForCalculationButton.setColor(QColor("black"))
        self.ShadowForCalculationButton.setOffset(2,2)
        self.PushButtonForCalculation.setGraphicsEffect(self.ShadowForCalculationButton)
        self.PushButtonForCalculation.setCursor(Qt.CursorShape.PointingHandCursor)
        self.LineEditForResultedValue.setGeometry(410,360,300,50)
        self.LineEditForResultedValue.setReadOnly(True)
        self.LineEditForResultedValue.setStyleSheet("QLineEdit{background-color:purple;padding-bottom:10px;purple;color:white;border-radius:8px;font-size:18px;border:1px solid orange;padding-top:10px;}QLineEdit:hover{background-color:#cc99ff;color:black;}")
        self.ShadowForResultedValue = QGraphicsDropShadowEffect(self)
        self.ShadowForResultedValue.setBlurRadius(20)
        self.ShadowForResultedValue.setColor(QColor("black"))
        self.ShadowForResultedValue.setOffset(2,2)
        self.LineEditForResultedValue.setGraphicsEffect(self.ShadowForResultedValue)
        self.LineEditForResultedValue.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.LineEditForResultedValue.setCursor(Qt.CursorShape.PointingHandCursor)
        
        def CalculateTheResistance(event):
             ColorValues  = {"Siyah":0,"Kahverengi":1,"Kırmızı":2,"Turuncu":3,"Sarı":4,"Yeşil":5,"Mavi":6,"Mor":7,"Gri":8,"Beyaz":9,"Altın":-1,"Gümüş":-2}
             TolerancesOfColors = {"Kahverengi":"±1%","Kırmızı":"±2%","Turuncu":"±3%","Sarı":"±4%","Yeşil":"±0.50%","Mavi":"±0.25%","Mor":"±0.10%","Gri":"±0.05%","Altın":"±5%","Gümüş":"±10%","Beyaz":"","Siyah":""}
             ComboBoxOne = self.ComboBoxForColorOne.isHidden()
             ComboBoxTwo = self.ComboBoxForColorTwo.isHidden()
             ComboBoxThree = self.ComboBoxForColorThree.isHidden()
             ComboBoxFour = self.ComboBoxForColorFour.isHidden()
             ComboBoxFive = self.ComboBoxForColorFive.isHidden()

             ComboBoxOneTextForThreeColorOption= self.ComboBoxForColorOne.currentText()
             ComboBoxTwoTextForThreeColorOption = self.ComboBoxForColorTwo.currentText()
             ComboBoxThreeTextFactorForThreeColorOption = self.ComboBoxForColorThree.currentText()
             if ComboBoxOne == False and ComboBoxTwo == False and ComboBoxThree == False:
                               if ComboBoxOneTextForThreeColorOption in ColorValues and ComboBoxTwoTextForThreeColorOption in ColorValues and ComboBoxThreeTextFactorForThreeColorOption in ColorValues:
                                Value1 = (ColorValues[ComboBoxOneTextForThreeColorOption])
                                Value2 = (ColorValues[ComboBoxTwoTextForThreeColorOption])
                                Factor = (ColorValues[ComboBoxThreeTextFactorForThreeColorOption])
                                StringValueOfTheNumber = f"{Value1}{Value2}"
                                IntValueOfTheNumber = int(StringValueOfTheNumber)
                                MetricUsageForResult = IntValueOfTheNumber*pow(10,Factor)
                                if MetricUsageForResult < 1000:
                                     MetricConversionZero = MetricUsageForResult/pow(10,0)
                                     DecimalProblemList = list(str(MetricConversionZero).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionZero}Ω ±20%")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionZero)}Ω ±20%")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionZero}Ω ±20%") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionZero)}Ω ±20%") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionZero).split(".")[0]}.{RealDecimalValueWithOutZero}Ω ±20%")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionZero).split(".")[0]}.{RealDecimalValueWithZero}Ω ±20%")                                                  
                                if MetricUsageForResult >= 1000 and MetricUsageForResult <=999999:
                                     MetricConversionOne = MetricUsageForResult/pow(10,3)
                                     DecimalProblemList = list(str(MetricConversionOne).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionOne}kΩ ±20%")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionOne)}kΩ ±20%")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionOne}kΩ ±20%") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionOne)}kΩ ±20%") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionOne).split(".")[0]}.{RealDecimalValueWithOutZero}kΩ ±20%")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionOne).split(".")[0]}.{RealDecimalValueWithZero}kΩ ±20%")     
                                if MetricUsageForResult >= 1000000 and MetricUsageForResult <= 999999999:
                                     MetricConversionTwo = MetricUsageForResult/pow(10,6)
                                     DecimalProblemList = list(str(MetricConversionTwo).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionTwo}MΩ ±20%")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionTwo)}MΩ ±20%")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionTwo}MΩ ±20%") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionTwo)}MΩ ±20%") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionTwo).split(".")[0]}.{RealDecimalValueWithOutZero}MΩ ±20%")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionTwo).split(".")[0]}.{RealDecimalValueWithZero}MΩ ±20%")     
                                if MetricUsageForResult >= 1000000000 and MetricUsageForResult <= 999999999999:
                                     MetricConversionThree = MetricUsageForResult/pow(10,9)
                                     DecimalProblemList = list(str(MetricConversionThree).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionThree}GΩ ±20%")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionThree)}GΩ ±20%")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionThree}GΩ ±20%") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionThree)}GΩ ±20%") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionThree).split(".")[0]}.{RealDecimalValueWithOutZero}GΩ ±20%")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionThree).split(".")[0]}.{RealDecimalValueWithZero}GΩ ±20%")     

             ComboBoxOneTextForFourColorOption= self.ComboBoxForColorOne.currentText()
             ComboBoxTwoTextForFourColorOption = self.ComboBoxForColorTwo.currentText()
             ComboBoxThreeTextFactorForFourColorOption= self.ComboBoxForColorThree.currentText()
             ComboBoxFourTextToleranceForFourColorOption = self.ComboBoxForColorFour.currentText()
             if ComboBoxOne == False and ComboBoxTwo == False and ComboBoxThree == False and ComboBoxFour == False:
                               if ComboBoxOneTextForFourColorOption in ColorValues and ComboBoxTwoTextForFourColorOption in ColorValues and ComboBoxThreeTextFactorForFourColorOption in ColorValues and ComboBoxFourTextToleranceForFourColorOption in TolerancesOfColors :
                                Value1 = (ColorValues[ComboBoxOneTextForFourColorOption])
                                Value2 = (ColorValues[ComboBoxTwoTextForFourColorOption])
                                Factor = (ColorValues[ComboBoxThreeTextFactorForFourColorOption])
                                Tolerance = (TolerancesOfColors[ComboBoxFourTextToleranceForFourColorOption])
                                StringValueOfTheNumber = f"{Value1}{Value2}"
                                IntValueOfTheNumber = int(StringValueOfTheNumber)
                                MetricUsageForResult = IntValueOfTheNumber*pow(10,Factor)
                                if MetricUsageForResult < 1000:
                                     MetricConversionZero = MetricUsageForResult/pow(10,0)
                                     DecimalProblemList = list(str(MetricConversionZero).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionZero}Ω {Tolerance}")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionZero)}Ω {Tolerance}")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionZero}Ω {Tolerance}") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionZero)}Ω {Tolerance}") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionZero).split(".")[0]}.{RealDecimalValueWithOutZero}Ω {Tolerance}")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionZero).split(".")[0]}.{RealDecimalValueWithZero}Ω {Tolerance}")                                                  
                                if MetricUsageForResult >= 1000 and MetricUsageForResult <=999999:
                                     MetricConversionOne = MetricUsageForResult/pow(10,3)
                                     DecimalProblemList = list(str(MetricConversionOne).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionOne}kΩ {Tolerance}")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionOne)}kΩ {Tolerance}")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionOne}kΩ {Tolerance}") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionOne)}kΩ {Tolerance}") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionOne).split(".")[0]}.{RealDecimalValueWithOutZero}kΩ {Tolerance}")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionOne).split(".")[0]}.{RealDecimalValueWithZero}kΩ {Tolerance}")     
                                if MetricUsageForResult >= 1000000 and MetricUsageForResult <= 999999999:
                                     MetricConversionTwo = MetricUsageForResult/pow(10,6)
                                     DecimalProblemList = list(str(MetricConversionTwo).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionTwo}MΩ {Tolerance}")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionTwo)}MΩ {Tolerance}")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionTwo}MΩ {Tolerance}") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionTwo)}MΩ {Tolerance}") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionTwo).split(".")[0]}.{RealDecimalValueWithOutZero}MΩ {Tolerance}")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionTwo).split(".")[0]}.{RealDecimalValueWithZero}MΩ {Tolerance}")     
                                if MetricUsageForResult >= 1000000000 and MetricUsageForResult <= 999999999999:
                                     MetricConversionThree = MetricUsageForResult/pow(10,9)
                                     DecimalProblemList = list(str(MetricConversionThree).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionThree}GΩ {Tolerance}")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionThree)}GΩ {Tolerance}")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionThree}GΩ {Tolerance}") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionThree)}GΩ {Tolerance}") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionThree).split(".")[0]}.{RealDecimalValueWithOutZero}GΩ {Tolerance}")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionThree).split(".")[0]}.{RealDecimalValueWithZero}GΩ {Tolerance}")     

             ComboBoxOneTextForFiveColorOption= self.ComboBoxForColorOne.currentText()
             ComboBoxTwoTextForFiveColorOption = self.ComboBoxForColorTwo.currentText()
             ComboBoxThreeTextForFiveColorOption= self.ComboBoxForColorThree.currentText()
             ComboBoxFourTextFactorForFiveColorOption = self.ComboBoxForColorFour.currentText()
             ComboBoxFiveTextToleranceForFiveColorOption = self.ComboBoxForColorFive.currentText()
             if ComboBoxOne == False and ComboBoxTwo == False and ComboBoxThree == False and ComboBoxFour == False and ComboBoxFive == False:
                               if ComboBoxOneTextForFiveColorOption in ColorValues and ComboBoxTwoTextForFiveColorOption in ColorValues and ComboBoxThreeTextForFiveColorOption in ColorValues and ComboBoxFourTextFactorForFiveColorOption in ColorValues and ComboBoxFiveTextToleranceForFiveColorOption in TolerancesOfColors :
                                Value1 = (ColorValues[ComboBoxOneTextForFiveColorOption])
                                Value2 = (ColorValues[ComboBoxTwoTextForFiveColorOption])
                                Value3 = (ColorValues[ComboBoxThreeTextForFiveColorOption])
                                Factor = (ColorValues[ComboBoxFourTextFactorForFiveColorOption])
                                Tolerance = (TolerancesOfColors[ComboBoxFiveTextToleranceForFiveColorOption])
                                StringValueOfTheNumber = f"{Value1}{Value2}{Value3}"
                                IntValueOfTheNumber = int(StringValueOfTheNumber)
                                MetricUsageForResult = IntValueOfTheNumber*pow(10,Factor)
                                if MetricUsageForResult < 1000:
                                     MetricConversionZero = MetricUsageForResult/pow(10,0)
                                     DecimalProblemList = list(str(MetricConversionZero).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionZero}Ω {Tolerance}")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionZero)}Ω {Tolerance}")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionZero}Ω {Tolerance}") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionZero)}Ω {Tolerance}") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionZero).split(".")[0]}.{RealDecimalValueWithOutZero}Ω {Tolerance}")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionZero).split(".")[0]}.{RealDecimalValueWithZero}Ω {Tolerance}")                                                  
                                if MetricUsageForResult >= 1000 and MetricUsageForResult <=999999:
                                     MetricConversionOne = MetricUsageForResult/pow(10,3)
                                     DecimalProblemList = list(str(MetricConversionOne).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionOne}kΩ {Tolerance}")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionOne)}kΩ {Tolerance}")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionOne}kΩ {Tolerance}") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionOne)}kΩ {Tolerance}") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionOne).split(".")[0]}.{RealDecimalValueWithOutZero}kΩ {Tolerance}")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionOne).split(".")[0]}.{RealDecimalValueWithZero}kΩ {Tolerance}")     
                                if MetricUsageForResult >= 1000000 and MetricUsageForResult <= 999999999:
                                     MetricConversionTwo = MetricUsageForResult/pow(10,6)
                                     DecimalProblemList = list(str(MetricConversionTwo).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionTwo}MΩ {Tolerance}")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionTwo)}MΩ {Tolerance}")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionTwo}MΩ {Tolerance}") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionTwo)}MΩ {Tolerance}") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionTwo).split(".")[0]}.{RealDecimalValueWithOutZero}MΩ {Tolerance}")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionTwo).split(".")[0]}.{RealDecimalValueWithZero}MΩ {Tolerance}")     
                                if MetricUsageForResult >= 1000000000 and MetricUsageForResult <= 999999999999:
                                     MetricConversionThree = MetricUsageForResult/pow(10,9)
                                     DecimalProblemList = list(str(MetricConversionThree).split(".")[1])
                                     if len(DecimalProblemList) == 1:
                                          if DecimalProblemList[0] != "0":                                     
                                                self.LineEditForResultedValue.setText(f"{MetricConversionThree}GΩ {Tolerance}")
                                          if DecimalProblemList[0] == "0":
                                                self.LineEditForResultedValue.setText(f"{int(MetricConversionThree)}GΩ {Tolerance}")
                                     if len(DecimalProblemList) == 2:
                                                self.LineEditForResultedValue.setText(f"{MetricConversionThree}GΩ {Tolerance}") 
                                     if len(DecimalProblemList) >2:
                                          if DecimalProblemList[0] == "0" and DecimalProblemList[1] == "0":
                                                self.LineEditForResultedValue.setText(f"{round(MetricConversionThree)}GΩ {Tolerance}") 
                                          else:
                                               ListForUseableDigits = list()
                                               for x in range(0,2):
                                                    ListForUseableDigits.append(DecimalProblemList[x])
                                               if ListForUseableDigits[1] != "0":
                                                     RealDecimalValueWithOutZero = f"{ListForUseableDigits[0]}{ListForUseableDigits[1]}"
                                                     self.LineEditForResultedValue.setText(f"{str(MetricConversionThree).split(".")[0]}.{RealDecimalValueWithOutZero}GΩ {Tolerance}")
                                               else:
                                                    RealDecimalValueWithZero = f"{ListForUseableDigits[0]}"
                                                    self.LineEditForResultedValue.setText(f"{str(MetricConversionThree).split(".")[0]}.{RealDecimalValueWithZero}GΩ {Tolerance}")     
        self.PushButtonForCalculation.mousePressEvent = CalculateTheResistance
                  
        self.setGeometry(400,40,800,800)
        self.setFixedSize(800,800)
        self.setWindowTitle("Direnç Renk Kodu Uygulaması")
        self.setWindowIcon(QIcon("C:/Users/ugury/Masaüstü/Python PyQt6 Applications/Direnç Renk Kodu Uygulaması/icon.ico"))
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    WindowForGUI = GUI_Main_Window()
    sys.exit(App.exec())
    
