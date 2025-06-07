# Project-TDS-Virtual-TA
# 🧠 TDS Virtual TA — Intelligent Teaching Assistant for IITM Data Science

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-green)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/LLM-OpenAI-blue)](https://platform.openai.com/)

## 📘 Overview

**TDS Virtual TA** is a virtual Teaching Assistant built for the **IIT Madras BSc in Data Science** program. It is designed to **automatically answer student queries** based on:

- The official course material (as of 15 April 2025)
- Discourse forum discussions (between 1 Jan 2025 – 14 Apr 2025)
- Image inputs (via OCR on base64 screenshots)

The API takes a question (optionally with an image) and returns:
- An accurate, LLM-generated answer
- A list of helpful reference links from course discussions

---

## 🔍 Features

✅ Ask questions in natural language  
✅ Upload a screenshot (base64) and get OCR-assisted answers  
✅ Semantic search using FAISS and OpenAI embeddings  
✅ References to actual Discourse posts  
✅ Ready to deploy via [Render](https://render.com), [Railway](https://railway.app), or any cloud platform  
✅ Evaluation-ready for `promptfoo`

---

## 🛠 Tech Stack

| Layer          | Tool                    |
|----------------|--------------------------|
| API            | [FastAPI](https://fastapi.tiangolo.com/) |
| OCR            | [pytesseract](https://github.com/madmaze/pytesseract) + [Pillow](https://python-pillow.org/) |
| Embeddings     | OpenAI `text-embedding-ada-002` |
| Search Index   | FAISS                   |
| Scraping       | requests + BeautifulSoup |
| Hosting        | Render / Railway        |
| Evaluation     | [promptfoo](https://github.com/promptfoo/promptfoo) |

---

## 🚀 How It Works

1. **User submits a question**, optionally with a screenshot.
2. If an image is provided, OCR is applied to extract visible text.
3. The combined question + image text is searched semantically over the indexed course & Discourse content.
4. The **most relevant content** is used to prompt OpenAI’s GPT model.
5. The **answer** and relevant **reference links** are returned.

---

## 📦 Project Structure

