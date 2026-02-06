📰 AI-Based Multilingual Fake News Detection System

An AI-powered fake news detection system capable of identifying misinformation across multiple languages.
The project leverages transformer-based language models and a Retrieval-Augmented Generation (RAG) pipeline to not only classify news as real or fake, but also provide supporting evidence from online sources.

🚀 Features

🌍 Multilingual Fake News Detection

English news detection using DistilBERT

Indian language news detection using IndicBERT

🤖 Transformer-based text classification

🔎 RAG (Retrieval-Augmented Generation) Pipeline

Fetches supporting evidence from online sources

Helps explain and justify predictions

📊 Scalable and modular architecture

🧠 Designed for real-world misinformation analysis

🧩 System Architecture

Input News Article

Language Identification

Model Selection

English → DistilBERT

Indian Languages → IndicBERT

Fake News Classification

RAG Pipeline

Query formulation

Online evidence retrieval

Evidence generation

Final Output

Prediction (Fake / Real)

Supporting evidence

🧠 Models Used
🔹 DistilBERT

Used for English fake news classification

Lightweight and faster variant of BERT

Fine-tuned on labeled fake news datasets

🔹 IndicBERT

Used for Indian languages such as Hindi, Bengali, Tamil, Telugu, etc.

Pretrained on large multilingual Indian corpora

Fine-tuned for fake news detection

🔍 Retrieval-Augmented Generation (RAG)

To enhance transparency and trust, this project includes a RAG pipeline that:

Searches online sources related to the news claim

Retrieves relevant documents/articles

Generates supporting or contradicting evidence

Helps users understand why a piece of news is labeled fake or real

This makes the system more explainable and fact-driven.

🛠️ Tech Stack

Python

PyTorch

Hugging Face Transformers

DistilBERT

IndicBERT

FAISS / Vector Database (for retrieval)

Web Search APIs / Scrapers (for evidence collection)

NLP & ML libraries
