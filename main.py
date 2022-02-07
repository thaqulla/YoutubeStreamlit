import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

st.write("pregress_bar!")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

st.write("Dataframe")

df = pd.DataFrame(
  np.random.rand(100, 2)/[50,50]+[35.69,139.70],
  columns=["lat","lon",]
)



st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))

# st.line_chart(df)
# st.area_chart(df)
st.map(df)

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
  
  
"""

st.write("Image")



if st.checkbox("showImage"):
  img = Image.open("IMG_4448.png")
  st.image(img, caption="test", use_column_width=True)

st.video("IMG_5585.MP4" ,format="video/mp4", start_time=0)

option = st.sidebar.selectbox(
  "あなたが好きな数字を教えてください",
  list(range(1,11))
)

"あなたの好きな数字は",option,"です。"

text = st.sidebar.text_input("あなたの趣味を教えてください")

"貴方の趣味は",text

condition = st.sidebar.slider("How do you feel ?",0,100,50) #50%start

"condition",condition

expander1 = st.expander("お問い合わせ1")
expander1.write("問い合わせ1の回答")
expander2 = st.expander("お問い合わせ2")
expander2.write("問い合わせ2の回答")
expander3 = st.expander("お問い合わせ3")
expander3.write("問い合わせ3の回答")

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
  right_column.write("ここは右カラム")
  
