n=input()
a=map(int,input().split())
a=list(set(a))
a.remove(max(a))
print (max(a))