print("|===============================|")
print("|MINIMUM EDIT DISTANCE PROTOTYPE|")
print("|ANITA DYAH PERTIWI      1401309|")
print("|===============================|")

word1=input("Put your first text here: ")
word2=input("Put your second text here: ")

#min_ed is a function to find minimum edit distance from 2 words that has input by user, 
def min_ed(s1, s2):
    len_1=len(word1)    
    len_2=len(word2)

    x =[[0]*(len_2+1) for _ in range(len_1+1)]#the matrix whose last element ->edit distance
    for i in range(0,len_1+1): 
        x[i][0]=i
    for j in range(0,len_2+1):
        x[0][j]=j
    for i in range (1,len_1+1):
        for j in range(1,len_2+1):
            if word1[i-1]==word2[j-1]:
                x[i][j] = x[i-1][j-1] 
            else :
                x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1 #minimum edit distance
    return x #matrix of edit distance

len1 = len(word1)
len2 = len(word2)
print("Result:")
print(end="")
print("MED : ",end="")
print (min_ed(word1, word2)[len1][len2])
valueMED = min_ed(word1,word2)

#class operasi has function to accomodate attributes needed.
class Operasi:
  i = 0
  j = 0
  operasi = 0 

#backTrace is a function to find what's operation happened to the text, is it deletion, substitution, insert, or equal
def backTrace(x,len1,len2):
    # x =[[0]*(len_2+1) for _ in range(len_1+1)
    y = [Operasi() for i in range(0,len1+len2)]

    seq = 0
    i = len1
    j = len2
    while i>=0 and j>=0:
        if i-1>=0 and j-1>=0:
            #small = 0
            small = min(x[i][j-1],x[i-1][j],x[i-1][j-1])
            if small == x[i-1][j-1]:
                if x[i][j] == x[i-1][j-1]:
                    y[seq].i = i
                    y[seq].j = j
                    y[seq].operasi = 4
                    i=i-1
                    j=j-1
                else:
                    y[seq].operasi = 3
                    y[seq].i = i
                    y[seq].j = j
                    i=i-1
                    j=j-1
                    
            elif small == x[i-1][j]:
                y[seq].operasi = 2
                y[seq].i = i
                y[seq].j = j
                i=i-1
            elif small == x[i][j-1]:
                y[seq].operasi = 1
                y[seq].i = i
                y[seq].j = j
                j=j-1
        else:
            #condition if in top or left ends
            if i-1<0:
                y[seq].operasi = 1
                y[seq].i = 0
                y[seq].j = j
                j=j-1
            elif j-1<0: 
                y[seq].operasi = 1
                y[seq].i = i
                y[seq].j = j
                j=j-1

        seq=seq+1        

    return y;

#print matrix
print("|======|");
print("|Matrix|");
print("|======|");
for i in range(0,len1+1):
    for j in range(0, len2+1):
        if(i==0):
            if(j == 0):
                print("#",end="")
            else:    
                print(" ",word2[j-1],end="")
        else:
            if(j == 0):
                print(word1[i-1],end="")
            else:    
                print(" ",valueMED[i-1][j-1],end="")
        
    print("")
    
test = backTrace(valueMED,len1,len2);
count = 0

#print alignment
print("|=========|");
print("|Alignment|");
print("|=========|");
for op in test:
    if(op.operasi != 0):
        count = count + 1
    
for i in range(count-2,-1,-1):
    if(test[i].operasi == 2):
        print("#",end='')
    else:
        print(word2[test[i].j-1],end='')
print("")

for i in range(count-2,-1,-1):
    print("|",end='')

print("")
for i in range(count-2,-1,-1):
    if(test[i].operasi == 1):
        print("#",end='')
    else:
        print(word1[test[i].i-1],end='')


