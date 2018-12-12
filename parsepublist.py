#!/usr/bin/python

out="""
    <body>
        <div id="all">
            <div class="heading">
                Tijl Grootswagers
            </div>
            <div class="header"> 
            <p>
 		            <br>
                    Postdoctoral Research Associate
                    <br>
                    School of Psychology
                    <br>
                    The University of Sydney
                    <br>
                    </p>
                    <div class="emailaddress">
                    tijl.grootswagers@sydney.edu.au
                    </div>
            </div>
            <div class="heading">
                Research
            </div>
            <p>
              
            </p>
            
        </div>

    <div class="heading">
        Publications
    </div>
    <i>*</i> indicates equal contribution
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

def formatpub(e):
    [year,authors,title,journal,pages,link]=e   
    
    fs = '%s%s. %s. <i>%s</i>, %s %s<br><br>'%(
        authors.replace('Grootswagers T','<strong>Grootswagers T</strong>'),
        ' (%s)'%year.replace('inpress','in press').replace('preprint',''),
        title,
        journal,
        pages,
        '<a target="_blank" href="%s">[link]</a>'%link)
    
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
    </div>
    </body>
"""

with open('index.html','w') as f:
    f.write(out)
