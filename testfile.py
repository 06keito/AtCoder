import sys
import os
import shutil
f = open('input.txt', 'r')
sys.stdin = f
#--------------------------

print("hello")


#--------------------------
filename = 'testfile.py'#ファイルネームを書いてくれ
out = open(filename,"w")
shutil.copy("code.py",filename)
out.close()
f.close()
