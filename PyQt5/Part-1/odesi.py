# -*- coding: utf-8 -*-

import sys

#PYQT5 PyQt4’s QtGui module has been split into PyQt5’s QtGui, QtPrintSupport and QtWidgets modules

from PyQt5 import QtWidgets
#PYQT5 QAction, QMainWindow, QApplication, QTextEdit, QFileDialog, QDialog

from PyQt5 import QtPrintSupport
#PYQT5 QPrintPreviewDialog, QPrintDialog

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt


class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.filename = ""

        self.initUI()

    def initToolbar(self):

        self.newAction = QtWidgets.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon("icons/save_color.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.printAction = QtWidgets.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
        self.printAction.setStatusTip("Print document")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.printHandler)

        self.cutAction = QtWidgets.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
        self.cutAction.setStatusTip("Delete and copy text to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        self.copyAction = QtWidgets.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
        self.copyAction.setStatusTip("Copy text to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        self.pasteAction = QtWidgets.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
        self.pasteAction.setStatusTip("Paste text from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        self.undoAction = QtWidgets.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        self.redoAction = QtWidgets.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)


        self.serverAction = QtWidgets.QAction(QtGui.QIcon("icons/server_black.png"),"Connect to server",self)
        self.serverAction.setStatusTip("Server Connection")
        self.serverAction.setShortcut("Ctrl+I")
        #self.serverAction.triggered.connect(self.text.redo)

        self.helpAction = QtWidgets.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.helpAction.setShortcut("Ctrl+T")
        self.helpAction.setStatusTip("help.")
        self.helpAction.triggered.connect(self.getHelp)


        self.publish_it_Action = QtWidgets.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.publish_it_Action.setShortcut("Ctrl+T")
        self.publish_it_Action.setStatusTip("help.")
        self.publish_it_Action.triggered.connect(self.publishDataset)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.printAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.cutAction)
        self.toolbar.addAction(self.copyAction)
        self.toolbar.addAction(self.pasteAction)
        self.toolbar.addAction(self.undoAction)
        self.toolbar.addAction(self.redoAction)

        self.toolbar.addSeparator()

        self.toolbar.addAction(self.serverAction)

        # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()

    def initFormatbar(self):

      self.formatbar = self.addToolBar("Format")


    def initMenubar(self):

      menubar = self.menuBar()

      file = menubar.addMenu("File")
      edit = menubar.addMenu("Edit")
      view = menubar.addMenu("View")
      server = menubar.addMenu("Server")
      preferences = menubar.addMenu("Preferences")
      documentation = menubar.addMenu("Documentation")
      helpmenu = menubar.addMenu("Help")

      helpmenu.addAction(self.helpAction)
      server.addAction(self.publish_it_Action)
      file.addAction(self.newAction)
      file.addAction(self.openAction)
      file.addAction(self.saveAction)
      file.addAction(self.printAction)

      edit.addAction(self.undoAction)
      edit.addAction(self.redoAction)
      edit.addAction(self.cutAction)
      edit.addAction(self.copyAction)
      edit.addAction(self.pasteAction)

    def initUI(self):

        self.text = QtWidgets.QTextEdit(self)

        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        # Set the tab stop width to around 33 pixels which is
        # about 8 spaces
        self.text.setTabStopWidth(33)

        self.setCentralWidget(self.text)

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # If the cursor position changes, call the function that displays
        # the line and column number
        self.text.cursorPositionChanged.connect(self.cursorPosition)

        # x and y coordinates on the screen, width, height
        self.setGeometry(100,100,1030,800)

        self.setWindowTitle("Writer")

        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))

    def getHelp(self):
        print('Getting Help action')

    def publishDataset(self):
        print('Publishing the dataset')

    def new(self):

        spawn = Main(self)
        spawn.show()

    def open(self):

        # Get filename and show only .sav *.py *.xml files
        #PYQT5 Returns a tuple in PyQt5, we only need the filename
        #self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',".","(*.xml)")[0]
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '.', "DDI file (*.xml *.sav *.py)")[0]

        if self.filename:
            with open(self.filename,"rt") as file:
                self.text.setText(file.read())

    def save(self):

        # Only open dialog if there is no filename yet
        #PYQT5 Returns a tuple in PyQt5, we only need the filename
        if not self.filename:
          self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]

        if self.filename:

            # Append extension if not there yet
            if not self.filename.endswith(".odesi"):
              self.filename += ".odesi"

            # We just store the contents of the text file along with the
            # format in html, which Qt does in a very nice way for us
            with open(self.filename,"wt") as file:
                file.write(self.text.toHtml())

            self.changesSaved = True

    def printHandler(self):

        # Open printing dialog
        dialog = QtPrintSupport.QPrintDialog()

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.text.document().print_(dialog.printer())


    def cursorPosition(self):

        cursor = self.text.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))


def main():

    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
