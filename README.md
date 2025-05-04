# 🔐 Pyrogram String Session Generator

This is a simple and secure Python script to generate a **Telegram String Session** using the [Pyrogram](https://github.com/pyrogram/pyrogram) library.

It performs the following actions:
- Authenticates your Telegram account using your API ID and API Hash.
- Generates a **string session** for Telethon client reusability.
- Sends the generated session to your **Telegram Saved Messages**.
- Saves the session as a `.txt` file in the same directory.

---

## 🚀 Features

- ✔️ Easy to use and lightweight
- 🔒 Secure authentication with your API ID and API Hash
- 📬 Sends the session to your Telegram Saved Messages
- 📁 Saves the session as a `.txt` file
- 💬 Supports 2FA (Two-Factor Authentication)
- 📜 Pyrogram-based implementation

---

## 📦 Installation

Follow these steps to get started:

### 1. Clone the Repository

```bash
git clone https://github.com/Chamindu-Gayanuka/Pyrogram-String-Session-Generator.git
```

### 2. Change Directory
```bash
cd Pyrogram-String-Session-Generator
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Get Your API ID and API Hash
- Visit [my.telegram.org](https://my.telegram.org).
- Log in with your phone number.
- Click on **API Development Tools**.
- Create a new application.
- Copy your **API ID** and **API Hash**.

### 4. Run the Script
```bash
python main.py
```

### 5. Enter Your API ID and API Hash
- When prompted, enter your **API ID** and **API Hash**.
- The script will generate a string session and send it to your **Telegram Saved Messages**.
- The session will also be saved as a `.txt` file in the same directory.

## Sample Usage
<img src="Assets/Sample%20Usage.svg" alt="Sample Usage"/>

## Warning
- **Do not share your API ID, API Hash, or string session with anyone.**
- Keep your credentials secure to prevent unauthorized access to your Telegram account.
- This script is for educational purposes only. Use it responsibly and in accordance with Telegram's terms of service.
- Use at your own risk. The author is not responsible for any misuse or damage caused by this script.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/Chamindu-Gayanuka/Pyrogram-String-Session-Generator/blob/main/LICENSE) file for details.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

