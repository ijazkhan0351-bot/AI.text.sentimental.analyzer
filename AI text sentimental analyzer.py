from tkinter import *
from tkinter import messagebox

# Knowledge base (words list)
positive_words = [
    "good", "great", "excellent", "happy",
    "love", "amazing", "nice", "awesome"
]

negative_words = [
    "bad", "worst", "sad", "hate",
    "angry", "poor", "terrible", "boring"
]

def analyze_sentiment():
    # User ka text lena
    text = text_input.get("1.0", END)

    # Text clean karna
    text = text.strip().lower()

    # Empty input validation
    if text == "":
        messagebox.showerror("Error", "Please enter some text")
        return

    # Words me convert karna (tokenization)
    words = text.split()

    # Member-2 ke liye data pass
    process_sentiment(words)

# ---------- GUI Design ----------
root = Tk()
root.title("Rule-Based Sentiment Analyzer")
root.geometry("500x400")
root.resizable(False, False)

Label(root, text="Enter Text:", font=("Arial", 14)).pack(pady=10)

text_input = Text(root, height=6, width=50)
text_input.pack()

Button(
    root,
    text="Analyze Sentiment",
    font=("Arial", 14),
    command=analyze_sentiment
).pack(pady=10)

result_label = Label(root, text="Sentiment:", font=("Arial", 14))
result_label.pack(pady=20)

# ---------- Member-2: Rule-Based Sentiment Logic ----------

def process_sentiment(words):

    positive_count = 0
    negative_count = 0

    # Loop se har word check karna
    for word in words:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    # Decision making
    if positive_count > negative_count:
        result = "Positive 😊"
    elif negative_count > positive_count:
        result = "Negative 😞"
    else:
        result = "Neutral 😐"

    # Output GUI pe show karna
    result_label.config(
        text=(
            f"Sentiment: {result}\n"
            f"Positive Words: {positive_count}\n"
            f"Negative Words: {negative_count}"
        )
    )

# GUI loop
root.mainloop()