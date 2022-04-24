ll = [0,2,4,6,8,10, 12, 14, 16]
a = self.BigVectList[0,:]*0


for elem in ll:
    a += self.BigVectList[elem,:]

plt.plot(self.tList, a); plt.show()