"""
═══════════════════════════════════════════════════════════════════════════════
GENAI KNOWLEDGE MAPPER - NLP EXTRACTOR MODULE
═══════════════════════════════════════════════════════════════════════════════

This module handles:
- Text cleaning and preprocessing
- Entity extraction (NER)
- Relation extraction
- POS tagging
- AI-powered summarization
- Confidence scoring
"""

import spacy
import re
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

# ═══════════════════════════════════════════════════════════════════════════════
# LOAD MODELS
# ═══════════════════════════════════════════════════════════════════════════════

try:
    nlp = spacy.load("en_core_web_sm")
    print("✅ spaCy model loaded successfully")
except OSError:
    raise Exception("""
    ❌ spaCy model not found!
    
    Install it with:
    python -m spacy download en_core_web_sm
    """)

# Load Groq API
GROQ_API_KEY = "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"

try:
    groq_client = Groq(api_key=GROQ_API_KEY)
    print("✅ Groq API initialized")
except Exception as e:
    print(f"⚠️ Groq API initialization warning: {e}")
    groq_client = None

# ═══════════════════════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

# Useful entity labels for extraction
USEFUL_LABELS = {
    "PERSON",       # People, names
    "ORG",          # Companies, organizations
    "GPE",          # Countries, cities, states
    "LOC",          # Locations, mountains, rivers
    "PRODUCT",      # Products, objects
    "EVENT",        # Named events
    "WORK_OF_ART",  # Books, songs, movies
    "LAW",          # Laws, acts
    "DATE",         # Dates, times
    "MONEY",        # Money amounts
    "FACILITY",     # Buildings, airports
    "LANGUAGE"      # Languages
}

# Useful POS (Part of Speech) tags
USEFUL_POS = {
    "NOUN",         # Nouns
    "VERB",         # Verbs
    "PROPN",        # Proper nouns
    "ADJ",          # Adjectives
    "ADV"           # Adverbs
}

# Dependency relations for relation extraction
SUBJECT_DEPS = {"nsubj", "nsubjpass", "agent"}  # Subject relations
OBJECT_DEPS = {"dobj", "attr", "pobj", "oprd", "acomp", "iobj"}  # Object relations

# ═══════════════════════════════════════════════════════════════════════════════
# TEXT CLEANING & PREPROCESSING
# ═══════════════════════════════════════════════════════════════════════════════

def clean_text(text, max_length=5000):
    """
    Clean and preprocess text
    
    Args:
        text: Input text string
        max_length: Maximum length to keep
        
    Returns:
        Cleaned text string
    """
    if not text or not isinstance(text, str):
        return ""
    
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)
    
    # Remove special characters but keep basic punctuation
    text = re.sub(r"[^A-Za-z0-9.,!?;:'\"\-\(\)\[\] ]", "", text)
    
    # Limit length
    if len(text) > max_length:
        text = text[:max_length]
    
    return text.strip()

