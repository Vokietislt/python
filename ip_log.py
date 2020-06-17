
def pList () :
    i = 1
    s = []
    try:
        with open("ip.log") as f:
            for line in f:
                s.append(line)
    except IOError:
        print("File is missing!")
    for x in range (len(s)):
            f=s[x].split("\n")
            l=f[0].split(" ")
            l.append(f[1])
            l.insert(0,i)
            i+=1
            s[x]=l
    for x in range (len(s)):
        print("%-2s | %-15s | %-5s | %-4s" %(s[x][0],s[x][1] , s[x][2],s[x][3]))
    print("Delete (d+index),\nadd (a) ,\nsort according field  (s+[1-3]),\nmark/unmark x (m+index), \nedit ip (e), \nreset counter (r+index)")

def wFile(s,name):
  listToStr=""
  for x in range (len(s)):
    listToStr += ' '.join([str(elem) for elem in s[x]])+"\n"
    with open(name,'w') as f:
     f.write(listToStr)

def add():
    ip= input("Add IP adress x.x.x.x: ")
    count= input("What's the count: ")
    mark= input("Is it marked (Y/N): ")
    if mark == "Y" or mark == "y":
        mark = "x"
    else:
        mark = ""
    s=ip+" "+count+" "+mark+"\n"
    try:
        f= open("ip.log",'a')
        f.write(s)
    except IOError:
        print("something went wrong")

def dele (index):
    i=1
    s=[]
    try:
        convert = int(index)
    except ValueError:
        print("wrong index input")
    with open('ip.log',"r") as f:
        for line in f:
            if convert != i :
                s.append(line)
                i+=1
            else:
                i+=1
    with open('ip.log', 'w') as f:
        for x in range (len(s)):
            f.write(s[x])
def sort (index):
    index = int(index)
    s=fix()
    if index == 1 or index == 3:
        f=sorted(s, key=lambda item:str(item[index-1]))
    elif index == 2:
        f=sorted(s, key=lambda item:int(item[index-1]))
    else:
        print("wrong index")
    wFile(f,'ip.log')
def fix():
    s=[]
    with open('ip.log','r') as f:
        for line in f:
            s.append(line)
        for x in range (len(s)):
            s[x]=s[x].replace("\n","")
            s[x]=s[x].split(" ")
            if len(s[x])<3:
                s[x].append(" ")
    return s
def mark(index):
    s=[]
    f=[]
    index = int(index)
    indexFile = 1
    s=fix()
    for x in range (len(s)):
        if index == indexFile:
            if "x" in s[x][2]:
                s[x][2]= ""
            else:
                s[x][2]='x'
        indexFile+=1
    wFile(s,'ip.log')
def edit ():
    l= int(input("Select  line to edit [index]: "))
    r = int(input("Select  row to edit [ip-1, count-2,]: "))
    if (0<r<3):
        s=fix()
        s[l-1][r-1]=input("Input: ")
        wFile(s,'ip.log')
    else:
        print("WRONG INPUT")

def reset(index):
    index=int(index)
    s=fix()
    for x in range(len(s)):
        if x==index-1:
            s[x][1]="0"
    wFile(s,'ip.log')

pList()
l = input()
while(l != 0):
    if (l[0]=="a"):
        add()
    elif (l[0]=="d"):
        dele(l[1:])
    elif(l[0]=="s"):
            try:
                convert = int(l[1:])
                if(0<convert<4):
                    sort(convert)
                else:
                    print("\nwrong input. choose [1-3]")
            except ValueError:
                print("\nwrong input. choose [1-3]")
    elif(l[0]=="m"):
        try:
            mark(l[1:])
        except ValueError:
                    print("\nwrong input. [m+index]")

    elif(l[0]=="e"):
        edit()
    elif(l[0]=="r"):
        reset(l[1:])
    else:
        print("Wrong input")

    pList()
    l = input()
