import streamlit as st

st.set_page_config(page_title="iOS Calculator", page_icon="🧮", layout="centered")

# --- CSS styling ---
st.markdown("""
    <style>
    body {
        background-color: white;
    }
    .stButton button {
        width: 100px;
        height: 100px;
        font-size: 60px;
        font-weight: bold;
        border-radius: 50%;
        margin: 5px;
        border: 2px solid #444;
    }
    /* Number buttons */
    .num button {
        background-color: #333333;
        color: white;
    }
    /* Operator buttons */
    .op button {
        background-color: #ff9f0a;
        color: white;
    }
    /* Function buttons */
    .func button {
        background-color: #a5a5a5;
        color: black;
    }
    /* Result display */
    .result-box {
        font-size: 50px;
        text-align: right;
        padding: 20px;
        border: 2px solid #666;
        border-radius: 12px;
        background-color: black;
        color: white;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Calculator")

# --- Session state ---
if "calc" not in st.session_state:
    st.session_state.calc = ""

def press(symbol):
    if symbol == "AC":
        st.session_state.calc = ""
    elif symbol == "=":
        try:
            st.session_state.calc = str(eval(st.session_state.calc))
        except:
            st.session_state.calc = "Error"
    else:
        st.session_state.calc += str(symbol)

# --- Display ---
st.markdown(f'<div class="result-box">{st.session_state.calc}</div>', unsafe_allow_html=True)

# --- Button layout ---
buttons = [
    ["AC", "%", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", ""]
]

for row in buttons:
    cols = st.columns(4)
    for i, symbol in enumerate(row):
        if symbol == "":
            continue
        css_class = "num"
        if symbol in ["AC", "%"]:
            css_class = "func"
        elif symbol in ["/", "*", "-", "+", "="]:
            css_class = "op"

        with cols[i]:
            st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
            st.button(symbol, on_click=press, args=(symbol,))
            st.markdown('</div>', unsafe_allow_html=True)
