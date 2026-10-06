import streamlit as st
from backend.ai_engine import LocalRAG, build_guidance
from backend.url_analyzer import analyze_url
from backend.message_analyzer import analyze_message
from backend.security_scanner import scan_text
from backend.complaint_assistant import prepare_checklist
from backend.location_service import get_demo_locations, cities

@st.cache_resource(show_spinner="Loading local RAG model…")
def get_rag(): return LocalRAG()

def risk_badge(level):
    cls={"Low Risk":"risk-low","Suspicious":"risk-medium","High Risk":"risk-high"}.get(level,"risk-info")
    st.markdown(f'<div class="risk-badge {cls}">{level}</div>',unsafe_allow_html=True)

def render():
    st.markdown("""<div class="hero"><div class="eyebrow">AI-POWERED SAFETY • COLLEGE PROJECT</div><h1>🛡️ CyberShield AI</h1><p>A local-first safety and cyber-awareness assistant for practical, responsible guidance.</p></div>""",unsafe_allow_html=True)
    tabs=st.tabs(["🛡️ Women Safety","🤖 AI Chatbot","📝 Complaint","🔗 URL Analyzer","💬 Message Analyzer","📍 Nearby Help","☎️ Voice Prototype","📚 Resources","🔎 Threat Scanner"])
    with tabs[0]:
        st.subheader("Women Safety Assistant")
        situation=st.text_area("Describe what is happening",key="women_situation",height=140,placeholder="Example: Someone is repeatedly threatening me online…")
        if st.button("Get calm guidance",key="women_guidance"):
            if not situation.strip(): st.warning("Please describe the situation first.")
            else:
                result=build_guidance(situation,get_rag()); st.info(result["answer"])
                st.caption("General educational guidance only — not police, emergency, legal, or medical advice.")
    with tabs[1]:
        st.subheader("AI Safety Chatbot")
        q=st.chat_input("Ask about OTPs, phishing, harassment, privacy, reporting, or evidence…")
        if q:
            st.chat_message("user").write(q)
            rag=get_rag()
            if rag.error: st.warning("Semantic model is unavailable; using local keyword retrieval instead.")
            out=build_guidance(q,rag)
            st.chat_message("assistant").write(out["answer"])
            for s in out["sources"]: st.caption(f"Knowledge category: {s['category']} • {s['title']}")
    with tabs[2]:
        st.subheader("Complaint Assistance")
        desc=st.text_area("Incident description",key="complaint_desc")
        dt=st.text_input("Date / approximate time",key="complaint_dt")
        loc=st.text_input("Location / platform",key="complaint_loc")
        ev=st.text_area("Evidence you have",key="complaint_ev")
        if st.button("Prepare checklist",key="complaint_btn"):
            out=prepare_checklist(desc,dt,loc,ev)
            for x in out["items"]: st.markdown(f"☐ {x}")
            st.info(out["disclaimer"])
    with tabs[3]:
        st.subheader("Suspicious URL Analyzer")
        u=st.text_input("URL",key="url_input",placeholder="https://example.com/login")
        if st.button("Analyze URL",key="url_btn"):
            if not u.strip(): st.warning("Enter a URL.")
            else:
                out=analyze_url(u); risk_badge(out["risk_level"]); st.metric("Heuristic score", f"{out["score"]}/100")
                for x in out["indicators"]: st.warning(x)
                st.caption(out["explanation"])
    with tabs[4]:
        st.subheader("Suspicious Message Analyzer")
        m=st.text_area("Paste message text",key="message_input",height=160)
        if st.button("Analyze message",key="message_btn"):
            if not m.strip(): st.warning("Paste a message first.")
            else:
                out=analyze_message(m); risk_badge(out["risk_level"])
                st.write("**Detected indicators:**", ", ".join(out["indicators"]) if out["indicators"] else "None")
                st.write(out["explanation"])
                st.write("**Safe next steps**")
                for x in out["next_steps"]: st.markdown(f"• {x}")
    with tabs[5]:
        st.subheader("Nearby Help — DEMO / MOCK DATA")
        st.warning("These entries are fictional demo records for the college project. They are NOT real police stations, emergency services, or verified contacts.")
        city=st.selectbox("Select demo city",cities(),key="city_select")
        rows=get_demo_locations(city)
        for r in rows:
            with st.expander(f"{r['name']} • {r['category']}"):
                st.write(f"City: {r['city']}")
                st.write(f"Type: {r['type']}")
                st.caption("DEMO/MOCK — replace with verified API data before any real-world use.")
        st.markdown("**Future integration:** connect a verified maps/public-safety API, validate freshness, and display source timestamps.")
    with tabs[6]:
        st.subheader("Emergency / Voice Prototype")
        st.warning("PROTOTYPE ONLY — this demo cannot place calls, contact police, dispatch responders, or provide a real CyberShield phone number.")
        st.markdown("**Future architecture**")
        for x in ["Verified phone/IVR gateway receives a call.","Speech-to-text converts the caller's words to structured incident data.","A safety policy layer retrieves trusted guidance.","Human escalation / verified emergency routing handles real-world action.","Audit logs and consent controls protect sensitive information."]: st.markdown("1. "+x)
        st.caption("No fake phone numbers or emergency contacts are included.")
    with tabs[7]:
        st.subheader("Safety Resources")
        rag=get_rag()
        cats=sorted(rag.df["category"].unique())
        cat=st.selectbox("Topic",cats,key="resource_category")
        for _,r in rag.df[rag.df["category"]==cat].iterrows():
            with st.expander(r["title"]): st.write(r["content"])
    with tabs[8]:
        st.subheader("Local Cyber Threat Scanner")
        text=st.text_area("Scan text for common attack patterns",key="threat_text",height=150)
        if st.button("Scan patterns",key="threat_btn"):
            if not text.strip(): st.warning("Enter text first.")
            else:
                out=scan_text(text); risk_badge(out["risk_level"])
                for f in out["findings"]: st.warning(f"Detected: {f['category']}")
                st.caption(out["summary"])
