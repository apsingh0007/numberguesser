[README.md](https://github.com/user-attachments/files/29155116/README.md)
# 🎯 Number Guesser

A classic number guessing game available in two flavors: a **web app** built with Flask, HTML, CSS & JavaScript, and a **desktop app** built with Python's Tkinter. The computer picks a random number between 1 and 100, and you try to guess it in as few attempts as possible.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

- 🌐 **Web version** — sleek glassmorphism UI with animated gradient background
- 🖥️ **Desktop version** — lightweight native GUI using Tkinter
- 🎉 Confetti celebration animation on a correct guess (web)
- 📊 Live attempt counter
- 🔄 One-click "Play Again" / reset functionality
- ⌨️ Keyboard support — press <kbd>Enter</kbd> to submit a guess
- 🛡️ Input validation with friendly error feedback
- 🔒 Session-based game state (web version) — no database required

---

## 📸 Preview

```
🎯 Number Guesser
I'm thinking of a number between 1 and 100

[ Enter your guess... ]     [ Guess! ]

⚠️  Too high! Try again.

Attempts: 3
```

---

## 🗂️ Project Structure

```
number-guesser/
├── app.py                     # Flask web server & game logic
├── number_guessing_app.py     # Standalone Tkinter desktop version
├── requirements.txt           # Python dependencies
├── templates/
│   └── index.html             # Web UI markup
└── static/
    ├── style.css               # Glassmorphism styling
    └── script.js                # Frontend game logic & confetti effect
```

> **Note:** Flask expects `index.html` inside a `templates/` folder, and `style.css` / `script.js` inside a `static/` folder. Make sure your files are organized this way before running the web app.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/number-guesser.git
   cd number-guesser
   ```

2. **Create a virtual environment** *(recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### Option 1 — Web App (Flask)

```bash
python app.py
```

Then open your browser and navigate to:
```
http://127.0.0.1:5000
```

### Option 2 — Desktop App (Tkinter)

```bash
python number_guessing_app.py
```

No browser needed — this launches a native desktop window.

---

## 🎮 How to Play

1. The app secretly picks a random number between **1** and **100**
2. Enter your guess and click **Guess!** (or press <kbd>Enter</kbd>)
3. You'll be told if your guess is **too high** or **too low**
4. Keep guessing until you find the correct number
5. Once you win, click **Play Again** to start a new round

---

## 🛠️ Tech Stack

| Layer       | Technology              |
|-------------|--------------------------|
| Backend     | Python, Flask            |
| Frontend    | HTML5, CSS3, JavaScript  |
| Desktop GUI | Tkinter                  |
| Styling     | Custom CSS (Glassmorphism, CSS animations) |

---

## 🧩 API Endpoints (Web Version)

| Method | Endpoint  | Description                                     |
|--------|-----------|--------------------------------------------------|
| GET    | `/`       | Renders the game page & starts a new session     |
| POST   | `/guess`  | Submits a guess, returns feedback (`low` / `high` / `correct`) |
| POST   | `/reset`  | Resets the game with a new random number          |

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

## 🙌 Acknowledgements

- [Flask](https://flask.palletsprojects.com/) for the lightweight web framework
- [Google Fonts](https://fonts.google.com/) for the **Outfit** typeface
- Built with ❤️ for fun and to practice full-stack basics

---

<p align="center">If you enjoyed this project, consider giving it a ⭐ on GitHub!</p>
