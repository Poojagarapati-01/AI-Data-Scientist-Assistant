import streamlit as st

from src.ingestion.validator import validate_file
from src.ingestion.loader import load_csv
from src.profiling.summary import get_dataset_summary

# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="AI Data Scientist Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Scientist Assistant")
st.write("Upload a CSV dataset to begin your ML journey.")

st.divider()

# -------------------------
# Dataset Upload
# -------------------------

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

# -------------------------
# Validation & Loading
# -------------------------

if uploaded_file is not None:

    is_valid, message = validate_file(uploaded_file)

    if is_valid:

        st.success(message)

        df = load_csv(uploaded_file)

        # Store dataset for later modules
        st.session_state["dataset"] = df

        st.subheader("Dataset Preview")

        st.dataframe(df.head(10))
        summary = get_dataset_summary(df)

        st.subheader("Dataset Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows", df.shape[0])
            st.metric("Columns", df.shape[1])

        with col2:
            st.metric("Missing Values", df.isnull().sum().sum())
            st.metric("Duplicate Rows", df.duplicated().sum())

    else:

        st.error(message)