#@Author:QQcoin
import jieba
from matplotlib import pyplot as plt
from wordcloud import ImageColorGenerator, WordCloud, wordcloud
from PIL import Image
import numpy as np
import sqlite3

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql='select instroduction from movie250'
data1=cur.execute(sql)
text=""
for item in data1:
    text = text +item[0]
#print(text)
cur.close()
con.close()

cut=jieba.cut(text)
string=' '.join(cut)
print(len(string))

img= Image.open(r'E:\code\Python\Flask\douban\static\image\OIP-C.jpg')
img_array=np.array(img)
wc=WordCloud(
    background_color='white',
    mask=img_array,
    font_path="msyh.ttc",
    random_state=42
)
wc.generate_from_text(string)

image_colors = ImageColorGenerator(img_array)

#绘制
fig=plt.figure(1)
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')

plt.show()