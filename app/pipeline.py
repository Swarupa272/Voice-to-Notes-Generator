from .asr import transcribe_audio
from .summarizer import summarize_text
import math

def chunk_text_by_sentences(text, max_chars=3000):
    # naive: split by paragraphs / sentences. Replace with better sentence tokenizer as needed.
    sentences = text.split('. ')
    chunks = []
    cur = []
    cur_len = 0
    for s in sentences:
        slen = len(s)
        if cur_len + slen > max_chars and cur:
            chunks.append('. '.join(cur) + '.')
            cur = [s]
            cur_len = slen
        else:
            cur.append(s)
            cur_len += slen
    if cur:
        chunks.append('. '.join(cur) + '.')
    return chunks

def process_audio_file(path):
    t = transcribe_audio(path)
    transcript = t["text"]
    chunks = chunk_text_by_sentences(transcript, max_chars=3000)
    chunk_summaries = [summarize_text(c) for c in chunks]
    combined = " ".join(chunk_summaries)
    final_summary = summarize_text(combined, max_length=200)
    return {
        "transcript": transcript,
        "chunk_summaries": chunk_summaries,
        "final_summary": final_summary
    }