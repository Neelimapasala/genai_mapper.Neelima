# rag_engine.py
# RAG Engine using Groq (free, fast)

from groq import Groq

# ✅ Paste your Groq API key here
GROQ_API_KEY = "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"

class RAGEngine:
    def __init__(self):
        self.chunks = []
        self.client = Groq(api_key=GROQ_API_KEY)

    def build_index(self, chunks):
        """Store chunks for retrieval"""
        self.chunks = chunks

    def query(self, question, top_k=3):
        """Return top_k relevant chunks based on keyword matching"""
        if not self.chunks:
            return []

        question_words = question.lower().split()
        scored = []

        for chunk in self.chunks:
            score = sum(1 for word in question_words if word in chunk.lower())
            if score > 0:
                scored.append((score, chunk))

        scored.sort(reverse=True, key=lambda x: x[0])
        return [chunk for _, chunk in scored[:top_k]]

    def answer(self, question):
        """Use Groq to answer based on retrieved chunks"""
        if not self.chunks:
            return "No document has been processed yet. Please paste text on the Map page first."

        relevant = self.query(question, top_k=3)
        context = "\n".join(relevant) if relevant else "\n".join(self.chunks[:3])

        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": f"""You are an AI assistant helping users understand their documents.

Document context:
---
{context}
---

Answer based on the context above. If the answer is not in the context, say so and answer from general knowledge."""
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Groq error: {e}")
            return f"Groq error: {str(e)}"

    def get_answer(self, question, context_id=None):
        """Alias for uniformity"""
        return self.answer(question)