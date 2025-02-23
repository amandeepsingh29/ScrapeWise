# ScrapeWise: Streamlit Web Scraper & Q&A with Gemini API

**ScrapeWise** is a **Streamlit web app** that scrapes dynamic website content using **Selenium** and **BeautifulSoup**, then utilizes **Google's Gemini API** to generate summaries and answer user queries based on the scraped content.
<p align="center">
  <img width="1000" alt="Wise" src="https://github.com/amandeepsingh29/ScrapeWise/blob/main/Wise.png">
</p>

## 🚀 Features
- Dynamic content scraping with Selenium
- Extracts relevant data (headings, paragraphs, meta descriptions)
- Gemini API integration for generating summaries and answering questions
- Simple and interactive UI with Streamlit

## 💡 Requirements
- Python 3.8+
- Streamlit
- Selenium
- BeautifulSoup4
- google-generativeai

## 🔧 Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/scrapewise.git
cd scrapewise

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

## 📝 Usage
1. **Set your Gemini API key:**
   - Replace `YOUR_API_KEY_HERE` in the code with your Gemini API key.

2. **Run the ScrapeWise app:**
```bash
streamlit run app.py
```

3. **Interact with ScrapeWise:**
   - Enter a website URL.
   - View a summary of the website.
   - Ask questions about the content.

## ⚡ Dependencies
```plaintext
streamlit
selenium
beautifulsoup4
google-generativeai
```

## 💡 Project Structure
```
ScrapeWise/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

## 📄 License
[MIT License](LICENSE)

---

✨ **Happy Scraping and Exploring with ScrapeWise!** ✨
