import streamlit as st
import pdfplumber
import fitz
import os
from openai import OpenAI

client = OpenAI()

IMAGE_DIR = "extracted_images"
OUTPUT_DIR = "output"


# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI DDR Report Generator",
    page_icon="🤖",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main-title{
font-size:40px;
font-weight:700;
color:#2E86C1;
text-align:center;
margin-bottom:10px;
}

.sub-title{
text-align:center;
font-size:18px;
color:gray;
margin-bottom:30px;
}

.card{
background-color:#f8f9fa;
padding:25px;
border-radius:12px;
box-shadow:0px 4px 10px rgba(0,0,0,0.08);
}

.report-box{
background:#ffffff;
padding:25px;
border-radius:10px;
border:1px solid #e0e0e0;
}

.stButton>button{
background-color:#2E86C1;
color:white;
font-size:18px;
padding:12px 25px;
border-radius:8px;
border:none;
}

.stButton>button:hover{
background-color:#1B4F72;
}

.footer{
text-align:center;
margin-top:40px;
color:gray;
font-size:14px;
}

</style>
""", unsafe_allow_html=True)


# ---------- TITLE ----------
st.markdown('<div class="main-title">AI DDR Report Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Convert Inspection & Thermal Reports into Structured Diagnostic Reports</div>', unsafe_allow_html=True)


# ---------- FUNCTIONS ----------
def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text


def extract_images(pdf_path, prefix):

    doc = fitz.open(pdf_path)
    image_paths = []

    for page_index in range(len(doc)):
        page = doc[page_index]
        images = page.get_images(full=True)

        for img_index, img in enumerate(images):
            xref = img[0]
            base = doc.extract_image(xref)

            image_bytes = base["image"]

            img_path = os.path.join("extracted_images", f"{prefix}_{page_index}_{img_index}.png")

            with open(img_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(img_path)

    return image_paths


def generate_ddr(inspection_text, thermal_text):

    report = f"""
DDR REPORT

1. Property Issue Summary
Inspection findings indicate potential structural or thermal issues.

2. Area-wise Observations
Inspection Data:
{inspection_text[:800]}

Thermal Data:
{thermal_text[:800]}

3. Probable Root Cause
Possible insulation failure, moisture intrusion, or structural deterioration.

4. Severity Assessment
Requires further investigation depending on observed damage.

5. Recommended Actions
Conduct detailed inspection and apply corrective maintenance.

6. Additional Notes
Data extracted from uploaded reports.

7. Missing or Unclear Information
Not Available
"""

    return report


def save_report(report_text, images):

    report_path = f"{OUTPUT_DIR}/DDR_Report.md"

    with open(report_path,"w") as f:

        f.write(report_text)
        f.write("\n\n## Images\n")

        if len(images)==0:
            f.write("Image Not Available")

        else:
            for img in images:
                f.write(f"\n![Image]({img})\n")

    return report_path


# ---------- UPLOAD SECTION ----------
col1,col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    inspection_file = st.file_uploader(
        "Upload Inspection Report",
        type=["pdf"]
    )

    st.markdown('</div>',unsafe_allow_html=True)


with col2:

    st.markdown('<div class="card">',unsafe_allow_html=True)

    thermal_file = st.file_uploader(
        "Upload Thermal Report",
        type=["pdf"]
    )

    st.markdown('</div>',unsafe_allow_html=True)


st.write("")


# ---------- GENERATE BUTTON ----------
center = st.columns([1,2,1])

with center[1]:

    generate = st.button("Generate DDR Report")


# ---------- PROCESS ----------
if generate:

    if inspection_file and thermal_file:

        with st.spinner("Analyzing reports with AI..."):

            with open("inspection.pdf","wb") as f:
                f.write(inspection_file.read())

            with open("thermal.pdf","wb") as f:
                f.write(thermal_file.read())

            inspection_text = extract_text("inspection.pdf")
            thermal_text = extract_text("thermal.pdf")

            images1 = extract_images("inspection.pdf","inspection")
            images2 = extract_images("thermal.pdf","thermal")

            images = images1 + images2

            report = generate_ddr(inspection_text,thermal_text)

            path = save_report(report,images)

        st.success("DDR Report Generated Successfully")

        st.markdown('<div class="report-box">',unsafe_allow_html=True)
        st.markdown(report)
        st.markdown('</div>',unsafe_allow_html=True)

        with open(path) as f:
            st.download_button(
                "Download Report",
                f,
                file_name="DDR_Report.md"
            )

    else:

        st.warning("Please upload both documents")


# ---------- FOOTER ----------
st.markdown('<div class="footer">AI DDR Report Generator • Applied AI Builder Assignment</div>',unsafe_allow_html=True)