#!/usr/bin/env python

import sys
import shutil
import json
import codecs

RELEASE_DIR = '../html/'
FILE_NAME_ARR = [
    {'id': 'home', 'name': 'Home', 'link': 'index.html'},
    {'id': 'people', 'name': 'People', 'link': 'people.html'},
    {'id': 'announce', 'name': 'Announcements', 'link': 'announcements.html'},
    {'id': 'seminars', 'name': 'Seminars', 'link': 'seminars.html'},
    {'id': 'projects', 'name': 'Projects', 'link': 'projects.html'},
    {'id': 'papers', 'name': 'Papers/Resources', 'link': 'papers.html'},
    ]
HOME_LIMIT = 3
PAGE_LIMIT = 10


def gen_html(data):
  for t in FILE_NAME_ARR:
    hstr = ''
    hstr += gen_header(t)
    hstr += gen_body(t, data)
    hstr += gen_footer(t, data)

    f_name = RELEASE_DIR + t['link']
    with codecs.open(f_name, 'w', "utf-8") as output:
      output.write(hstr)
      output.close()


def gen_body(p, data):
  hstr = ''
  hstr += globals()['gen_body_' + p['id']](p, data)
  return hstr


def gen_body_home(p, data):
  hstr = ''
  hstr += \
      '''
      <div class="boxes">
      <div class="one-half dashed-line">
      <div class="box-title">
      <h3>What's New</h3>
      </div>
      <div class="box-title">
      '''
  index = 0
  for t in data['announcements']['announcement']:
    if t == []:
      continue
    if t['importance'] == '1':
      hstr += '<h4>%s</h4>' % t['title']
      hstr += '<p>%s</p>' % t['details']
      index += 1
      if index >= HOME_LIMIT:
        break

  hstr += \
      '''
      </div>
      </div>
      <div class="one-half">
          <div class="box-title">
            <h3>Introduction</h3>
          </div>
          <div class="box-title">
            <p>We are trying to understand the role of randomness in computation, computational intractability, their relations, and their applications.</p>
            <p>We are part of the <a href='http://www.iiis.tsinghua.edu.cn/en/' target="_blank">Institute for Interdisciplinary Information Sciences</a> (IIIS), at Tsinghua University. IIIS is founded and directed by <a href='http://www.iiis.tsinghua.edu.cn/yao/' target="_blank">Andrew Yao</a>.</p>
            <p>For recent activities see <a href='seminars.html' target="_blank">here</a>, and for a list of our members <a href='people.html' target="_blank">here</a>.</p>
            <img src="img/logo2.png" align="right" style="width: 150px; padding-top: 10px;" alt="ITCS" />
          </div>
        </div>
      '''
  return hstr


def gen_body_people(p, data):
  hstr = ''
  hstr += \
      '''
      <h3>People</h3>
      <div class="boxes">
      <div class="box-title">
        <div class="full-width">
      '''
  type_list = ['Faculty', 'Graduate Students', 'Undergraduate Students']

  for g in type_list:
    hstr += '<h4>%s</h4>' % g
    for t in data['people']['member']:
      if t == [] or t['type'] != g:
        continue
      hstr += '<div style="min-height: 120px; margin-top: 5px;">'
      if t['photo'] != '':
        hstr += '<img src="%s" align="left" width="75px"/>' % t['photo']
      hstr += '<div style="margin-left: 100px;">'
      hstr += '<p class="name">%s</p>' % t['name']
      hstr += '<p class="title">%s</p>' % t['role']
      hstr += '<p class="link"><a href="%s" target="_blank">%s</a></p>' % (t['homepage'], t['homepage'])
      if t['interest'] != '':
        hstr += '<p class="interest">%s</p>' % t['interest']
      if t['details'] != '':
        hstr += '<p class="details">%s</p>' % t['details']
      hstr += '</div>'
      hstr += '</div>'
      hstr += '<div class="clear"></div>'
      hstr += '<div class="dashed-line-h"></div>'

  if data['people']['former_member'] != []:
    hstr += \
        '''
        <div class="cat-btn" style="display: none;">
           <button onclick="show_member()">Former Members</button>
        </div>
        '''
    hstr += '<div id="former-member: style="display: none;">'
    hstr += '<h4>Former Members</h4>'
    for t in data['people']['former_member']:
      if t == []:
        continue
      hstr += '<div style="min-height: 120px; margin-top: 5px;">'
      if t['photo'] != '':
        hstr += '<img src="%s" align="left" width="75px"/>' % t['photo']
      hstr += '<div style="margin-left: 100px;">'
      hstr += '<p class="name">%s</p>' % t['name']
      hstr += '<p class="title">%s</p>' % t['role']
      hstr += '<p class="title">%s</p>' % t['current_affiliation']
      hstr += '<p class="link"><a href="%s" target="_blank">%s</a></p>' % (t['current_homepage'], t['current_homepage'])
      if t['interest'] != '':
        hstr += '<p class="interest">%s</p>' % t['interest']
      if t['details'] != '':
        hstr += '<p class="details">%s</p>' % t['details']
      hstr += '</div>'
      hstr += '</div>'
      hstr += '<div class="clear"></div>'
      hstr += '<div class="dashed-line-h"></div>'
    hstr += '</div>'
  hstr += '</div>'

  return hstr


