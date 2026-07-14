"""Professional SaaS sidebar."""

import os

import streamlit as st


def render_sidebar():
    with st.sidebar:
        # ── Brand ──────────────────────────────────────
        st.markdown(
            """
            <div class="sb-brand">
              <div style="display:flex;align-items:center;gap:.65rem">
                <div style="
                    width:32px;
                    height:32px;
                    background:linear-gradient(135deg,#6366f1,#a855f7);
                    border-radius:9px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:.95rem;
                    box-shadow:0 4px 12px rgba(99,102,241,.3)
                ">
                    🔍
                </div>

                <div>
                  <div style="
                      font-weight:700;
                      font-size:.9rem;
                      color:var(--t1);
                      letter-spacing:-.02em
                  ">
                      CodeReview AI
                  </div>

                  <div style="
                      font-size:.62rem;
                      color:var(--t3);
                      font-family:var(--mono)
                  ">
                      v2.0 · Groq + Llama 3.3
                  </div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ── API Connection Status ──────────────────────
        st.markdown(
            '<div class="sb-section">Configuration</div>',
            unsafe_allow_html=True,
        )

        api_key = os.environ.get("GROQ_API_KEY", "").strip()

        if api_key:
            st.markdown(
                """
                <div class="sb-key-status-ok">
                  <div class="sb-key-dot-ok"></div>
                  <span style="font-size:.7rem;color:var(--green)">
                    Connected · Groq API
                  </span>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
                <div class="sb-key-status-err">
                  <div class="sb-key-dot-err"></div>
                  <span style="font-size:.7rem;color:var(--red)">
                    API configuration missing
                  </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.caption(
                "Add GROQ_API_KEY in Streamlit Cloud → Manage app → Settings → Secrets."
            )

        # ── File Explorer ───────────────────────────────
        from storage.result_store import store

        if not store.is_empty():
            st.markdown(
                '<div class="sb-section">File Explorer</div>',
                unsafe_allow_html=True,
            )

            severity_icons = {
                "Critical": "🔴",
                "High": "🟠",
                "Medium": "🟡",
                "Low": "🟢",
                "Clean": "✅",
            }

            for index, result in enumerate(store.sorted_by_severity()):
                icon = severity_icons.get(
                    result.worst_severity,
                    "📄",
                )

                is_selected = (
                    st.session_state.get("selected_file")
                    == result.path
                )

                if st.button(
                    f"{icon}  {result.name[:21]}",
                    key=f"fb_{index}",
                    use_container_width=True,
                    type="primary" if is_selected else "secondary",
                    help=result.path,
                ):
                    st.session_state.selected_file = result.path
                    st.rerun()

            # ── Session Statistics ──────────────────────
            st.markdown(
                f"""
                <div style="
                    margin:.75rem .25rem 0;
                    padding:.65rem .8rem;
                    background:var(--bg3);
                    border:1px solid var(--border);
                    border-radius:var(--rs)
                ">
                  <div style="
                      font-size:.62rem;
                      color:var(--t3);
                      margin-bottom:.4rem;
                      font-weight:600;
                      text-transform:uppercase;
                      letter-spacing:.07em
                  ">
                      Session
                  </div>

                  <div style="
                      font-family:var(--mono);
                      font-size:.7rem;
                      color:var(--t2)
                  ">
                    {store.total_files} files ·
                    {store.total_issues} issues
                    <br>

                    <span style="color:var(--red)">
                        {store.critical_count} critical
                    </span>
                    ·
                    <span style="color:var(--orange)">
                        {store.high_count} high
                    </span>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ── Footer ──────────────────────────────────────
        st.markdown(
            """
            <div class="sb-footer">
              Powered by
              <span style="color:var(--accent2);font-weight:600">
                Llama 3.3 70B
              </span>
              <br>

              via Groq Infrastructure
            </div>
            """,
            unsafe_allow_html=True,
        )