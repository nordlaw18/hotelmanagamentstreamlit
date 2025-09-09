import streamlit as st
from datetime import date

# --- Custom CSS for Styling ---
st.markdown(
    """
    <style>
        /* Background color */
        .stApp {
            background-color: #f5f5f5;
        }
        
        /* Titles */
        h1, h2, h3 {
            color: #2c3e50;
        }
        
        /* Card styling */
        .card {
            background-color: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        
        /* Buttons */
        div.stButton > button {
            background-color: #2980b9;
            color: white;
            border-radius: 8px;
            padding: 8px 20px;
        }
        div.stButton > button:hover {
            background-color: #3498db;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "Properties & Rooms", "Bookings", "Invoices", "Payments", "Tenant Profile"]
)

# --- Home ---
if menu == "Home":
    st.title("🏨 Hotel & Tenant Management System")
    st.write("Manage bookings, rooms, invoices, and tenants seamlessly with our hotel management app.")
    
    st.image(
        "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb",
        caption="Luxury Stays Await You ✨",
        use_column_width=True
    )

# --- Properties & Rooms ---
elif menu == "Properties & Rooms":
    st.header("🏘️ Available Properties & Rooms")

    # Property 1
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

    # Property 2
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
        ["Single AC - Sunrise Residency",
         "Double AC - Sunrise Residency",
         "Non-AC Single - Green Stay",
         "AC Double - Green Stay"]
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
