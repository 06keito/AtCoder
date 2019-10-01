import sys
import os
import shutil
f = open('input.txt', 'r')
sys.stdin = f
#--------------------------
#--------------------------
filename = 'test.py'
out = open(filename,"w")
shutil.copy("code.py",filename)
out.close()
f.close()
