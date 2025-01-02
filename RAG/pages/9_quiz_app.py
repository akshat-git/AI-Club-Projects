import streamlit as st
import pandas as pd

@st.cache_data
def load_csv(url):
  print("\n\n======REFRESHING")
  print(f"1. Source CSV is {url}")
  df=pd.read_csv(url)
  return df


def on_change_radio(slot):
  print(f"On-change-radio: Selection changed to {st.session_state.MAIN} ")
  #print(f"A is {a} and B is {b} and C is {c} ")
  dict_row=st.session_state["question"]
  a1=dict_row["A1"][0]
  a2=dict_row["A2"][0]
  a3=dict_row["A3"][0]
  a4=dict_row["A4"][0]
  r1=dict_row["R1"][0]
  r2=dict_row["R2"][0]
  r3=dict_row["R3"][0]
  r4=dict_row["R4"][0]
  q=st.session_state.MAIN
  print(f"in on-change-radio, q is {q}, a1 is {a1}, a2 is {a2}, a3 is {a3}, a4 is {a4}")
  print(f"Radio Slot is {slot}")
  # This is hacky. Rewrite as if-then-else-if-...
  st.session_state["additional_info"]="Please select one of the available options above"
  if q==a1:
    print("Matched a1")
    st.session_state["additional_info"]=r1
  if q==a2:
    print("Matched a2")
    st.session_state["additional_info"]=r2
  if q==a3:
    print("Matched a3")
    st.session_state["additional_info"]=r3
  if q==a4:
    print("Matched a4")
    st.session_state["additional_info"]=r4
  print(f"Finished matching in on-change-radio, with additional state={st.session_state.additional_info}")

#
# Full code
#

slot1=st.container()
slot3=st.container()
slot2=st.container()

#print(f"++++START{st.__version__}")

if slot2.button("Next question"):
  print("Next button pressed")
  del st.session_state["question"]

if "question" not in st.session_state:
  print(f"\n*** Getting next question \n")
  df=load_csv(st.secrets["QUIZ_CSV"])
  row=df.sample()
  dict_row=row.to_dict(orient='list')
  st.session_state["question"]=dict_row

dict_row=st.session_state["question"]
#print(f"2. Dict row is {dict_row}")
question=dict_row["Question"][0]
a1=dict_row["A1"][0]
a2=dict_row["A2"][0]
a3=dict_row["A3"][0]
a4=dict_row["A4"][0]
r1=dict_row["R1"][0]
r2=dict_row["R2"][0]
r3=dict_row["R3"][0]
r4=dict_row["R4"][0]
q=slot1.radio(question,(a1,a2,a3,a4),key="MAIN",index=None,on_change=on_change_radio,kwargs={"slot":slot3})
st.markdown(
    """<style>
div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {
    font-size: 24px;
}
    </style>
    """, unsafe_allow_html=True)
corr=dict_row["Correct"][0]
if "additional_info" in st.session_state:
  additional=st.session_state["additional_info"]
  print(f"Found additional info: {additional}")
  slot3.markdown(":blue["+additional+"]")
  del st.session_state["additional_info"]
#print(f"Row is {dict_row}")
#print(f"Question is {question}")
#for key in st.session_state.keys():
#  print(f"*** SESSION STATE {key} = {st.session_state[key]}")
#print("++++COMPLETE")