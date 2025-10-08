import glob,os,re,sys

os.chdir(os.path.dirname(sys.argv[0]))

##################
### make index ###
##################

out="""
    <!DOCTYPE html>
    <html lang="en" dir="ltr" xmlns="http://www.w3.org/1999/xhtml">
    <head>
    
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-Y7NMRW3VS5"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-Y7NMRW3VS5');
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
                Dr. Tijl Grootswagers
            </h1>
            <p style="float:left;">
                ARC DECRA Senior Research Fellow in Computational Neuroscience<br /> 
                The MARCS Institute for Brain, Behaviour and Development<br />
                School of Computer, Data and Mathematical Sciences<br />
                Western Sydney University, Sydney, Australia
            </p>
            <div class="photo">
                <img src="tijl-grootswagers.jpg" alt="Tijl Grootswagers" width="100px;">
            </div>
            <p style="float:left;">
                email:&nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="mailto:t.grootswagers@westernsydney.edu.au">t.grootswagers@westernsydney.edu.au</a><br />
                homepage:&nbsp;<a target="_blank" href="https://tijl.github.io/">https://tijl.github.io/</a><br />
                linktree:&nbsp;<a target="_blank" href="https://linktr.ee/tgro">https://linktr.ee/tgro</a><br />
                scholar:&nbsp;&nbsp;<a target="_blank" href="https://scholar.google.com.au/citations?user=TNI8FOoAAAAJ&hl=en">TNI8FOoAAAAJ</a><br />
                twitter:&nbsp;&nbsp;<a target="_blank" href="https://twitter.com/TGrootswagers">@TGrootswagers</a><br />
                github:&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://github.com/Tijl">github.com/Tijl</a><br />
                orcid:&nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://orcid.org/0000-0002-7961-5002">0000-0002-7961-5002</a><br />
            </p>
            <p style="float:left;">
            I am a computational cognitive neuroscientist combining machine learning, neuroimaging, and behavioural data to understand how the brain represents and processes information.
            The focus of my research is to investigate how the brain perceives and represents visual objects, and how it uses these representations for decision making.
            Feel free to email me with inquiries about research opportunities in the lab.
            </p>
            <div style="clear:both;"></div>

    <h2 class="heading">
        Publications
    </h2>
    <p>
        * equal contribution
    </p>
    """
with open('publicationlist.tsv') as f:
    data = f.readlines()
entries=[]
for (i,line) in enumerate(data):
    e=line.strip().split('\t')
    if len(e)>3:
        entries.append(e)
    elif line.strip():
        print('could not parse line %i: %s'%(1+i,e))

years = set([x[0] for x in entries])
print(years)
pdflist = glob.glob('tijl-grootswagers-pdf/*.pdf')
for x in pdflist:
    os.rename(x,x.replace(' ','_').replace('.pdf','').replace('.','')+'.pdf')
pdflist = glob.glob('tijl-grootswagers-pdf/*.pdf')

def formatpub(e,cv=False):
    while len(e)<7:
        e.append('')
    [year,authors,title,journal,pages,doilink,otherlinks]=e   
    
    articletype = ''
    if 'preprint' in year:
        articletype='[PREPRINT] '
    if 'inpress' in year:
        articletype='[IN PRESS] '

    otherinfo = ''
    if otherlinks:
        parts = re.findall(r'(\[.*?\])\[(.*?)\]',otherlinks)
        for group in parts:
            otherinfo+=' <a target="_blank" href="%s">%s</a>'%(group[1],group[0])
    
    f = lambda x: ''.join(filter(str.isalpha, x.lower()))
    
    c = [x for x in pdflist if f(title).find(f(x.strip('.pdf').split('_-_')[-1]))>-1]
    #print(title)
    #print([x.strip('.pdf').split(' - ')[-1] for x in pdflist])
    if len(c)==1:
        url = '%s'%c[0]
    elif len(c) > 1:
        print('\nError: multiple pdf found for:\n%s'%'\n'.join(e))
        print(f(title))
        url=''
    else:
        print('\nError: pdf not found for:\n%s'%'\n'.join(e))
        print(f(title))
        url=''
    if cv:
        fs = '<p>%s%s. %s. <i>%s</i>%s %s</p>'%(
            authors.replace('Grootswagers T','<strong>Grootswagers T</strong>'),
            ' (%s)'%year.replace('inpress','in press').replace('preprint',''),
            title,
            journal,
            ', '+pages if pages else '',
            '<a target="_blank" href="%s">%s</a>'%(doilink,doilink))
    else:
        fs = '<p>%s%s%s. %s. <i>%s</i>%s %s%s%s</p>'%(
            articletype,
            authors,
            ' (%s)'%year.replace('inpress','in press').replace('preprint',''),
            title,
            journal,
            ', '+pages if pages else '',
            '<a target="_blank" class="doilink" href="%s">[doi]</a>'%(doilink),
            '<a target="_blank" class="pdflink" href="%s"> [pdf]</a>'%(url if url else ''),
            otherinfo)
    return fs
    
