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
            background: rgba(255, 255, 255, 0.85);
            padding: 20px;
            border-radius: 12px;
        }
        .card {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #444;
            font-size: 14px;
        }
        div.stButton > button {
            background-color: #d35400;
            color: white;
            border-radius: 8px;
            padding: 8px 20px;
            border: none;
        }
        div.stButton > button:hover {
            background-color: #e67e22;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Menu ---
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Properties & Rooms", "Bookings", "Invoices", "Payments", "Tenant Profile", "About Us", "Contact Us"]
)

# --- Home Page ---
if menu == "Home":
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Star_Hotel_Logo.svg/512px-Star_Hotel_Logo.svg.png",
        width=120
    )
    st.title("🏨 Welcome to Luxury Stay Hotels")
    st.write("Experience comfort, convenience, and premium services at our hotels across India.")
    st.image(
        "https://images.unsplash.com/photo-1551776235-dde6d4829808",
        use_container_width=True,  # changed
        caption="Your Comfort, Our Priority ✨"
    )

# --- Properties & Rooms ---
elif menu == "Properties & Rooms":
    st.header("🏘️ Available Properties & Rooms")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌅 Sunrise Residency, Mumbai")
    st.write("Verified ✅ | AC Rooms | Near Airport")
    st.table({
        "Room Type": ["Single", "Double"],
        "AC": ["Yes", "Yes"],
        "Base Rent": ["₹1200/night", "₹2000/night"],
        "Deposit": ["₹2000", "₹3000"],
        "Capacity": [1, 2],
    })
    st.button("Book Sunrise Residency", key="book1")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌿 Green Stay, Bangalore")
    st.write("Verified ✅ | Non-AC + AC | Near Metro")
    st.table({
        "Room Type": ["Non-AC Single", "AC Double"],
        "AC": ["No", "Yes"],
        "Base Rent": ["₹800/night", "₹1800/night"],
        "Deposit": ["₹1000", "₹2500"],
        "Capacity": [1, 2],
    })
    st.button("Book Green Stay", key="book2")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Bookings ---
elif menu == "Bookings":
    st.header("📅 Make a Booking")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    room = st.selectbox(
        "Select Room", 
        ["Single AC - Sunrise Residency", "Double AC - Sunrise Residency", "Non-AC Single - Green Stay", "AC Double - Green Stay"]
    )
    check_in = st.date_input("Check-in Date", value=date.today())
    check_out = st.date_input("Check-out Date", value=date.today())
    guests = st.number_input("Number of Guests", min_value=1, max_value=4, value=1)

    if st.button("Confirm Booking"):
        st.success(f"✅ Booking confirmed for {room} from {check_in} to {check_out} for {guests} guest(s).")

    st.markdown('</div>', unsafe_allow_html=True)

# --- Invoices ---
elif menu == "Invoices":
    st.header("🧾 Your Invoices")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("**Invoice #101** | Sunrise Residency | ₹5000 | Status: ❌ Unpaid")
    st.write("**Invoice #102** | Green Stay | ₹3600 | Status: ✅ Paid")
    st.download_button("📥 Download Invoice #101 (PDF)", "Sample Invoice Content", file_name="invoice_101.pdf")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Payments ---
elif menu == "Payments":
    st.header("💳 Make a Payment")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    invoice_id = st.selectbox("Select Invoice", ["101 - ₹5000 - Unpaid", "102 - ₹3600 - Paid"])
    method = st.radio("Payment Method", ["UPI", "Credit Card", "Net Banking", "Cash"])

    if st.button("Pay Now"):
        st.success(f"✅ Payment for Invoice {invoice_id} successful via {method}!")

    st.markdown('</div>', unsafe_allow_html=True)

# --- Tenant Profile ---
elif menu == "Tenant Profile":
    st.header("👤 Tenant Profile")
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.text_input("Full Name", "John Doe")
    st.text_input("Email", "johndoe@example.com")
    st.number_input("Age", 18, 60, 25)
    st.selectbox("Gender", ["Male", "Female", "Other"])
    st.text_input("Food Preference", "Vegetarian")
    st.text_input("Work Type", "IT Professional")
    st.text_area("Bio", "Love traveling and working remotely!")

    if st.button("Update Profile"):
        st.success("✅ Profile updated successfully")

    st.markdown('</div>', unsafe_allow_html=True)

# --- About Us ---
elif menu == "About Us":
    st.header("ℹ️ About Us")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("""
        Welcome to **Luxury Stay Hotels** — your trusted partner for comfort and convenience.  
        Established in 2010, we offer premium hotel services across major Indian cities.  
        Our mission is to provide guests with unforgettable experiences combining luxury, 
        affordability, and world-class hospitality.
    """)
    st.image(
        "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267",
        use_container_width=True  # changed
    )
    st.markdown('</div>', unsafe_allow_html=True)

# --- Contact Us ---
elif menu == "Contact Us":
    st.header("📞 Contact Us")
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("📍 Address: 123 Luxury Street, Mumbai, India")
    st.write("📧 Email: support@luxurystay.com")
    st.write("📞 Phone: +91 98765 43210")
    st.markdown(
        """
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d241317.1160996496!2d72.7410999515156!3d19.082197839963376!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3be7b63e0f5f1f0d%3A0xdeadbeefcafe1234!2sMumbai%2C%20Maharashtra!5e0!3m2!1sen!2sin!4v1694343511450!5m2!1sen!2sin" 
        width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown('<div class="footer">© 2025 Luxury Stay Hotels | Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
