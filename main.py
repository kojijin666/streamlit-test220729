from cgitb import text
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
st.title('test作成中')

st.write('チェックぼっくす')

left_column, right_column = st.columns(2)
button=left_column.button('右からむに文字を表示')
if button:
    right_column.write('ここは右からむ')
st.write('よくある問い合わせ一覧')
expander1=st.expander('これはなんですか？')
expander1.write('それは〇●ということです')
expander2=st.expander('これはなんですか？')
expander2.write('それは〇●ということです')
expander3=st.expander('これはなんですか？')
expander3.write('それは〇●ということです')

# text=st.text_input('あなたの趣味を教えてください')
# condition=st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味は、',text,'です。'
# 'コンディション:',condition,





# if st.checkbox('画像を表示するならこちらにチェック！'):
#  img = Image.open('sample.jpg')
#  st.image(img, caption='台風',use_column_width=True)

