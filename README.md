# 📰 AI-Based Multilingual Fake News Detection System

An AI-powered fake news detection system that identifies misinformation across **multiple languages** using transformer-based models and a **Retrieval-Augmented Generation (RAG)** pipeline to provide supporting evidence from online sources.

---

## 🚀 Features

- 🌍 **Multilingual Fake News Detection**
  - English news classification using **DistilBERT**
  - Indian language news classification using **IndicBERT**
- 🤖 Transformer-based text classification
- 🔎 **Retrieval-Augmented Generation (RAG) Pipeline**
  - Retrieves evidence from online sources
  - Supports and explains the prediction
- 🧠 Modular and scalable architecture
- 📊 Real-world misinformation analysis support

---

## 🧩 System Overview

1. News article is provided as input  
2. Language detection is performed  
3. Model selection:
   - English → DistilBERT
   - Indian Languages → IndicBERT  
4. News is classified as **Fake** or **Real**
5. RAG pipeline retrieves online evidence
6. Final output includes:
   - Classification result
   - Supporting evidence

---

## 🧠 Models Used

### DistilBERT
- Used for English fake news detection
- Lightweight and efficient transformer model
- Fine-tuned on fake news datasets

### IndicBERT
- Used for Indian languages (Hindi, Tamil, Telugu, Bengali, etc.)
- Pretrained on large-scale Indian language corpora
- Fine-tuned for fake news classification

---

## 🔍 Retrieval-Augmented Generation (RAG)

The RAG pipeline improves explainability by:

- Querying online sources related to the news claim
- Retrieving relevant articles and documents
- Generating evidence that supports or contradicts the claim

This makes predictions more **transparent** and **trustworthy**.

---

## 🛠️ Tech Stack

- Python
- PyTorch
- Hugging Face Transformers
- DistilBERT
- IndicBERT
- FAISS / Vector Database
- Web Search APIs
- NLP & Machine Learning Libraries

---

