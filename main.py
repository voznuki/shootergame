#создай тут фоторедактор Easy Editor!
import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Диалог открытия файлов (и папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt # нужна константа Qt.KeepAspectRatio для изменения размеров с сохранением пропорций
from PyQt5.QtGui import QPixmap # оптимизированная для показа на экране картинка
 
from PIL import Image
app = QApplication([])
win = QWidget()
btn_dir = QPushButton("Папка")
btn_dir1 = QPushButton("Плаво")
btn_dir2 = QPushButton("Лево")
btn_dir3 = QPushButton("ч\б")
btn_dir4 = QPushButton("зеркало")
btn_dir5 = QPushButton("резкость")
win.resize(700, 400)
lb_image = QLabel()
files = QListWidget()
row = QHBoxLayout()
col1 = QVBoxLayout()
col3 = QVBoxLayout()
col2 = QHBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(files)
col2.addWidget(btn_dir2)
col2.addWidget(btn_dir1)
col2.addWidget(btn_dir3)
col2.addWidget(btn_dir4)
col2.addWidget(btn_dir5)
col3.addWidget(lb_image)
col3.addLayout(col2)
row.addLayout(col1)
row.addLayout(col3)
win.setLayout(row)
win.show()

workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extensions)
    files.clear()
    for filename in filenames:
        files.addItem(filename)

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        
    def loadImage(self, filename):
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)

        self.image.save(fullname)

    def do_dir3(self):
        self.image = self.image.convert("P")
        self.saveImage()
        image_path = os.path.join(workdir, self.seve_dir, self.filename)
        self.showImage(image_path)

    def do_dir2(self):
        self.image = self.image.transpose(image.ROTATE_90)
        self.saveImage()
        image_path = os.path.join(workdir, self.seve_dir, self.filename)
        self.showImage(image_path)

    def do_dir1(self):
        self.image = self.image.transpose(image.ROTATE_270)
        self.saveImage()
        image_path = os.path.join(workdir, self.seve_dir, self.filename)
        self.showImage(image_path)

    def do_dir4(self):
        self.image = self.image.transpose(image.FLIP_LEFT_RIGHT)
        self.saveImage()
        image_path = os.path.join(workdir, self.seve_dir, self.filename)
        self.showImage(image_path)

    def do_dir5(self):
        self.image = self.image.filter(SHARPEN)
        self.saveImage()
        image_path = os.path.join(workdir, self.seve_dir, self.filename)
        self.showImage(image_path)

    def showImage(self, path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

workimage = ImageProcessor()

def showChosenImage():
    if files.currentRow() >= 0:
        filename = files.currentItem().text()
        workimage.loadImage(filename)
        workimage.showImage(os.path.join(workdir, workimage.filename))

btn_dir.clicked.connect(showFilenamesList)
files.currentRowChanged.connect(showChosenImage)

btn_dir3.clicked.connect(workimage.do_dir3)
btn_dir2.clicked.connect(workimage.do_dir2)
btn_dir1.clicked.connect(workimage.do_dir1)
btn_dir4.clicked.connect(workimage.do_dir4)
btn_dir5.clicked.connect(workimage.do_dir5)

app.exec()




