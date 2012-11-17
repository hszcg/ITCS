#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore

structArr = {
    'people': [
      {'id': 'member', 'data': ['name', 'role', 'homepage', 'interest', 'details']},
      {'id': 'former_member', 'data': ['name', 'role', 'current_affiliation', 'current_homepage', 'interest', 'details']},
      {'id': 'colleague', 'data': ['name', 'homepage']},
        ],
    'announcements': [
      {'id': 'announcement', 'data': ['title', 'date', 'details', 'importance']},
      ],
    'seminars': [
      {'id': 'seminar', 'data': ['title', 'date', 'time', 'venue', 'abstract', 'extra', 'urls']},
      ],
    'projects': [
      {'id': 'project', 'data': ['title', 'author', 'abstract', 'details']},
      ],
    'papers': [
      {'id': 'paper', 'data' : ['category', 'title', 'author', 'date', 'venue', 'paper_url', 'fullpaper_url', 'abstract', 'bibtex']},
      {'id': 'video', 'data' : ['title', 'date', 'url', 'description']},
      {'id': 'slide_files', 'data' : ['title', 'date', 'url', 'description']},
      ],
    }


class MainWin(QtGui.QWidget):
  def __init__(self):
    super(MainWin, self).__init__()
    self.initUI()


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
    topLayout.addLayout(self.listDetail, 0, 3, 1, 1)

    addButton = QtGui.QPushButton("Add")
    # editButton = QtGui.QPushButton("Edit")
    delButton = QtGui.QPushButton("Delete")

    addButton.clicked.connect(self._slotAddClicked)
    # self.connect(editbutton, SIGNAL("clicked()"), self._slotEditClicked)
    delButton.clicked.connect(self._slotDelClicked)

    saveButton = QtGui.QPushButton("Save All")
    topLayout.addWidget(saveButton, 1, 0, 1, 1)

    hbox = QtGui.QHBoxLayout()
    hbox.addWidget(addButton)
    #hbox.addWidget(editButton)
    hbox.addWidget(delButton)
    hbox.addStretch(1)
    topLayout.addLayout(hbox, 1, 2, 1, 1)
    
    topLayout.setColumnMinimumWidth(0, 120)
    topLayout.setColumnStretch(3, 1)
    topLayout.setRowMinimumHeight(0, 200)
    self.setLayout(topLayout)
    self.setGeometry(200, 150, 640, 480)
    self.setWindowTitle('Content Editor')
    self.show()


  def _itemAClicked(self, item):
    self.listB.clear()
    self.listC.clear()
    self.subStruct = structArr[str(item.text())]
    for t in self.subStruct:
      self.listB.addItem(t['id'])


  def _itemBClicked(self, item):
    self.listC.clear()
    self.items = filter(lambda x: x['id'] == str(item.text()), self.subStruct)
    for t in self.items[0]['data']:
      self.listC.addItem(t)


  def _itemCClicked(self, item):
    pass
    # TODO


  def _slotAddClicked(self):
    lvi = QtGui.QListWidgetItem('haha %d' % self.listC.count())
    self.listC.insertItem(0, lvi)


  def _slotDelClicked(self):
    self.listC.takeItem(self.listC.currentRow())


def main():
  app = QtGui.QApplication(sys.argv)
  ex = MainWin()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()
