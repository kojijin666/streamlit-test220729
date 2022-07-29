import streamlit as st
import time

st.title('stremlitお勉強中')

st.write('プログレスバーの表示')
'start'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1) #ここで入力する秒数ごとにfor文がまわる

'done'
