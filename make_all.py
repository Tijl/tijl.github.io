import glob,os

##################
### make index ###
##################

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
                <img src="tijl-grootswagers.jpg" alt="Tijl Grootswagers" width="130px;">
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


###############
### make cv ###
###############

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
                <img src="tijl-grootswagers.jpg" alt="Tijl Grootswagers" width="130px;">
            </div>
            <p style="float:left;">
                Postdoctoral Research Associate  <br />
                School of Psychology   <br />
                The University of Sydney
            </p>
            <p style="float:left;">
                email:&nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="mailto:tijl.grootswagers@sydney.edu.au">tijl.grootswagers@sydney.edu.au</a><br />
                homepage:&nbsp;<a target="_blank" href="https://tijl.github.io/">https://tijl.github.io/</a><br />
                twitter:&nbsp;&nbsp;<a target="_blank" href="https://twitter.com/TGrootswagers">@TGrootswagers</a><br />
                github:&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://github.com/Tijl">https://github.com/Tijl</a>
            </p>
            <div style="clear:both;"></div>

    <h2 class="heading">
        Academic Track
    </h2>
    <p>2017-current: Postdoctoral Research Associate. School of Psychology, The University of Sydney, Australia</p>
    <p>2017-current: Associate Member. Perception in Action Research Centre, Macquarie University, Sydney, Australia</p> 
    <p>2017-2019: Associate Investigator. ARC Centre for Excellence in Cognition and its Disorders, Australia</p>

    <h2 class="heading">
        Education
    </h2>
    <p>2014-2017: Ph.D. Cognitive Science, Macquarie University, Sydney, NSW, Australia.</p>
    <p>2011-2013: MSc. (cum laude) Artificial Intelligence, Radboud University Nijmegen</p> 
    <p>2007-2011: BSc. Artificial Intelligence, Radboud University Nijmegen</p>

    <h2 class="heading">
        Teaching and supervision
    </h2>
    <p>2017-2019: Co-supervision of six honours students at the University of Sydney</p>
    <p>2019: Led two classes of an honours level seminar series at the University of Sydney</p>
    <p>2018: Guest lecture on deep convolutional neural networks for PSYCH3012: Cognition, Language & Thought at the University of Sydney</p>
    <p>2018: Led two classes of an honours level seminar series at the University of Sydney</p>
    <p>2016: Tutor: Cognitive and Brain Sciences at Macquarie University</p>
    <p>2012-2013: Teacher of two python (programming) courses at the Max Planck Institute, Nijmegen, the Netherlands</p>

    <h2 class="heading">
        Ad-hoc reviewing
    </h2> 
    <p>Journal of Neuroscience, Nature Communications, NeuroImage, Cerebral Cortex, Human Brain Mapping, Neuroinformatics, Scientific Reports, PLOS One, Psychophysiology, Cognitive Science <a target="_blank" href="https://publons.com/a/1341382/">https://publons.com/a/1341382/</a></p>

    <h2 class="heading">
        Activities
    </h2>
    <p>2018-2020: Member of the Australian Cognitive Neuroscience Society executive committee <a target="_blank" href="https://www.acns.org.au">www.acns.org.au</a></p>
    <p>2016-current: Contributor to the CoSMoMVPA multi-variate pattern analysis toolbox in Matlab <a target="_blank" href="http://www.cosmomvpa.org">www.cosmomvpa.org</a></p>
    <p>Lab visits: MRC-CBU Cambridge UK (2019), NIH, Bethesda, USA (2017), University of Maryland, Maryland USA (2017), Freie Universität Berlin, Germany (2016), Utrecht University, the Netherlands (2016).</p>
    <br />

    <h2 class="heading">
        Grants, Awards, and nominations
    </h2>
    <p>2019: Australian Cognitive Neuroscience Society Emerging Researcher Award</p>
    <p>2019: Carlson T, Robinson A, & Grootswagers T. Lie to me: what can one's face (and brain) tell us about a person's emotional state? University of Sydney Booster Grant 2019 ($40,000)</p>
    <p>2018: Australian Cognitive Neuroscience Society Best Poster Presentation by an Early Career Post-Doc</p>
    <p>2018: Carlson T, Robinson A, Grootswagers T. A novel method for studying representations and transformations in the human brain. University of Sydney Compact Grant 2018 ($20,000)</p>
    <p>2018: Carlson T, Robinson A, Grootswagers T. Linking brain and decision-making using a new informational ”seed and network” approach. University of Sydney Seed Grant 2018 ($19,664)</p>
    <p>2018: ARC Centre for Excellence in Cognition and its Disorders  Excellence in Research Student Award: Outstanding 2017 Publication ($1,000)</p>
    <p>2017: Macquarie University Faculty of Human Sciences Higher Degree Research Excellence Award ($250)</p>
    <p>2017: Australian Cognitive Neuroscience Society Best Poster Presentation by an Early Career Post-Doc</p>
    <p>2016: Australian Cognitive Neuroscience Society Student Travel Award ($250)</p>
    <p>2016: ARC Centre for Excellence in Cognition and its Disorders Annual Workshop Highly Commended Poster Award ($100)</p>
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
    data = [x for x in f.readlines() if 'The Cognitive Neurosciences' not in x]
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
        Published conference proceedings
    </div>
    <p>%i. <strong>Grootswagers T</strong>, Dijkstra K, ten Bosch L, Brandmeyer A, Sadakata M (2013). Word identification using phonetic features: towards a method to support multivariate fMRI speech decoding. In: <i>INTERSPEECH</i>. 3201-3205.</p>
    <p>%i. Gerke P, Langevoort J, Lagarde S, Bax L, <strong>Grootswagers T</strong>, Drenth R, Slieker V, Vuurpijl L, Haselager W, Sprinkhuizen-Kuyper I (2011). BioMAV: bio-inspired intelligence for autonomous flight. In: <i>Proceedings International Micro Air Vehicle Conference and Flight Competition</i>.</p>

    <div class="year">
        Published conference abstracts
    </div>
    <p>%i. Tovar D, <strong>Grootswagers T</strong>, Robinson A, Wallace M, Carlson T (2019). Optimizing the Number of Visual Presentations for Time-Resolved Decoding Studies. <i>Perception</i>, 48, 134-134.</p>
    <p>%i. Teichmann L, <strong>Grootswagers T</strong>, Carlson T, Rich A (2018). Tomatoes are red, cucumbers are green: Decoding the temporal dynamics of object-colour knowledge using Magnetoencephalography. <i>Journal of Vision</i>, 18(10), 861-861.</p>
    <p>%i. <strong>Grootswagers T</strong>, Cichy R, Carlson T (2016). Predicting behavior from decoded searchlight representations shows where decodable information relates to behavior. <i>Perception</i>, 45, 360-360.</p>
    <p>%i. Contini E, Williams M, Grootswagers T</strong>, Goddard E, Carlson T (2016). Dichotomy Versus Continuum: Evidence for a More Complex Agency Model of Visual Object Categorisation. <i>Journal of Vision</i>, 16(12), 252- 252.</p>
    <p>%i. <strong>Grootswagers T</strong>, Carlson T (2015). Decoding the emerging representation of degraded visual objects in the human brain. <i>Journal of Vision</i>, 15(12), 1087-1087.</p>