def normalize_text(text):
    """
    Normalize text for processing
    
    Args:
        text: Input text
        
    Returns:
        Normalized text
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()

# ═══════════════════════════════════════════════════════════════════════════════
# ENTITY EXTRACTION
# ═══════════════════════════════════════════════════════════════════════════════

def extract_entities(doc):
    """
    Extract named entities from spaCy doc
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of entity dictionaries
    """
    entities = {}
    
    for ent in doc.ents:
        # Only keep useful entity types
        if ent.label_ not in USEFUL_LABELS:
            continue
        
        # Normalize key
        key = ent.text.lower().strip()
        
        # Skip very short entities
        if len(key) < 2:
            continue
        
        # Avoid duplicates
        if key not in entities:
            try:
                description = spacy.explain(ent.label_) or ent.label_
            except:
                description = ent.label_
            
            entities[key] = {
                "text": ent.text,
                "label": ent.label_,
                "start": ent.start_char,
                "end": ent.end_char,
                "description": description
            }
    
    return list(entities.values())

def extract_entity_frequencies(doc):
    """
    Extract and count entity frequencies
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        Dictionary with entity frequencies
    """
    entity_freq = {}
    
    for ent in doc.ents:
        if ent.label_ not in USEFUL_LABELS:
            continue
        
        key = ent.text.lower()
        if key not in entity_freq:
            entity_freq[key] = {"text": ent.text, "label": ent.label_, "count": 0}
        entity_freq[key]["count"] += 1
    
    # Sort by frequency
    sorted_entities = sorted(
        entity_freq.values(),
        key=lambda x: x["count"],
        reverse=True
    )
    
    return sorted_entities[:20]  # Return top 20

# ═══════════════════════════════════════════════════════════════════════════════
# POS TAGGING
# ═══════════════════════════════════════════════════════════════════════════════

def extract_pos_tags(doc):
    """
    Extract POS tags from spaCy doc
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of POS tag dictionaries
    """
    pos_tags = []
    
    for token in doc:
        # Only keep useful POS tags
        if token.pos_ not in USEFUL_POS:
            continue
        
        # Skip stopwords and very short tokens
        if token.is_stop or len(token.text) <= 1:
            continue
        
        pos_tags.append({
            "token": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "tag": token.tag_,
            "dep": token.dep_,
            "is_alpha": token.is_alpha,
            "is_stop": token.is_stop
        })
    
    return pos_tags

def extract_nouns(doc):
    """
    Extract all nouns from text (for keywords)
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of noun dictionaries
    """
    nouns = {}
    
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and len(token.text) > 2:
            key = token.lemma_.lower()
            if key not in nouns:
                nouns[key] = {"text": token.text, "count": 0}
            nouns[key]["count"] += 1
    
    # Sort by frequency
    sorted_nouns = sorted(
        nouns.values(),
        key=lambda x: x["count"],
        reverse=True
    )
    
    return sorted_nouns[:30]  # Return top 30

# ═══════════════════════════════════════════════════════════════════════════════
# RELATION EXTRACTION
# ═══════════════════════════════════════════════════════════════════════════════

def extract_relations(doc):
    """
    Extract relations (subject-verb-object) from spaCy doc
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of relation dictionaries
    """
    relations = []
    
    for token in doc:
        # Only process verbs
        if token.pos_ != "VERB" or token.is_stop:
            continue
        
        subjects = []
        objects = []
        
        # Extract subjects and objects from children
        for child in token.children:
            # Extract subjects
            if child.dep_ in SUBJECT_DEPS:
                subj_tokens = [t.text for t in child.subtree if not t.is_punct]
                subj_text = " ".join(subj_tokens).strip()
                if subj_text:
                    subjects.append(subj_text)
            
            # Extract objects
            if child.dep_ in OBJECT_DEPS:
                obj_tokens = [t.text for t in child.subtree if not t.is_punct]
                obj_text = " ".join(obj_tokens).strip()
                if obj_text:
                    objects.append(obj_text)
        
        # Create relations
        for subject in subjects:
            for obj in objects:
                if subject.lower() != obj.lower():  # Avoid reflexive relations
                    relations.append({
                        "subject": subject,
                        "verb": token.lemma_,
                        "object": obj,
                        "confidence": 0.8
                    })
    
    # Remove duplicates while preserving order
    seen = set()
    unique_relations = []
    
    for rel in relations:
        key = (rel["subject"].lower(), rel["verb"], rel["object"].lower())
        if key not in seen:
            seen.add(key)
            unique_relations.append(rel)
    
    return unique_relations

def extract_verb_phrases(doc):
    """
    Extract verb phrases from text
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of verb phrase dictionaries
    """
    verb_phrases = []
    
    for token in doc:
        if token.pos_ == "VERB" and not token.is_stop:
            # Get the phrase around the verb
            start = max(0, token.i - 2)
            end = min(len(doc), token.i + 3)
            phrase = " ".join([t.text for t in doc[start:end]])
            
            verb_phrases.append({
                "verb": token.lemma_,
                "phrase": phrase,
                "pos": token.pos_
            })
    
    return verb_phrases

# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARIZATION
# ═══════════════════════════════════════════════════════════════════════════════

def generate_summary(text):
    """
    Generate AI summary using Groq LLaMA
    
    Args:
        text: Input text to summarize
        
    Returns:
        Summary string
    """
    # Skip if text is too short
    if len(text.split()) < 15:
        return text
    
    # Limit text length for API
    text_to_summarize = text[:2000]
    
    if not groq_client:
        return generate_fallback_summary(text)
    
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """You are an expert summarizer. Create a clear, concise summary that:
- Captures the main ideas
- Identifies key entities (people, places, organizations)
- Highlights important relationships
- Is 3-5 sentences long
- Uses simple, professional language"""
                },
                {
                    "role": "user",
                    "content": f"Summarize this text:\n\n{text_to_summarize}"
                }
            ],
            max_tokens=300,
            temperature=0.5
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"⚠️ Groq summary error: {e}")
        return generate_fallback_summary(text)

def generate_fallback_summary(text):
    """
    Generate extractive summary as fallback
    
    Args:
        text: Input text
        
    Returns:
        Summary string
    """
    sentences = text.split(".")
    
    # Return first 3 sentences or less if fewer exist
    summary_sentences = sentences[:min(3, len(sentences))]
    summary = ". ".join([s.strip() for s in summary_sentences if s.strip()])
    
    if summary and not summary.endswith("."):
        summary += "."
    
    return summary

def generate_detailed_summary(text, doc):
    """
    Generate a detailed summary with structure
    
    Args:
        text: Original text
        doc: spaCy Doc object
        
    Returns:
        Dictionary with structured summary
    """
    try:
        base_summary = generate_summary(text)
    except:
        base_summary = generate_fallback_summary(text)
    
    entities = extract_entity_frequencies(doc)
    nouns = extract_nouns(doc)
    
    return {
        "summary": base_summary,
        "key_entities": entities[:5],
        "key_topics": nouns[:5],
        "text_length": len(text.split()),
        "entity_count": len(entities),
        "topic_count": len(nouns)
    }

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIDENCE SCORING
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_confidence(entity_count, relation_count, text_length):
    """
    Calculate confidence score for extraction
    
    Args:
        entity_count: Number of entities found
        relation_count: Number of relations found
        text_length: Length of input text in words
        
    Returns:
        Confidence score (0-100)
    """
    # Base score
    score = 50
    
    # Add points for entities
    score += min(entity_count * 1.5, 20)
    
    # Add points for relations
    score += min(relation_count * 2, 20)
    
    # Add points for text length (longer = more confidence)
    if text_length > 50:
        score += 5
    if text_length > 200:
        score += 5
    if text_length > 500:
        score += 5
    
    # Cap at 100
    return min(score, 100)

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN EXTRACTION FUNCTION
# ═══════════════════════════════════════════════════════════════════════════════

def extract_entities_relations(text):
    """
    Main extraction function - extracts everything from text
    
    Args:
        text: Input text to analyze
        
    Returns:
        Dictionary with all extraction results
    """
    # Validate input
    if not text or not isinstance(text, str):
        return {
            "error": "Invalid input: text must be a non-empty string",
            "entities": [],
            "relations": [],
            "pos_tags": [],
            "summary": "",
            "metrics": {
                "entity_count": 0,
                "relation_count": 0,
                "confidence_score": 0
            }
        }
    
    # Clean text
    cleaned_text = clean_text(text)
    
    if not cleaned_text:
        return {
            "error": "Empty or invalid input text after cleaning",
            "entities": [],
            "relations": [],
            "pos_tags": [],
            "summary": "",
            "metrics": {
                "entity_count": 0,
                "relation_count": 0,
                "confidence_score": 0
            }
        }
    
    try:
        # Process with spaCy
        doc = nlp(cleaned_text)
        
        # Extract everything
        entities = extract_entities(doc)
        relations = extract_relations(doc)
        pos_tags = extract_pos_tags(doc)
        summary = generate_summary(cleaned_text)
        
        # Extract sentences for parse tree selection
        sentences = [
            sent.text.strip()
            for sent in doc.sents
            if len(sent.text.strip()) > 8 and len(sent.text.strip().split()) >= 3
        ]

        # Calculate metrics
        entity_count = len(entities)
        relation_count = len(relations)
        text_length = len(cleaned_text.split())
        confidence = calculate_confidence(entity_count, relation_count, text_length)
        
        return {
            "cleaned_text": cleaned_text,
            "summary": summary,
            "entities": entities,
            "relations": relations,
            "pos_tags": pos_tags,
            "sentences": sentences,
            "metrics": {
                "entity_count": entity_count,
                "relation_count": relation_count,
                "text_length": text_length,
                "confidence_score": confidence
            }
        }
    
    except Exception as e:
        print(f"❌ Extraction error: {e}")
        return {
            "error": f"Processing error: {str(e)}",
            "entities": [],
            "relations": [],
            "pos_tags": [],
            "summary": "",
            "metrics": {
                "entity_count": 0,
                "relation_count": 0,
                "confidence_score": 0
            }
        }

# ═══════════════════════════════════════════════════════════════════════════════
# ADDITIONAL ANALYSIS FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def analyze_text_complexity(doc):
    """
    Analyze text complexity metrics
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        Dictionary with complexity metrics
    """
    # Count different POS types
    pos_counts = {}
    for token in doc:
        pos = token.pos_
        pos_counts[pos] = pos_counts.get(pos, 0) + 1
    
    # Count sentence count
    sentences = list(doc.sents)
    
    # Average words per sentence
    avg_words_per_sent = len(doc) / len(sentences) if sentences else 0
    
    return {
        "token_count": len(doc),
        "sentence_count": len(sentences),
        "avg_tokens_per_sentence": round(avg_words_per_sent, 2),
        "pos_distribution": pos_counts,
        "unique_tokens": len(set([token.text.lower() for token in doc]))
    }

def extract_key_phrases(doc):
    """
    Extract noun phrases and key phrases
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of key phrases
    """
    key_phrases = []
    
    for chunk in doc.noun_chunks:
        if len(chunk.text) > 2:  # Skip very short phrases
            key_phrases.append({
                "phrase": chunk.text,
                "root": chunk.root.text,
                "root_pos": chunk.root.pos_
            })
    
    return key_phrases

def extract_dependencies(doc):
    """
    Extract dependency parse information
    
    Args:
        doc: spaCy Doc object
        
    Returns:
        List of dependency relationships
    """
    dependencies = []
    
    for token in doc:
        if token.dep_ != "ROOT":
            dependencies.append({
                "token": token.text,
                "pos": token.pos_,
                "dep": token.dep_,
                "head": token.head.text,
                "head_pos": token.head.pos_
            })
    
    return dependencies

# ═══════════════════════════════════════════════════════════════════════════════
# BATCH PROCESSING
# ═══════════════════════════════════════════════════════════════════════════════

def batch_extract(texts):
    """
    Extract entities and relations from multiple texts
    
    Args:
        texts: List of text strings
        
    Returns:
        List of extraction results
    """
    results = []
    
    for text in texts:
        result = extract_entities_relations(text)
        results.append(result)
    
    return results

# ═══════════════════════════════════════════════════════════════════════════════
# EXPORT
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # Test the extractor
    test_text = """
    Apple Inc. is a technology company founded by Steve Jobs in 1976 in Los Angeles, California.
    The company manufactures and sells smartphones, computers, and tablets.
    Tim Cook is the current CEO of Apple and leads the company's operations worldwide.
    Apple's headquarters is located in Cupertino, California, and it employs over 150,000 people.
    """
    
    print("Testing extractor.py...")
    print("=" * 80)
    
    result = extract_entities_relations(test_text)
    
    print(f"\n✅ Summary:\n{result['summary']}\n")
    print(f"✅ Entities Found: {result['metrics']['entity_count']}")
    for ent in result['entities'][:5]:
        print(f"   - {ent['text']} ({ent['label']})")
    
    print(f"\n✅ Relations Found: {result['metrics']['relation_count']}")
    for rel in result['relations'][:3]:
        print(f"   - {rel['subject']} {rel['verb']} {rel['object']}")
    
    print(f"\n✅ Confidence Score: {result['metrics']['confidence_score']}/100")
    print("=" * 80)