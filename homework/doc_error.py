def write_t():
    we=input("诗句：")
    f=open("gushi.txt","w")
    f.write(we)
    f.close()

def read_t():
    f=open("gushi.txt","r")
    content_t=f.read()
    o=open("copy.txt","w")
    o.write(content_t)
    o.close()
    o=open("copy.txt","r")
    t=o.read()
    print(t)
    o.close()
    print("复制完毕")
    f.close()
    
if __name__ == "__main__": 
    write_t()
    read_t()