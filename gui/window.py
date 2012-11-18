#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
import shutil
import json

structArr = {
    'people': {
      'member': ['name', 'role', 'homepage', 'interest', 'details'],
      'former_member': ['name', 'role', 'current_affiliation', 'current_homepage', 'interest', 'details'],
      'colleague': ['name', 'homepage'],
      },
    'announcements': {
      'announcement': ['title', 'date', 'details', 'importance'],
      },
    'seminars': {
      'seminar': ['title', 'date', 'time', 'venue', 'abstract', 'extra', 'urls'],
      },
    'projects': {
      'project': ['title', 'author', 'abstract', 'details'],
      },
    'papers': {
      'paper': ['category', 'title', 'author', 'date', 'venue', 'paper_url', 'fullpaper_url', 'abstract', 'bibtex'],
      'video': ['title', 'date', 'url', 'description'],
      'slide_files': ['title', 'date', 'url', 'description'],
      },
    }

FILE_NAME = 'data.json'
BACKUP_NAME = 'data.json.bak'


class MainWin(QtGui.QWidget):
  def __init__(self):
    super(MainWin, self).__init__()
    self.dataArr = {}
    self.loadData()
    self.initUI()


  def loadData(self):
    try:
      isLoad = 1
      with open(FILE_NAME) as f:
        self.dataArr = json.load(f)
    except:
      isLoad = 0

    if isLoad == 0:
      for t in structArr.keys():
        temp = {}
        for tt in structArr[t].keys():
          temp[tt] = []
        self.dataArr[t] = temp
    
    print json.dumps(self.dataArr)


  def saveData(self):
    shutil.copy2(FILE_NAME, BACKUP_NAME)
    with open(FILE_NAME, 'w') as output:
      json.dump(self.dataArr, output)


  def initUI(self):
    topLayout = QtGui.QGridLayout(self)

    self.listA = QtGui.QListWidget(self)
    for t in structArr.keys():
      self.listA.addItem(t)
    self.listA.itemClicked.connect(self._itemAClicked)
    topLayout.addWidget(self.listA, 0, 0, 1, 1)

    self.listB = QtGui.QListWidget(self)
    self.listB.itemClicked.connect(self._itemBClicked)
    topLayout.addWidget(self.listB, 0, 1, 1, 1)

    self.listC = QtGui.QListWidget(self)
    self.listC.itemClicked.connect(self._itemCClicked)
    topLayout.addWidget(self.listC, 0, 2, 1, 1)

    self.listDetail = QtGui.QGridLayout()
    self.listDetail.setSpacing(10)
    topLayout.addLayout(self.listDetail, 0, 3, 1, 1)

    addButton = QtGui.QPushButton("Add")
    # editButton = QtGui.QPushButton("Edit")
    delButton = QtGui.QPushButton("Delete")

    addButton.clicked.connect(self._slotAddClicked)
    # self.connect(editbutton, SIGNAL("clicked()"), self._slotEditClicked)
    delButton.clicked.connect(self._slotDelClicked)

    saveFileButton = QtGui.QPushButton("Save All")
    saveFileButton.clicked.connect(self._slotSaveFileClicked)
    topLayout.addWidget(saveFileButton, 1, 0, 1, 1)

    hbox = QtGui.QHBoxLayout()
    hbox.addWidget(addButton)
    #hbox.addWidget(editButton)
    hbox.addWidget(delButton)
    hbox.addStretch(1)
    topLayout.addLayout(hbox, 1, 2, 1, 1)
    
    saveButton = QtGui.QPushButton("Save Item")
    saveButton.clicked.connect(self._slotSaveClicked)
    sbox = QtGui.QHBoxLayout()
    sbox.addStretch(1)
    sbox.addWidget(saveButton)
    topLayout.addLayout(sbox, 1, 3, 1, 1)
    
    topLayout.setColumnMinimumWidth(0, 120)
    topLayout.setColumnMinimumWidth(1, 120)
    topLayout.setColumnMinimumWidth(2, 200)
    topLayout.setColumnMinimumWidth(3, 400)
    topLayout.setColumnStretch(3, 100)
    topLayout.setRowMinimumHeight(0, 200)
    self.setLayout(topLayout)
    self.setGeometry(200, 150, 640, 480)
    self.setWindowTitle('Content Editor')
    self.show()


  def clearPage(self):
    self.dataList = []
    for i in range(self.listDetail.count()):
      self.listDetail.itemAt(i).widget().close()


  def initPage(self, data):
    self.clearPage()
    index = 0
    for t in self.template:
      self.listDetail.addWidget(QtGui.QLabel(t), index, 0)
      text = ''
      if t in data.keys():
        text = data[t]
      textItem = QtGui.QTextEdit(text)
      self.dataList.append(textItem)
      self.listDetail.addWidget(textItem, index, 1)
      index += 1
    

  def _itemAClicked(self, item):
    self.listB.clear()
    self.listC.clear()
    self.keyA = str(item.text())

    self.subStruct = structArr[self.keyA]
    for t in self.subStruct.keys():
      self.listB.addItem(t)

    self.listB.setCurrentRow(0)
    if self.listB.count() > 0:
      self._itemBClicked(self.listB.item(0))


  def _itemBClicked(self, item):
    self.listC.clear()
    self.keyB = str(item.text())
    self.template = self.subStruct[self.keyB]
    for t in self.dataArr[self.keyA][self.keyB]:
      text = '%s: %s' % (self.template[0], t[self.template[0]])
      self.listC.addItem(text)

    self.clearPage()
    self.listC.setCurrentRow(0)
    if self.listC.count() > 0:
      self._itemCClicked(self.listC.item(0))


  def _itemCClicked(self, item):
    index = self.listC.currentRow()
    self.initPage(self.dataArr[self.keyA][self.keyB][index])


  def _slotAddClicked(self):
    lvi = QtGui.QListWidgetItem('NEW %s' % self.listC.count())
    self.listC.insertItem(0, lvi)
    data = {}
    for t in self.template:
      data[t] = ''
    self.dataArr[self.keyA][self.keyB].insert(0, data)
    
    self.listC.setCurrentRow(0)
    if self.listC.count() > 0:
      self._itemCClicked(self.listC.item(0))


  def _slotDelClicked(self):
    index = self.listC.currentRow()
    self.listC.takeItem(index)
    del self.dataArr[self.keyA][self.keyB][index]

  def _slotSaveFileClicked(self):
    self.saveData()
    reply = QtGui.QMessageBox.information(
        self, 'Message',
        "Data saved to %s\nBackup data saved to %s" % (FILE_NAME, BACKUP_NAME),
        QtGui.QMessageBox.Yes)


  def _slotSaveClicked(self):
    data = {}
    index = 0
    for t in self.template:
      textItem = self.dataList[index]
      text = str(textItem.toPlainText())
      data[t] = text
      index += 1

    index = self.listC.currentRow()
    if index >= 0:
      self.dataArr[self.keyA][self.keyB][index] = data
    self._itemBClicked(self.listB.currentItem())


def main():
  app = QtGui.QApplication(sys.argv)
  ex = MainWin()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
