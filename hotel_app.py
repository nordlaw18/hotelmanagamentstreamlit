# --- Home Page ---
if st.session_state.page == "Home":
    # Centered Logo
    st.markdown('<div style="text-align:center;">', unsafe_allow_html=True)
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Star_Hotel_Logo.svg/512px-Star_Hotel_Logo.svg.png",
        width=120
    )
    # Centered Welcome Text
    st.markdown('<h1 style="text-align:center;">🏨 Welcome to Luxury Stay Hotels</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">Experience comfort, convenience, and premium services at our hotels across India.</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Centered Hero Image
    st.image(
        "https://images.unsplash.com/photo-1551776235-dde6d4829808",
        use_container_width=True,
        caption="Your Comfort, Our Priority ✨"
    )

    # --- Navbar (Only on Home Page) ---
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
