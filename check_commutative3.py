# define a function
def compose(args):
    o1 = digit_to_op(args[0])
    o2 = digit_to_op(args[1])
    o3 = digit_to_op(args[2])
    return superposition(o1,o2,o3)

def unary(args):
    o = digit_to_op(args[0])
    o1 = [[0,0,0],[0,0,0],[0,0,0]]
    res=0
    for i in range(0,3):
        for j in range(i+1,3):
            o1[i][j] = o[o[o[i][j]][i]][o[o[i][j]][j]]
            res = 3*res+o1[i][j]
    return res
    
def unary2(args):
    o = digit_to_op(args[0])
    o1 = [[0,0,0],[0,0,0],[0,0,0]]
    res=0
    for i in range(0,3):
        for j in range(i+1,3):
            xy = o[i][j]
            xyx = o[xy][i]
            xyxy = o[xyx][j]
            yx = xy
            yxy = o[yx][j]
            yxyx = o[yxy][i]
            o1[i][j] = o[xyxy][yxyx]
            res = 3*res+o1[i][j]
    return res
    
def digit_to_op(dig):
    op = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(2,-1,-1):
        op[i][i] = i
        for j in range(2,i,-1):
            op[i][j] = dig%3
            op[j][i] = dig%3
            dig = int(dig/3)
    return op

def superposition(o1,o2,o3):
    o = [[0,0,0],[0,0,0],[0,0,0]]
    res=0
    for i in range(0,3):
        for j in range(i+1,3):
            o[i][j] = o1[o2[i][j]][o3[i][j]]
            res = 3*res+o[i][j]
    for i in range(0,3):
        for j in range(0,3):
            o[i][j] = o1[o2[i][j]][o3[i][j]]
    return res



def compute_degree():
    cur = range(27)
    is_in_range = range(27)
    pro = 1
    count = 0
    while(pro):
        count = count+1
        pro=0
        res = []
        for i in cur:
            out = unary([i])
            res.append(out)
        cur = res
        for i in range(27):
            is_in_range[i]=0
        for i in range(27):
            if cur[i]==i:
                is_in_range[i]=1
        for i in range(27):
            if is_in_range[cur[i]] != 1:
                pro = 1
    n = 0
    num_to_index = range(27)
    index_to_num = range(27)
    for i in range(27):
        if is_in_range[i]:
            num_to_index[n]=i
            index_to_num[i]=n
            n=n+1
    print count
    return [n,cur,index_to_num,num_to_index]

N,Table,Index_to_num,Num_to_index = compute_degree()

def reduct_ternary(args):
    Args = [Num_to_index[args[0]], Num_to_index[args[1]], Num_to_index[args[2]]]   
    res = Table[compose(Args)] 
    return Index_to_num[res]

def twisted(args):
    reduct_ternary([args[0], args[0], args[1]])


def check_twisted():
    for i in range(N):
        for j in range(N):
            if twisted([i,j])!=twisted([j,i]):
                print "Not really"
#            if twisted([i,i,j])!=twisted([i,j,i]):
#                print "Not really"

check_twisted()