# if 'preprint' in ''.join(years):
#     out+="""
#     <div class="year">
#         Preprints
#     </div>
#     """
#     for e in [x for x in entries if 'preprint' in x[0]]:
#         out+="""
#         %s
#         """%formatpub(e)

# if 'inpress' in years:
#     out+="""
#     <div class="year">
#         in press
#     </div>
#     """
#     for e in [x for x in entries if x[0]=='inpress']:
#         out+="""
#         %s
#         """%formatpub(e)

publisthtml = ''
for i in range(2100,2000,-1):
    if str(i) in years:
        publisthtml+="""
    <div class="year">
        %i
    </div>
    """%i
    for e in [x for x in entries if str(i) in x[0]]:
        publisthtml+="""
        %s
        """%formatpub(e)
publisthtmlcv = ''
for i in range(2100,2000,-1):
    if str(i) in years:
        publisthtmlcv+="""
    <div class="year">
        %i
    </div>
    """%i
    for e in [x for x in entries if str(i) in x[0]]:
        publisthtmlcv+="""
        %s
        """%formatpub(e,cv=1)

out+=publisthtml
out+="""
    <p style="margin-bottom: 50px;"><br /></p>
    </div>

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
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-Y7NMRW3VS5"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-Y7NMRW3VS5');
    </script>

    <title>CV Dr. Tijl Grootswagers</title>
    <meta http-equiv="content-type" content="text/xml; charset=utf-8">
    <meta name="viewport" content="width=device-width" />
    <meta name="description" content="Publications by Tijl Grootswagers" />
    <link rel="stylesheet" type="text/css" href="tgrootswagers.css">
    </head>    
    
    <body>
        <div id="all" style="width: 850px;">
            <h1 class="heading">
                Dr. Tijl Grootswagers
            </h1>
            <p style="float:left;">
                ARC DECRA Senior Research Fellow in Computational Neuroscience<br /> 
                The MARCS Institute for Brain, Behaviour and Development<br />
                School of Computer, Data and Mathematical Sciences<br />
                Western Sydney University, Sydney, Australia
            </p>
            <div class="photo">
                <img src="tijl-grootswagers.jpg" alt="Tijl Grootswagers" width="100px;">
            </div>
            <p style="float:left;">
                email:&nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="mailto:t.grootswagers@westernsydney.edu.au">t.grootswagers@westernsydney.edu.au</a><br />
                homepage:&nbsp;<a target="_blank" href="https://tijl.github.io/">https://tijl.github.io/</a><br />
                linktree:&nbsp;<a target="_blank" href="https://linktr.ee/tgro">https://linktr.ee/tgro</a><br />
                scholar:&nbsp;&nbsp;<a target="_blank" href="https://scholar.google.com.au/citations?user=TNI8FOoAAAAJ&hl=en">https://scholar.google.com.au/citations?user=TNI8FOoAAAAJ</a><br />
                twitter:&nbsp;&nbsp;<a target="_blank" href="https://twitter.com/TGrootswagers">https://twitter.com/TGrootswagers</a><br />
                github:&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://github.com/Tijl">https://github.com/Tijl</a><br />
                orcid:&nbsp;&nbsp;&nbsp;&nbsp;<a target="_blank" href="https://orcid.org/0000-0002-7961-5002">https://orcid.org/0000-0002-7961-5002</a><br />
            </p>
            <div style="clear:both;"></div>

    <h2 class="heading">
        Academic track
    </h2>
    <p>2023-current: ARC DECRA Senior Research Fellow in Computational Neuroscience. The MARCS Institute for Brain, Behaviour and Development, Western Sydney University, Australia</p>
    <p>2023-current: Senior Research Fellow in Computational Neuroscience. School of Computer, Data and Mathematical Sciences, Western Sydney University, Australia</p>
    <p>2020-2022: Vice Chancellor's Research Fellow in Cognitive Neuroscience. The MARCS Institute for Brain, Behaviour and Development, Western Sydney University, Australia</p>
    <p>2020-current: Honorary Research fellow. School of Psychology, The University of Sydney, Australia</p> 
    <p>2017-2020: Postdoctoral Research Associate. School of Psychology, The University of Sydney, Australia</p>
    <p>2017-current: Associate Member. Perception in Action Research Centre, Macquarie University, Sydney, Australia</p> 
    <p>2017-2019: Associate Investigator. ARC Centre for Excellence in Cognition and its Disorders, Australia</p>

    <h2 class="heading">
        Education
    </h2>
    <p>2014-2017: Ph.D. Cognitive Science, Macquarie University, Sydney, NSW, Australia.</p>
    <p>2011-2013: MSc. (cum laude) Artificial Intelligence, Radboud University Nijmegen</p> 
    <p>2007-2011: BSc. Artificial Intelligence, Radboud University Nijmegen</p>

    <h2 class="heading">
        Research funding (total > $3M)
    </h2>
    <p>2024: Australian Research Council Linkage Project ($567,000)</p>
    <p>2024: National Intelligence & Security Discovery Research Grant ($770,000)</p>
    <p>2024: Defence Innovation Network Scholarship ($110,000)</p>
    <p>2022: Australian Research Council Linkage Infrastructure, Equipment and Facilities ($930,000)</p>
    <p>2022: Australian Research Council Discovery Early Career Researcher Award ($450,000)</p>
    <p>2022: MARCS Institute Scholarship ($100,000)</p>
    <p>2021: Innovations Connections grant ($25,000)</p>
    <p>2019: University of Sydney Booster Grant 2019 ($40,000)</p>
    <p>2018: University of Sydney Compact Grant 2018 ($20,000)</p>
    <p>2018: University of Sydney Seed Grant 2018 ($20,000)</p>
    <p>2015: Macquarie University Postgraduate Research Fund ($5,000)</p>

    <h2 class="heading">
        Postdoc supervision
    </h2>
    <p>Dr. Sophie Smit (primary supervisor)</p>

    <h2 class="heading">
        PhD supervision
    </h2>
    <p>Dalia Israel (primary supervisor)</p>
    <p>Florian Burger (primary supervisor)</p>
    <p>Almudena Ramírez Haro (primary supervisor)</p>
    <p>Nazanin Sheykh Andalibi (primary supervisor)</p>
    <p>Nusrat Samiya (co-supervisor)</p>
    <p>Mahdiyeh Khanbagi (co-supervisor)</p>
    <p>Martina Ventura (co-supervisor)</p>
    <p>Violet Chae (co-supervisor)</p>
    <p>Wing Hong Fu (co-supervisor)</p>

    <h2 class="heading">
        Other supervision and mentoring
    </h2>
    <p>2021-2023 Mentor of 4 PhD students (OHBM International Online Mentoring Program)</p>
    <p>2020-current: Supervision of 15 honours, 4 summer/winter scholars, 3 masters students at Western Sydney University</p>
    <p>2017-2020: Co-supervision of eight honour and two masters students at the University of Sydney</p>

    <h2 class="heading">
        Teaching
    </h2>
    <p>2022, 2023, 2025: Guest lecturer (9 lectures) for INFS7003 Advanced Topics in ICT at Western Sydney University</p>
    <p>2021-2022: Developed a 6-week EEG course at Western Sydney University</p>
    <p>2020: Tutor: Research Methods at Western Sydney University</p>
    <p>2018: Guest lecture for PSYCH3012: Cognition, Language & Thought at the University of Sydney</p>
    <p>2018-2019: Led four classes of an honours level seminar series at the University of Sydney</p>
    <p>2016: Tutor: Cognitive and Brain Sciences at Macquarie University</p>
    <p>2012-2013: Teacher of two python (programming) courses at the Max Planck Institute, Nijmegen, the Netherlands</p>

    <h2 class="heading">
        Leadership and service
    </h2>
    <p>2024: Member of the organising committee for the Australian Cognitive Neuroscience Society conference</p>
    <p>2024: Member of the organising committee for the International Conference on Biomagnetism (BIOMAG)</p>
    <p>2023: Member of the organising committee for the Australian Cognitive Neuroscience Society conference</p>
    <p>2022: Session Chair at the Australasian Brain and Psychological Sciences conference</p>
    <p>2020-current: At Western Sydney University: Leading institute-wide Cognitive Neuroscience group; leading University-wide Neuroscience network; equity and diversity working group member; work-plan committee member; EEG-lab leader; member of PhD candidature confirmation panels
    <p>2021: Member of the organising committee for the Australian Cognitive Neuroscience Society conference</p>
    <p>2020: Session Chair at the international NeuroMatch3 virtual conference</p>
    <p>2019: Session Chair at the Australian Cognitive Neuroscience Society conference</p>
    <p>2019-current: Member of the Australian Cognitive Neuroscience Society executive committee (environment working group chair) <a target="_blank" href="https://www.acns.org.au/acns-committee/">https://www.acns.org.au/acns-committee/</a></p>
    <p>2018-2019: Member of the Australian Cognitive Neuroscience Society executive committee <a target="_blank" href="https://www.acns.org.au/acns-committee/">https://www.acns.org.au/acns-committee/</a></p>
    <p>2016-current: Contributor to the CoSMoMVPA multi-variate pattern analysis toolbox in Matlab <a target="_blank" href="http://www.cosmomvpa.org">www.cosmomvpa.org</a></p>
    
    <h2 class="heading">
        Lab visits
    </h2>
    <p>2024: NIH, Bethesda, USA</p>
    <p>2024: John's Hopkins University, Baltimore, USA</p>
    <p>2023: MRC-CBU Cambridge UK</p>
    <p>2023: University of Giessen, Germany</p>
    <p>2022: University of Melbourne</p>
    <p>2022: Queensland Brain Institute</p>
    <p>2020: University of Melbourne</p>
    <p>2019: MRC-CBU Cambridge UK</p>
    <p>2017: NIH, Bethesda, USA</p>
    <p>2017: University of Maryland, USA.</p>
    <p>2016: Freie Universität Berlin, Germany</p>
    <p>2016: Utrecht University, the Netherlands</p>
    </p>

    <h2 class="heading">
        Editing and reviewing services
    </h2> 
    <p>2025-current: Member of the editorial board for Scientific Reports</p>
    <p>2025: Guest editor: Journal of Vision special issue</p>
    <p>2021-current: Member of the advisory board for meta-psychology</p>
    <p>Ad-hoc Reviewer for Nature Neuroscience, Science Advances, Nature Human Behaviour, PLOS Computational Biology, Journal of Neuroscience, Nature Communications, NeuroImage, Cerebral Cortex, Human Brain Mapping, Neuroinformatics, Journal of Neuroscience Methods, Scientific Reports, PLOS One, Psychophysiology, Cognitive Science</p>
    <p>Ad-hoc Grant reviewer for Australian Research Council (ARC) and National Science Foundation (NSF)</p>

    <h2 class="heading">
        Awards and nominations
    </h2>
    <p>2023 & 2024: Nominated for the Society For Neuroscience (SFN) Young Investigator Award</p>
    <p>2021: Nominated for Early Career Researcher Award at Western Sydney University</p>
    <p>2019: Australian Cognitive Neuroscience Society Emerging Researcher Award</p>
    <p>2018: Australian Cognitive Neuroscience Society Best Poster Presentation by an Early Career Post-Doc</p>
    <p>2018: ARC Centre for Excellence in Cognition and its Disorders  Excellence in Research Student Award: Outstanding 2017 Publication ($1,000)</p>
    <p>2017: Macquarie University Faculty of Human Sciences Higher Degree Research Excellence Award ($250)</p>
    <p>2017: Australian Cognitive Neuroscience Society Best Poster Presentation by an Early Career Post-Doc</p>
    <p>2016: Australian Cognitive Neuroscience Society Student Travel Award ($250)</p>
    <p>2016: ARC Centre for Excellence in Cognition and its Disorders Annual Workshop Highly Commended Poster Award ($100)</p>
    <p>2013: Interspeech best student paper nomination</p>

    <h2 class="heading">
        Research Output
    </h2>
    <p>
        * equal contribution
    </p>
    """
