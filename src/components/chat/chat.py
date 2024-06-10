import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 加载你微调的模型和 tokenizer
model_name = "your-fine-tuned-model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# 侧边栏（不再需要 API Key）
with st.sidebar:
    st.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)")


# 设置标题和简介
st.title("👩‍⚕️🧑‍⚕️ 医生与患者聊天")
st.caption("🚀 使用微调模型的 Streamlit 医患聊天界面")

# 初始化消息列表
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "您好，我是您的医生，请问有什么问题需要咨询？"}]

# 显示聊天记录
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 处理用户输入
if prompt := st.chat_input("请输入您的问题..."):
    # 记录用户输入
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    # 使用微调模型生成回复
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs.input_ids, max_length=500)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # 记录医生回复
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