"""%tuple([totalpub+x for x in range(7)])

out+="""
    <div class="year">
        Conference presentations (presenting author)
    </div>
<p><strong>Grootswagers T</strong>, Robinson A, Shatek S, Carlson T (2019). The influence of task context on the neural dynamics of rapid stimulus processing. Poster presented at the Australian OHBM Chapter, Newcastle, NSW, Australia</p>
<p><strong>Grootswagers T</strong>, Robinson A, Carlson T (2018). Assessing the temporal dynamics of object processing using rapid-MVPA. Poster presented at the Australian Cognitive Neuroscience Society Conference (ACNS), Melbourne, VIC, Australia</p>
<p><strong>Grootswagers T</strong>, Staines A, Teichmann L, Heathcote A, Carlson T (2018). Linking brain decoding methods to evidence accumulation models of decision behaviour. Poster presented at the Annual Meeting of the Organisation for Human Brain Mapping (OHBM), Singapore</p>
<p><strong>Grootswagers T</strong>, Kennedy B, Most S, Carlson T (2017). Neural signatures of dynamic emotion constructs in the human brain. Poster presented at the Australian Cognitive Neuroscience Society Conference (ACNS), Adelaide, SA, Australia</p>
<p><strong>Grootswagers T</strong>, Contini E, Carlson T (2017). Hyperalignment of dynamic responses using MEG. Poster presented at the Annual Meeting of the Organisation for Human Brain Mapping (OHBM), Vancouver, BC, Canada</p>
<p><strong>Grootswagers T</strong>, Cichy R, Carlson T (2016). Beyond brain decoding: Searching for information in the brain that also predicts behaviour. Talk presented at the Australian Cognitive Neuroscience Society Conference (ACNS), Shoal Bay, NSW, Australia</p>
<p><strong>Grootswagers T</strong>, Cichy R, Carlson T (2016). Predicting behaviour from decoded searchlight representations shows where decodable information relates to behaviour. Talk presented at the Annual Meeting of the Society for Neuroscience (SFN), San Diego, CA, USA</p>
<p><strong>Grootswagers T</strong>, Cichy R, Carlson T (2016). Predicting behaviour from decoded searchlight representations shows where decodable information relates to behaviour. Talk presented at the European Conference on Visual Perception (ECVP), Barcelona, Spain</p>
<p><strong>Grootswagers T</strong>, McMahon D, Leopold D, Carlson T (2015). Not all that glitters is gold: predicting behavior from brain representations suggests that only a subset of decodable information is used by the brain. Talk presented at the Annual Meeting of the Society for Neuroscience (SFN), Chicago, IL, USA</p>
<p><strong>Grootswagers T</strong>, Ritchie B, Heathcote A, Carlson T (2015). Decoding the emerging representation of degraded visual objects in the human brain. Poster presented at the Annual Meeting of the Vision Sciences Society (VSS), St. Pete Beach, FL, USA</p>
<p><strong>Grootswagers T</strong>, Carlson T (2015). Decoding human minds from monkey brains. Poster presented at the Annual Australasian Experimental Psychology Conference (EPC), Sydney, NSW, Australia</p>
"""

out+="""
    <div class="year">
        Invited talks, symposia, and workshops
    </div>
    <p>2020: Decoding and Representational Dynamics in MEG & EEG. Talk presented at the IDEALAB Winter School, Macquarie University, Australia</p>    
    <p>2019: Using rapid stimulus presentation and multivariate decoding to study information processing in the human brain. Award talk presented at the Australian Cognitive Neuroscience Society Conference (ACNS), Launceston, Australia</p>
    <p>2019: Talk presented in early researcher career workshop at the Australian Cognitive Neuroscience Society Conference, Launceston, Australia</p>
    <p>2019: The representational dynamics of visual objects in rapid serial visual processing streams. Talk presented at Macquarie University, Australia</p>
    <p>2019: The representational dynamics of visual objects in rapid serial visual processing streams. Talk presented at the MRC Cognition and Brain sciences unit, Cambridge, UK</p>
    <p>2018: The representational dynamics of visual objects in rapid serial visual processing streams. Symposium presented at the Australian Cognitive Neuroscience Society Conference, Melbournce, VIC, Australia</p>
    <p>2018: Decoding and Representational Dynamics in MEG & EEG. Talk presented at the Kavli Summer Institute in Cognitive Neuroscience, Tahoe, CA, USA</p>
    <p>2018: MVPA applied to time-series neuroimaging data. Workshop presented at the University of Sydney, Australia</p>
    <p>2017: Beyond Brain Decoding: Methodological and empirical contributions to brain decoding methods and their link to behaviour. Talk presented at the Perception in Action Research Centre, Macquarie University, Sydney, NSW, Australia</p>
    <p>2017: Decoding Dynamic Brain Patterns: MVPA applied to time-series neuroimaging data. Workshop presented at the Australian Cognitive Neuroscience Society Conference, Adelaide, SA, Australia</p>
    <p>2016: Linking neural decoding methods to behavior. Talk presented at the Center for Cognitive Neuroscience, Freie Universität Berlin, Germany</p>
    <p>2016: Linking neural decoding methods to behavior. Talk presented at the department of Experimental Psychology, Utrecht University, the Netherlands</p>
    <p>2015: Modeling the relationship between behavior and decodable information in the brain. Talk presented at the UMD Neurotheory Lab, University of Maryland, MD, USA</p>
    <p>2015: Modeling the relationship between behavior and decodable information in the brain. Talk presented at the Laboratory of Neuropsychology, National Institute of Mental Health, Bethesda, MD, USA</p>
    <p>2015: Decoding human minds from monkey brains. Talk presented at the department of Experimental Psychology, Utrecht University, the Netherlands</p>
    <p>2015: Predicting Reaction Times from the Emerging Representation of Degraded Visual Objects. Talk presented at the Cognitive Research Group, University of Newcastle, NSW, Australia</p>
"""

out+="""
    <p style="margin-bottom: 50px;"><br /></p>
    </div>
    </body>
    </html>
"""

with open('cv.html','w') as f:
    f.write(out)
