from lxml import etree
from lxml import objectify

DATA_SRC = 'data.xml'

def dataReader():
  # open the xml file for reading:
  file = open(DATA_SRC, 'r')
  # convert to string:
  data = file.read()
  # close file because we dont need it anymore:
  file.close()

  print data
  obj = objectify.fromstring(data)

  print obj.tag
  print obj.text
  print obj.attrib

  for e in obj.people:
    print e.tag
    print e.text
    print e.attrib
  return

def dataWriter():
  return

def main():
  dataReader()
  return

if __name__ == '__main__':
  main()
