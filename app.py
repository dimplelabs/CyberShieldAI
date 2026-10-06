import streamlit as st
from frontend.dashboard import render

st.set_page_config(page_title="CyberShield AI",page_icon="🛡️",layout="wide",initial_sidebar_state="expanded")
st.markdown("""<style>
.block-container{max-width:1200px;padding-top:2rem}
.hero{padding:2rem;border:1px solid rgba(128,128,128,.25);border-radius:22px;margin-bottom:1.2rem;background:linear-gradient(135deg,rgba(80,120,255,.12),rgba(130,70,200,.08))}
.hero h1{font-size:3rem;margin:.2rem 0}.eyebrow{font-size:.75rem;letter-spacing:.16em;font-weight:700;opacity:.7}
.risk-badge{display:inline-block;padding:.45rem .8rem;border-radius:999px;font-weight:800;margin:.4rem 0 1rem}
.risk-low{background:#dff7e7;color:#176b36}.risk-medium{background:#fff0c2;color:#7a5400}.risk-high{background:#ffdede;color:#9d2020}.risk-info{background:#e5e7eb;color:#374151}
div[data-testid="stTabs"] button{font-weight:600}
</style>""",unsafe_allow_html=True)
with st.sidebar:
    st.markdown("## 🛡️ CyberShield AI")
    st.caption("Responsible safety + cyber-awareness prototype")
    st.markdown("---")
    st.info("Core demo works without external API keys. RAG uses a local knowledge base.")
render()
