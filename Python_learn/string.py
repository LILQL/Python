#引号
word = 'zifuchuan'
sentence = "senTencent \"bb\""
pra = '''dasd
dsf
sad
fdsg
dfs
gfdg
'''
'''
a=[word,sentence,pra]

for i in range(len(a)):
    print(a[i])
'''
#字符串的截取
str ="chengdu"
print(str)
print(str[0])
print(str[0:5])
print(str[1:7:2]) 
print(str[4:])
print(str[:6])

#转译字符 "\"
print(r"hello\nworld") #'r'让字符串中的转义字符失效

