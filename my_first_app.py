# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 23:35:48 2025

@author: X1C2018
"""

import streamlit as st

st.title("我的首个Web应用")
user_input = st.text_input("请输入内容")
if user_input:
    st.success(f"您输入了: {user_input}")

st.button("点击测试")