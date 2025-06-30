import customtkinter as ctk
import json
import pathlib
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load FAQ Data
FAQ_PATH = pathlib.Path(r"C:\Users\HP\Desktop\FYP\faq product data.json")
if not FAQ_PATH.exists():
    raise FileNotFoundError("FAQ JSON not found at specified path.")
faq_items = json.loads(FAQ_PATH.read_text(encoding="utf-8"))
questions = [item["question"] for item in faq_items]
answers = [item["answer"] for item in faq_items]

# NLP Setup
nlp = spacy.load("en_core_web_sm")
def spacy_tokenizer(text: str):
    doc = nlp(text.lower())
    return [t.lemma_ for t in doc if not t.is_stop and t.is_alpha]

vectorizer = TfidfVectorizer(tokenizer=spacy_tokenizer)
faq_matrix = vectorizer.fit_transform(questions)

def answer_query(query: str):
    vec = vectorizer.transform([query])
    scores = cosine_similarity(vec, faq_matrix).flatten()
    best = int(np.argmax(scores))
    return answers[best], float(scores[best])

# GUI Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class ProductChatbot(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🛍️ Product Information Chatbot")
        self.geometry("520x640")
        self.resizable(True, True)  # ✅ Now it's resizable!

        # Header
        ctk.CTkLabel(self, text="🛒 Product Info Assistant", font=("Segoe UI", 20, "bold")).pack(pady=(10, 5))

        # Chat Display
        self.chat_box = ctk.CTkTextbox(self, wrap="word", font=("Segoe UI", 13))
        self.chat_box.pack(padx=20, pady=(0, 10), fill="both", expand=True)
        self.chat_box.insert("end", "Bot: Hello! Ask me anything about our products 😊\n\n")
        self.chat_box.configure(state="disabled")

        # Input Frame
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(fill="x", padx=20, pady=10)

        self.entry = ctk.CTkEntry(input_frame, placeholder_text="Type your question...", font=("Segoe UI", 13))
        self.entry.pack(side="left", fill="x", expand=True, padx=(5, 10), pady=10)
        self.entry.bind("<Return>", self.on_send)

        send_btn = ctk.CTkButton(input_frame, text="Send", command=self.on_send)
        send_btn.pack(side="right", padx=5, pady=10)

    def append(self, who, msg):
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", f"{who}: {msg}\n\n")
        self.chat_box.configure(state="disabled")
        self.chat_box.see("end")

    def on_send(self, *_):
        q = self.entry.get().strip()
        if not q:
            return
        self.entry.delete(0, "end")
        self.append("You", q)
        a, s = answer_query(q)
        self.append("Bot", f"{a}  (Similarity ≈ {s:.2f})")

if __name__ == "__main__":
    ProductChatbot().mainloop()

