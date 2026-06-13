# QR Tool : Scanner & Generator

A lightweight, desktop utility built in Python using **Tkinter** and **OpenCV** that allows users to scan QR codes via a live webcam feed, upload QR images to extract data, and generate custom QR codes seamlessly.

---

## ✨ Features

* **📷 Live Camera Scan:** Launches a high-performance webcam feed utilizing OpenCV to instantly detect and decode QR codes. Press `q` to gracefully cancel.
* **📂 Image Upload:** Supports importing local images (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.webp`) to scan pre-saved QR codes.
* **📝 Copy-Friendly Layout:** Scanned data is rendered in a dedicated, read-only text block, preventing accidental overwrites while maintaining native `Ctrl+C` text highlights. Includes a one-click dedicated **"Copy to Clipboard"** button.
* **🎨 QR Code Generation:** Quickly turn links, passwords, or blocks of text into a QR code.
* **💾 Export Options:** Preview generated QR codes inside a dedicated staging window and save them locally as `.png` files.

---

## 🛠️ Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8 or higher installed on your operating system.

### 2. Clone the Repository
```bash
git clone https://github.com/prabhat-bidalia/qr_tool.git
cd qr-tool
