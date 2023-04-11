import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
from matplotlib.ticker import MaxNLocator
from gtts import gTTS
from pygame import mixer
import time


def read_audio(file):
    with open(file, "rb") as audio_file:
        audio_bytes = audio_file.read()
    return audio_bytes


# サイド画面
st.markdown(f'''
    <style>
    section[data-testid="stSidebar"] .css-ng1t4o {{width: 14rem;}}
    </style>
''',unsafe_allow_html=True)
st.sidebar.markdown('パラメータ設定')
right_notes = st.sidebar.number_input('検証用パラメータ', value=255)

# メイン画面
css = """
<style>
.text-center {
    text-align: center;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)
st.title("MIDI ノーツの分布")
st.header('')
st.header('サーバへのアクセスを停止し、ダミーデータを表示してます')
st.header('')

if 'clic_count' not in st.session_state:
    st.session_state["clic_count"] = 1
else :
    st.session_state["clic_count"] += 1

a_data = []
m_data = []

# GETリクエスト
# endpointのアクセス先も削除済み
endpoint = 'removed'
request_data= {
    'data_name': 'test_data',
    'data_version': '005',
}

url= endpoint
#res= requests.get(
#    url,
#    data = json.dumps(request_data)
#)
#st.write("res : ", res )

#res_json = res.json()
#a_data = res_json["data"]["accomp"]
#m_data = res_json["data"]["melody"]

a_data = [48, 48, 48]
m_data = [60, 60, 60]

# デバック情報
#st.write("Load Count : ", st.session_state["clic_count"] )
#st.write("check_a : ", a_data )
#st.write("check_m : ", m_data )

# グラフ設定
#sns.set(font_scale=0.8)
sns.set(font_scale=1)
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.set_xticks(np.arange(35, 108, 1))
#ax.set_xticks(np.arange(48, 83, 1))

#bins = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
#        55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
#        74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
#        93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]
bins = [48, 49, 50, 51, 52, 53, 54,
        55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73,
        74, 75, 76, 77, 78, 79, 80, 81, 82, 83, ]
#bins = [48, 49, 50, 51, 52, 53, 54,
#        55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, ]

sns.distplot(a_data, ax=ax, label='', kde=False, bins=bins)
#sns.distplot(a_data, ax=ax, label='', kde=False, bins=range(37, 48, 84))
#sns.distplot(a_data, ax=ax, label='', kde=False, bins=range(49, 72, 1))
sns.distplot(m_data, ax=ax, label='', kde=False, bins=bins)

ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_ylabel('count', fontsize='medium', labelpad=10)
ax.set_xlabel('MIDI note number (C4 = 60)', fontsize='medium', labelpad=20)
ax.set_title('', fontsize='xx-large')

#fig.tight_layout()

st.pyplot(fig)

# ボタン設定
st.header('')
button_css = f"""
<style>
  div.stButton > button:first-child  {{
    display: block;
    border       :  2px solid #f36     ;
    border-radius: 10px 10px 10px 10px ;
    width: 320px;
    height: 32px;
  }}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)
if st.button("解析", key=0):
    st.session_state["clic_count"] += 0
    
    test_tts = '長い文章だとTTSの再生にどのくらいの時間がかかるか確認しようと思います。なので、とりあえずダラダラと文章をつづっています。むしろ徒然なるままに何とやらという感じで文章を書いています。この位の文字数だと200文字くらいでしょうか。このくらいの長さでなめらかに再生できるといろいろと活用場面が広がるかなと思います。'
    
    tts1 = gTTS(text=test_tts, lang='ja')
    tts1.save('tes_tts.mp3')
    
    # streamlit版
    #st.audio(read_audio('tes_tts.mp3'))
    
    # HTML版
    ####audio_placeholder = st.empty()
    #contents = read_audio('tes_tts.mp3')

    #audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
    ####audio_html = """
    ####                <audio autoplay=True>
    ####                <source src="tes_tts.mp3" type="audio/mp3" autoplay=True>
    ####                Your browser does not support the audio element.
    ####                </audio>
    ####            """

    ####audio_placeholder.empty()
    ####time.sleep(0.5)
    ####audio_placeholder.markdown(audio_html, unsafe_allow_html=True)
    
    audio_placeholder = st.empty()
    audio_html = """
                    <audio controls autoplay src="tes_tts.mp3" type="audio/mp3">テストTTS</audio>
                """
    audio_placeholder.empty()
    time.sleep(0.5)
    audio_placeholder.markdown(audio_html, unsafe_allow_html=True)
    
    
    #mixer.init()
    #mixer.music.load('tes_tts.mp3')
    #mixer.music.play()
    #time.sleep(5)
    
