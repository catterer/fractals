#!/usr/bin/python3
fname="Drosophila.txt"
foutname="counterSimonova.txt"
f_in=open(fname)
f_out=open(foutname,"w")
 
cAT=0
cGC=0
cTA=0
cCG=0
 
for line in f_in:
    if line.startswith("##"):
            continue
    else:
        s=line.split(";")
     
        if s[1].find("seq=T")>0 and s[3].find("seq=A")>0 :
            cAT+=1
        if s[1].find("seq=C")>0 and s[3].find("seq=G")>0 :
            cGC+=1
        if s[1].find("seq=A")>0 and s[3].find("seq=T")>0 :
            cTA+=1
        if s[1].find("seq=G")>0 and s[3].find("seq=C")>0 :
            cCG+=1
 
f_out.write("A->T Replaced "+str(cAT)+" times.\n")
f_out.write("G->C Replaced "+str(cGC)+" times.\n")
f_out.write("T->A Replaced "+str(cTA)+" times.\n")
f_out.write("C->G Replaced "+str(cCG)+" times.\n")
 
f_out=open(foutname)
for line in f_out:
    print(line)
 
f_out.close()
f_in.close()
