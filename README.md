# AI DDR Report Generator

An AI-powered system that converts raw **Inspection Reports** and **Thermal Reports** into a structured **DDR (Detailed Diagnostic Report)**.
The system reads technical site inspection documents, extracts key observations and images, and generates a clear **client-friendly diagnostic report** using AI.

🌐 **Live Application:**
https://ai-ddr-report--generator.streamlit.app/

---

# Project Overview

In property inspection workflows, engineers often work with multiple technical documents such as inspection notes and thermal analysis reports. Manually converting this raw data into a clear client-ready report takes significant time and effort.

This project automates that process by building an **AI-driven workflow** that:

* Reads inspection documents
* Extracts key observations
* Combines inspection and thermal findings
* Identifies missing or conflicting information
* Generates a professional **Detailed Diagnostic Report (DDR)**

The solution is designed to work on **similar inspection datasets**, not just the provided samples.

---

## Project Screenshots

### Application Interface
![Homepage]("Screenshot 2026-03-15 193212.png")


### Generated DDR Report Output
![Report Output]("Screenshot 2026-03-15 193652.png")

---

# Key Features

• Upload **Inspection Report (PDF)**
• Upload **Thermal Report (PDF)**
• Automatic **text extraction from reports**
• **Image extraction from PDFs**
• AI-based **analysis and report generation**
• Logical merging of inspection + thermal findings
• Handles **missing or conflicting information**
• Generates structured **client-friendly DDR report**
• Interactive **Streamlit web interface**

---

# DDR Report Structure

The generated report contains the following structured sections:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

Images extracted from the reports are included where relevant.

---

# Live Demo

You can access the deployed application here:

https://ai-ddr-report--generator.streamlit.app/

Steps to use the application:

1. Upload **Inspection Report PDF**
2. Upload **Thermal Report PDF**
3. Click **Generate DDR Report**
4. View the generated report
5. Download the report

---

# Project Architecture

Workflow of the system:

Document Upload
↓
PDF Text Extraction
↓
Image Extraction from Documents
↓
AI Processing & Analysis
↓
Structured DDR Report Generation

---

# Tech Stack

**Programming Language**

* Python

**Framework**

* Streamlit

**AI Model**

* OpenAI API

**Libraries Used**

* pdfplumber (text extraction)
* PyMuPDF (image extraction)
* Pillow (image processing)

---

# Installation Guide

Clone the repository:

```
git clone https://github.com/ananyajain827/ai-ddr-report-generator.git
```

Navigate to the project directory:

```
cd ai-ddr-report-generator
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

---

# Environment Setup

Create an OpenAI API key from:

https://platform.openai.com/api-keys

Add the key as an environment variable:

```
OPENAI_API_KEY="your_api_key"
```

For Streamlit deployment, add the key inside **Streamlit Secrets**.

---

# Example Use Cases

• Property inspection reporting
• Building diagnostics
• Infrastructure maintenance reports
• Automated technical documentation
• Inspection data summarization

---

# Future Improvements

* Automatic section classification
* Improved image placement within reports
* Export reports directly as **PDF**
* Multi-property report processing
* AI confidence scoring for observations
* Dashboard analytics for inspection data

---

# Author

**Ananya Jain**

Computer Science Student
AI & Software Development Enthusiast

---

# Acknowledgment

This project was developed as part of the **Applied AI Builder Assignment**, focusing on building real-world AI workflows that convert raw inspection data into structured diagnostic reports.
