import streamlit as st
from data.products import products

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛒",
    layout="wide"
)

# ---------- CSS ----------

st.markdown("""
<style>


.support-btn:hover {
    background: #4338CA;
} 

.hero {
    background: linear-gradient(135deg,#4F46E5,#7C3AED);
    padding:40px;
    border-radius:15px;
    text-align:center;
    color:white;
    margin-bottom:30px;
}

.product-card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom:20px;
    height:260px;
}

.product-title {
    font-size:20px;
    font-weight:bold;
}

.product-price {
    color:green;
    font-size:22px;
    font-weight:bold;
}

.product-category {
    background:#E0E7FF;
    color:#4338CA;
    padding:4px 10px;
    border-radius:20px;
    display:inline-block;
    margin-bottom:10px;
}

.support-btn {
    position:fixed;
    bottom:20px;
    right:20px;
    background:#4F46E5;
    color:white;
    padding:15px 20px;
    border-radius:50px;
    text-decoration:none;
    font-weight:bold;
    z-index:9999;
}

</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------

st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")

st.sidebar.write("Items: 3")
st.sidebar.write("Subtotal: $249.97")
st.sidebar.write("Shipping: Free")

st.sidebar.success("Total: $249.97")

# ---------- HERO ----------

st.markdown("""
<div class="hero">
<h1>🛒 MiniStore</h1>
<p>Your One-Stop Shop for Modern Lifestyle Products</p>
</div>
""", unsafe_allow_html=True)

# ---------- WELCOME ----------

st.header("Welcome to MiniStore")

st.write(
"""
Discover premium-quality products carefully selected
for modern living.
"""
)

# ---------- FILTER ----------

if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# ---------- PRODUCTS ----------

st.header("Featured Products")

cols = st.columns(3)

for i, product in enumerate(filtered_products):

    with cols[i % 3]:

        st.markdown(
            f"""
            <div class="product-card">

            <div class="product-category">
            {product['category']}
            </div>

            <div class="product-title">
            {product['name']}
            </div>

            <div class="product-price">
            ${product['price']}
            </div>

            <p>{product['description']}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.button(
            "Add to Cart",
            key=i
        )
# Floating Button CSS
st.markdown("""
<style>
div.stButton > button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    z-index: 9999;
    border-radius: 50px;
    background-color: #4F46E5;
    color: white;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# Floating Support Button
if st.button("💬 Support"):
    st.switch_page("pages/1_Supports_Chatbot.py")
    












