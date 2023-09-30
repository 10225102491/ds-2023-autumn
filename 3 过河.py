import queue
cnd=[0,0,0,2,0,0,2,2,2,2,0,0,2,0,0,0] #not visited = 0, visiting = 1,visited=2
node = queue.Queue()
prev = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
dic = ["狼","羊","菜"]
def show(opt):
    if opt == 1<<3:
        print("人过河")
    else:
        i=0
        while (opt>>i)&1!=1 :
            i = i + 1
        print("人带{}过河".format(dic[i]))
def change(t,i):
    bit1=int(not(t>>3)) 
    return t&~(1<<i)&~(1<<3)|(bit1<<i)|(bit1<<3)
def dfs(t,ans):
    if t == 0:
        for i in ans:
            show(i)
        print("")
        return
    for i in range(len(prev[t])):
        temp1=ans.copy()
        temp1.append(prev[t][i])
        dfs(t^prev[t][i],temp1)
t=0
node.put(0)
nodet = queue.Queue()
while len(prev[0xF])==0:          #bfs
    while(not node.empty()):
        t=node.get()
        for i in range(4):
            temp=change(t,i)
            if cnd[temp]!=2 and not (t^temp in prev[temp]):
                prev[temp].append(t^temp)
                if cnd[temp]==0:
                    nodet.put(temp)
                    cnd[temp]=1
    while(not nodet.empty()):
        node.put(nodet.get())
    for i in range(16):
        if cnd[i] == 1:
            cnd[i] = 2
dfs(0xf,[])
        
    
        