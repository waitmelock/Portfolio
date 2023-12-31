# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Q1234_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import tkinter
from tkinter import filedialog
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import cv2 as cv
import numpy as np
import os
from matplotlib.image import imread
from matplotlib import pyplot as plt
from pathlib import Path
import glob



class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 322)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Q3 = QtWidgets.QGroupBox(self.centralwidget)
        self.Q3.setGeometry(QtCore.QRect(510, 20, 150, 275))
        self.Q3.setObjectName("Q3")
        self.Button_3_1 = QtWidgets.QPushButton(self.Q3)
        self.Button_3_1.setGeometry(QtCore.QRect(20, 130, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3_1.sizePolicy().hasHeightForWidth())
        self.Button_3_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_3_1.setFont(font)
        self.Button_3_1.setAutoDefault(False)
        self.Button_3_1.setDefault(False)
        self.Button_3_1.setObjectName("Button_3_1")
        self.Button_3_1.clicked.connect (self.buttonclik_Button_3_1)

        self.Button_3_2 = QtWidgets.QPushButton(self.Q3)
        self.Button_3_2.setGeometry(QtCore.QRect(20, 200, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_3_2.sizePolicy().hasHeightForWidth())
        self.Button_3_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_3_2.setFont(font)
        self.Button_3_2.setAutoDefault(False)
        self.Button_3_2.setDefault(False)
        self.Button_3_2.setObjectName("Button_3_2")
        self.Button_3_2.clicked.connect (self.buttonclik_Button_3_2)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.Q3)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 55, 110, 25))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Q2 = QtWidgets.QGroupBox(self.centralwidget)
        self.Q2.setGeometry(QtCore.QRect(350, 20, 150, 275))
        self.Q2.setObjectName("Q2")
        self.Button_2_1 = QtWidgets.QPushButton(self.Q2)
        self.Button_2_1.setGeometry(QtCore.QRect(20, 30, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_1.sizePolicy().hasHeightForWidth())
        self.Button_2_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_1.setFont(font)
        self.Button_2_1.setAutoDefault(False)
        self.Button_2_1.setDefault(False)
        self.Button_2_1.setObjectName("Button_2_1")
        self.Button_2_1.clicked.connect (self.buttonclik_Button_2_1)

        self.Button_2_2 = QtWidgets.QPushButton(self.Q2)
        self.Button_2_2.setGeometry(QtCore.QRect(20, 70, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_2.sizePolicy().hasHeightForWidth())
        self.Button_2_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_2.setFont(font)
        self.Button_2_2.setAutoDefault(False)
        self.Button_2_2.setDefault(False)
        self.Button_2_2.setObjectName("Button_2_2")
        self.Button_2_2.clicked.connect (self.buttonclik_Button_2_2)

        self.Q2_3 = QtWidgets.QGroupBox(self.Q2)
        self.Q2_3.setGeometry(QtCore.QRect(10, 110, 130, 71))
        self.Q2_3.setObjectName("Q2_3")
        self.Button_2_3 = QtWidgets.QPushButton(self.Q2_3)
        self.Button_2_3.setGeometry(QtCore.QRect(10, 40, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_3.sizePolicy().hasHeightForWidth())
        self.Button_2_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_3.setFont(font)
        self.Button_2_3.setAutoDefault(False)
        self.Button_2_3.setDefault(False)
        self.Button_2_3.setObjectName("Button_2_3")
        self.Button_2_3.clicked.connect (self.buttonclik_Button_2_3)

        self.label_2_3 = QtWidgets.QLabel(self.Q2_3)
        self.label_2_3.setGeometry(QtCore.QRect(10, 10, 50, 20))
        self.label_2_3.setObjectName("label_2_3")
        self.spinBox2_3 = QtWidgets.QSpinBox(self.Q2_3)
        self.spinBox2_3.setGeometry(QtCore.QRect(62, 11, 50, 22))
        self.spinBox2_3.setReadOnly(False)
        self.spinBox2_3.setMinimum(1)
        self.spinBox2_3.setMaximum(15)
        self.spinBox2_3.setObjectName("spinBox2_3")
        #self.spinBox2_3.valueChanged.connect(self.shownumber)

        self.Button_2_4 = QtWidgets.QPushButton(self.Q2)
        self.Button_2_4.setGeometry(QtCore.QRect(20, 190, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_4.sizePolicy().hasHeightForWidth())
        self.Button_2_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_4.setFont(font)
        self.Button_2_4.setAutoDefault(False)
        self.Button_2_4.setDefault(False)
        self.Button_2_4.setObjectName("Button_2_4")
        self.Button_2_4.clicked.connect (self.buttonclik_Button_2_4)

        self.Button_2_5 = QtWidgets.QPushButton(self.Q2)
        self.Button_2_5.setGeometry(QtCore.QRect(20, 230, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_2_5.sizePolicy().hasHeightForWidth())
        self.Button_2_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_2_5.setFont(font)
        self.Button_2_5.setAutoDefault(False)
        self.Button_2_5.setDefault(False)
        self.Button_2_5.setObjectName("Button_2_5")
        self.Button_2_5.clicked.connect (self.buttonclik_Button_2_5)

        self.Q4 = QtWidgets.QGroupBox(self.centralwidget)
        self.Q4.setGeometry(QtCore.QRect(670, 20, 150, 275))
        self.Q4.setObjectName("Q4")
        self.Button_4_1 = QtWidgets.QPushButton(self.Q4)
        self.Button_4_1.setGeometry(QtCore.QRect(20, 130, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_4_1.sizePolicy().hasHeightForWidth())
        self.Button_4_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_4_1.setFont(font)
        self.Button_4_1.setAutoDefault(False)
        self.Button_4_1.setDefault(False)
        self.Button_4_1.setObjectName("Button_4_1")
        self.Button_4_1.clicked.connect (self.buttonclik_Button_4_1)

        self.LoadButton = QtWidgets.QGroupBox(self.centralwidget)
        self.LoadButton.setGeometry(QtCore.QRect(30, 20, 150, 275))
        self.LoadButton.setObjectName("LoadButton")
        self.Button_Folder = QtWidgets.QPushButton(self.LoadButton)
        self.Button_Folder.setGeometry(QtCore.QRect(20, 60, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_Folder.sizePolicy().hasHeightForWidth())
        self.Button_Folder.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_Folder.setFont(font)
        self.Button_Folder.setAutoDefault(False)
        self.Button_Folder.setDefault(False)
        self.Button_Folder.setObjectName("Button_Folder")
        self.Button_Folder.clicked.connect (self.buttonclik_Button_Folder)

        self.Button_LoadL = QtWidgets.QPushButton(self.LoadButton)
        self.Button_LoadL.setGeometry(QtCore.QRect(20, 120, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_LoadL.sizePolicy().hasHeightForWidth())
        self.Button_LoadL.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_LoadL.setFont(font)
        self.Button_LoadL.setAutoDefault(False)
        self.Button_LoadL.setDefault(False)
        self.Button_LoadL.setObjectName("Button_LoadL")
        self.Button_LoadL.clicked.connect (self.buttonclik_Button_LoadL)

        self.Button_LoadR = QtWidgets.QPushButton(self.LoadButton)
        self.Button_LoadR.setGeometry(QtCore.QRect(20, 180, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_LoadR.sizePolicy().hasHeightForWidth())
        self.Button_LoadR.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_LoadR.setFont(font)
        self.Button_LoadR.setAutoDefault(False)
        self.Button_LoadR.setDefault(False)
        self.Button_LoadR.setObjectName("Button_LoadR")
        self.Button_LoadR.clicked.connect (self.buttonclik_Button_LoadR)

        self.Q1 = QtWidgets.QGroupBox(self.centralwidget)
        self.Q1.setGeometry(QtCore.QRect(190, 20, 150, 275))
        self.Q1.setObjectName("Q1")
        self.Button_1_1 = QtWidgets.QPushButton(self.Q1)
        self.Button_1_1.setGeometry(QtCore.QRect(20, 90, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1_1.sizePolicy().hasHeightForWidth())
        self.Button_1_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_1_1.setFont(font)
        self.Button_1_1.setAutoDefault(False)
        self.Button_1_1.setDefault(False)
        self.Button_1_1.setObjectName("Button_1_1")
        self.Button_1_1.clicked.connect (self.buttonclik_Button_1_1)

        self.Button_1_2 = QtWidgets.QPushButton(self.Q1)
        self.Button_1_2.setGeometry(QtCore.QRect(20, 150, 110, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button_1_2.sizePolicy().hasHeightForWidth())
        self.Button_1_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Button_1_2.setFont(font)
        self.Button_1_2.setAutoDefault(False)
        self.Button_1_2.setDefault(False)
        self.Button_1_2.setObjectName("Button_1_2")
        self.Button_1_2.clicked.connect (self.buttonclik_Button_1_2)

        self.dir_path=[] #讀圖的絕對路徑
        self.images=[[]] #存15張圖list
        self.ok=0
        self.corners_list=[] #各角點座標
        self.object_points=[]
        self.image_points=[]
        self.board=0
        self.dist = np.empty((1,5))
        self.rvec = np.empty((3,1))
        self.tvec = np.empty((3,1))
        self.origin_size=(2048,2048)
        self.ret=np.empty((3, 3))
        self.mtx=np.empty((3, 3))
        self.file_path_L=''
        self.file_path_R=''
        self.ch=[[]] #讀文字座標
        self.text_list=[]
        self.cou={}

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def buttonclik_Button_Folder(self):#ok
        #解決絕對路徑中檔名有中文的問題
        def cv_imread(file_path):
            cv_img=cv.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
            return cv_img
        #讀檔問題
        root= tkinter.Tk()
        root.withdraw()
        file_path=tkinter.filedialog.askdirectory()
        file_end=".bmp"
        self.dir_path=[os.path.join(file_path,_) for _ in os.listdir(file_path) if _.endswith(file_end)]
        self.images=[[]]*len(self.dir_path)
        for i in range(len(self.dir_path)) :
        #讀檔路徑
            self.dir_path[i]=Path(self.dir_path[i])
            self.dir_path[i]=self.dir_path[i].__str__()
            #print(self.dir_path[i])
        #存入list
            self.images[i]=cv_imread(self.dir_path[i])#print(dir_path[i])

    def buttonclik_Button_LoadL(self):#ok
        root = tkinter.Tk()
        root.withdraw()
        self.file_path_L =filedialog.askopenfilename(parent=root, title='選擇檔案', filetypes=(("選擇檔案","*.PNG"),("all files","*.*")))

    def buttonclik_Button_LoadR(self):#ok
        root = tkinter.Tk()
        root.withdraw()
        self.file_path_R =filedialog.askopenfilename(parent=root, title='選擇檔案', filetypes=(("選擇檔案","*.PNG"),("all files","*.*")))

    def buttonclik_Button_1_1(self):#ok
        os.chdir(r"C:\Users\USER\Desktop\轉雙輔申請資料\Portfolio\影像處理、電腦視覺與深度學習概論(python)\imageprocessing\Hw2_F64101032_黃薇庭_V3")
        img1=cv.imread('img1.jpg')
        img1_gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(img1_gray, 127, 255, cv.THRESH_BINARY)
        contours, hierarchy1 = cv.findContours(binary, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(img1,contours,-1,(0,0,225),3) #contours=list存要畫線的(x,y)座標 #print (contours)
        cv.imshow("img1.jpg",img1)
    
        img2=cv.imread('img2.jpg')
        img2_gray=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(img2_gray, 127, 255, cv.THRESH_BINARY)
        contours, hierarchy2 = cv.findContours(binary, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(img2,contours,-1,(0,0,225),3)
        cv.imshow("img2.jpg",img2)
        cv.waitKey(0)
    
    def buttonclik_Button_1_2(self):#ok
        os.chdir(r"C:\Users\USER\Desktop\轉雙輔申請資料\Portfolio\影像處理、電腦視覺與深度學習概論(python)\imageprocessing\Hw2_F64101032_黃薇庭_V3")
        img1=cv.imread('img1.jpg')
        img1_gray=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(img1_gray, 127, 255, cv.THRESH_BINARY)
        contours, hierarchy1 = cv.findContours(binary, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(img1,contours,-1,(0,0,225),3) #contours=list存要畫線的(x,y)座標
        count1=np.array(hierarchy1)
        sum1=0
        for i in range(count1.shape[1]):
            if count1[0][i][2]!=-1:
                sum1+=1
        print("There are "+ str(sum1) + " rings in img1.jpg")
        img2=cv.imread('img2.jpg')
        img2_gray=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(img2_gray, 127, 255, cv.THRESH_BINARY)
        contours, hierarchy2 = cv.findContours(binary, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(img2,contours,-1,(0,0,225),3)
        count2=np.array(hierarchy2)
        sum2=0
        for i in range(count2.shape[1]):
            if count2[0][i][2]!=-1:
                sum2+=1
        print("There are "+ str(sum2) + " rings in img2.jpg")

    def buttonclik_Button_2_1(self):#ok
        for i in range (len(self.dir_path)):
            self.ok,self.corners_list=cv.findChessboardCorners(self.images[i],patternSize=(11,8))
            cv.drawChessboardCorners(self.images[i],patternSize=(11,8), corners=self.corners_list ,patternWasFound=self.ok )
            #show
            cv.namedWindow("Corner Detection ", cv.WINDOW_NORMAL) 
            cv.imshow("Corner Detection ",self.images[i])
            cv.waitKey(500)
        cv.destroyAllWindows()

    def buttonclik_Button_2_2(self):#ok
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((11 * 8, 3), np.float32)
        #objp = np.zeros((11 * 8, 3), np.float32)
        objp[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
        # Arrays to store object points and image points from all the images.
        # Select any index to grab an image from the list
        #解決絕對路徑中檔名有中文的問題
        def cv_imread(file_path):
            cv_img=cv.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
            return cv_img
        for i in range(len(self.dir_path)):
            # Read in the image
            image = cv_imread(self.dir_path[i]).astype(np.uint8)
            # Convert to grayscale
            # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            # Find the chessboard corners
            self.ok,corners=cv.findChessboardCorners(image,patternSize=(11,8))
            if self.ok == 1:
                self.object_points.append(objp)
                # corners2 = cv.cornerSubPix(gray,self.corners_list,(11,11),(-1,-1), criteria) #cornerSubPix圖片必須單通道
                #print(self.object_points)
                self.image_points.append(corners)
#
        # gray.shape[::-1] = (2048, 2048)
        self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv.calibrateCamera(self.object_points, self.image_points, self.origin_size, None, None)
        print("Intrinsic:")
        print(self.mtx)

    #def shownumber(self):
        #self.label_2_3.setText(str(self.spinBox2_3.value()))#可以用來顯示讀到spinbox的值

    def buttonclik_Button_2_3(self):#ok
       # print(self.dir_path[0])
        #解決絕對路徑中檔名有中文的問題
        R = cv.Rodrigues(self.rvecs[self.spinBox2_3.value()-1])
        ext = np.hstack((R[0], self.tvecs[self.spinBox2_3.value()-1]))  
        print("extrinsic matrix:")
        print(ext)

    def buttonclik_Button_2_4(self):#ok
        print("Distortion Matrix :")
        print(self.dist)

    def buttonclik_Button_2_5(self):
        for i in range (len(self.dir_path)):
            img=cv.cvtColor(self.images[i],cv.COLOR_BGR2GRAY)
            img_new = cv.undistort(self.images[i],self.mtx,self.dist,None,self.mtx)
            '''
            y_shift = 60    #experiment with
            x_shift = 70    #experiment with    
            imageShape = img.shape  #image.size
            print(imageShape)
            imageSize = (int(imageShape[0])+2*y_shift, int(imageShape[1])+2*x_shift)
            print(imageSize)
      # create a new camera matrix with the principal point offest according to the offset above
            newCameraMatrix, validPixROI = cv.getOptimalNewCameraMatrix(self.mtx, self.dist, imageSize,1)
      #newCameraMatrix = cv2.getDefaultNewCameraMatrix(cameraMatrix, imageSize, True) # imageSize, True
      # create undistortion maps
            R = np.array([[1,0,0],[0,1,0],[0,0,1]])
            map1, map2 = cv.initUndistortRectifyMap(self.mtx, self.dist, R, newCameraMatrix, imageSize,cv.CV_16SC2)
      # remap
            img_new = cv.remap(img, map1, map2, cv.INTER_LINEAR)
            '''
      #save output image as file with "FIX" appened to name - only works with .jpg files at the moment
            plt.subplot(1,2,1)
            plt.title("Distorted image")
            plt.imshow(img)
            plt.axis('off')

            plt.subplot(1,2,2)
            plt.title("Undistorted image")
            plt.imshow(img_new)
            plt.axis('off')
            plt.show()
            cv.waitKey(800)
            plt.close()
    def buttonclik_Button_3_1(self):
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((11 * 8, 3), np.float32)
        objp[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
        # Arrays to store object points and image points from all the images.
        # Select any index to grab an image from the list
        #解決絕對路徑中檔名有中文的問題
        def cv_imread(file_path):
            cv_img=cv.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
            return cv_img
        for i in range(len(self.dir_path)):
            # Read in the image
            image = cv_imread(self.dir_path[i])
            # Convert to grayscale
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            # Find the chessboard corners
            self.ok,self.corners_list=cv.findChessboardCorners(gray,patternSize=(11,8))
            if self.ok == 1:
                self.object_points.append(objp)
                corners2 = cv.cornerSubPix(gray,self.corners_list,(7,7),(-1,-1), criteria) #cornerSubPix圖片必須單通道
                #print(self.object_points)
                self.image_points.append(corners2)
        # gray.shape[::-1] = (2048, 2048)
        self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv.calibrateCamera(self.object_points, self.image_points, self.origin_size, None, None)

        #讀輸入的路徑
        fs = cv.FileStorage('alphabet_lib_onboard.txt', cv.FILE_STORAGE_READ)
        for j in range(len(self.lineEdit_3.text())):
            ch = fs.getNode(self.lineEdit_3.text()[j]).mat() 
            k=0
            for l in ch:
                self.text_list.append(l[0])
                self.text_list.append(l[1])
                k+=1
            self.cou[j]=k

            # axis=self.text_list.append(ch)
            # print(self.text_list[j])
            #  #字母點list
            # axis=np.append(self.text_list[j],self.text_list[j+1])
            # print(axis)
            # print("?")

        #axis= np.float32([[2, 2, 0] ,[2, 0, 0],[2, 0, 0],[1, 1, 0],[ 1, 1, 0], [0, 0, 0], [0, 0, 0],[0, 2, 0],[ 2, 0, 0], [2, 2, 0], [2, 2, 0], [0, 2, 0], [0, 2, 0], [0, 0, 0], [0, 0, 0],[2, 0, 0],[2, 0, 0],[2, 2, 0],[ 2, 2, 0], [0, 2, 0],[ 0, 2, 0], [0, 1, 0], [0, 1, 0],[2, 1, 0], [1, 1, 0], [0, 0, 0 ] ,[ 2, 0, 0],[ 2, 2, 0],[ 2, 2, 0],[ 1, 2, 0],[ 1, 2, 0], [0, 1, 0], [0, 1, 0],[1, 0, 0],[ 1, 0, 0], [2, 0, 0 ]]).reshape(-1, 3)
        # project 3D points to image plane
        ori_list=np.array([[7,5,0],[4,5,0],[1,5,0],[7,2,0],[4,2,0],[1,2,0]])
        def draw(image, imgpts):
            vector = np.vectorize(np.int_)
            x = vector(imgpts)
            '''
            for i in range(len(imgpts)-1):
                image = cv.line(image, x[i][0], x[i+1][0], (0, 0, 255), 5) 
            '''
            sum=0
            for i in range (len(self.lineEdit_3.text())):
                for j in range(2*self.cou[i]-1):
                    a=np.array(x[sum][0]-ori_imgpts[i][0],dtype=int)
                    b=np.array(x[sum+1][0]-ori_imgpts[i][0],dtype=int)
                    image = cv.line(image,tuple(a),tuple(b), (0, 0, 255), 5) 
                    sum+=1
            return image

        for i in range(len(self.dir_path)):
            #image = cv_imread(self.dir_path[i])
            imgpts, jac = cv.projectPoints(np.array(self.text_list).astype(np.float32), self.rvecs[i], self.tvecs[i],self.mtx, self.dist)
            ori_imgpts, jac = cv.projectPoints(np.array(ori_list).astype(np.float32), self.rvecs[i], self.tvecs[i],self.mtx, self.dist)
            #print (ori_imgpts)
            image = self.images[i].copy()

            image = draw(image, imgpts)
            cv.imwrite('%s_v.jpg' % i, image)
            image = cv.resize(image, (1024, 1024), interpolation=cv.INTER_AREA)
            cv.namedWindow('img')
            cv.imshow('img', image)
            cv.waitKey(1000)


    def buttonclik_Button_3_2(self):
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
        objp = np.zeros((11 * 8, 3), np.float32)
        objp[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
        # Arrays to store object points and image points from all the images.
        # Select any index to grab an image from the list
        #解決絕對路徑中檔名有中文的問題
        def cv_imread(file_path):
            cv_img=cv.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
            return cv_img
        for i in range(len(self.dir_path)):
            # Read in the image
            image = cv_imread(self.dir_path[i])
            # Convert to grayscale
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            # Find the chessboard corners
            self.ok,self.corners_list=cv.findChessboardCorners(gray,patternSize=(11,8))
            if self.ok == 1:
                self.object_points.append(objp)
                corners2 = cv.cornerSubPix(gray,self.corners_list,(7,7),(-1,-1), criteria) #cornerSubPix圖片必須單通道
                #print(self.object_points)
                self.image_points.append(corners2)
        # gray.shape[::-1] = (2048, 2048)
        self.ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv.calibrateCamera(self.object_points, self.image_points, self.origin_size, None, None)

        #讀輸入的路徑
        fs = cv.FileStorage('alphabet_lib_vertical.txt', cv.FILE_STORAGE_READ)
        for j in range(len(self.lineEdit_3.text())):
            ch = fs.getNode(self.lineEdit_3.text()[j]).mat() 
            k=0
            for l in ch:
                self.text_list.append(l[0])
                self.text_list.append(l[1])
                k+=1
            self.cou[j]=k

            # axis=self.text_list.append(ch)
            # print(self.text_list[j])
            #  #字母點list
            # axis=np.append(self.text_list[j],self.text_list[j+1])
            # print(axis)
            # print("?")

        #axis= np.float32([[2, 2, 0] ,[2, 0, 0],[2, 0, 0],[1, 1, 0],[ 1, 1, 0], [0, 0, 0], [0, 0, 0],[0, 2, 0],[ 2, 0, 0], [2, 2, 0], [2, 2, 0], [0, 2, 0], [0, 2, 0], [0, 0, 0], [0, 0, 0],[2, 0, 0],[2, 0, 0],[2, 2, 0],[ 2, 2, 0], [0, 2, 0],[ 0, 2, 0], [0, 1, 0], [0, 1, 0],[2, 1, 0], [1, 1, 0], [0, 0, 0 ] ,[ 2, 0, 0],[ 2, 2, 0],[ 2, 2, 0],[ 1, 2, 0],[ 1, 2, 0], [0, 1, 0], [0, 1, 0],[1, 0, 0],[ 1, 0, 0], [2, 0, 0 ]]).reshape(-1, 3)
        # project 3D points to image plane
        ori_list=np.array([[7,5,0],[4,5,0],[1,5,0],[7,2,0],[4,2,0],[1,2,0]])
        def draw(image, imgpts):
            vector = np.vectorize(np.int_)
            x = vector(imgpts)
            '''
            for i in range(len(imgpts)-1):
                image = cv.line(image, x[i][0], x[i+1][0], (0, 0, 255), 5) 
            '''
            sum=0
            for i in range (len(self.lineEdit_3.text())):
                for j in range(2*self.cou[i]-1):
                    a=np.array(x[sum][0]-ori_imgpts[i][0],dtype=int)
                    b=np.array(x[sum+1][0]-ori_imgpts[i][0],dtype=int)
                    image = cv.line(image,tuple(a),tuple(b), (0, 0, 255), 5) 
                    sum+=1
            return image

        for i in range(len(self.dir_path)):
            #image = cv_imread(self.dir_path[i])
            imgpts, jac = cv.projectPoints(np.array(self.text_list).astype(np.float32), self.rvecs[i], self.tvecs[i],self.mtx, self.dist)
            ori_imgpts, jac = cv.projectPoints(np.array(ori_list).astype(np.float32), self.rvecs[i], self.tvecs[i],self.mtx, self.dist)
            #print (ori_imgpts)
            image = self.images[i].copy()

            image = draw(image, imgpts)
            cv.imwrite('%s_v.jpg' % i, image)
            image = cv.resize(image, (1024, 1024), interpolation=cv.INTER_AREA)
            cv.namedWindow('img')
            cv.imshow('img', image)
            cv.waitKey(1000)

    def buttonclik_Button_4_1(self):#邊點位置偏
        #解決絕對路徑中檔名有中文的問題
        def cv_imread(file_path):
            cv_img=cv.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
            return cv_img
        imgL=cv_imread(self.file_path_L)
        imgR=cv_imread(self.file_path_R)
        imgL_gray=cv.cvtColor(imgL,cv.COLOR_BGR2GRAY)
        imgR_gray=cv.cvtColor(imgR,cv.COLOR_BGR2GRAY)
        stereo = cv.StereoBM_create(numDisparities=256, blockSize=25)
        disparity = stereo.compute(imgL_gray, imgR_gray).astype(np.float32) / 16.0
        # disparity = cv.resize(disparity, (255, 255), interpolation=cv.INTER_AREA)
        focal_length = 4019.284
        baseline = 342.789
        Cx = 279.184
        cv.namedWindow("Disparity",0)
        cv.resizeWindow("Disparity",(255,255))
        cv.imshow('Disparity', disparity) 

        # mouse callback function
        cv.namedWindow('imgL',cv.WINDOW_NORMAL)
        cv.resizeWindow('imgL',700,700)
        cv.moveWindow("imgL",700,0)
        cv.namedWindow('imgR',cv.WINDOW_NORMAL)
        cv.resizeWindow('imgR',700,700)
        cv.moveWindow("imgR",700,0)
        def draw_circle(event, x, y, flags, param):
            if event == cv.EVENT_LBUTTONDOWN:
                print(x,y)
                if disparity[y][x]>0:
                    print (disparity[y][x])
                    imgR_copy=imgR.copy()
                    # imgR_copy=cv.resize(imgR_copy,(255,255))
                    imgR_copy=cv.circle(imgR_copy,(x,y),2,(0, 255,0),thickness=30)
                    cv.imshow('imgR', imgR_copy)
                else:
                    imgR_copy=imgR.copy()
                    # imgR_copy=cv.resize(imgR_copy,(255,255))
                    cv.imshow('imgR', imgR_copy)

        while(1):
            cv.setMouseCallback('imgL', draw_circle)
            # imgL_copy=cv.resize(imgL,(255,255))
            cv.imshow('imgL', imgL)
            if cv.waitKey(20) & 0xFF == 13:
                break

        cv.waitKey(0)
        cv.destroyAllWindows()
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hw2"))
        self.Q3.setTitle(_translate("MainWindow", "3. Augmented Reality"))
        self.Button_3_1.setText(_translate("MainWindow", "3.1 Sow Words on Board"))
        self.Button_3_2.setText(_translate("MainWindow", "3.2 Sow Words Vertically"))
        self.lineEdit_3.setText(_translate("MainWindow", "1"))
        self.Q2.setTitle(_translate("MainWindow", "2. Calibration"))
        self.Button_2_1.setText(_translate("MainWindow", "2.1 Find Corners "))
        self.Button_2_2.setText(_translate("MainWindow", "2.2 Find Intrinsic"))
        self.Q2_3.setTitle(_translate("MainWindow", "2.3"))
        self.Button_2_3.setText(_translate("MainWindow", "2.3 Find Extrinsic"))
        self.label_2_3.setText(_translate("MainWindow", "Select image:"))
        self.Button_2_4.setText(_translate("MainWindow", "2.4 Find Distortion"))
        self.Button_2_5.setText(_translate("MainWindow", "2.5 Show Result"))
        self.Q4.setTitle(_translate("MainWindow", "4. Stereo Disparity Map "))
        self.Button_4_1.setText(_translate("MainWindow", "4.1 Stereo Disparity Map"))
        self.LoadButton.setTitle(_translate("MainWindow", "Load Data"))
        self.Button_Folder.setText(_translate("MainWindow", "Load Folder"))
        self.Button_LoadL.setText(_translate("MainWindow", "Load Image_L"))
        self.Button_LoadR.setText(_translate("MainWindow", "Load Image_R"))
        self.Q1.setTitle(_translate("MainWindow", "1. Find contour"))
        self.Button_1_1.setText(_translate("MainWindow", "1.1 Draw Contour"))
        self.Button_1_2.setText(_translate("MainWindow", "1.2 Count Rings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
