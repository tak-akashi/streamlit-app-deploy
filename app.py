import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数読み込み
load_dotenv()

# Streamlit Cloudの場合はst.secretsから取得
if 'OPENAI_API_KEY' in st.secrets:
    api_key = st.secrets['OPENAI_API_KEY']
 # ローカル開発時は.envファイルから取得（オプション）
else:
    api_key = os.getenv("OPENAI_API_KEY")

# 回答生成関数
def generate_response(role, user_input):
    system_msg = SystemMessage(content=f"あなたは{role}の専門家です。質問に優しく丁寧に答えてください。")
    human_msg = HumanMessage(content=user_input)
    chat = ChatOpenAI(temperature=0.7, openai_api_key=api_key)
    response = chat([system_msg, human_msg])
    return response.content

# Streamlit UI
st.title("💡 LLM専門家チャットアプリ")
st.write("👇 専門家を選んで、質問を入力してください")

role = st.radio("専門家を選択", ("医療の専門家", "法律の専門家", "ITコンサルタント"))
user_input = st.text_input("あなたの質問は？")

if st.button("送信"):
    if user_input:
        answer = generate_response(role, user_input)
        st.markdown(f"### 回答:\n{answer}")
    else:
        st.warning("質問を入力してください。")
