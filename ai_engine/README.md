# ai-integration
1. create a .env file and create variables OPENAI_API_KEY and GEMINI_API_KEY, set values.
2. Set pdfPath in run_ai.py file to the file path of where input pdf file is stored.
3. Set question in run_ai.py to the question you want to ask.
4. Run run_ai.py

# 📘 AI Integration Project

This project lets you **upload a PDF document** and **ask questions about it**.
The program uses two powerful AIs — **OpenAI** and **Google Gemini** — to read your document and give answers.


## ✅ What You Need Before Starting

1. Python 3.10 or higher → Download here
.

During installation, check ✅ “Add Python to PATH”.

2.  **Visual Studio Community (FREE)** → [Download here](https://visualstudio.microsoft.com/).

   * When installing, check ✅ **Python Development**.
   * (Optional) Also check ✅ **Git for Windows**.

3. **API Keys** (like secret passwords that let your computer talk to AI):

   * **OpenAI API Key** → [Create here](https://platform.openai.com/account/api-keys)

     * Click **Create new secret key** → Copy it.
   * **Gemini API Key** → [Create here](https://aistudio.google.com/app/apikey)

     * Click **Create API Key** → Copy it.

💡 *Keep these keys safe — they are private to you!*

---

## 🛠 Step 1: Download (Clone) the Project

1. Go to this project’s GitHub page. NIK-CLAIMSUB-AI
2. Click the green **Code** button → Copy the HTTPS link (it ends with `.git`).
   Example:

   ```
   https://github.com/your-username/ai-integration.git
   ```
3. Open **Visual Studio**.
4. From the top menu, select:
   **File → Clone Repository**.
5. Paste the link you copied → Choose a folder to save → Click **Clone**.

✅ Now the project will appear in Visual Studio.

---

## 🐍 Step 2: Set Up Python

We use **Python** (a programming language) to run this project.

1. In Visual Studio, open the **Terminal**:

   * From the top menu: **View → Terminal**.

2. Inside the terminal, type this to make a special Python environment just for this project:

```bash
python -m venv venv
```

3. Activate the environment:

   * On Windows:

     ```bash
     venv\Scripts\activate
     ```
   * On Mac/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required tools (from `requirements.txt`):

```bash
pip install -r requirements.txt
```

✅ You only need to do this once.

---

## 🔑 Step 3: Save Your API Keys

We need to give the program your **secret keys**.

1. In Visual Studio, find your project in the **Solution Explorer** (right side).

2. Right-click the project → **Add → New Item**.

3. Select **Text File**, name it:

   ```
   .env
   ```

   (Yes, it starts with a dot!)

4. Open the `.env` file and paste this (replace with your keys):

```
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
```

Save the file.

---

## 📑 Step 4: Choose Your Document and Question

1. Currently, pdf file is stored under requirement_docs folder(refer SOlutions Explorer). 
2. In Visual Studio, open the file `run_ai.py`.
3. Find these lines:

```python
pdfPath = "C:/path/to/your/file.pdf"
question = "What is the summary of this document?"
```

4. Change them:

   * Replace the path with where your PDF is saved.
   * Replace the question with what you want to ask.

Example:

```python
pdfPath = "/Documents/sample.pdf"
question = "List the main points of this document."
```

---

## ▶️ Step 5: Run the Program

1. In Solution Explorer, **right-click `run_ai.py`** → Choose **Set as Startup File**.
2. At the top of Visual Studio, click the **green Run button (▶)**.

✅ The program will run, and you’ll see answers in the **Output / Terminal window**.

---

## 🎯 Example

If you set:

```python
pdfPath = "/Documents/sample.pdf"
question = "What are the main points of this document?"
```

You might see:

```
OpenAI Response: The document explains...
Gemini Response: The main points are...
```

---

## 🛠 Troubleshooting (Common Problems)

* ❌ **Red text appears (errors)** → Make sure you ran `pip install -r requirements.txt`.
* ❌ **File not found** → Double-check your PDF path.
* ❌ **API key error** → Ensure `.env` file exists and has no spaces around `=`.
* ❌ **Run button is grey** → Right-click `run_ai.py` → **Set as Startup File**.
* ❌ **Program says “python not found”** → Reinstall Python with “Add to PATH” checked.

---

## 🎉 You’re Done!

