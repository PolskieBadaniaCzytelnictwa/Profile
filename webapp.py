import streamlit as st
import os
os.chdir(os.path.dirname(__file__))


st.set_page_config(page_title="Profile czytelników", page_icon=":book:")
st.markdown("<h1 style='margin-top: -80px; text-align: center;'>Profile czytelników</h1>", unsafe_allow_html=True)
st.markdown('---')

image_html = """
<img src="https://raw.githubusercontent.com/PolskieBadaniaCzytelnictwa/Profile/main/profile_wykres.png" alt="Profile czytelnikow" usemap="#imageMap">
<map name="imageMap">
    <area shape="rect" coords="250,44,290,146" href="https://www.pbc.pl/badane-tytuly/?filtry=dzienniki-ogolnopolskie" alt="Link 1" target="_blank">
    <area shape="rect" coords="305,46,345,144" href="https://www.pbc.pl/badane-tytuly/?filtry=dzienniki-regionalne" alt="Link 2" target="_blank">
    <area shape="rect" coords="360,46,400,144" href="https://www.pbc.pl/badane-tytuly/?filtry=opinii-spoleczno-polityczne,tygodniki" alt="Link 3" target="_blank">
    <area shape="rect" coords="415,46,455,144" href="https://www.pbc.pl/badane-tytuly/?filtry=telewizyjne" alt="Link 4" target="_blank">
    <area shape="rect" coords="470,44,510,146" href="https://www.pbc.pl/badane-tytuly/?filtry=kobiece-luksusowe" alt="Link 5" target="_blank">
    <area shape="rect" coords="525,44,565,146" href="https://www.pbc.pl/badane-tytuly/?filtry=kobiece-poradnikowe" alt="Link 6" target="_blank">
    <area shape="rect" coords="580,36,620,152" href="https://www.pbc.pl/badane-tytuly/?filtry=poradniczo-rozrywkowe" alt="Link 7" target="_blank">
    <area shape="rect" coords="690,50,730,138" href="https://www.pbc.pl/badane-tytuly/?filtry=people" alt="Link 8" target="_blank">
</map>
"""
st.markdown(image_html, unsafe_allow_html=True)

src = 'Źródło: Prasa drukowana, e-wydania, subskrypcje cyfrowe - PBC Zaangażowanie w reklamę, CCS 10.2021-09.2023. N = 46 942, wiek 15-75'
st.markdown(f"""<div style="font-size:12px">{src}</div>""", unsafe_allow_html=True)
