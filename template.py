import sys
import os
import shutil
f = open('input.txt', 'r')
sys.stdin = f
#--------------------------

"""
write your codes
"""

#--------------------------
filename = 'template.py'#ファイルネームを書いてくれ
out = open(filename,"w")
shutil.copy("code.py",filename)
out.close()
f.close()
