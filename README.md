# 🤖 Company Intelligence Agentic System

A **Multi-Agent AI System** built using **LangGraph** and **LangChain**, powered by **Ollama (local LLM)**, that generates structured company intelligence reports through collaborating agents.

This project was developed as part of the **Data Scientist Intern Technical Assessment – SoulPage IT Solutions**.

---

## 📌 Problem Statement

Design an **Agentic AI System** with two or more collaborating agents to perform a multi-step task such as generating a company market summary.

---

## 🎯 Objective

- Demonstrate understanding of agent workflows  
- Use LangGraph orchestration  
- Maintain shared state (memory) between agents  
- Implement tool usage  
- *(Optional)* Provide a Streamlit UI  

---

## 🏗️ System Architecture
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/78c570ce-8ddb-4110-b817-0f08e8766333" />

---

## 🧠 Agents Description

### 🔹 Agent 1: Data Collector
- Fetches company data from a local JSON knowledge base  
- Acts as a tool-using agent  
- Stores results in shared state (`raw_data`)  

### 🔹 Agent 2: Analyst
- Uses Ollama (LLaMA 3) for analysis  
- Generates:
  - Company overview / summary  
  - Key insights  
  - Potential risks  

**Auto-fallback behavior:**  
If structured data is missing → uses LLM’s general business knowledge

---

## 🔁 Orchestration (LangGraph)

- Implemented using `StateGraph`  
- Shared memory via `TypedDict` (`AgentState`)  

**Execution flow:**
Data Collector → Analyst → END


---

## 🖥️ Streamlit UI (Optional)

A clean Streamlit UI is provided to interact with the system:

- Enter company name  
- Trigger agent workflow  
- View generated intelligence report  

---

## 🛠️ Tech Stack

- Python 3.10+  
- LangChain  
- LangGraph  
- Ollama (local LLM runtime)  
- Streamlit  
- JSON-based knowledge base  
---

## ⚙️ Setup Instructions

### 1️⃣ Install Ollama

Download and install Ollama from:  
https://ollama.com

Pull the model:
```bash
ollama pull llama3
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run via CLI
python main.py
4️⃣ Run Streamlit UI
streamlit run app.py
🧪 Example Output
📊 Company Intelligence Report
Overview:
Amazon is a multinational technology company operating in e-commerce, cloud computing (AWS), digital streaming, and AI services.

Key Insights:

Strong diversification through AWS

Data-driven decision making

Global scale advantage

Potential Risks:

Regulatory scrutiny

Intense competition

Supply chain dependency

✅ Key Features Implemented
✔ Multi-agent collaboration

✔ Shared memory between agents

✔ Tool-based data collection

✔ LangGraph orchestration

✔ LLM fallback logic

✔ Local LLM (Ollama) — no API keys required

✔ Streamlit UI

🚀 Future Improvements
Integrate real-time APIs (news, stock prices)

Add vector database (FAISS / Chroma)

Extend to Task 2: Conversational Knowledge Bot

Add caching for faster responses

👤 Author
Abhinay Sangem
Data Scientist Intern Candidate
Profile Submitted via: Kodnest
