# codeAlphafaq
# 🛍️ Product Information Chatbot

This is a desktop-based FAQ Chatbot built using Python's `CustomTkinter`, `spaCy`, and `scikit-learn`. The chatbot intelligently answers user queries about products by matching the input question with a list of FAQs stored in a JSON file using Natural Language Processing and Cosine Similarity.

### 💡 Key Features
- Sleek and modern GUI using CustomTkinter (dark mode)
- NLP-powered question understanding with spaCy
- TF-IDF vectorization and cosine similarity to match best FAQ
- Real-time responses with similarity score
- Easy to modify by updating the JSON file

### 🛠️ Technologies Used
- Python 3.11
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [spaCy](https://spacy.io/)
- [scikit-learn](https://scikit-learn.org/)
- NumPy

### 📂 Project Files
- `faq_chatbot.py` → main chatbot code
- `faq product data.json` → contains question-answer pairs
- `README.md` → project overview and usage instructions

### 🚀 How to Run
1. **Install dependencies:**
   ```bash
   pip install customtkinter spacy scikit-learn numpy
   python -m spacy download en_core_web_sm
