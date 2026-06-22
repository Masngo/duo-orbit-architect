```python
import streamlit as st
from risk_dashboard import calculate_risk
from dependency_graph import build_graph
from risk_scenarios import generate_risk_report

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Duo Orbit Architect",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🚀 Duo Orbit Architect")
st.caption(
    "Blast-Radius AI Engine powered by GitLab Orbit, "
    "Knowledge Graph Intelligence, and Risk Scoring"
)

# ---------------------------------------------------
# MERGE REQUEST ANALYZER
# ---------------------------------------------------

st.header("🔍 Merge Request Risk Analyzer")

col1, col2 = st.columns(2)

with col1:
    dependency_depth = st.slider(
        "Dependency Depth",
        0,
        100,
        20
    )

    critical_services = st.slider(
        "Critical Services Affected",
        0,
        100,
        15
    )

with col2:
    files_changed = st.slider(
        "Files Changed",
        0,
        30,
        10
    )

    test_gap = st.slider(
        "Test Coverage Gap",
        0,
        100,
        10
    )

# ---------------------------------------------------
# RISK CALCULATION
# ---------------------------------------------------

score, level = calculate_risk(
    dependency_depth,
    critical_services,
    files_changed,
    test_gap
)

metric1, metric2 = st.columns(2)

with metric1:
    st.metric("Risk Score", f"{score:.1f}/100")

with metric2:
    st.metric("Risk Level", level)

# ---------------------------------------------------
# DEPENDENCY GRAPH
# ---------------------------------------------------

st.header("🕸 Dependency Graph")

graph_path = build_graph()

st.image(
    graph_path,
    caption="Repository Dependency Analysis"
)

# ---------------------------------------------------
# RECOMMENDATIONS
# ---------------------------------------------------

st.header("📋 Recommendations")

if level == "HIGH":

    st.error(
        "⚠ High blast-radius detected."
    )

    st.warning(
        "Review authentication, session, and downstream services."
    )

    st.warning(
        "Add integration and regression tests before merging."
    )

elif level == "MEDIUM":

    st.warning(
        "Moderate architectural impact detected."
    )

    st.info(
        "Improve test coverage and verify affected services."
    )

else:

    st.success(
        "Low risk merge request."
    )

    st.success(
        "Safe to merge after standard review."
    )

# ---------------------------------------------------
# EXAMPLE RISK REPORTS
# ---------------------------------------------------

st.header("📊 Example Risk Reports")

scenario = st.selectbox(
    "Choose Example Scenario",
    ["low", "medium", "high"]
)

report = generate_risk_report(scenario)

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "Scenario Risk Score",
        f"{report['risk_score']}/100"
    )

with col4:
    st.metric(
        "Scenario Risk Level",
        report["risk_level"]
    )

st.subheader("Analysis Summary")
st.write(report["summary"])

st.subheader("Recommendation")

if report["risk_level"] == "HIGH":
    st.error(report["recommendation"])

elif report["risk_level"] == "MEDIUM":
    st.warning(report["recommendation"])

else:
    st.success(report["recommendation"])

st.subheader("Scenario Details")

st.write(
    f"""
    **Files Changed:** {report['files_changed']}

    **Services Impacted:** {report['services_impacted']}
    """
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "Built with GitLab Duo Agent Platform, GitLab Orbit, "
    "Knowledge Graph, Python, Streamlit, and MCP."
)
```