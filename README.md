# AI DDR Report Generator

An AI-powered system that converts raw inspection and thermal reports into a structured DDR (Detailed Diagnostic Report).

## Features

- Extracts text from inspection and thermal reports
- Extracts images from PDF documents
- Combines information logically
- Generates structured DDR report
- Handles missing or conflicting information
- Simple client-friendly report format
- Web interface using Streamlit

## DDR Report Structure

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

## Tech Stack

Python  
Streamlit  
OpenAI / AI Model  
PDFPlumber  
PyMuPDF  

## Installation

Clone repository

git clone https://github.com/ananyajain827/ai-ddr-report-generator.git


Install dependencies
pip install -r requirements.txt


Run application

streamlit run app.py

## Usage

1. Upload Inspection Report
2. Upload Thermal Report
3. Click **Generate DDR Report**
4. Download the final report

## Project Workflow

PDF Upload → Data Extraction → AI Processing → DDR Report Generation

## Future Improvements

- Automatic section detection
- Better image placement
- PDF report export
- Multi-property analysis

## Author

Ananya