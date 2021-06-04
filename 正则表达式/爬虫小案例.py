path = '''<img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fcdn.duitang.com%2Fuploads%2Fitem%2F201410%2F20%2F20141020162058_UrMNe.jpeg&amp;refer=http%3A%2F%2Fcdn.duitang.com&amp;app=2002&amp;size=f9999,10000&amp;q=a80&amp;n=0&amp;g=0n&amp;fmt=jpeg?sec=1625033647&amp;t=4e8db2265543af4a801765a50e96a4cd" width="311.70661157025" height="313" style="top: 0px; left: 270px; width: 288.802px; height: 290px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">'''

import requests
import re

url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fcdn.duitang.com%2Fuploads%2Fitem%2F201410%2F20%2F20141020162058_UrMNe.jpeg&refer=http%3A%2F%2Fcdn.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1625035190&t=5fe69e9913ff921e6387486457ebfd9c'
response = requests.get(url)
with open('a.jpg', 'wb') as wstream:
    wstream.write(response.content)
