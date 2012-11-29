#!/usr/bin/env python

import sys
import shutil
import json

RELEASE_DIR = '../html/'
FILE_NAME_ARR = [
    {'id': 'home', 'name': 'Home', 'link': 'index.html'},
    {'id': 'people', 'name': 'People', 'link': 'people.html'},
    {'id': 'announce', 'name': 'Announcements', 'link': 'announcements.html'},
    {'id': 'seminars', 'name': 'Seminars', 'link': 'seminars.html'},
    {'id': 'projects', 'name': 'Projects', 'link': 'projects.html'},
    {'id': 'papers', 'name': 'Papers/Resources', 'link': 'papers.html'},
    ]


def gen_html(data):
  for t in FILE_NAME_ARR:
    hstr = ''
    hstr += gen_header(t)
    hstr += gen_body(t, data)
    hstr += gen_footer(t)

    f_name = RELEASE_DIR + t['link']
    with open(f_name, 'w') as output:
      output.write(hstr)
      output.close()


def gen_body(p, data):
  hstr = ''
  if p['id'] == 'home':
    hstr += \
        '''
        <div class="one-half dashed-line">
          <div class="box-title">
            <h3>What's New</h3>
          </div>
          <div class="box-title">
        '''
    index = 0
    LIMIT = 3
    for t in data['announcements']['announcement']:
      if t['importance'] == '1':
        hstr += '<h4>%s</h4>' % t['title']
        hstr += '<p>%s</p>' % t['details']
        index += 1
        if index >= LIMIT:
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

<p>We are part of the Institute for Interdisciplinary Information Sciences (IIIS), at Tsinghua University. IIIS is founded and directed by Andrew Yao.</p>

<p>For recent activities see here, and for a list of our members here.</p>
            <p>blabla...blabla.</p>
            <img src="img/logo2.png" align="right" style="width: 150px; padding-top: 10px;" alt="ITCS" />
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

  hstr += '<div class="boxes">'
  return hstr


def gen_js(p):
  hstr = ''
  if p['id'] == 'papers':
    hstr += \
    '''
<script type="text/javascript">
  function item_filter(str) {
    $('.box-title').hide();
    $('.'+str).show();
    $('.cat-btn .tag').css('background-color', '#A0A0A0');
    $('#'+str+'-btn').css('background-color', '#D36F03');
  }
  
  $(document).ready(function() {
    item_filter('papers')
  });
</script>
    '''
  elif p['id'] == 'people':
    hstr += \
    '''
<script type="text/javascript">
  function show_member(str) {
    $('#former-member').show();
    $('.cat-btn button').hide();
  }
</script>
    '''
  return hstr


def gen_footer(p):
  hstr = ''
  if p['id'] == 'home':
    hstr += \
        '''
      <div class="clear"></div>
      <div class="separator-line" style="margin-top: -5px"></div> 
      <p align="center">Copyright &copy; IIIS, Tsinghua University. All rights reserved.</a></p>
    </div><!-- end home page -->
  </div><!-- end right -->  
</body>
</html>
        '''
  else:
    hstr += \
        '''
      <div class="clear"></div>
      <div class="separator-line"></div>
      <img src="img/logo2.png" align="right" style="width: 80px; margin-top: -10px; margin-left: -80px;" alt="ITCS" />
      <p align="center">Copyright &copy; IIIS, Tsinghua University. All rights reserved.</a></p>
    </div><!-- end home page -->
  </div><!-- end right -->  
</body>
</html>
        '''
  return hstr


