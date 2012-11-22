#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
import shutil
import json

structArr = {
    'people': {
      'member': [
        {'id':'name', 'tip':'Guang Yang'},
        {'id':'role', 'tip':'phd OR faculty'},
        {'id':'homepage', 'tip':'http://itcs.tsinghua.edu.cn/guangyang/'},
        {'id':'interest', 'tip':'Cryptography, Derandomization'},
        {'id':'details', 'tip':'blah blah this may include HTML links and tags'},
        {'id':'photo', 'tip':'image/guangyang.jpg'},
        ],
      'former_member': [
        {'id':'name', 'tip':'Wei Yu'},
        {'id':'role', 'tip':'phd OR faculty'},
        {'id':'current_affiliation', 'tip':'CTIC, Aarhus University'},
        {'id':'current_homepage', 'tip':'http://pure.au.dk/portal/en/persons/id(f644ac9a-1af0-4ebc-863c-d9e909fbae5f).html'},
        {'id':'interest', 'tip':'Joking'},
        {'id':'details', 'tip':'blah blah this may include HTML links and tags'},
        {'id':'photo', 'tip':'image/weiyu.jpg'},
        ],
      },
    'announcements': {
      'announcement': [
        {'id':'title', 'tip':'Congratulations to Guang Yang for winning the new scientist Tsinghua award!'},
        {'id':'date', 'tip':'January 1, 2013'},
        {'id':'details', 'tip':'blah blah this may include HTML links and tags'},
        {'id':'importance', 'tip':'1~9'},
        ],
      },
    'seminars': {
      'seminar': [
        {'id':'title', 'tip':'Representations etc'},
        {'id':'date', 'tip':'Tuesday January 1, 2013' },
        {'id':'time', 'tip':'12pm'},
        {'id':'venue', 'tip':'1-222 FIT Building'},
        {'id':'abstract', 'tip':'blabla'},
        {'id':'extra', 'tip':'blabla'},
        {'id':'urls', 'tip':'http://link1.com,http://link2.com'},
        {'id':'speaker', 'tip':'Bangsheng Tang'},
        {'id':'speaker_homepage', 'tip':'http://link.com'},
        {'id':'speaker_bio', 'tip':'blabla'},
        ],
      },
    'projects': {
      'project': [
        {'id':'title', 'tip':'Halloween'},
        {'id':'details_html', 'tip':'blah blah this may include HTML links and tags'},
        ],
      },
    'papers': {
      'paper': [
        {'id':'category', 'tip':'Derandomization'},
        {'id':'title', 'tip':'blabla'},
        {'id':'author', 'tip':'Eric Allende[http://link1.com],Shiteng Chen[http://link2.com]'},
        {'id':'date', 'tip':'January 1, 2013'},
        {'id':'venue', 'tip':'Conference or Journal name'},
        {'id':'paper_url', 'tip':'http://link.com'},
        {'id':'fullpaper_url', 'tip':'http://link.com'},
        {'id':'abstract', 'tip':'blabla'},
        {'id':'bibtex', 'tip':'blabla'},
        ],
      'video': [
        {'id':'title', 'tip':'blabla'},
        {'id':'date', 'tip':'January 1, 2013'},
        {'id':'url', 'tip':'http://link.com'},
        {'id':'description', 'tip':'blabla'},
        ],
      'slide_files': [
        {'id':'title', 'tip':'blabla'},
        {'id':'date', 'tip':'January 1, 2013'},
        {'id':'url', 'tip':'http://link.com'},
        {'id':'description', 'tip':'blabla'},
        ],
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

    saveFileButton = QtGui.QPushButton("Save All")
    saveFileButton.clicked.connect(self._slotSaveFileClicked)
    topLayout.addWidget(saveFileButton, 1, 0, 1, 1)

    addButton = QtGui.QPushButton("Add")
    delButton = QtGui.QPushButton("Delete")
    addButton.clicked.connect(self._slotAddClicked)
    delButton.clicked.connect(self._slotDelClicked)

    hbox = QtGui.QHBoxLayout()
    hbox.addWidget(addButton)
    hbox.addWidget(delButton)
    hbox.addStretch(1)
    topLayout.addLayout(hbox, 1, 2, 1, 1)
    
    upButton = QtGui.QPushButton("Up")
    downButton = QtGui.QPushButton("Down")
    topButton = QtGui.QPushButton("Top")
    bottomButton = QtGui.QPushButton("Bottom")
    upButton.clicked.connect(self._slotUpClicked)
    downButton.clicked.connect(self._slotDownClicked)
    topButton.clicked.connect(self._slotTopClicked)
    bottomButton.clicked.connect(self._slotBottomClicked)
    
    saveButton = QtGui.QPushButton("Save Item")
    saveButton.clicked.connect(self._slotSaveClicked)
    
    sbox = QtGui.QHBoxLayout()
    sbox.addWidget(upButton)
    sbox.addWidget(downButton)
    sbox.addWidget(topButton)
    sbox.addWidget(bottomButton)
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
      labelItem = QtGui.QLabel(t['id'])
      self.listDetail.addWidget(labelItem, index, 0)
      text = ''
      if t['id'] in data.keys():
        text = data[t['id']]
      textItem = QtGui.QTextEdit(text)
      textItem.setToolTip("<font size='10'>%s</font>" % t['tip'])
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
      text = '%s: %s' % (self.template[0]['id'], t[self.template[0]['id']])
      self.listC.addItem(text)

    self.clearPage()
    self.listC.setCurrentRow(0)
    if self.listC.count() > 0:
      self._itemCClicked(self.listC.item(0))


  def _itemCClicked(self, item):
    index = self.listC.currentRow()
    self.initPage(self.dataArr[self.keyA][self.keyB][index])


  def _slotAddClicked(self):
    item = {}
    for t in self.template:
      item[t['id']] = ''
    self.dataArr[self.keyA][self.keyB].insert(0, item)
    
    text = '%s: %s' % (self.template[0]['id'], item[self.template[0]['id']])
    lvi = QtGui.QListWidgetItem(text)
    self.listC.insertItem(0, lvi)
    
    self.listC.setCurrentRow(0)
    if self.listC.count() > 0:
      self._itemCClicked(self.listC.item(0))


  def _slotDelClicked(self):
    index = self.listC.currentRow()
    self.listC.takeItem(index)
    del self.dataArr[self.keyA][self.keyB][index]


  def _slotUpClicked(self):
    index = self.listC.currentRow()
    self.moveCurrentItem(index - 1)


  def _slotDownClicked(self):
    index = self.listC.currentRow()
    self.moveCurrentItem(index + 1)


  def _slotTopClicked(self):
    self.moveCurrentItem(0)


  def _slotBottomClicked(self):
    index = self.listC.count()
    self.moveCurrentItem(index - 1)


  def moveCurrentItem(self, tarIndex):
    if tarIndex < 0 or tarIndex >= self.listC.count():
      return
    index = self.listC.currentRow()
    if index < 0 or index == tarIndex:
      return 
    item = self.dataArr[self.keyA][self.keyB][index]
    del self.dataArr[self.keyA][self.keyB][index]
    self.listC.takeItem(index)
    self.dataArr[self.keyA][self.keyB].insert(tarIndex, item)
    text = '%s: %s' % (self.template[0]['id'], item[self.template[0]['id']])
    lvi = QtGui.QListWidgetItem(text)
    self.listC.insertItem(tarIndex, lvi)
    
    self.clearPage()
    self.listC.setCurrentRow(tarIndex)
    self._itemCClicked(self.listC.item(tarIndex))


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
      data[t['id']] = text
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
