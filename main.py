import gensim # Changed to import the entire gensim package

def summarize_text(text, ratio=0.2):
    """
    Summarizes the given text using the TextRank algorithm.

    Args:
        text (str): The input text (e.g., a lengthy article) to be summarized.
        ratio (float): The ratio of the original text's length that the summary
                       should aim for. For example, 0.2 means the summary will
                       be approximately 20% of the original text length.
                       You can also use 'word_count' instead of 'ratio' to
                       specify the maximum number of words in the summary.

    Returns:
        str: The concise summary of the input text.
    """
    try:
        # Use gensim's summarize function.
        # It extracts important sentences based on their similarity to other sentences.
        # Now called as gensim.summarize since we imported the whole package
        summary = gensim.summarize.summarize(text, ratio=ratio)
        return summary
    except Exception as e:
        return f"An error occurred during summarization: {e}"

if __name__ == "__main__":
    # --- Example Usage ---

    # 1. Define a lengthy article (replace with your actual article content)
    # This is a placeholder example. In a real application, you might read
    # this from a file, a web page, or user input.
    lengthy_article = """
    Artificial intelligence (AI) is rapidly transforming various aspects of human society,
    from healthcare to transportation, and from entertainment to education. Its capabilities
    are expanding at an unprecedented pace, driven by advancements in machine learning,
    deep learning, and neural networks. AI refers to the simulation of human intelligence
    in machines that are programmed to think like humans and mimic their actions. The term
    may also be applied to any machine that exhibits traits associated with a human mind
    such as learning and problem-solving.

    One of the most significant applications of AI is in data analysis. AI algorithms can
    process vast amounts of data much faster and more efficiently than humans, identifying
    patterns and insights that would otherwise be impossible to detect. This is particularly
    valuable in fields like finance, where AI can predict market trends, and in scientific
    research, where it can accelerate discoveries.

    In healthcare, AI is being used for disease diagnosis, drug discovery, and personalized
    treatment plans. For instance, AI-powered systems can analyze medical images with high
    accuracy, assisting doctors in detecting early signs of diseases like cancer. Robotic
    surgery, powered by AI, allows for greater precision and less invasive procedures.

    The ethical implications of AI are also a growing concern. Issues such as job displacement
    due to automation, algorithmic bias, and privacy concerns need careful consideration.
    As AI becomes more integrated into our daily lives, it's crucial to develop robust
    ethical guidelines and regulations to ensure its responsible development and deployment.
    The future of AI holds immense promise, but it also presents significant challenges
    that require collaborative efforts from researchers, policymakers, and the public.
    """

    print("--- Original Article ---")
    print(lengthy_article)
    print("\n" + "="*50 + "\n") # Separator

    # 2. Summarize the article
    # You can adjust the 'ratio' (e.g., 0.1 for a shorter summary, 0.3 for a longer one)
    # or use word_count=50 for a summary of approximately 50 words.
    concise_summary = summarize_text(lengthy_article, ratio=0.3)

    print("--- Concise Summary (Ratio 0.3) ---")
    print(concise_summary)
    print("\n" + "="*50 + "\n") # Separator

    # Example with a different ratio
    concise_summary_shorter = summarize_text(lengthy_article, ratio=0.15)
    print("--- Concise Summary (Ratio 0.15) ---")
    print(concise_summary_shorter)
    print("\n" + "="*50 + "\n") # Separator

    # Example with word count
    # Note: gensim.summarize's `word_count` parameter is deprecated
    # in newer versions of gensim (4.0.0+). It's recommended to use `ratio` instead.
    # If you are using an older gensim version where word_count is still supported,
    # you can uncomment the line below.
    # concise_summary_word_count = summarize_text(lengthy_article, word_count=70)
    # print("--- Concise Summary (Word Count 70) ---")
    # print(concise_summary_word_count)
    # print("\n" + "="*50 + "\n") # Separator

    # Example of a very short text (might not summarize well or raise an error if too short)
    short_text = "This is a very short sentence. It has no more information."
    print("--- Short Text Example ---")
    print(short_text)
    print("\n--- Summary of Short Text ---")
    print(summarize_text(short_text, ratio=0.5))
    print("\n" + "="*50 + "\n") # Separator
