# nlp_pipeline.py
import spacy
from collections import Counter

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")

class NLPResult:
    """Class to store NLP results"""
    def __init__(self):
        self.cleaned_text = ""
        self.pos_tags = []         # [(token, pos)]
        self.entities = []         # [(entity_text, label, pos)]
        self.relations = []        # [(subject, subj_pos, verb, verb_pos, object, obj_pos)]
        self.summary = ""          # Extractive summary

# --- File reader for txt/docx ---
def read_file(file):
    ext = file.filename.split('.')[-1].lower()
    text = ""
    if ext == "txt":
        text = file.read().decode("utf-8")
    elif ext == "docx":
        from docx import Document
        doc = Document(file)
        text = "\n".join([p.text for p in doc.paragraphs])
    return text

# --- Main NLP processing ---
def process_text(text, options=None):
    """
    Process text with options: lowercase, remove_stopwords, lemmatize, remove_punct
    Returns NLPResult
    """
    if options is None:
        options = {}
    result = NLPResult()
    doc = nlp(text)

    # --- Clean text ---
    cleaned_tokens = []
    for token in doc:
        t = token.text
        if options.get("lowercase"): t = t.lower()
        if options.get("remove_stopwords") and token.is_stop: continue
        if options.get("remove_punct") and token.is_punct: continue
        if options.get("lemmatize"): t = token.lemma_
        cleaned_tokens.append(t)
    result.cleaned_text = " ".join(cleaned_tokens)

    # --- POS tags ---
    result.pos_tags = [(token.text, token.pos_) for token in doc]

    # --- Named Entities with POS ---
    result.entities = [(ent.text, ent.label_, ent.root.pos_) for ent in doc.ents]

    # --- Relations (Simple Subject-Verb-Object) ---
    result.relations = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "ROOT":
                subjects = [w for w in token.lefts if w.dep_ in ["nsubj","nsubjpass"]]
                objects = [w for w in token.rights if w.dep_ in ["dobj","pobj"]]
                for s in subjects:
                    for o in objects:
                        result.relations.append(
                            (s.text, s.pos_, token.text, token.pos_, o.text, o.pos_)
                        )

    # --- Extractive summary: top 3 sentences by noun/verb frequency ---
    word_freq = Counter([t.text.lower() for t in doc if t.pos_ in ["NOUN","VERB"]])
    sentences = list(doc.sents)
    top_sents = sorted(
        sentences,
        key=lambda s: sum(word_freq.get(w.text.lower(),0) for w in s),
        reverse=True
    )
    result.summary = " ".join([str(s) for s in top_sents[:3]])

    return result

# --- Build Knowledge Graph data for front-end (Cytoscape.js) ---
def build_graph(entities, relations):
    nodes = [{"data":{"id":ent,"label":f"{ent}\n({label})"}} for ent, label, pos in entities]
    edges = [{"data":{"source":subj,"target":obj,"label":verb}} for subj, subj_pos, verb, verb_pos, obj, obj_pos in relations]
    return {"nodes": nodes, "edges": edges}

# --- Chatbot AI placeholder ---
def chatbot_answer(question):
    # Replace this with OpenAI API or your own AI model
    return f"AI Answer: {question}"