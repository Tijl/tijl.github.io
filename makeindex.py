#!/usr/bin/python

import glob,os

out="""
    <!DOCTYPE html>
    <html lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-130925994-1"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
    
      gtag('config', 'UA-130925994-1');
    </script>

    <title>Tijl Grootswagers</title>
    <meta http-equiv="content-type" content="text/xml; charset=utf-8">
    <meta name="viewport" content="width=device-width" />
    <meta name="description" content="Publications by Tijl Grootswagers" />
    <link rel="stylesheet" type="text/css" href="tgrootswagers.css">
    </head>    
    
    <body>
        <div id="all">
            <h1 class="heading">
                Tijl Grootswagers
            </h1>
            <div class="photo">
                <img src="tijl-grootswagers.png" alt="Tijl Grootswagers" width="100px;">
            </div>
            <p style="float:left;">
                Postdoctoral Research Associate  <br />
                School of Psychology   <br />
                The University of Sydney
            </p>
            <p style="float:left;">
                email:&nbsp;&nbsp;&nbsp;<a target="_blank" href="mailto:tijl.grootswagers@sydney.edu.au">tijl.grootswagers@sydney.edu.au</a><br />
                twitter:&nbsp;<a target="_blank" href="https://twitter.com/TGrootswagers">@TGrootswagers</a><br />
                github:&nbsp;&nbsp;<a target="_blank" href="https://github.com/Tijl">https://github.com/Tijl</a>
            </p>
            <div style="clear:both;"></div>

    <h2 class="heading">
        Publications
    </h2>
    <p>
        * equal contribution
    </p>
    """
with open('publicationlist.csv') as f:
    data = f.readlines()
entries=[]
for (i,line) in enumerate(data):
    e=line.strip().split('\t');
    if len(e)==6:
        entries.append(e)
    elif line.strip():
        print('could not parse line %i: %s'%(1+i,e))

years = set([x[0] for x in entries])
print(years)
pdflist = glob.glob('tijl-grootswagers-pdf/*.pdf');
for x in pdflist:
    os.rename(x,x.replace(' ','_').replace('.pdf','').replace('.','')+'.pdf')
pdflist = glob.glob('tijl-grootswagers-pdf/*.pdf');


def formatpub(e):
    [year,authors,title,journal,pages,link]=e   
    
    f = lambda x: ''.join(filter(str.isalpha, x.lower()))
    
    c = [x for x in pdflist if f(title).find(f(x.strip('.pdf').split('_-_')[-1]))>-1]
    #print(title)
    #print([x.strip('.pdf').split(' - ')[-1] for x in pdflist])
    if len(c)==1:
        url = '%s'%c[0]
    else:
        print('\npdf not found for:\n%s'%'\n'.join(e))
        url=''
    
    fs = '<p>%s%s. %s. <i>%s</i>%s %s%s</p>'%(
        authors.replace('Grootswagers T','<strong>Grootswagers T</strong>'),
        ' (%s)'%year.replace('inpress','in press').replace('preprint',''),
        title,
        journal,
        ', '+pages if pages else '',
        '<a target="_blank" class="doilink" href="%s">[doi]</a>'%(link),
        '<a target="_blank" class="pdflink" href="%s"> [pdf]</a>'%(url if url else ''))
    
    return fs
    
    

if 'preprint' in ''.join(years):
    out+="""
    <div class="year">
        preprints
    </div>
    """
    for e in [x for x in entries if 'preprint' in x[0]]:
        out+="""
        %s
        """%formatpub(e)

if 'inpress' in years:
    out+="""
    <div class="year">
        in press
    </div>
    """
    for e in [x for x in entries if x[0]=='inpress']:
        out+="""
        %s
        """%formatpub(e)

for i in range(2100,2000,-1):
    if str(i) in years:
        out+="""
    <div class="year">
        %i
    </div>
    """%i
    for e in [x for x in entries if x[0]==str(i)]:
        out+="""
        %s
        """%formatpub(e)
    
out+="""
    <p style="margin-bottom: 50px;"><br /></p>
    </div>

    <script>
        var x = document.getElementsByClassName("pdflink");
        for (var i = 0; i < x.length; i++) {
            x[i].onclick = function() {clickevent(this,'PDF')};
        }
        
        var x = document.getElementsByClassName("doilink");
        for (var i = 0; i < x.length; i++) {
            x[i].onclick = function() {clickevent(this,'DOI')};
        }
        
        function clickevent(e,t){
            gtag('event', 'click', {
                'event_category':t, 
                'event_label':e.getAttribute('href')
                });
            return true;
        }
    </script>

    </body>
    </html>
"""

with open('index.html','w') as f:
    f.write(out)
