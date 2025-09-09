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
        .main {
            background: rgba(255, 255, 255, 0.9);
            padding: 40px 50px;
            border-radius: 15px;
            margin: 20px auto;
            max-width: 1000px;
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
            color: #444;
            font-size: 14px;
        }
        .center-text {
            text-align: center;
        }
        iframe {
            border-radius: 12px;
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
        "Properties": "Properties & Rooms",
        "Bookings": "Bookings",
        "Invoices": "Invoices",
        "Payments": "Payments",
        "Tenant": "Tenant Profile",
        "About": "About Us",
        "Contact": "Contact Us",
    }
    st.session_state.page = page_map.get(query_params["page"], "Home")

# --- Page Content Wrapper ---
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # --- Home Page ---
    if st.session_state.page == "Home":
        # Centered Logo and Text
        st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Star_Hotel_Logo.svg/512px-Star_Hotel_Logo.svg.png",
            width=120
        )
        st.markdown('<h1 style="text-align:center;">🏨 Welcome to Luxury Stay Hotels</h1>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center;">Experience comfort, convenience, and premium services at our hotels across India.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Hero Image
        st.image(
            "https://images.unsplash.com/photo-1551776235-dde6d4829808",
            use_container_width=True,
            caption="Your Comfort, Our Priority ✨"
        )

        # Navbar (Only for Homepage)
        st.markdown(
            """
            <div class="navbar">
                <a href="/?page=Properties">🏘️ Properties & Rooms</a>
                <a href="/?page=Bookings">📅 Bookings</a>
                <a href="/?page=Invoices">🧾 Invoices</a>
                <a href="/?page=Payments">💳 Payments</a>
                <a href="/?page=Tenant">👤 Tenant Profile</a>
                <a href="/?page=About">ℹ️ About Us</a>
                <a href="/?page=Contact">📞 Contact Us</a>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --- Properties & Rooms ---
    elif st.session_state.page == "Properties & Rooms":
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

    # --- Bookings ---
    elif st.session_state.page == "Bookings":
        st.header("📅 Make a Booking")
        room = st.selectbox("Select Room", 
            ["Single AC - Sunrise Residency", "Double AC - Sunrise Residency", "Non-AC Single - Green Stay", "AC Double - Green Stay"])
        check_in = st.date_input("Check-in Date", value=date.today())
        check_out = st.date_input("Check-out Date", value=date.today())
        guests = st.number_input("Number of Guests", min_value=1, max_value=4, value=1)

        if st.button("Confirm Booking"):
            st.success(f"✅ Booking confirmed for {room} from {check_in} to {check_out} for {guests} guest(s).")

    # --- Invoices ---
    elif st.session_state.page == "Invoices":
        st.header("🧾 Your Invoices")
        st.markdown('<p class="center-text"><b>Invoice #101</b> | Sunrise Residency | ₹5000 | Status: ❌ Unpaid</p>', unsafe_allow_html=True)
        st.markdown('<p class="center-text"><b>Invoice #102</b> | Green Stay | ₹3600 | Status: ✅ Paid</p>', unsafe_allow_html=True)
        st.download_button("📥 Download Invoice #101 (PDF)", "Sample Invoice Content", file_name="invoice_101.pdf")

    # --- Payments ---
    elif st.session_state.page == "Payments":
        st.header("💳 Make a Payment")
        invoice_id = st.selectbox("Select Invoice", ["101 - ₹5000 - Unpaid", "102 - ₹3600 - Paid"])
        method = st.radio("Payment Method", ["UPI", "Credit Card", "Net Banking", "Cash"])
        if st.button("Pay Now"):
            st.success(f"✅ Payment for Invoice {invoice_id} successful via {method}!")

    # --- Tenant Profile ---
    elif st.session_state.page == "Tenant Profile":
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

    # --- About Us ---
    elif st.session_state.page == "About Us":
        st.header("ℹ️ About Us")
        st.write("""
            Welcome to **Luxury Stay Hotels** — your trusted partner for comfort and convenience.  
            Established in 2010, we offer premium hotel services across major Indian cities.  
            Our mission is to provide guests with unforgettable experiences combining luxury, 
            affordability, and world-class hospitality.
        """)
        st.image(
            "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
            use_container_width=True
        )

    # --- Contact Us ---
    elif st.session_state.page == "Contact Us":
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

    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown('<div class="footer">© 2025 Luxury Stay Hotels | Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
