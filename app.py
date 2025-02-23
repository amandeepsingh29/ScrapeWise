import streamlit as st
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import google.generativeai as genai  # Correct import for google-generativeai

# Configure Gemini API
genai.configure(api_key="AIzaSyD079ZxmJVMT4n7IbwuaDQLxYj25CBnux0")  # Replace with your actual API key

# Function to scrape website with dynamic content support using Selenium
def scrape_with_bs4(url):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        service = Service()
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get(url)
        time.sleep(5)  # Allow time for JavaScript to load

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

        # Extract relevant content: headings, paragraphs, and meta descriptions
        content = []
        for tag in soup.find_all(['h1', 'h2', 'h3', 'p']):
            if tag.get_text(strip=True):
                content.append(tag.get_text(strip=True))

        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            content.append(meta_desc.get('content'))

        return "\n".join(content)
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Gemini Model Initialization
def initialize_genai():
    return genai.GenerativeModel("gemini-2.0-flash")  # Updated model to a valid one

def get_summary(model, html_content, url):
    response = model.generate_content(
        f""" '''{html_content}''' 
        I have provided you the scraped and relevant content for the link: {url}, 
        Give me a single line summary about the website. """
    )
    return response.text

def get_answer(model, html_content, url, question):
    response = model.generate_content(
        f""" '''{html_content}''' 
        I have provided you the scraped and relevant content for the link: {url}. 
        Answer the following question based on the scraped content: 
        Question: {question} """
    )
    return response.text

# Streamlit App UI
st.set_page_config(page_title="Website Scraper & Q&A", layout="centered")
st.title("🌐 Website Scraper & Q&A using Gemini API")

url = st.text_input("🔗 Enter the URL to scrape:", placeholder="https://example.com")

if url:
    st.info("⏳ Scraping website...")
    scraped_content = scrape_with_bs4(url)
    if scraped_content:
        st.success("✅ Website scraped successfully!")
        with st.spinner("Generating summary..."):
            model = initialize_genai()
            summary = get_summary(model, scraped_content, url)
            st.subheader("📄 Website Summary:")
            st.write(summary)

        question = st.text_input("❓ Ask a question about this website:", placeholder="e.g., Who is the founder?")
        if question:
            with st.spinner("Generating answer..."):
                answer = get_answer(model, scraped_content, url, question)
                st.subheader("💡 Answer:")
                st.write(answer)
else:
    st.info("🔎 Please provide a URL to begin scraping.")
