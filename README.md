# LPU Chatbot

A custom AI chatbot that provides information about **Lovely Professional University (LPU)** using a preloaded dataset. The chatbot can answer university-related queries efficiently and fall back on AI-generated responses for unknown questions.

## 🚀 Features
- Fast and optimized dataset lookup
- Uses **fuzzy matching** for similar questions
- AI-powered responses for unknown queries
- **Smooth typing effect** for better user experience
- No external search engine API required

## 🛠️ Installation
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/lpu-chatbot.git
cd lpu-chatbot
```

### 2️⃣ Install dependencies
Make sure you have **Python 3.7+** installed. Then, install required libraries:
```bash
pip install ollama fuzzywuzzy python-Levenshtein
```

### 3️⃣ Download or prepare `lpu.json`
Ensure you have a structured dataset `lpu.json` in the root directory.

### 4️⃣ Run the chatbot
```bash
python chatbot.py
```

## 📜 Usage
- Type a question related to LPU.
- The chatbot will first check the **dataset** for an exact or close match.
- If no relevant answer is found, it will **use AI to generate a response**.
- To exit, type `quit`, `exit`, or `bye`.

## 📂 Project Structure
```
📦 lpu-chatbot
 ┣ 📜 Ai.py    # Main chatbot script
 ┣ 📜 lpu.json      # FAQ dataset for LPU
 ┣ 📜 README.md     # Project documentation
```

## 📌 Example
```
You: What is UMS?
AI: UMS (University Management System) is LPU’s platform for students to access academic and administrative services.
```

## 🤝 Contributing
Feel free to submit issues or pull requests if you have improvements!

## 📄 License
This project is licensed under the **MIT License**.
