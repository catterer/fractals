#!/usr/bin/python3
import argparse
 
def wordCounter(fname,amount):
   
    f_in=open(fname)
 
    wordlist={}
 
    for line in f_in:
        line=line.replace("\n"," ")
        line=line.replace("\f"," ")
        line=line.replace("\t"," ")
        line=line.replace("\v"," ")
        line=line.replace("."," ")
        line=line.replace(","," ")
        line=line.replace("?"," ")
        line=line.replace("!"," ")
       
        s=line.split()
        for i in range(len(s)):
            if s[i] in wordlist:
                    wordlist[s[i]]+=1
            else:
                    wordlist[s[i]]=1
    for word in wordlist:
        if wordlist[word]>=amount:
                print('{}: {}'.format(word, wordlist[word]))
    f_in.close()
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
   
    parser.add_argument('filename', type=str, help='This is filename')
    parser.add_argument('--fromn', '-f', type=int, default=0, help='This is minimum frequency of words, default is 0')
    args = parser.parse_args()
   
wordCounter(args.filename,args.fromn)
