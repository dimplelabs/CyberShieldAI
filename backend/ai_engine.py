import pandas as pd
from .config import KNOWLEDGE_BASE_PATH, MODEL_NAME

class LocalRAG:
    def __init__(self):
        self.df=pd.read_csv(KNOWLEDGE_BASE_PATH).fillna("")
        self.model=None
        self.embeddings=None
        self.error=None
        try:
            from sentence_transformers import SentenceTransformer
            import numpy as np
            self.model=SentenceTransformer(MODEL_NAME)
            self.embeddings=self.model.encode(self.df["content"].tolist(), normalize_embeddings=True)
        except Exception as exc:
            self.error=str(exc)

    def retrieve(self, query, top_k=3):
        if not query.strip():
            return []
        if self.model is None:
            terms=set(query.lower().split())
            scored=[]
            for i,row in self.df.iterrows():
                overlap=len(terms & set(str(row["content"]).lower().split()))
                scored.append((overlap,i))
            idx=[i for _,i in sorted(scored,reverse=True)[:top_k]]
        else:
            import numpy as np
            q=self.model.encode([query],normalize_embeddings=True)[0]
            scores=self.embeddings @ q
            idx=np.argsort(scores)[::-1][:top_k]
        return [self.df.iloc[int(i)].to_dict() for i in idx]

def build_guidance(query, rag):
    rows=rag.retrieve(query)
    if not rows:
        return {"answer":"Please describe the situation so I can retrieve relevant general guidance.","sources":[]}
    lines=["Here is general safety guidance based on the local knowledge base:"]
    for r in rows:
        lines.append(f"• {r['content']}")
    lines.append("If you are in immediate danger, prioritize getting to a safer place and contacting an appropriate trusted person or locally verified emergency resource.")
    return {"answer":"\n".join(lines),"sources":[{"title":r["title"],"category":r["category"]} for r in rows]}
