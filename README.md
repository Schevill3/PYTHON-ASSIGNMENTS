# CORD-19 Data Explorer

This project analyzes the **CORD-19 research dataset** (metadata.csv) and builds a simple **Streamlit web application** to explore COVID-19 research papers.

## 📌 Features
- Load and clean CORD-19 metadata
- Analyze publications by year, journals, and sources
- Generate visualizations (bar charts, word cloud)
- Interactive Streamlit dashboard with filters

## 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Frameworks_Assignment.git
   cd Frameworks_Assignment
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add the `metadata.csv` file (download from [CORD-19 Kaggle Dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)) into the project folder.

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📊 Analysis
The notebook (`notebook.ipynb`) includes:
- Data loading & cleaning
- Publications by year
- Top journals
- Word cloud of paper titles
- Sources distribution

## ✅ Deliverables
- `app.py` (Streamlit app)
- `notebook.ipynb` (data exploration)
- `requirements.txt` (dependencies)
- `README.md` (documentation)
