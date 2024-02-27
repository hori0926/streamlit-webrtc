#面接前の設定の画面


#まだ適当なので後々修正
import streamlit as st
import subprocess

# 面接を始める関数の定義
def start_interview(company, position, ideal_candidate):
    # ここで、入力された情報を利用して何か処理を行うことができます
    # 例えば、これらの情報をログに記録したり、他の関数に渡して処理を行ったりすることができます
    # この例では単に情報を表示しています
    st.success(f"面接を開始します：{company}, {position}, {ideal_candidate}")
    # interview_ongoing.pyへの画面遷移（仮のコード、実際の画面遷移方法に合わせて修正が必要）
    subprocess.run(["streamlit", "run", "interview_ongoing.py"])

# Streamlitのレイアウト設定
st.title("面接練習の設定")

# 希望する企業とその役職の名前を入力するフィールド
company_name = st.text_input("希望する企業名")
position_name = st.text_input("希望する役職名")

# 志望先が求める人材像を入力するフィールド
ideal_candidate_description = st.text_area("志望先が求める人材像")

# 「面接を始める」ボタンとその動作
if st.button("面接を始める"):
    start_interview(company_name, position_name, ideal_candidate_description)