out+=publisthtmlcv

out+="""
    <div class="year">
        Published conference abstracts
    </div>
    <p><strong>Grootswagers T</strong>, Robinson A, Shatek S, Carlson T (2022). The time course of visual feature coding in the human brain. <i>Perception</i>, 51, 360-360.</p>
    <p>Johnson P, <strong>Grootswagers T</strong>, Moran C, Hogendoorn H (2021) Temporal dynamics of visual population receptive fields. <i>Perception</i>, 50, 48-48</p>
    <p>Robinson A, <strong>Grootswagers T</strong>, Shatek S, Behrmann M, Carlson, T (2020). The temporal dynamics of information integration within and across the hemispheres. <i>Journal of Vision</i>, 20(11), 1016-1016.</p>
    <p>Tovar D, <strong>Grootswagers T</strong>, Robinson A, Wallace M, Carlson T (2019). Optimizing the Number of Visual Presentations for Time-Resolved Decoding Studies. <i>Perception</i>, 48, 134-134.</p>
    <p>Teichmann L, <strong>Grootswagers T</strong>, Carlson T, Rich A (2018). Tomatoes are red, cucumbers are green: Decoding the temporal dynamics of object-colour knowledge using Magnetoencephalography. <i>Journal of Vision</i>, 18(10), 861-861.</p>
    <p><strong>Grootswagers T</strong>, Cichy R, Carlson T (2016). Predicting behavior from decoded searchlight representations shows where decodable information relates to behavior. <i>Perception</i>, 45, 360-360.</p>
    <p>Contini E, Williams M, Grootswagers T</strong>, Goddard E, Carlson T (2016). Dichotomy Versus Continuum: Evidence for a More Complex Agency Model of Visual Object Categorisation. <i>Journal of Vision</i>, 16(12), 252- 252.</p>
    <p><strong>Grootswagers T</strong>, Carlson T (2015). Decoding the emerging representation of degraded visual objects in the human brain. <i>Journal of Vision</i>, 15(12), 1087-1087.</p>
"""

