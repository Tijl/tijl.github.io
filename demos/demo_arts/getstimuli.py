import os,glob,sys

os.chdir(os.path.dirname(sys.argv[0]))
stims = sorted(glob.glob('stimuli/*.jpg'))

open('stimuli.js','w').write('var stimlist = ["'+'",\n"'.join(stims)+'"];')