def gen_body_announce(p, data):
  hstr = ''
  hstr += \
      '''
      <h3>Announcements</h3>
      <div class="boxes">
        <div class="full-width">
      '''
  index = 0
  for t in data['announcements']['announcement']:
    if t == []:
      continue
    hstr += '<div class="box-title" value="%s">' % index
    if t['importance'] == '1':
      hstr += '<h4 class="bg-yellow">%s</h4>' % t['title']
    else:
      hstr += '<h4 class="bg-gray">%s</h4>' % t['title']
    hstr += '<p>%s</p>' % t['details']
    hstr += '<div class="clear"></div>'
    hstr += '<div class="dashed-line-h"></div>'
    hstr += '</div>'
    index += 1

  hstr += \
      '''
          <div id='foot' align="center" style="margin-top: 10px;">
            <a onclick='gotopage(1);' href='#'><img src="img/button/first.png"/></a>
            <a onclick='shiftpage(-1);' href='#'><img src="img/button/prev.png" style="margin-left: 8px;"/></a>
            <div id='foot_number' style="display: inline;"></div>
            <a onclick='shiftpage(1);' href='#'><img src="img/button/next.png" style="margin-left: 8px;"/></a>
            <a onclick='gotopage(total_page);' href='#'><img src="img/button/last.png" style="margin-left: 8px;"/></a>
          </div>
        </div>
      </div>
      '''
  return hstr


def gen_body_seminars(p, data):
  hstr = ''
  hstr += \
      '''
      <h3>Seminars</h3>
      <div class="boxes">
        <div class="full-width">
      '''

  index = 0
  for t in data['seminars']['seminar']:
    if t == []:
      continue
    hstr += '<div class="box-title" value="%s">' % index
    hstr += '<h4 class="bg-red">%s</h4>' % t['title']
    hstr += '<p class="title">%s</p>' % t['date']
    hstr += '<p class="title">Speaker: <a href="%s" target="_blank">%s</a></p>' % (t['speaker_homepage'], t['speaker'])
    hstr += '<p class="title">Place: %s, Time: %s</p>' % (t['venue'], t['time'])
    hstr += '<div class="cat-btn">'
    hstr += '<button class="basic-modal" value="det-%d">Details</button>' % index
    hstr += '</div>'
    
    hstr += '<div id="basic-modal-content-det-%d" class="basic-modal-hide">' % index
    if t['speaker_photo'] != '':
      hstr += '<img src="%s" align="right" width="150px" style="margin-right: 20px;"/>' % t['speaker_photo']
    hstr += '<h4>%s</h4>' % t['title']
    hstr += '<p class="title">%s</p>' % t['date']
    hstr += '<p class="title">Speaker: <a href="%s" target="_blank">%s</a></p>' % (t['speaker_homepage'], t['speaker'])
    hstr += '<p class="title">Place: %s, Time: %s</p>' % (t['venue'], t['time'])
    hstr += '<li style="margin-top: 5px;">Abstract</li>'
    hstr += '<p class="details">%s</p>' % t['abstract']
    hstr += '<li style="margin-top: 5px;">Bio</li>'
    hstr += '<p class="details">%s</p>' % t['speaker_bio']
    if t['urls'] != '':
      hstr += '<li style="margin-top: 5px;">Links</li>'
      for u in t['urls'].split(','):
        hstr += '<p class="details"><a href="%s" target="_blank">%s</a></p>' % (u, u)
    hstr += '</div>'
    
    hstr += '<div class="clear"></div>'
    hstr += '<div class="dashed-line-h"></div>'
    hstr += '</div>'
    index += 1

  hstr += \
      '''
          <div id='foot' align="center" style="margin-top: 10px;">
            <a onclick='gotopage(1);' href='#'><img src="img/button/first.png"/></a>
            <a onclick='shiftpage(-1);' href='#'><img src="img/button/prev.png" style="margin-left: 8px;"/></a>
            <div id='foot_number' style="display: inline;"></div>
            <a onclick='shiftpage(1);' href='#'><img src="img/button/next.png" style="margin-left: 8px;"/></a>
            <a onclick='gotopage(total_page);' href='#'><img src="img/button/last.png" style="margin-left: 8px;"/></a>
          </div>
        </div>
      </div>
      '''
  return hstr