out+="""
    <h2 class="heading">
        Conference presentations (presenting author)
    </h2>
<p><strong>Grootswagers T</strong>, Robinson A (2024). Decoding Rapid Object Representations. Symposium presented at the Annual Meeting of the Vision Sciences Society (VSS), St. Pete Beach, FL, USA</p>
<p><strong>Grootswagers T</strong> (2024). Decoding Rapid Object Representations. Talk presented at the Annual Australasian Experimental Psychology Conference (EPC), Sydney, NSW, Australia</p>
<p><strong>Grootswagers T</strong> (2024). AI in cognitive neuroscience: pitfalls and potentials. Talk presented at the virtual Australasian Cognitive Neuroscience Society Conference (ACNS)</p>
<p><strong>Grootswagers T</strong>, Quek G, Chin J, Varlet M (2023). Using synthetic images to drive object responses in the human brain. Talk presented at the European Conference on Visual Perception (ECVP), Paphos, Cyprus</p>
<p><strong>Grootswagers T</strong>, Robinson A, Shatek S, Carlson T (2023). Dynamics of visual feature coding: Insights into perception and integration. Talk presented at the Annual Australasian Experimental Psychology Conference (EPC), Canberra, Act, Australia</p>
<p><strong>Grootswagers T</strong>, Robinson A, Shatek S, Carlson T (2022). The time course of visual feature coding in the human brain. Poster presented at the European Conference on Visual Perception (ECVP), Nijmegen, the Netherlands</p>
<p><strong>Grootswagers T</strong>, Quek G, Chin J, Sharabas D, Varlet M (2022). That's not a knife: using synthetic images to drive object responses in the human brain. Talk presented at the Australasian Brain and Psychological Sciences Conference (ABPS)</p>
<p><strong>Grootswagers T</strong>, Chin J, Sharabas D, Nguyen A, Jerebicanin E, Mamic P, Varlet M (2022). Human behavioural and neural responses to hyperrealistic AI-generated faces. Talk presented at the Australasian Society for Social and Affective Neuroscience (AS4SAN)</p>
<p><strong>Grootswagers T</strong>, McKay H, Varlet M (2021). Unique contributions of perceptual and conceptual humanness to object representations in the human brain. Talk presented at the virtual Australasian Cognitive Neuroscience Society Conference (ACNS)</p>
<p><strong>Grootswagers T</strong>, Robinson A, Shatek S, Carlson T (2021). What makes perceptual information memorable? Talk presented at the Annual Australasian Experimental Psychology Conference (EPC), Brisbane, Qld, Australia</p>
<p><strong>Grootswagers T</strong>, Robinson A, Shatek S, Carlson T (2020). The neural dynamics underlying prioritisation of task-relevant information. Talk presented at the international NeuroMatch3 virtual conference</p>
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
    <h2 class="heading">
        Talks, symposia, and workshops (selection)
    </h2>
    <p>2024: Seeing in a Flash: Neural Decoding of Rapid Object Recognition. Talk presented at National Institutes for Mental Health (NIMH), Bethesda, MD, USA</p>
    <p>2024: Seeing in a Flash: Neural Decoding of Rapid Object Recognition. Talk presented at Johns Hopkins University, Baltimore, MD, USA</p>
    <p>2024: Seeing in a Flash: Neural Decoding of Rapid Object Recognition. Talk presented at The University of New South Wales, Sydney, Australia</p>
    <p>2023: Using synthetic images to drive object responses in the human brain. Talk presented at the MRC Cognition and Brain sciences unit, Cambridge, UK</p>
    <p>2023: Using synthetic images to drive object responses in the human brain. Talk presented at the Justus Liebig University Giessen, Germany</p>
    <p>2023: Human behavioural and neural responses to hyperrealistic AI-generated content. AI Frontiers Symposium, Sydney, Australia</p>
    <p>2023: On brain decoding and representational geometry: how computational techniques are shaping our understanding of the human brain. School of Computer, Data & Mathematical Sciences Research Seminar, Western Sydney University, Australia</p>
    <p>2022: Representational Geometry in the brain. Invited Talk at the Maths in the brain workshop, Monash University, Melbourne, Australia</p>
    <p>2022: Using rapid stimulus presentation and multivariate classification to study information processing in the human brain. Talk presented at the School of Computer, Data & Mathematical Sciences, Western Sydney University, Australia</p>
    <p>2021: An empirically-driven guide on using Bayes Factors for M/EEG decoding. Talk presented in the Woolgar lab at the MRC Cognition and Brain sciences unit, Cambridge, UK</p>
    <p>2021: An overview of open-science practices, and how to adopt (some of) them in your work. Talk presented at the MARCS Institute, Western Sydney University, Australia</p>
    <p>2020: Decoding and Representational Dynamics in MEG & EEG. Talk presented at the virtual 7th Iranian Human Brain Mapping Congress</p>
    <p>2020: Can we still trust our eyes? Talk presented at the MARCS Afternoon Colloquium, Western Sydney University, Australia</p>
    <p>2020: Can we trust our eyes? Talk presented at the University of Melbourne, Australia</p>
    <p>2020: Decoding and Representational Dynamics in MEG & EEG. Talk presented at Macquarie University, Australia</p>
    <p>2020: Using rapid stimulus presentation and multivariate decoding to study information processing in the human brain. Talk presented at the MARCS Institute, Western Sydney University, Australia</p>
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
