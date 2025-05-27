import streamlit as st
import psycopg2
from psycopg2.extras import RealDictCursor

st.title("Expense Tracker")

# Connect to PostgreSQL database using secrets
conn = psycopg2.connect(
    host=st.secrets["db"]["host"],
    dbname=st.secrets["db"]["dbname"],
    user=st.secrets["db"]["user"],
    password=st.secrets["db"]["password"],
    port=st.secrets["db"]["port"],
    cursor_factory=RealDictCursor
)
cur = conn.cursor()

# Create table if not exists
cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id SERIAL PRIMARY KEY,
        name TEXT,
        amount NUMERIC,
        category TEXT
    );
""")
conn.commit()

# Input form
with st.form("add_expense"):
    name = st.text_input("Expense Name")
    amount = st.number_input("Amount", min_value=0.0)
    category = st.selectbox("Category", ["Food", "Transport", "Health", "Other"])
    submitted = st.form_submit_button("Add")
    if submitted and name:
        cur.execute("INSERT INTO expenses (name, amount, category) VALUES (%s, %s, %s)", (name, amount, category))
        conn.commit()
        st.success("Expense added!")

# Display expenses
st.subheader("All Expenses")
cur.execute("SELECT * FROM expenses")
rows = cur.fetchall()
st.table(rows)
