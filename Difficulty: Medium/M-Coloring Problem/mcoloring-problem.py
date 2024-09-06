#User function Template for python3
#Function to determine if graph can be coloured with at most M colours such



#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    def issafe(n,kl,colr):
        for i in range(V):
            if graph[i][n]==1 and colr[i]==kl:
                return False
        return True
    def helper(v,colr,kl):
        if V==v:
            return True
        if kl>k:
            return False
        if issafe(v,kl,colr):
            colr[v]=kl
            if(helper(v+1,colr,1)):#start next with checking color from first
                return True
            colr[v]=-1
        return helper(v,colr,kl+1)

    colr=[-1]*V
    return helper(0,colr,1)
    
    
    
    #your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        V = int(input())
        k = int(input())
        m = int(input())
        l = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[l[cnt] - 1][l[cnt + 1] - 1] = 1
            graph[l[cnt + 1] - 1][l[cnt] - 1] = 1
            cnt += 2
        if (graphColoring(graph, k, V) == True):
            print(1)
        else:
            print(0)

        t = t - 1

# } Driver Code Ends