def gen_body_projects(p, data):
  hstr = ''
  hstr += \
      '''
      <h3>Projects</h3>
      <div class="boxes">
      '''

  index = 0
  for t in data['projects']['project']:
    if t == []:
      continue
    hstr += \
        '''
        <div class="one-half bd-blue">
          <h3 class="bg-blue">Introduction</h3>
          <div class="box-title">
            <h4>%s</h4>
            <p>%s</p>
          </div>
        </div>
        ''' % (t['title'], t['details_html'])
    index += 1

  if index == 0:
    hstr += \
        '''
        <center>
          <img src="img/under_construction.gif" height="250px" alt="Tsinghua" />
          <h2 style="text-align: center; margin-top: 20px;">Under Construction</h2>
        </center>
        '''
  hstr += '</div>'
  return hstr


def gen_body_papers(p, data):
  hstr = ''
  hstr += \
      '''
      <h3>Papers/Resources</h3>
        <div class="cat-btn">
          <button id="papers-btn" class="tag" onclick="item_filter('papers')">Papers</button>
          <button id="videos-btn" class="tag" onclick="item_filter('videos')">Videos</button>
          <button id="slides-btn" class="tag" onclick="item_filter('slides')">Slides</button>
        </div>
      <div class="boxes">
        <div class="full-width">
        <div class="separator-line"></div>
      '''
  index = 0
  c_n = 0
  for t in data['papers']['paper']:
    if t == []:
      continue
    hstr += '<div class="box-title papers" value="%s">' % index
    hstr += '<div style="min-height: 120px; margin-top: 5px;">'
    hstr += '<h4 class="bg-red">%s</h4>' % t['title']
    hstr += '<p class="title">%s</p>' % t['author']
    if t['venue'] != '' and t['date'] != '':
      hstr += '<p class="title">%s, %s</p>' % (t['venue'], t['date'])

    hstr += '<div class="cat-btn">'
    if t['paper_url'] != '':
      hstr += '<button onclick="window.open(\'%s\');">Paper</button>' % t['paper_url']
    if t['fullpaper_url'] != '':
      hstr += '<button onclick="window.open(\'%s\');">Full Paper</button>' % t['fullpaper_url']
    hstr += '<button class="basic-modal" value="det-%d">Details</button>' % index
    hstr += '<button class="basic-modal" value="bib-%d">Bibtex</button>' % index
    hstr += '</div>'
    
    hstr += '<div id="basic-modal-content-det-%d" class="basic-modal-hide">' % index
    hstr += '<h4>%s</h4>' % t['title']
    hstr += '<p class="title">%s</p>' % t['author']
    if t['venue'] != '' and t['date'] != '':
      hstr += '<p class="title">%s, %s</p>' % (t['venue'], t['date'])
    hstr += '<li style="margin-top: 5px;">Abstract</li>'
    hstr += '<p class="details">%s</p>' % t['abstract']
    hstr += '</div>'
    
    hstr += '<div id="basic-modal-content-bib-%d" class="basic-modal-hide">' % index
    hstr += '<li style="margin-top: 5px;">Bibtex</li>'
    hstr += '<p class="details">%s</p>' % t['bibtex']
    hstr += '</div>'

    hstr += '</div>'
    hstr += '<div class="clear"></div>'
    hstr += '<div class="dashed-line-h"></div>'
    hstr += '</div>'
    index += 1
    c_n += 1

  c_n = 0
  for t in data['papers']['video']:
    if t == []:
      continue
    hstr += '<div class="box-title videos" value="%s">' % index
    hstr += '<div style="min-height: 120px; margin-top: 5px;">'
    hstr += '<h4 class="bg-red">%s</h4>' % t['title']
    hstr += '<p class="title">%s</p>' % t['date']
    if t['url'] != '':
      hstr += '<li style="margin-top: 5px;">Download: <a href="%s" target="_blank">%s</a></li>' % (t['url'], t['url'])
    hstr += '<div class="cat-btn">'
    hstr += '<button class="basic-modal" value="det-%d">Details</button>' % index
    hstr += '</div>'
    
    hstr += '<div id="basic-modal-content-det-%d" class="basic-modal-hide">' % index
    hstr += '<h4>%s</h4>' % t['title']
    hstr += '<p class="title">%s</p>' % t['date']
    if t['url'] != '':
      hstr += '<li style="margin-top: 5px;">Download: <a href="%s" target="_blank">%s</a></li>' % (t['url'], t['url'])
    hstr += '<li style="margin-top: 5px;">About</li>'
    hstr += '<p class="details">%s</p>' % t['description']
    hstr += '</div>'
    
    hstr += '</div>'
    hstr += '<div class="clear"></div>'
    hstr += '<div class="dashed-line-h"></div>'
    hstr += '</div>'
    index += 1
    c_n += 1

  if c_n == 0:
    hstr += '<div class="box-title videos" value="%s">' % index
    hstr += '<h4 class="bg-red">This page is under construction -- entering paper details</h4>'
    hstr += '<div class="clear"></div>'
    hstr += '<div class="dashed-line-h"></div>'
    hstr += '</div>'

  c_n = 0
  for t in data['papers']['slide']:
    if t == []:
      continue
    hstr += '<div class="box-title slides" value="%s">' % index
    hstr += '<div style="min-height: 120px; margin-top: 5px;">'
    hstr += '<h4 class="bg-red">%s</h4>' % t['title']
    hstr += '<p class="title">%s</p>' % t['date']
    if t['url'] != '':
      hstr += '<li style="margin-top: 5px;">Download: <a href="%s" target="_blank">%s</a></li>' % (t['url'], t['url'])
    hstr += '<div class="cat-btn">'
    hstr += '<button class="basic-modal" value="det-%d">Details</button>' % index
    hstr += '</div>'
    
    hstr += '<div id="basic-modal-content-det-%d" class="basic-modal-hide">' % index
    hstr += '<h4>%s</h4>' % t['title']
    hstr += '<p class="title">%s</p>' % t['date']
    if t['url'] != '':
      hstr += '<li style="margin-top: 5px;">Download: <a href="%s" target="_blank">%s</a></li>' % (t['url'], t['url'])
    hstr += '<li style="margin-top: 5px;">About</li>'
    hstr += '<p class="details">%s</p>' % t['description']
    hstr += '</div>'
    
    hstr += '</div>'
    hstr += '<div class="clear"></div>'
    hstr += '<div class="dashed-line-h"></div>'
    hstr += '</div>'
    index += 1
    c_n += 1

  if c_n == 0:
    hstr += '<div class="box-title slides" value="%s">' % index
    hstr += '<h4 class="bg-red">This page is under construction -- entering paper details</h4>'
    hstr += '<div class="clear"></div>'
    hstr += '<div class="dashed-line-h"></div>'
    hstr += '</div>'

  hstr += \
      '''
          <div id='foot' align="center" style="margin-top: 10px;">
            <a onclick='gotopage(1);' href='#'><img src="img/button/first.png"/></a>
            <a onclick='shiftpage(-1);' href='#'><img src="img/button/prev.png" style="margin-left: 8px;"/></a>
            <div id='foot_number' style="display: inline;"></div>
            <a onclick='shiftpage(1);' href='#'><img src="img/button/next.png" style="margin-left: 8px;"/></a>
            <a onclick='gotopage(total_page);' href='#'><img src="img/button/last.png" style="margin-left: 8px;"/></a>
          </div>
        </div>
      </div>
      '''
  return hstr


