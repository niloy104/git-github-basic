def mx(*args):
    hg=0
    for i in args:
        if i>hg:
            hg=i
    return hg


list =[5,10,15]

ans=mx(*list)
print(ans)
