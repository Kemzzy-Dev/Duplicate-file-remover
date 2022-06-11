import os
from PyQt5 import QtWidgets, uic
import qtvscodestyle as qtvsc
import sys 
import hashlib
from tkinter import filedialog
import tkinter as tk



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('duplicate.ui', self)
        self.show()
        self.dir = ''
        
        #All call backs to any function goes here
        self.actionDark_Mode.triggered.connect(self.darkMode)
        self.actionLight_Mode.triggered.connect(self.lightMode)
        self.folderButton.clicked.connect(self.selectFolder)
        self.actionAbout.triggered.connect(self.about_window)
        self.actionHow_to_use.triggered.connect(self.help_window)
        self.scan.clicked.connect(self.scan_window)

    #funtions go here
    def darkMode(self): 
        stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.DARK_VS)
        # stylesheet = load_stylesheet(qtvsc.Theme.LIGHT_VS)
        app.setStyleSheet(stylesheet)

    def lightMode(self):
        # custom_colors = {"editor.foreground": "#a4f0ce"}
        stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.QUIET_LIGHT)
        app.setStyleSheet(stylesheet)

    def selectFolder(self):
        root = tk.Tk()
        root.withdraw()
        self.dir = filedialog.askdirectory()
        if os.path.isdir(self.dir):
            self.labelFolder.setText(self.dir)
        else:
            self.labelFolder.setText('No Folder Selected')

    def remove_duplicates(self, dir):
        unique = []
        self.counter = 0
        for filename in os.listdir(dir):
            filepath = os.path.join(dir, filename)
            if os.path.isfile(filepath):
                filehash = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
                if filehash not in unique: 
                    unique.append(filehash)
                else: 
                    os.remove(filepath)
                    self.counter += 1
        print(self.counter)
    
    def about_window(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('About')
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("""This is a simple graphical interface to delete duplicate files
                        Creator: kemzzy
                        Twitter: @coder_kemzzy
                        version: 1.0
                        """)
        x = msg.exec_()

    def help_window(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle('Help!')
        msg.setText("""                   Help!!!

    1. Click on the select folder button and choose your desired folder for scanning
    2. After selcting the folder, the file path will automatically display itself
    3. Then click on the 'SCAN' button
    4. Click on "OK" to delete the found files
                        OR
    1. Drag and drop the desired folder into the window 
    2. Then continue from number 3

            Thank you for using
                        """)
        x = msg.exec_()
   
    def popup_clicked(self, i):
        self.remove_duplicates(self.dir)

    def scan_window(self):
        if os.path.isdir(self.dir) == True:
            msg = QtWidgets.QMessageBox()
            msg.setText("""
    Duplicate files found!!!

    Delete now?            
            """)
            msg.setWindowTitle('Delete Popup')
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok|QtWidgets.QMessageBox.Cancel)
            msg.setDefaultButton(QtWidgets.QMessageBox.Ok)
            msg.buttonClicked.connect(self.popup_clicked)
            x = msg.exec_()
            # self.window = QtWidgets.QDialog()
            # uic.loadUi('Scanning.ui', self.window))
            # self.remove_duplicates(self.dir)
            # self.window.show())
        elif self.counter == 0:
            msg = QtWidgets.QMessageBox()
            msg.setText("Please select a file before clicking can")
            msg.setWindowTitle('ERROR')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            x = msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #the sytlesheet i'm using for the project
    stylesheet = qtvsc.load_stylesheet(qtvsc.Theme.DARK_VS)
    app.setStyleSheet(stylesheet)
    window = Ui()
    app.exec_()

