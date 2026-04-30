import streamlit as st
from datetime import date

# =========================
# إعداد الحالة (State)
# =========================
if "lang" not in st.session_state:
    st.session_state.lang = "en"

if "theme" not in st.session_state:
    st.session_state.theme = "light"


# =========================
# نصوص اللغة
# =========================
def T(en, ar):
    return en if st.session_state.lang == "en" else ar


# =========================
# الثيم
# =========================
def apply_theme():
    if st.session_state.theme == "dark":
        st.markdown(
            """
            <style>
            body { background-color: #111; color: white; }
            </style>
            """,
            unsafe_allow_html=True
        )


apply_theme()

# =========================
# الواجهة
# =========================
st.title(T("Date Calculator", "حاسبة التاريخ"))

# =========================
# Sidebar (الإعدادات)
# =========================
st.sidebar.header(T("Settings", "الإعدادات"))

# اللغة
lang = st.sidebar.selectbox("Language / اللغة", ["English", "Arabic"])
st.session_state.lang = "en" if lang == "English" else "ar"

# الثيم
theme = st.sidebar.selectbox("Theme / الثيم", ["Light", "Dark"])
st.session_state.theme = "light" if theme == "Light" else "dark"

st.sidebar.write("---")


# =========================
# إدخال التواريخ
# =========================
st.subheader(T("First Date", "التاريخ الأول"))

col1, col2, col3 = st.columns(3)

with col1:
    d1 = st.number_input(T("Day", "اليوم"), 1, 31, 1)

with col2:
    m1 = st.number_input(T("Month", "الشهر"), 1, 12, 1)

with col3:
    y1 = st.number_input(T("Year", "السنة"), 1, 3000, 2024)


st.subheader(T("Second Date", "التاريخ الثاني"))

col4, col5, col6 = st.columns(3)

with col4:
    d2 = st.number_input(T("Day ", "اليوم "), 1, 31, 1, key="d2")

with col5:
    m2 = st.number_input(T("Month ", "الشهر "), 1, 12, 1, key="m2")

with col6:
    y2 = st.number_input(T("Year ", "السنة "), 1, 3000, 2024, key="y2")


# =========================
# الحساب
# =========================
def calculate():
    try:
        date1 = date(int(y1), int(m1), int(d1))
        date2 = date(int(y2), int(m2), int(d2))
        diff = abs(date2 - date1)

        days = diff.days
        months = days // 30
        years = days // 365

        return days, months, years

    except:
        return None, None, None


# =========================
# زر الحساب
# =========================
if st.button(T("Calculate", "احسب")):
    days, months, years = calculate()

    if days is None:
        st.error(T("Invalid input", "خطأ في الإدخال"))
    else:
        st.success(T("Result", "النتيجة"))

        st.write(T("Total Days:", "مجموع الأيام:"), days)
        st.write(T("Approx Months:", "تقريب الأشهر:"), months)
        st.write(T("Approx Years:", "تقريب السنوات:"), years)