## 🚀 AgentOps Hackathon

### 📌 About
Given a Nasdaq or NYSE ticker of your choice, this AI agent will conduct a thorough analysis to help you understand why the company's stock is doing well or not. This AI agent will check the following:
-If competitors are doing things that could impact your company's status.
-If recent political activity or government regulations could help or harm the company's status.
-If the CEO's recent actions could impact the way the company is being led.
-If the company's most recent earnings report provides insight into company performance.

---

## 📂 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/GSDV/agentops-hackathon.git
cd agentops-hackathon
```

### 2️⃣ Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3️⃣ Install Dependencies
```bash
pip3 install agentops
pip3 install python-dotenv
pip3 install openai-agents
```

---

## ▶️ Running the Project

To run `main.py`, use:
```bash
python main.py
```

If any environment variables are required (like API keys), specify them in a `.env` file and load them using `dotenv`.

Example `.env` file:
```
API_KEY=your_api_key_here
```

---

## 🛠 Troubleshooting

- **Missing dependencies?** Run `pip install -r requirements.txt` again.
- **Python version issues?** Ensure you're using Python 3.8+ (`python --version`).
- **Permissions error?** Try running `chmod +x main.py` and execute again.

---

## 📜 Contributing
Guidelines for contributing to the project.

---
