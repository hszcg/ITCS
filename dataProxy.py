from lxml import etree
from lxml import objectify
from dataStruct import *

DATA_SRC = 'data.xml'
HEAD_SRC = 'header.src'
FOOT_SRC = 'footer.src'

OUT_FILE = './output/index.html'


def dataReader():
  # open the xml file for reading:
  file = open(DATA_SRC, 'r')
  data = file.read()
  file.close()

  obj = objectify.fromstring(data)

  res = FullData()

  # people
  for arr in obj.people:
    for t in arr.person:
      res.peo_list.append(Person(t))

  # announce
  for arr in obj.announce:
    for t in arr.item:
      res.ann_list.append(Announce(t))

  # seminar
  for arr in obj.seminar:
    for t in arr.item:
      res.sem_list.append(Seminar(t))

  # project
  for arr in obj.project:
    for t in arr.item:
      res.pro_list.append(Project(t))

  # paper
  for arr in obj.paper:
    for t in arr.item:
      res.pap_list.append(Paper(t))

  return res


def dataWriter():
  return


def htmlWriter(obj):
  # loed header and footer
  file = open(HEAD_SRC, 'r')
  head_str = file.read()
  file.close()

  file = open(FOOT_SRC, 'r')
  foot_str = file.read()
  file.close()

  # write to html
  file = open(OUT_FILE, 'w')
  file.write(head_str)

  file.write("<h1 id='people'>People</h1>\n")
  file.write(obj.peoHtml())

  file.write("<h1 id='announce'>Announce</h1>\n")
  file.write(obj.annHtml())

  file.write("<h1 id='seminar'>Seminar</h1>\n")
  file.write(obj.semHtml())

  file.write("<h1 id='project'>Project</h1>\n")
  file.write(obj.proHtml())

  file.write("<h1 id='paper'>Paper</h1>\n")
  file.write(obj.papHtml())

  
  file.write(foot_str)
  file.close()

  return


def main():
  obj = dataReader()
  htmlWriter(obj)
  return

if __name__ == '__main__':
  main()
