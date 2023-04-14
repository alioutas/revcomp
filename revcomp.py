import streamlit as st

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# # Make a function that will reverse complement a DNA sequence
def revcomp(seq):
    # check if seq is a DNA sequence, must contain only A, T, C, G and N
    if not set(seq.upper()).issubset(set('ATCGN')):
        st.error('Not a DNA sequence, must contain only A, T, C, G and N')
        return
    seq = seq.upper()
    seq = seq.replace('A', 't')
    seq = seq.replace('T', 'a')
    seq = seq.replace('C', 'g')
    seq = seq.replace('G', 'c')
    seq = seq.upper()
    seq = seq[::-1]
    return seq

st.title('Reverse Complement DNA Sequence')
st.markdown('###### by Antonios Lioutas')
st.markdown('---')

# Get the DNA sequence from the user
seq = st.text_input('Enter your DNA sequence')

# # If the user has entered a sequence, then show the reverse complement
# keep on showing reverse complements for this session

if seq:
    st.write('Reverse complement :')
    st.write(revcomp(seq))
