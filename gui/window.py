#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
import shutil
import json
import make_html
import check_link

structArr = {
    'home': {
      'counter': [
        {'id':'code', 'tip':'Enter&nbsp;Code&nbsp;Here.', 'size': 20},
        ],
      },
    'people': {
      'counter': [
        {'id':'code', 'tip':'Enter&nbsp;Code&nbsp;Here.', 'size': 20},
        ],
      'member': [
        {'id':'name', 'tip':'Guang&nbsp;Yang', 'size': 1},
        {'id':'type', 'tip':'Faculty&nbsp;OR&nbsp;Graduate&nbsp;OR&nbsp;Undergraduate', 'size': 1},
        {'id':'role', 'tip':'Assistant&nbsp;Professor&nbsp;OR&nbsp;MS&nbsp;Student&nbsp;OR&nbsp;PhD&nbsp;Student', 'size': 1},
        {'id':'homepage', 'tip':'http://itcs.tsinghua.edu.cn/guangyang/', 'size': 2},
        {'id':'interest', 'tip':'Cryptography,&nbsp;Derandomization', 'size': 1},
        {'id':'details', 'tip':'blah&nbsp;blah&nbsp;this&nbsp;may&nbsp;include&nbsp;HTML&nbsp;links&nbsp;and&nbsp;tags', 'size': 8},
        {'id':'photo', 'tip':'image/guangyang.jpg', 'size': -1},
        ],
      'former_member': [
        {'id':'name', 'tip':'Wei&nbsp;Yu', 'size': 1},
        {'id':'role', 'tip':'Faculty&nbsp;OR&nbsp;Graduate&nbsp;OR&nbsp;Undergraduate', 'size': 1},
        {'id':'current_affiliation', 'tip':'CTIC,&nbsp;Aarhus&nbsp;University', 'size': 1},
        {'id':'current_homepage', 'tip':'http://pure.au.dk/portal/en/persons/id(f644ac9a-1af0-4ebc-863c-d9e909fbae5f).html', 'size': 2},
        {'id':'interest', 'tip':'Joking', 'size': 1},
        {'id':'details', 'tip':'blah&nbsp;blah&nbsp;this&nbsp;may&nbsp;include&nbsp;HTML&nbsp;links&nbsp;and&nbsp;tags', 'size': 8},
        {'id':'photo', 'tip':'image/weiyu.jpg', 'size': -1},
        ],
      },
    'announcements': {
      'counter': [
        {'id':'code', 'tip':'Enter&nbsp;Code&nbsp;Here.', 'size': 20},
        ],
      'announcement': [
        {'id':'title', 'tip':'Congratulations&nbsp;to&nbsp;Guang&nbsp;Yang&nbsp;for&nbsp;winning&nbsp;the&nbsp;new&nbsp;scientist&nbsp;Tsinghua&nbsp;award!', 'size': 3},
        {'id':'date', 'tip':'January&nbsp;1,&nbsp;2013', 'size': 1},
        {'id':'details', 'tip':'blah&nbsp;blah&nbsp;this&nbsp;may&nbsp;include&nbsp;HTML&nbsp;links&nbsp;and&nbsp;tags', 'size': 8},
        {'id':'importance', 'tip':'1-Important,&nbsp;0-Not', 'size': 1},
        ],
      },
    'seminars': {
      'counter': [
        {'id':'code', 'tip':'Enter&nbsp;Code&nbsp;Here.', 'size': 20},
        ],
      'seminar': [
        {'id':'title', 'tip':'Representations&nbsp;etc', 'size': 2},
        {'id':'date', 'tip':'Tuesday&nbsp;January&nbsp;1,&nbsp;2013', 'size': 1},
        {'id':'time', 'tip':'12pm', 'size': 1},
        {'id':'venue', 'tip':'1-222&nbsp;FIT&nbsp;Building', 'size': 1},
        {'id':'abstract', 'tip':'blabla', 'size': 4},
        {'id':'extra', 'tip':'blabla', 'size': 4},
        {'id':'urls', 'tip':'http://link1.com,http://link2.com', 'size': 2},
        {'id':'speaker', 'tip':'Bangsheng&nbsp;Tang', 'size': 1},
        {'id':'speaker_homepage', 'tip':'http://link.com', 'size': 1},
        {'id':'speaker_bio', 'tip':'blabla', 'size': 5},
        {'id':'speaker_photo', 'tip':'image/weiyu.jpg', 'size': -1},
        ],
      },
    'projects': {
      'counter': [
        {'id':'code', 'tip':'Enter&nbsp;Code&nbsp;Here.', 'size': 20},
        ],
      'project': [
        {'id':'title', 'tip':'Halloween', 'size': 2},
        {'id':'details_html', 'tip':'blah&nbsp;blah&nbsp;this&nbsp;may&nbsp;include&nbsp;HTML&nbsp;links&nbsp;and&nbsp;tags', 'size': 10},
        ],
      },
    'papers': {
      'counter': [
        {'id':'code', 'tip':'Enter&nbsp;Code&nbsp;Here.', 'size': 20},
        ],
      'paper': [
        {'id':'title', 'tip':'blabla', 'size': 2},
        {'id':'category', 'tip':'Derandomization', 'size': 1},
        {'id':'author', 'tip':'Eric&nbsp;Allende#http://link1.com,&nbsp;Shiteng&nbsp;Chen#http://link2.com', 'size': 3},
        {'id':'date', 'tip':'January&nbsp;1,&nbsp;2013', 'size': 1},
        {'id':'venue', 'tip':'Conference&nbsp;or&nbsp;Journal&nbsp;name', 'size': 1},
        {'id':'paper_url', 'tip':'http://link.com', 'size': 1},
        {'id':'fullpaper_url', 'tip':'http://link.com', 'size': 1},
        {'id':'abstract', 'tip':'blabla', 'size': 6},
        {'id':'bibtex', 'tip':'blabla', 'size': 5},
        ],
      'unrefer': [
        {'id':'title', 'tip':'blabla', 'size': 2},
        {'id':'category', 'tip':'Derandomization', 'size': 1},
        {'id':'author', 'tip':'Eric&nbsp;Allende#http://link1.com,&nbsp;Shiteng&nbsp;Chen#http://link2.com', 'size': 3},
        {'id':'date', 'tip':'January&nbsp;1,&nbsp;2013', 'size': 1},
        {'id':'venue', 'tip':'Conference&nbsp;or&nbsp;Journal&nbsp;name', 'size': 1},
        {'id':'paper_url', 'tip':'http://link.com', 'size': 1},
        {'id':'fullpaper_url', 'tip':'http://link.com', 'size': 1},
        {'id':'abstract', 'tip':'blabla', 'size': 6},
        {'id':'bibtex', 'tip':'blabla', 'size': 5},
        ],
      'video': [
        {'id':'title', 'tip':'blabla', 'size': 2},
        {'id':'date', 'tip':'January&nbsp;1,&nbsp;2013', 'size': 1},
        {'id':'url', 'tip':'http://link.com', 'size': 1},
        {'id':'description', 'tip':'blabla', 'size': 10},
        ],
      'slide': [
        {'id':'title', 'tip':'blabla', 'size': 2},
        {'id':'date', 'tip':'January&nbsp;1,&nbsp;2013', 'size': 1},
        {'id':'url', 'tip':'http://link.com', 'size': 1},
        {'id':'description', 'tip':'blabla', 'size': 10},
        ],
      },
    }

