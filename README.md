\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{hyperref}
\usepackage{graphicx}
\usepackage{listings}
\usepackage{xcolor}

\title{\textbf{Ramayana Story Generator 🛕✨}}
\author{By Vishnuvardhan Chowdary}
\date{}

\definecolor{codebg}{rgb}{0.95,0.95,0.95}
\lstset{
  backgroundcolor=\color{codebg},
  basicstyle=\ttfamily\footnotesize,
  breaklines=true,
  frame=single,
  showstringspaces=false,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{red}
}

\begin{document}

\maketitle

\section*{📌 Overview}
This is a fun and creative AI-powered project built for \textbf{Sri Rama Navami}. It takes any keyword or theme, generates a \textbf{Ramayana-based story}, creates matching images, and compiles everything into a cute and engaging \textbf{Story Card PDF} — perfect for kids, students, or story lovers.

\section*{⚙️ Tech Stack}
\begin{itemize}
  \item \textbf{Gemini API (Google)} - For story generation using LLM
  \item \textbf{Hugging Face API} - For generating story-based images
  \item \textbf{ReportLab} - For creating the final PDF Story Card
  \item \textbf{Streamlit} - Web interface for user interaction
\end{itemize}

\section*{🚀 Features}
\begin{itemize}
  \item Generates a story from Ramayana based on input theme
  \item Uses generative AI to create story illustrations
  \item Converts it all into a clean and attractive story PDF
  \item Simple and customizable UI using Streamlit
\end{itemize}

\section*{🧠 How It Works}
\begin{enumerate}
  \item User gives a keyword or theme.
  \item Gemini API generates a structured JSON with title, story, moral, and image prompts.
  \item Hugging Face API converts prompts into images.
  \item ReportLab assembles the story and images into a PDF.
  \item Streamlit allows user to run everything easily from the browser.
\end{enumerate}

\section*{📂 Project Structure}
\begin{lstlisting}
.
├── app.py              # Streamlit web interface
├── story_gen.py        # Gemini story generation code
├── image_gen.py        # Hugging Face image generation code
├── pdf_gen.py          # ReportLab PDF creation code
├── assets/             # Fonts, background images
├── output/             # Generated PDFs
└── README.tex          # This file
\end{lstlisting}

\section*{📸 Sample Output}
\begin{center}
\includegraphics[width=0.6\textwidth]{sample_output.png}
\end{center}

\section*{🔑 API Keys}
You’ll need:
\begin{itemize}
  \item Gemini API Key (Get from \url{https://makersuite.google.com/app})
  \item Hugging Face API Key (Get from \url{https://huggingface.co/settings/tokens})
\end{itemize}

\section*{🛠️ Installation}
\begin{lstlisting}[language=bash]
git clone https://github.com/yourusername/Ramayana-Story-Generator
cd Ramayana-Story-Generator
python -m venv env
env\Scripts\activate  # On Windows
pip install -r requirements.txt
streamlit run app.py
\end{lstlisting}

\section*{🎯 TODOs / Improvements}
\begin{itemize}
  \item Add audio narration
  \item Add more font customization
  \item Add story translations in regional languages
\end{itemize}

\section*{🙌 Credits}
Made with 💖 by Vishnuvardhan Chowdary on the occasion of Sri Rama Navami  
Follow me on \href{https://www.linkedin.com/in/your-profile}{LinkedIn}  

\end{document}
