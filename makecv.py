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
        Academic Track
    </h2>
    <p>2017-current: Postdoctoral Research Associate. School of Psychology, The University of Sydney, Australia</p>
    <p>2017-current: Associate Member. Perception in Action Research Centre, Macquarie University, Sydney, Australia</p> 
    <p>2017-current: Associate Investigator. ARC Centre for Excellence in Cognition and its Disorders, Australia</p>

    <h2 class="heading">
        Education
    </h2>
    <p>2014-2017: Ph.D. Cognitive Science, Macquarie University, Sydney, NSW, Australia.</p>
    <p>2011-2013: MSc. (cum laude) Artificial Intelligence, Radboud University Nijmegen</p> 
    <p>2007-2011: BSc. Artificial Intelligence, Radboud University Nijmegen</p>

    <h2 class="heading">
        Teaching and supervision
    </h2>
    <p>2017-2019: Assisted in supervision of six honours students at the University of Sydney</p>
    <p>2018: Guest lecture on deep convolutional neural networks for PSYCH3012: Cognition, Language & Thought at the University of Sydney</p>
    <p>2018: Led two classes of an honours level seminar series at the University of Sydney</p>
    <p>2016: Tutor: Cognitive and Brain Sciences at Macquarie University</p>
    <p>2012-2013: Teacher of two python (programming) courses at the Max Planck Institute, Nijmegen, the Netherlands</p>

    <h2 class="heading">
        Ad-hoc reviewing
    </h2> 
    <p>NeuroImage, Cerebral Cortex, Scientific Reports, PLOS One, Cognitive Science <a target="_blank" href="https://publons.com/a/1341382/">https://publons.com/a/1341382/</a></p>

    <h2 class="heading">
        Activities
    </h2>
    <p>2018-2019: Australian Cognitive Neuroscience Society executive committee member</p>
    <p>2016-current: Contributor to the CoSMoMVPA multi-variate pattern analysis toolbox in Matlab <a target="_blank" href="www.cosmomvpa.org">www.cosmomvpa.org</a></p>
    
    <br />

    <h2 class="heading">
        Grants, Awards, and nominations
    </h2>
    <p>2018: Australian Cognitive Neuroscience Society Best Poster Presentation by an Early Career Post-Doc</p>
    <p>2018: Carlson T, Robinson A, Grootswagers T. A novel method for studying representations and transformations in the human brain. University of Sydney, School of Psychology Compact Grant 2018 ($20,000)</p>
    <p>2018: Carlson T, Robinson A, Grootswagers T. Linking brain and decision-making using a new informational ”seed and network” approach. University of Sydney, School of Psychology Seed Grant 2018 ($19,664)</p>
    <p>2018: CCD Excellence in Research Student Award: Outstanding 2017 Publication ($1,000)</p>
    <p>2017: Macquarie University Faculty of Human Sciences Higher Degree Research Excellence Award ($250)</p>
    <p>2017: Australian Cognitive Neuroscience Society Best Poster Presentation by an Early Career Post-Doc</p>
    <p>2016: Australian Cognitive Neuroscience Society Student Travel Award ($250)</p>
    <p>2016: CCD Annual Workshop Highly Commended Poster Award ($100)</p>
    <p>2015: Macquarie University Postgraduate Research Fund ($5,000)</p>
    <p>2014: International Macquarie University Research Excellence Scholarship</p>
    <p>2013: Interspeech best student paper nomination</p>

    <h2 class="heading">
        Publications
    </h2>
    <p>
        * equal contribution
    </p>

    <div class="year">
        Book chapter
    </div>

    <p>1. Carlson T, <strong>Grootswagers T</strong>, Robinson A (in press). An introduction to time-resolved decoding analysis for M/EEG. in: (Gazzaniga, Mangun, & Poeppel, eds.) <i>The Cognitive Neurosciences, 6th edition.</i></p>

    <div class="year">
        Refereed journal publications
    </div>
    """

totalpub=1

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

def formatpub(e):
    [year,authors,title,journal,pages,link]=e   
    
    f = lambda x: ''.join(filter(str.isalpha, x.lower()))
    global totalpub
    totalpub+=1

    fs = '<p>%i. %s%s. %s. <i>%s</i>%s %s</p>'%(totalpub,
        authors.replace('Grootswagers T','<strong>Grootswagers T</strong>'),
        ' (%s)'%year.replace('inpress','in press').replace('preprint',''),
        title,
        journal,
        ', '+pages if pages else '',
        '<a target="_blank" href="%s">%s</a>'%(link,link))
    
    return fs

if 'inpress' in years:
    for e in [x for x in entries if x[0]=='inpress']:
        out+="""
        %s
        """%formatpub(e)

for i in range(2100,2000,-1):
    for e in [x for x in entries if x[0]==str(i)]:
        out+="""
        %s
        """%formatpub(e)
out+="""
<div class="year">
    Other research outputs
</div>
"""

if 'preprint' in ''.join(years):
    out+="""
    <div class="year">
        Preprints
    </div>
    """
    for e in [x for x in entries if 'preprint' in x[0]]:
        out+="""
        %s
        """%formatpub(e)

totalpub+=1
out+="""
    <div class="year">
        Fully refereed conference proceedings
    </div>
    <p>%i. <strong>Grootswagers T</strong>, Dijkstra K, ten Bosch L, Brandmeyer A, Sadakata M (2013). Word identification using phonetic features: towards a method to support multivariate fMRI speech decoding. In: <i>INTERSPEECH</i>. 3201-3205.</p>
    <p>%i. Gerke P, Langevoort J, Lagarde S, Bax L, <strong>Grootswagers T</strong>, Drenth R, Slieker V, Vuurpijl L, Haselager W, Sprinkhuizen-Kuyper I (2011). BioMAV: bio-inspired intelligence for autonomous flight. In: <i>Proceedings International Micro Air Vehicle Conference and Flight Competition</i>.</p>

    <div class="year">
        Refereed conference abstracts
    </div>
    <p>%i. Teichmann L, <strong>Grootswagers T</strong>, Carlson T, Rich A (2018). Tomatoes are red, cucumbers are green: Decoding the temporal dynamics of object-colour knowledge using Magnetoencephalography. <i>Journal of Vision</i>, 18(10), 861-861.</p>
    <p>%i. <strong>Grootswagers T</strong>, Cichy R, Carlson T (2016). Predicting behavior from decoded searchlight representations shows where decodable information relates to behavior. <i>Perception</i>, 45, 360-360.</p>
    <p>%i. Contini E, Williams M, Grootswagers T</strong>, Goddard E, Carlson T (2016). Dichotomy Versus Continuum: Evidence for a More Complex Agency Model of Visual Object Categorisation. <i>Journal of Vision</i>, 16(12), 252- 252.</p>
    <p>%i. <strong>Grootswagers T</strong>, Carlson T (2015). Decoding the emerging representation of degraded visual objects in the human brain. <i>Journal of Vision</i>, 15(12), 1087-1087.</p>

    <p style="margin-bottom: 50px;"><br /></p>
    </div>
    </body>
    </html>
"""%tuple([totalpub+x for x in range(6)])

with open('cv.html','w') as f:
    f.write(out)