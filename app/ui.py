import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from app.agent import run_agent

# ---------- CONFIG ----------
st.set_page_config(page_title="Festiva Planner AI", layout="wide")

# ---------- GLOBAL STYLES ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0e1117, #111827);
}

/* HERO */
.hero {
    text-align: center;
    padding: 60px 0;
}
.hero h1 {
    font-size: 64px;
    font-weight: 800;
}
.hero p {
    font-size: 18px;
    color: #9aa0a6;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
    box-shadow: 0px 6px 30px rgba(0,0,0,0.4);
}

/* PLAN ITEM */
.plan-item {
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 8px;
    background: rgba(255,255,255,0.06);
}

/* SUCCESS */
.success {
    background: linear-gradient(90deg, #22c55e, #15803d);
    padding: 15px;
    border-radius: 12px;
    color: white;
    margin-bottom: 20px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <h1>🎉 Festiva Planner AI</h1>
    <p>Plan weddings, birthdays & corporate events in seconds with AI</p>
</div>
""", unsafe_allow_html=True)

# ---------- INPUT ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

user_input = st.text_input(
    "✨ Describe your event",
    placeholder="Wedding in Bangalore with 10 lakh budget"
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- ACTION ----------
if st.button("🚀 Generate Plan"):

    if user_input:

        # 🔥 Loading animation
        with st.spinner("🤖 AI is building your perfect event..."):
            time.sleep(1.5)
            result = run_agent(user_input)

        st.markdown('<div class="success">✅ Your AI plan is ready!</div>', unsafe_allow_html=True)

        # ---------- METRICS ----------
        m1, m2, m3 = st.columns(3)

        m1.metric("🎯 Event", result["event"].capitalize())
        m2.metric("📍 City", result["city"])
        m3.metric("💰 Budget", f"₹{result['input_budget']}")

        # ---------- TABS ----------
        tab1, tab2, tab3, tab4 = st.tabs([
            "📊 Overview",
            "📋 Plan",
            "🏪 Vendors",
            "💡 Insights"
        ])

        # ---------- TAB 1 ----------
        with tab1:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            col1, col2 = st.columns([1, 1])

            with col1:
                st.subheader("💰 Budget Comparison")

                fig, ax = plt.subplots(figsize=(5,3))
                values = [result["input_budget"], result["predicted_budget"]]

                bars = ax.bar(["Your Budget", "AI Estimate"], values)

                for bar in bars:
                    bar.set_color("#22c55e")

                fig.patch.set_facecolor("#0e1117")
                ax.set_facecolor("#0e1117")
                ax.tick_params(colors='white')

                st.pyplot(fig)

            with col2:
                st.subheader("🥧 Budget Breakdown")

                breakdown = [
                    result["predicted_budget"] * 0.4,
                    result["predicted_budget"] * 0.3,
                    result["predicted_budget"] * 0.2,
                    result["predicted_budget"] * 0.1
                ]

                labels = ["Venue", "Catering", "Decoration", "Others"]

                fig2, ax2 = plt.subplots()

                ax2.pie(
                    breakdown,
                    labels=labels,
                    autopct='%1.1f%%',
                    colors=["#22c55e","#3b82f6","#f59e0b","#ef4444"],
                    textprops={'color':"white"}
                )

                fig2.patch.set_facecolor("#0e1117")
                st.pyplot(fig2)

            st.markdown('</div>', unsafe_allow_html=True)

        # ---------- TAB 2 ----------
        with tab2:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader("✨ Event Plan")

            for step in result["plan"]:
                st.markdown(f'<div class="plan-item">✔ {step}</div>', unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

        # ---------- TAB 3 ----------
        with tab3:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader("🏪 Recommended Vendors")

            for v in result["vendors"]:
                st.write(f"⭐ {v}")

            st.markdown('</div>', unsafe_allow_html=True)

        # ---------- TAB 4 ----------
        with tab4:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.subheader("📚 Smart Insights")

            for k in result["knowledge"]:
                st.write(f"💡 {k.strip()}")

            st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter event details")