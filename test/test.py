if __name__=='__main__':
        a=lambda x:x%2
        r=filter(a,[0,1,2,3,4])
        print(type(r))
        for item in r:
                print(item)