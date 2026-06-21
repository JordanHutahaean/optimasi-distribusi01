import streamlit as st
import matplotlib.pyplot as plt

from algorithms.greedy import greedy
from algorithms.bnb import branch_and_bound

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Optimasi Distribusi",
    page_icon="",
    layout="wide"
)

# =========================
# CSS CUSTOM UI
# =========================
st.markdown("""
<style>

/* Center container */
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

/* Input box lebih besar */
input {
    font-size: 18px !important;
}

/* Judul */
.title {
    text-align: center;
    font-size: 34px;
    font-weight: bold;
    margin-bottom: 20px;
}

/* Card input */
.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

/* Button full */
.stButton>button {
    width: 100%;
    height: 50px;
    font-size: 18px;
    border-radius: 10px;
    background-color: #4CAF50;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================
st.markdown("<div class='title'> Optimasi Distribusi Dashboard</div>", unsafe_allow_html=True)

# =========================
# INPUT CENTER
# =========================
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.subheader(" Input Parameter")

col1, col2, col3 = st.columns(3)

with col1:
    target = st.number_input("Target", min_value=0, value=100)

with col2:
    kapA = st.number_input("Kapasitas A", min_value=1, value=10)
    kapB = st.number_input("Kapasitas B", min_value=1, value=20)
    kapC = st.number_input("Kapasitas C", min_value=1, value=30)

with col3:
    rasioA = st.number_input("Rasio A", min_value=0, value=1)
    rasioB = st.number_input("Rasio B", min_value=0, value=1)
    rasioC = st.number_input("Rasio C", min_value=0, value=1)

run = st.button(" Jalankan Optimasi")

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# HITUNG
# =========================
if run:

    kapasitas = [kapA, kapB, kapC]

    kapasitas_siklus = (
        kapA * rasioA +
        kapB * rasioB +
        kapC * rasioC
    )

    if kapasitas_siklus == 0:
        st.error("Rasio tidak boleh semua 0")

    else:

        jumlah_siklus = target // kapasitas_siklus

        jumlah_kardus = [
            jumlah_siklus * rasioA,
            jumlah_siklus * rasioB,
            jumlah_siklus * rasioC
        ]

        total_distribusi = (
            jumlah_kardus[0] * kapA +
            jumlah_kardus[1] * kapB +
            jumlah_kardus[2] * kapC
        )

        sisa = target - total_distribusi

        hasil_greedy = greedy(sisa, kapasitas)
        hasil_bnb = branch_and_bound(sisa, kapA, kapB, kapC)

        # =========================
        # LAYOUT HASIL (KANAN-KIRI)
        # =========================
        colA, colB = st.columns([1, 1])

        with colA:
            st.subheader(" Perbandingan Algoritma")

            labels = ["Greedy", "BnB"]
            values = [
                hasil_greedy["kelebihan"],
                hasil_bnb["kelebihan"]
            ]

            fig1, ax1 = plt.subplots(figsize=(4,3))  
            ax1.bar(labels, values)
            ax1.set_title("Kelebihan")
            st.pyplot(fig1)

        with colB:
            st.subheader(" Distribusi")

            labels = ["A", "B", "C"]
            values = jumlah_kardus

            fig2, ax2 = plt.subplots(figsize=(4,3))

            # Cegah error jika semua nilai nol
            if sum(values) > 0:
                ax2.pie(values, labels=labels, autopct="%1.1f%%")
            else:
                ax2.text(
                    0.5,
                    0.5,
                    "Tidak ada distribusi",
                    ha="center",
                    va="center",
                    fontsize=12
                )
                ax2.set_axis_off()

            ax2.set_title("Proporsi")
            st.pyplot(fig2)

        # =========================
        # METRIC
        # =========================
        st.write("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(" Sisa", sisa)

        with col2:
            st.metric(" Greedy", hasil_greedy["kelebihan"])

        with col3:
            st.metric(" BnB", hasil_bnb["kelebihan"])

        # =========================
        # DETAIL
        # =========================
        with st.expander(" Detail Hasil"):  
            st.json({
                "greedy": hasil_greedy,
                "bnb": hasil_bnb
            })
