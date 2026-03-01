from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)  # set device=0 if GPU

def summarize_text(text, max_length=150, min_length=40):
    # For long text, chunk before calling summarizer
    return summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]["summary_text"]