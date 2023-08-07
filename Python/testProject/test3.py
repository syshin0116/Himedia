class MyMatrix:
    def getNewMatrix(self, N):

        if type(N) != int or N < 3 or N % 2 ==0:
            return -1
        else:
            mid = (N // 2)
            result = []
            for i in range(1,N+1):
                row = []
                for j in range(1,N+1):
                    if i == mid and j == mid:
                        row.append(N * N)
                    elif i<=mid:
                        if j<= mid:
                            row.append(N ** min(j,i))
                        elif j> mid:
                            row.append(N ** max(N-i,N-j))
                    elif i>mid:
                        if j<= mid:
                            row.append(N ** min(j,i))
                        elif j> mid:
                            row.append(N ** min(N-i,N-j))
                    else:
                        row.append(N ** min(N-i,N-j))
                result.append(row)

            return result

class New:
    def Method(self,a):
          self.helppp = a
          return self.helppp

if __name__ == '__main__':

    new = New()
    print(new.Method("aaa"))
    print(new.helppp)

