import streamlit as st
from openai import OpenAI
from data.products import products

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="MiniStore Support",
    page_icon="💬",
    layout="wide"
)

st.title("💬 MiniStore AI Support")

st.write(
    "Ask questions about products, orders, shipping, refunds, returns, and payments."
)

# ==========================================
# OPENAI CLIENT
# ==========================================

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# ==========================================
# BUILD PRODUCT CATALOG
# ==========================================

catalog_text = ""

for product in products:
    catalog_text += f"""
Product Name: {product['name']}
Category: {product['category']}
Price: ${product['price']}
Description: {product['description']}

"""

# ==========================================
# SYSTEM PROMPT
# ==========================================

SYSTEM_PROMPT = f"""
You are a professional customer support representative
for MiniStore.

Your job is to assist customers with:

- Products
- Product recommendations
- Orders
- Shipping and delivery
- Refunds
- Returns
- Payment methods
- Store policies

MiniStore Product Catalog:

{catalog_text}

Rules:

1. Only answer questions related to MiniStore.
2. Use the product catalog when answering product questions.
3. Be polite, professional, and concise.
4. If asked about topics unrelated to MiniStore,
politely explain that you can only help with
MiniStore products and customer support.
5. Never make up products that do not exist in the catalog.
"""

# ==========================================
# CHAT HISTORY
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==========================================
# DISPLAY CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==========================================
# USER INPUT
# ==========================================

user_prompt = st.chat_input(
    "How can I help you today?"
)

if user_prompt:

    # Store user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Build conversation

    conversation = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    conversation.extend(st.session_state.messages)

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation,
            temperature=0.3
        )

        assistant_reply = response.choices[0].message.content

    except Exception as e:

        assistant_reply = (
            f"Error connecting to support assistant:\n\n{str(e)}"
        )

    # Store assistant message

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(assistant_reply)
        

