# 🚀 Automated Pull Request Review Agent  
### FastAPI • Groq Llama 3.3 • Multi-Agent Code Analysis

This project is built for the **Lyzr AI Engineering Challenge**.  
It implements a fully functional **AI-powered Pull Request Review Agent** capable of analyzing code diffs and generating structured, human-like review comments.

The system detects:

- 🔍 Logic errors  
- 🔐 Security vulnerabilities  
- ⚡ Performance bottlenecks  
- 🧼 Code quality & readability issues  

It uses a **multi-agent AI architecture** powered by **Groq's Llama 3.3** model.

---

## ✨ Features

### ✔ PR Diff Parsing  
Parses unified diffs and extracts changed code segments.

### ✔ Multi-Agent Architecture  
- **Logic Agent** – detects incorrect logic & missing cases  
- **Security Agent** – finds secrets, SQLi, unsafe functions  
- **Performance Agent** – detects heavy loops & inefficiencies  
- **Synthesizer** – merges outputs into one clean response  

### ✔ Groq LLM Integration  
Uses **llama-3.3-70b-versatile** for ultra-fast inference.

### ✔ GitHub PR Support  
Fetch diff directly using:  
```
/review-pr?owner=<user>&repo=<repo>&pr=<number>
```

### ✔ FastAPI Backend  
Clean, minimal, production-ready API.

---

## 📡 API Endpoints

### **1️⃣ POST /review-diff**
Analyze raw diff manually.

**Request:**
```json
{
  "diff": "diff --git a/app.py b/app.py
+ password = "123456""
}
```

---

### **2️⃣ GET /review-pr**
Fetch and analyze a GitHub PR automatically.

**Example:**
```
/review-pr?owner=vercel&repo=next.js&pr=12345
```

Optional:  
```
token=<gh_personal_access_token>
```

---

## 🛠 Installation

### 1. Clone the repo
```
git clone https://github.com/<your-username>/pr-review-agent
cd pr-review-agent
```

### 2. Create virtual environment  
```
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

### 3. Install dependencies  
```
pip install -r requirements.txt
```

### 4. Set Groq API Key  
```
setx GROQ_API_KEY "your_key_here"     # Windows
export GROQ_API_KEY="your_key_here"   # Linux/Mac
```

---

## ▶️ Run the Server

```
uvicorn app.main:app --reload --port 8000
```

Open Swagger UI:  
👉 http://127.0.0.1:8000/docs

---

## 📂 Project Structure

```
app/
 ├── main.py
 ├── github.py
 └── agents/
      ├── base.py
      ├── logic.py
      ├── security.py
      ├── performance.py
      ├── parser.py
      └── synthesizer.py
tests/
requirements.txt
README.md
.gitignore
```

---

## 🎥 Demo Video  
(Attach link after recording)

---

## 🧑‍💻 Author  
**Harshith**  
Backend Developer • FastAPI • Python • AI Engineering  
Email: *harshithhmk2@gmail.com*

---

## ⭐️ Notes  
- `venv/` is purposely excluded and should not be uploaded.  
- Add a personal access token only if testing private repos.  
- Built in 2–3 days as required by the challenge.