FILE_NAME = 'data.json'
BACKUP_NAME = 'data.json.bak'
IMG_DIR = '../html/img/'


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
    
    # print json.dumps(self.dataArr)


  def saveData(self):
    try:
      shutil.copy2(FILE_NAME, BACKUP_NAME)
    except:
      print 'Skip backup: no old data file detected.'
    with open(FILE_NAME, 'w') as output:
      json.dump(self.dataArr, output)


  def makeHtml(self):
     make_html.gen_html(self.dataArr)
      

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

    saveFileButton = QtGui.QPushButton("Save File")
    saveFileButton.clicked.connect(self._slotSaveFileClicked)
    htmlFileButton = QtGui.QPushButton("Make Html")
    htmlFileButton.clicked.connect(self._slotGenHtmlClicked)
    
    vbox = QtGui.QVBoxLayout()
    vbox.addWidget(saveFileButton)
    vbox.addWidget(htmlFileButton)
    topLayout.addLayout(vbox, 1, 0, 1, 1)

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
      textItem = QtGui.QTextEdit()
      textItem.setPlainText(text)
      if t['size'] > 0:
        textItem.setMaximumHeight(labelItem.sizeHint().height() * t['size'])
        textItem.setToolTip("<a style='font-size: 14px'>%s</a>" % t['tip'])
        self.listDetail.addWidget(textItem, index, 1)
        self.imgPathItem = None
      else:
        textItem.setMaximumHeight(labelItem.sizeHint().height() * 3)
        openButton = QtGui.QPushButton("Open")
        openButton.clicked.connect(self._slotOpenClicked)
        self.listDetail.addWidget(textItem, index, 1)
        self.listDetail.addWidget(openButton, index, 2)
        self.imgPathItem = textItem
      self.dataList.append(textItem)
      index += 1
  

  def _slotOpenClicked(self, item):
    fileName = QtGui.QFileDialog.getOpenFileName(
        self,self.tr("Open Image"), '',
        self.tr("Image Files(*.png *.jpg *.jpeg *.bmp)"))
    if fileName == '':
      return
    fileInfo = QtCore.QFileInfo(fileName)
    base = unicode(fileInfo.baseName())
    ext = unicode(fileInfo.completeSuffix())
    index = 0
    while True:
      tarName = "%s%s/%s%d.%s" % (IMG_DIR, self.keyA, base, index, ext)
      print tarName
      tarInfo = QtCore.QFileInfo(tarName)
      if tarInfo.exists() != True:
        break
      index += 1
    shutil.copy2(fileName, tarName)
    self.imgPathItem.setPlainText(tarName)


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


  def _slotGenHtmlClicked(self):
    self.makeHtml()
        

  def _slotSaveClicked(self):
    data = {}
    index = 0
    for t in self.template:
      textItem = self.dataList[index]
      text = unicode(textItem.toPlainText())
      data[t['id']] = text.strip()
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