def gen_header(p):
  hstr = ''
  hstr += \
  '''
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>RC3/IIIS - Tsinghua Univ.</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

<script type='text/javascript' src='js/jquery.js'></script>
<script type='text/javascript' src='js/jquery.simplemodal.js'></script>
<script type='text/javascript' src='js/basic.js'></script>

<link rel="stylesheet" type="text/css" href="css/dblue.css" media="screen" />
<link rel='stylesheet' type='text/css' href='css/basic.css' media='screen' />

<!--[if IE 7]>
<link type="text/css" href="css/ie7.css" rel="stylesheet" media="screen" />
<![endif]-->
<!--[if lt IE 7]>
<link type='text/css' href='css/basic_ie.css' rel='stylesheet' media='screen' />
<![endif]-->
  '''
  hstr += gen_js(p)
  hstr += \
      '''
</head>
<body>
  <div id="left" class="plates">
    <ul id="navigation">
      '''

  for t in FILE_NAME_ARR:
    hstr += '<li><a '
    if t['id'] == p['id']:
      hstr += 'class="active"'
    hstr += 'href="%s">%s</a></li>' % (t['link'], t['name'])

  hstr += \
      '''
    </ul>
  </div><!-- end left --> 
  
  <div id="right" class="square-grid">
    <div id="home" class="page">
      <div style="min-height: 50px;">
        <img src="img/logo.png" align="left" style="width: 150px;" alt="ITCS" />
        <h2>Laboratory For The Study of <font class='red'>R</font>andomness</h2>
        <br>
        <h2>in <font class='red'>C</font>omputation and <font class='red'>C</font>ryptographic <font class='red'>C</font>omplexity</h2>
      </div>
      <div class="separator-line"></div>  
      '''

  if p['id'] == 'home':
    hstr += \
        '''
      <div class="featured cycle">
        <img src="img/slide-0.gif" alt="image" style="width: 900px;"/>
      </div><!-- end featured -->     
      <div class="separator-line"></div>
        '''

  return hstr


