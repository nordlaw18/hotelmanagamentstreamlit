import streamlit as st
from datetime import date

# --- Page Config ---
st.set_page_config(page_title="Hotel Management System", page_icon="🏨", layout="wide")

# --- Custom CSS ---
st.markdown(
    """
    <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1501117716987-c8e1ecb2101d");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }
        .navbar {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            background-color: rgba(0,0,0,0.7);
            padding: 10px 0;
            border-radius: 10px;
            margin-top: 20px;
            margin-bottom: 30px;
        }
        .navbar a {
            color: white;
            padding: 12px 25px;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
            margin: 5px;
        }
        .navbar a:hover {
            background-color: #e67e22;
            border-radius: 6px;
            transition: 0.3s;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            color: #fff;
            font-size: 14px;
        }
        .center-text {
            text-align: center;
            color: white;
        }
        iframe {
            border-radius: 12px;
        }
        h1, p {
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Session State for Navigation ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- URL Param Hack for Navbar Clicks ---
query_params = st.query_params
if "page" in query_params:
    page_map = {
        "PropertiesBooking": "Properties & Booking",
        "Invoices": "Invoices",
        "Payments": "Payments",
        "Tenant": "Tenant Profile",
        "About": "About Us",
        "Contact": "Contact Us",
    }
    st.session_state.page = page_map.get(query_params["page"], "Home")

# --- Navbar Function ---
def show_navbar():
    # Links will open in the same tab
    st.markdown(
        """
        <div class="navbar">
            <a href="/?page=PropertiesBooking">🏘️ Properties & Booking</a>
            <a href="/?page=Invoices">🧾 Invoices</a>
            <a href="/?page=Payments">💳 Payments</a>
            <a href="/?page=Tenant">👤 Tenant Profile</a>
            <a href="/?page=About">ℹ️ About Us</a>
            <a href="/?page=Contact">📞 Contact Us</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Homepage ---
if st.session_state.page == "Home":
    st.markdown('<div style="text-align:center; padding-top:150px;">', unsafe_allow_html=True)
    st.markdown('<h1 style="text-align:center; font-size:48px;">🏨 Welcome to Luxury Stay Hotels</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; font-size:20px;">Experience comfort, convenience, and premium services at our hotels across India.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Navbar below welcome text on homepage
    show_navbar()

# --- Combined Properties & Booking Page ---
elif st.session_state.page == "Properties & Booking":
    # Navbar at top
    show_navbar()

    st.header("🏘️ Available Properties & Rooms")
    st.subheader("🌅 Sunrise Residency, Mumbai")
    st.table({
        "Room Type": ["Single", "Double"],
        "AC": ["Yes", "Yes"],
        "Base Rent": ["₹1200/night", "₹2000/night"],
        "Deposit": ["₹2000", "₹3000"],
        "Capacity": [1, 2],
    })
    st.subheader("🌿 Green Stay, Bangalore")
    st.table({
        "Room Type": ["Non-AC Single", "AC Double"],
        "AC": ["No", "Yes"],
        "Base Rent": ["₹800/night", "₹1800/night"],
        "Deposit": ["₹1000", "₹2500"],
        "Capacity": [1, 2],
    })

    st.markdown("---")
    st.header("📅 Make a Booking")
    room = st.selectbox("Select Room", 
        ["Single AC - Sunrise Residency", "Double AC - Sunrise Residency", "Non-AC Single - Green Stay", "AC Double - Green Stay"])
    check_in = st.date_input("Check-in Date", value=date.today())
    check_out = st.date_input("Check-out Date", value=date.today())
    guests = st.number_input("Number of Guests", min_value=1, max_value=4, value=1)
    if st.button("Confirm Booking"):
        st.success(f"✅ Booking confirmed for {room} from {check_in} to {check_out} for {guests} guest(s).")

# --- Invoices Page ---
elif st.session_state.page == "Invoices":
    show_navbar()
    st.header("🧾 Your Invoices")
    st.markdown('<p class="center-text"><b>Invoice #101</b> | Sunrise Residency | ₹5000 | Status: ❌ Unpaid</p>', unsafe_allow_html=True)
    st.markdown('<p class="center-text"><b>Invoice #102</b> | Green Stay | ₹3600 | Status: ✅ Paid</p>', unsafe_allow_html=True)
    st.download_button("📥 Download Invoice #101 (PDF)", "Sample Invoice Content", file_name="invoice_101.pdf")

# --- Payments Page ---
elif st.session_state.page == "Payments":
    show_navbar()
    st.header("💳 Make a Payment")
    invoice_id = st.selectbox("Select Invoice", ["101 - ₹5000 - Unpaid", "102 - ₹3600 - Paid"])
    method = st.radio("Payment Method", ["UPI", "Credit Card", "Net Banking", "Cash"])
    if st.button("Pay Now"):
        st.success(f"✅ Payment for Invoice {invoice_id} successful via {method}!")

# --- Tenant Profile Page ---
elif st.session_state.page == "Tenant Profile":
    show_navbar()
    st.header("👤 Tenant Profile")
    st.text_input("Full Name", "John Doe")
    st.text_input("Email", "johndoe@example.com")
    st.number_input("Age", 18, 60, 25)
    st.selectbox("Gender", ["Male", "Female", "Other"])
    st.text_input("Food Preference", "Vegetarian")
    st.text_input("Work Type", "IT Professional")
    st.text_area("Bio", "Love traveling and working remotely!")
    if st.button("Update Profile"):
        st.success("✅ Profile updated successfully")

# --- About Us Page ---
elif st.session_state.page == "About Us":
    show_navbar()
    st.header("ℹ️ About Us")
    st.write("""
        Welcome to **Luxury Stay Hotels** — your trusted partner for comfort and convenience.  
        Established in 2010, we offer premium hotel services across major Indian cities.  
        Our mission is to provide guests with unforgettable experiences combining luxury, 
        affordability, and world-class hospitality.
    """)
    st.image("https://images.unsplash.com/photo-1522708323590-d24dbb6b0267", use_container_width=True)

# --- Contact Us Page ---
elif st.session_state.page == "Contact Us":
    show_navbar()
    st.header("📞 Contact Us")
    st.markdown('<p class="center-text">📍 Address: 123 Luxury Street, Mumbai, India</p>', unsafe_allow_html=True)
    st.markdown('<p class="center-text">📧 Email: support@luxurystay.com</p>', unsafe_allow_html=True)
    st.markdown('<p class="center-text">📞 Phone: +91 98765 43210</p>', unsafe_allow_html=True)
    st.markdown(
        """
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d241317.1160996496!2d72.7410999515156!3d19.082197839963376!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b63e0f5f1f0d%3A0xdeadbeefcafe1234!2sMumbai%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1694343511450!5m2!1sen!2sin" 
        width="100%" height="300" allowfullscreen="" loading="lazy"></iframe>
        """,
        unsafe_allow_html=True,
    )

# --- Footer ---
st.markdown('<div class="footer">© 2025 Luxury Stay Hotels</div>', unsafe_allow_html=True)
