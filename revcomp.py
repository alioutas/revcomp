import streamlit as st

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)


def reverse_complement(sequence, molecule):
    if molecule == "DNA":
        complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
    elif molecule == "RNA":
        complement = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}

    return ''.join([complement[base] for base in reversed(sequence)])

st.title('Reverse Complement DNA/RNA Sequence')
st.caption('by Antonios Lioutas')
st.markdown('---')

input_sequence = st.text_input("Enter your DNA or RNA sequence")

# Determine if input is DNA or RNA
if all(base in 'ATGCN' for base in input_sequence):
    input_type = "DNA"
elif all(base in 'AUGC' for base in input_sequence):
    input_type = "RNA"
else:
    input_type = None
    st.error("Invalid input. Please enter a valid DNA or RNA sequence.")

if input_type is not None:
    length = len(input_sequence)
    st.write(f"Input sequence is {input_type} and has {length} bases.")
    st.markdown('---')

    # Allow user to choose output type (DNA or RNA)
    output_type = st.radio("Select output nucleic acid type", ("DNA", "RNA"))

    # Convert input to output type if necessary
    if input_type != output_type:
        if output_type == "DNA":
            conversion = {'U': 'T'}
        else:
            conversion = {'T': 'U'}
        input_sequence = ''.join([conversion.get(base, base) for base in input_sequence])

    # Calculate reverse complement and display it
    if input_sequence:
        reverse_complement_sequence = reverse_complement(input_sequence, output_type)
        st.write(f"Reverse complement {output_type} sequence:")
        st.subheader(reverse_complement_sequence)
