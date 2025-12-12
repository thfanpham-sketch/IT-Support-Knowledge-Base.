
import re
import streamlit as st
from pathlib import Path


st.set_page_config(page_title="IT Support Knowledge Base", page_icon="🛠️")
st.title("🛠️ IT Support Knowledge Base")
st.write("Search and browse troubleshooting guides for hardware, software, and network issues.")


BASE = Path(__file__).resolve().parent.parent
DOCS = BASE / "A_Troubleshooting guides"


section = st.sidebar.selectbox("Choose a section", ["All", "Hardware", "Software", "Network"])
query = st.sidebar.text_input("Search keywords", "").strip()


DOC_FILES = ["hardware.md", "software.md", "network.md"]
content_map = {}
for fname in DOC_FILES:
    p = DOCS / fname
    content_map[fname] = p.read_text(encoding="utf-8") if p.exists() else ""

# Keyword match
def matches(text: str, q: str) -> bool:
    return (not q) or (q.lower() in text.lower())

# Highlight text with <mark> (real tags, not escaped)
def highlight_all(text: str, q: str) -> str:
    if not q:
        return text
    pattern = re.compile(re.escape(q), re.IGNORECASE)
    return pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", text)

# Render 
def render_with_focus(title: str, text: str, q: str):
    st.subheader(title)
    if not q:
        
        st.markdown(text, unsafe_allow_html=True)
        return

  
    m = re.search(re.escape(q), text, flags=re.IGNORECASE)
    if not m:
        # No match
        st.markdown(text, unsafe_allow_html=True)
        return

    start_idx = m.start()

    # Split content 
    before = text[:start_idx]
    after = text[start_idx:]

    
    st.caption("Showing content from the first match. Earlier content is available below.")

    
    if before.strip():
        with st.expander("Show earlier content", expanded=False):
            st.markdown(highlight_all(before, q), unsafe_allow_html=True)

    
    st.markdown(highlight_all(after, q), unsafe_allow_html=True)


sections_map = {
    "Hardware": "hardware.md",
    "Software": "software.md",
    "Network": "network.md",
}

# Display
if section == "All":
    any_rendered = False
    for fname in DOC_FILES:
        content = content_map.get(fname, "")
        if content and matches(content, query):
            any_rendered = True
            title = fname.replace(".md", "").capitalize()
            render_with_focus(title, content, query)
    if not any_rendered:
        st.info("No matching content. Try clearing the search box or choose another section.")
else:
    fname = sections_map.get(section)
    content = content_map.get(fname, "")
    if content and matches(content, query):
        render_with_focus(section, content, query)
    else:
        st.info("No matching content. Try clearing the search box or choose another section.")
