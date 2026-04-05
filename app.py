import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Data Explorer App")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Dataset Preview")
    st.dataframe(df)

    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()

    selected_column = st.selectbox("Select a numeric column", numeric_columns)

    if selected_column:
        st.write("### Statistics")

        mean = df[selected_column].mean()
        median = df[selected_column].median()
        std = df[selected_column].std()
        min_val = df[selected_column].min()
        max_val = df[selected_column].max()

        st.write(f"Mean: {mean}")
        st.write(f"Median: {median}")
        st.write(f"Standard Deviation: {std}")
        st.write(f"Minimum: {min_val}")
        st.write(f"Maximum: {max_val}")

        st.write("### Histogram")

        fig, ax = plt.subplots()
        ax.hist(df[selected_column])
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")

        st.pyplot(fig)

        st.write("### Write Your Insights")

        insights = st.text_area("Explain what you observe from the data")

        if insights:
            st.write("Your Insight:")
            st.write(insights)