def gen_js(p):
  hstr = ''
  if p['id'] == 'papers':
    hstr += \
    '''
<script type="text/javascript">
  var cur_page = 1;
  var total_page = 1;
  var type = '';
  function item_filter(str) {
    type = str;
    $('.box-title').hide();
    $('.'+type).show();
    $('.cat-btn .tag').css('background-color', '#A0A0A0');
    $('#'+type+'-btn').css('background-color', '#D36F03');
    makefoot();
  }
  
  function makefoot()
  {
    total_page = Math.ceil($('.'+type).size()/10);
    var str = '';
    for (var i=1; i<=total_page; i++)
    { 
      str += '<a onclick="gotopage('+i+')" style="margin-left: 8px;" href="#">'+i+'</a>';
    }
    $('#foot_number').html(str);
    gotopage(1);
  }

  function shiftpage(value)
  {
    gotopage(value + cur_page);
  }
  
  function gotopage(value)
  {
    if (value <= 0)
      value = 1;
    if (value > total_page)
      value = total_page;
    $('.'+type).hide();
    $('.'+type).slice(value*%d-%d, value*%d).show();
    $('#foot_number a').eq(cur_page-1).css('font-weight', 'normal')
    $('#foot_number a').eq(value-1).css('font-weight', 'bold')
    cur_page = value;
  }

  $(document).ready(function() {
    item_filter('papers');
  });
</script>
    ''' % (PAGE_LIMIT, PAGE_LIMIT, PAGE_LIMIT)
  elif p['id'] == 'announce' or p['id'] == 'seminars':
    hstr += \
    '''
<script type="text/javascript">
  var cur_page = 1;
  var total_page = 1;
  $(document).ready(function()
  {
    makefoot();
  });

  function makefoot()
  {
    total_page = Math.ceil($('.box-title').size()/10);
    var str = '';
    for (var i=1; i<=total_page; i++)
    { 
      str += '<a onclick="gotopage('+i+')" style="margin-left: 8px;" href="#">'+i+'</a>';
    }
    $('#foot_number').html(str);
    gotopage(1);
  }

  function shiftpage(value)
  {
    gotopage(value + cur_page);
  }
  
  function gotopage(value)
  {
    if (value <= 0)
      value = 1;
    if (value > total_page)
      value = total_page;
    $('.box-title').hide();
    $('.box-title').slice(value*%d-%d, value*%d).show();
    $('#foot_number a').eq(cur_page-1).css('font-weight', 'normal')
    $('#foot_number a').eq(value-1).css('font-weight', 'bold')
    cur_page = value;
  }
</script>
    ''' % (PAGE_LIMIT, PAGE_LIMIT, PAGE_LIMIT)
  elif p['id'] == 'people':
    hstr += \
    '''
<script type="text/javascript">
  function show_member(str)
  {
    $('#former-member').show();
    $('.cat-btn button').hide();
  }
</script>
    '''
  return hstr


def gen_footer(p, data):
  hstr = ''
  if p['id'] == 'home':
    hstr += \
        '''
      <div class="clear"></div>
      <div class="separator-line" style="margin-top: -5px"></div> 
      <p align="center">Copyright &copy; IIIS, Tsinghua University. All rights reserved.</a></p>
      </div>
    </div><!-- end home page -->
  </div><!-- end right -->  
        '''
  else:
    hstr += \
        '''
      <div class="clear"></div>
      <div class="separator-line"></div>
      <img src="img/logo3.png" align="right" style="width: 80px; margin-top: -10px; margin-left: -80px;" alt="ITCS" />
      <p align="center">Copyright &copy; IIIS, Tsinghua University. All rights reserved.</a></p>
    </div><!-- end home page -->
  </div><!-- end right -->  
        '''

  # Add counter script code
  try:
    hstr += "%s" % data[p['id']]['counter'][0]['code']
  except:
    pass
  hstr += "</body></html>"
  return hstr


