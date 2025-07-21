PythonTextSummarizer
A simple and effective text summarization tool built with Python, leveraging the gensim library's TextRank algorithm to condense lengthy articles into concise summaries.

Table of Contents
About

Features

Prerequisites

Installation

Usage

Example Output

Contributing

License

About
This project provides a Python script that can summarize long pieces of text, such as articles, reports, or documents. It utilizes Natural Language Processing (NLP) techniques, specifically the TextRank algorithm implemented in the gensim library, to identify and extract the most important sentences, forming a coherent summary.

Features
Extractive Summarization: Identifies and extracts key sentences from the original text.

Adjustable Summary Length: Control the summary's length using a ratio parameter (e.g., 0.2 for 20% of original length).

Simple Python Script: Easy to run and integrate into other projects.

Leverages gensim: Built on a robust and widely used NLP library.

Prerequisites
Before running the script, ensure you have the following installed:

Python 3.6+

pip (Python package installer)

Installation
Clone the repository (or download the summarizer.py file):

git clone https://github.com/your-username/PythonTextSummarizer.git
cd PythonTextSummarizer

(Replace your-username with your actual GitHub username)

Install the gensim library:
Open your terminal or command prompt and run:

pip install gensim

Usage
Save the script: Ensure the summarizer.py file is in your project directory.

Open summarizer.py: You can open it in any text editor or IDE (like VS Code, PyCharm, or even a simple text editor).

Modify the lengthy_article variable:
Inside the if __name__ == "__main__": block, you'll find a multi-line string assigned to lengthy_article. Replace this placeholder text with the actual article content you wish to summarize.

lengthy_article = """
# PASTE YOUR ARTICLE CONTENT HERE
"""

Adjust Summary Ratio (Optional):
You can change the ratio parameter in the summarize_text function call to control the length of the summary.

ratio=0.3 (default in the example) means the summary will be approximately 30% of the original text's length.

A smaller ratio (e.g., 0.1) will produce a shorter summary.

A larger ratio (e.g., 0.5) will produce a longer summary.

concise_summary = summarize_text(lengthy_article, ratio=0.3)

Run the script:
Open your terminal or command prompt, navigate to your project directory, and execute the script:

python summarizer.py

The script will print the original article and its generated summaries to your console.

Example Output
--- Original Article ---
Artificial intelligence (AI) is rapidly transforming various aspects of human society,
from healthcare to transportation, and from entertainment to education. Its capabilities
are expanding at an unprecedented pace, driven by advancements in machine learning,
deep learning, and neural networks. AI refers to the simulation of human intelligence
in machines that are programmed to think like humans and mimic their actions. The term
may also be applied to any machine that exhibits traits associated with a human mind
such as learning and problem-solving.
... (rest of the original article) ...

==================================================

--- Concise Summary (Ratio 0.3) ---
Artificial intelligence (AI) is rapidly transforming various aspects of human society,
from healthcare to transportation, and from entertainment to education. AI refers to the simulation of human intelligence
in machines that are programmed to think like humans and mimic their actions. In healthcare, AI is being used for disease diagnosis, drug discovery, and personalized
treatment plans. The ethical implications of AI are also a growing concern.

==================================================

--- Concise Summary (Ratio 0.15) ---
Artificial intelligence (AI) is rapidly transforming various aspects of human society,
from healthcare to transportation, and from entertainment to education. In healthcare, AI is being used for disease diagnosis, drug discovery, and personalized
treatment plans.

==================================================

--- Concise Summary (Word Count 70) ---
Artificial intelligence (AI) is rapidly transforming various aspects of human society,
from healthcare to transportation, and from entertainment to education. Its capabilities
are expanding at an unprecedented pace, driven by advancements in machine learning,
deep learning, and neural networks. AI refers to the simulation of human intelligence
in machines that are programmed to think like humans and mimic their actions. The term
may also be applied to any machine that exhibits traits associated with a human mind
such as learning and problem-solving.

==================================================

--- Short Text Example ---
This is a very short sentence. It has no more information.

--- Summary of Short Text ---
This is a very short sentence.

==================================================

Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Make your changes.

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
