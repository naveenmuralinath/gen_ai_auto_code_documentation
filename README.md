# gen_ai_auto_code_documentation

# AutoCodeDocGen - Automated Code Documentation Generator

## Overview
AutoCodeDocGen is an AI-powered tool that **automatically generates professional documentation** for source code files. 
It uses the **DeepSeek-Coder 1.3B** model running **locally via Ollama**.

It produces a detailed, step-by-step, and beautifully structured **Markdown** documentation covering:
- Overview of the Code
- Classes and Functions Documentation
- Parameters, Return types
- Usage Examples
- Important Notes and Assumptions

## ✨ Why DeepSeek-Coder 1.3B?
- Specifically trained for **code understanding and generation**.
- Small enough (1.3B parameters) to run efficiently **on local GPUs/CPUs**.
- Very high performance for generating **clean**, **professional**, and **domain-specific** technical documentation.
- Free, open-source, privacy-preserving (no need to send code to external APIs).

## ⚙️ System Architecture

| Component         | Description                                         |
|-------------------|-----------------------------------------------------|
| Ollama            | Local LLM Server that serves DeepSeek-Coder         |
| DeepSeek-Coder    | Language model optimized for code tasks             |
| Streamlit         | Frontend Web App for Uploading code and viewing docs|
| Async Python      | For real-time, streaming response                   |

## 📥 How It Works
1. User uploads a **source code file** (.py, .java, .cpp, .js, etc.).
2. A professional **System prompt** is created around the uploaded code.
3. The **DeepSeek-Coder model** running via **Ollama** is called **locally**.
4. The model **streams the documentation** back in **Markdown** format.
5. Documentation is **displayed live** and **available for download** as `.md`.

## 🚀 Installation and Running the App

### 1. Install Ollama
Download and install Ollama from [https://ollama.com/download](https://ollama.com/download).

Once installed, make sure Ollama server is running:
```bash
ollama serve
```

### 2. Pull DeepSeek-Coder Model
You need the **DeepSeek-Coder 1.3B** model locally.
```bash
ollama pull deepseek-coder:1.3b
```

### 3. Clone the Repo and Install Python Packages
```bash
git clone https://github.com/naveenmuralinath/gen_ai_auto_code_documentation.git
cd AutoCodeDocGen

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
streamlit run app.py
```

Make sure `ollama serve` is already running in a separate terminal.

---

## 📜 Requirements

- Python 3.10+
- Streamlit
- Ollama Python Client (`pip install ollama`)
- DeepSeek-Coder Model (`deepseek-coder:1.3b`)

`requirements.txt`:
```
streamlit
asyncio
requests
python-dotenv
ollama
httpx
```

---

## 📈 Features

- 🧠 Understands and documents code logic.
- 📑 Outputs documentation in clean Markdown.
- 💾 Download documentation as `.md` file.
- 🚀 Runs 100% locally without internet dependency after setup.
- ⚡ Fast, Streaming, and Responsive.

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| `ollama` command not found | Install and run Ollama |
| Model not found error | Pull the DeepSeek-Coder model |
| Port 11434 busy error | Close previous Ollama sessions |
| Slow generation | Make sure sufficient CPU/GPU is allocated |

---

## 🤖 Future Enhancements

- Multi-file support
- Auto language detection
- Improve summarization quality
- Add Code commenting feature
- Dividing the large code base and processing in batch

---

## 📢 Credits

- [DeepSeek](https://deepseek.com/) for DeepSeek-Coder
- [Ollama](https://ollama.com/) for Local LLM serving
- [Streamlit](https://streamlit.io/) for frontend

---

# 📜 License
This project is licensed under the **MIT License**.

# 🤝 Contributions
**Contributions are welcome!**  
Feel free to open an **Issue** or **Pull Request**.  
Let's make AutoCodeDocGen even better together! 🚀

# ✨ Acknowledgments
- Thanks to **Ollama** for making local LLMs easy to run and interact with.
- Thanks to **DeepSeek AI** for building outstanding code-specialized LLMs like DeepSeek Coder.
- Thanks to the **Streamlit** team for providing the best UI experience for Python developers.

# 🚀 Final Words
With **AutoCodeDocGen**, you now have an AI assistant that **reads your code** and **writes professional documentation** for you in **seconds** — fully offline, powered by your own machine!

**Code smarter, document faster!** 🧠💬

---

# 👨‍💻 Developed By
**Naveen Murali**

# 📬 Contact
- GitHub: [naveenmuralinath](https://github.com/naveenmuralinath)
- Feel free to contribute more to improve this idea and project! 🚀

---