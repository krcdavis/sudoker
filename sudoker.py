#generally, i is field-place  and n is value ok

class Sudoker(object):
    def __init__(self,st):
        if len(st)!=81:
            pass
            #ABOART
        else:
            self.things=st
            self.prev=st
            self.unmodified=st

    def __str__(self):
        st="-------------"
        for n in range(0,7,3):
            for m in range(0,26,3):
                if m%9==0: st=st+'\n|'
                st=st+self.things[n*9+m:n*9+m+3]+'|'
                
            st=st+"\n-------------"
            
        return st

    def index(self,row,col): return self.things[row*9 + col]

    def subbox(self,r,c):
        #r c 0-2
        #start at each *3, ret 9 chars
        row=r*3
        col=c*3
        st=""
        for x in range(col,col+3):
            for y in range(row,row+3):
                st=st+self.index(y,x)
        return st

    def subboxcheck(self,r,c,n):
        #n is 1-9 or .
        #get subbox, check
        tempbox=self.subbox(int(r/3),int(c/3))
        #return place in string or not
        return tempbox.find(str(n))!=-1

    def rowcheck(self,row,n): return self.things[row*9:row*9+9].find(str(n))!=-1

    def colcheck(self,col,n):
        #e
        j=False
        for ay in range(col,81,9):#step
            if self.things[ay]==str(n): j=True
        return j

    def rowfromindex(self,n): return int(n/9)

    def colfromindex(self,n): return n%9

    def subboxfromindex(self,n): return self.rowfromindex(n)/3,self.colfromindex(n)/3

    def subboxfromrc(self,r,c): return r/3,c/3

    def seti(self,i,n):
        self.things=self.things[:i]+str(n)+self.things[i+1:]

    def point_solve(self,i):
        #if a single place in field is empty, check row/col/sbox for one value possible
        if self.things[i]!='.': return
        g=0
        r=self.rowfromindex(i)
        c=self.colfromindex(i)
        #sr,sc=self.subboxfromindex(i)
        for n in range(1,10):
            #yes those subbox vals are fine ok
            if not self.subboxcheck(r,c,n) and not self.rowcheck(r,n) and not self.colcheck(c,n):
                if g==0:g=n
                else: return
        #if only one number was found...
        if g!=0: self.seti(i,g)
            

    def solveloop(self):
        for lmao in range(0,81):
            self.point_solve(lmao)

        for ay in range(9):#rows
            for lmao in range(1,10):#n
                self.rowplace(ay,lmao)

        if self.things==self.prev:
            return False
        else:
            self.prev=self.things
            return True

    def rowplace(self,r,n):
        #if val n not yet in row, check for one possible place
        if self.rowcheck(r,n): return
        temp=[True,True,True,True,True,True,True,True,True]
        for ayy in range(9):
            if self.things[r*9+ayy]!='.' or self.colcheck(ayy,n): temp[ayy]=False
        for kek in range(0,8,3):
            if self.subboxcheck(r,kek,n):
                temp[kek]=False
                temp[kek+1]=False
                temp[kek+2]=False
        yk=-1
        for gay in range(9):
            if temp[gay]:
                if yk==-1: yk=gay
                else: yk=-2
        if yk>=0:
            self.seti(r*9+yk,n)
        #print(n,temp)


    def colplace(self,c,n):
        #if val n not yet in col, check for one possible place
        if self.colcheck(c,n): return
        temp=[True,True,True,True,True,True,True,True,True]
        for ayy in range(9):
            if self.things[ayy*9+c]!='.' or self.rowcheck(ayy,n): temp[ayy]=False
                
        for kek in range(0,8,3):
            if self.subboxcheck(kek,c,n):
                temp[kek]=False
                temp[kek+1]=False
                temp[kek+2]=False

        yk=-1
        for gay in range(9):
            if temp[gay]:
                if yk==-1: yk=gay
                else: yk=-2

        if yk>=0:
            self.seti(r*9+yk,n)
            
        #print(n,temp)

    
def main():
    sd=Sudoker("7..53.1...14...3.7.5.7..6.42...45..3.9..8..4.5..17...61.9..8.6.6.2...53...5.61..8")
    print(sd)
    ayy=True
    while(ayy):
       ayy=sd.solveloop()
    print(sd)


if __name__ == "__main__":
    main( )
