class FullData:
  peo_list = []
  ann_list = []
  sem_list = []
  pro_list = []
  pap_list = []

  def peoHtml(self):
    html = ''
    for t in self.peo_list:
      html += t.toHTML()
    return html

  def annHtml(self):
    html = ''
    for t in self.ann_list:
      html += t.toHTML()
    return html

  def semHtml(self):
    html = ''
    for t in self.sem_list:
      html += t.toHTML()
    return html

  def proHtml(self):
    html = ''
    for t in self.pro_list:
      html += t.toHTML()
    return html

  def papHtml(self):
    html = ''
    for t in self.pap_list:
      html += t.toHTML()
    return html


class Author:
  name = ''
  url = ''


class Person:
  name = ''
  role = ''
  url = ''
  interest = ''
  details = ''

  def __init__( self, obj ):
    self.readFromXml(obj)
    return
    
  def readFromXml( self, obj ):
    self.name = obj.name.text
    self.role = obj.role.text
    self.url = obj.url.text
    self.interest = obj.interest.text
    self.details = obj.details.text
    return

  def toXML(self):
    xml_str = ''
    return xml_str

  def toHTML(self):
    html_str = "<h2>%s</h2>" % self.name
    html_str += "<p>%s</p>" % self.details
    return html_str


class Announce:
  title = ''
  date = ''
  details = ''

  def __init__( self, obj ):
    self.readFromXml(obj)
    return
    
  def readFromXml( self, obj ):
    self.title = obj.title.text
    self.dete = obj.date.text
    self.details = obj.details.text
    return

  def toXML(self):
    xml_str = ''
    return xml_str

  def toHTML(self):
    html_str = "<h2>%s</h2>" % self.title
    html_str += "<p>%s</p>" % self.details
    return html_str


class Seminar:
  title = ''
  date = ''
  time = ''
  venue = ''
  abstract = ''
  extra = ''
  url_list = []
  is_active = False

  def __init__( self, obj ):
    self.readFromXml(obj)
    return
    
  def readFromXml( self, obj ):
    self.title = obj.title.text
    self.dete = obj.date.text
    self.time = obj.time.text
    self.venue = obj.venue.text
    self.abstract = obj.abstract.text
    self.extra = obj.extra.text
    for t in obj.url:
      self.url_list.append(t.text)

    # TODO: active or not
    return

  def toXML(self):
    xml_str = ''
    return xml_str

  def toHTML(self):
    html_str = "<h2>%s</h2>" % self.title
    html_str += "<p>%s</p>" % self.date
    return html_str


class Project:
  title = ''
  author_list = []

  def __init__( self, obj ):
    self.readFromXml(obj)
    return
    
  def readFromXml( self, obj ):
    self.title = obj.title.text
    for t in obj.author:
      e = Author()
      e.name = t.name.text
      e.url = t.url.text

      self.author_list.append(e)
    return

  def toXML(self):
    xml_str = ''
    return xml_str

  def toHTML(self):
    html_str = "<h2>%s</h2>" % self.title
    html_str += "<p>%s</p>" % ','.join(i.name for i in self.author_list)

    # TODO: link to lab people
    return html_str


class Paper:
  title = ''
  category = ''
  date = ''
  venue = ''
  abstract = ''
  paperURL = ''
  fullpaperURL = ''
  BIB = ''
  author_list = []

  def __init__( self, obj ):
    self.readFromXml(obj)
    return
    
  def readFromXml( self, obj ):
    self.title = obj.title.text
    self.category = obj.category.text
    self.date = obj.date.text
    self.venue = obj.venue.text
    self.abstract = obj.abstract.text
    self.paperURL = obj.paperURL.text
    self.fullpaperURL = obj.fullpaperURL.text
    self.BIB = obj.BIB.text
    for t in obj.author:
      e = Author()
      e.name = t.name.text
      e.url = t.url.text

      self.author_list.append(e)
    return

  def toXML(self):
    xml_str = ''
    return xml_str

  def toHTML(self):
    html_str = "<h2>%s</h2>" % self.title
    html_str += "<p>%s</p>" % ','.join(i.name for i in self.author_list)
    
    # TODO: link to lab people
    return html_str

