#!/usr/bin/python
import argparse

def wordCounter(fname,scale):
   
    fprocname='processing.txt'
 
    f_in=open(fname)
    f_process=open(fprocname,'w')
 
    wordslist={}
 
    for line in f_in:
        line=line.replace('\n',' ')
        line=line.replace('\f',' ')
        line=line.replace('\t',' ')
        line=line.replace('\v',' ')
        line=line.replace('.',' ')
        line=line.replace(',',' ')
        line=line.replace('?',' ')
        line=line.replace('!',' ')
        f_process.write(line)
   
    f_process=open(fprocname)        
 
    for line in f_process:
        s=line.split()
    for i in range(len(s)):
        amount=0
        for j in range(len(s)):
           if s[j] == s[i]:
               amount+=1
               if amount>=scale:
                   wordslist[s[i]]=amount
 
    print(wordslist)
 
    f_process.close()
    f_in.close()
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('filename', type=str, help='This is filename')
    parser.add_argument('--fromn', '-f', type=int, default=0, help='This is minimum frequency of words, default is 0')
    args = parser.parse_args()
    
    wordCounter(args.filename,args.fromn)
