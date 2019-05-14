#四位玫瑰数
if __name__=='__main__':
    for i in range(1,10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    a=i*1000+j*100+k*10+l
                    if pow(i,4)+pow(j,4)+pow(k,4)+pow(l,4)==a:
                        print(a)