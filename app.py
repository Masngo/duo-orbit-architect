import streamlit as st
from risk_dashboard import calculate_risk
from dependency_graph import build_graph
from risk_scenarios import generate_risk_report

st.title("🚀 Duo Orbit Architect")

st.subheader("Merge Request Risk Analyzer")

# Inputs (simulate MR changes)
dependency_depth = st.slider("Dependency Depth", 0, 50, 20)
critical_services = st.slider("Critical Services Affected", 0, 50, 15)
files_changed = st.slider("Files Changed", 0, 30, 10)
test_gap = st.slider("Test Coverage Gap", 0, 30, 10)

# Risk calculation
score, level = calculate_risk(
    dependency_depth,
    critical_services,
    files_changed,
    test_gap
)

st.metric("Risk Score", f"{score:.1f}")
st.metric("Risk Level", level)

# Graph visualization
st.subheader("Dependency Graph")
graph_path = build_graph()
st.image(graph_path)

# Recommendations
st.subheader("Recommendations")

if level == "HIGH":
    st.error("⚠ Add integration tests before merging")
    st.warning("Review authentication and session flows carefully")

elif level == "MEDIUM":
    st.warning("Improve test coverage before merging")

else:
    st.success("Safe to merge with minor checks")
    st.subheader("Example Risk Reports")

scenario = st.selectbox(
    "Choose Scenario",
    ["low", "medium", "high"]
)

report = generate_risk_report(scenario)

st.metric("Risk Score", f"{report['risk_score']}/100")
st.metric("Risk Level", report["risk_level"])

st.write("### Analysis Summary")
st.write(report["summary"])

st.write("### Recommendation")
st.success(report["recommendation"])

st.write("### Details")

st.write(
    f"""
    - Files Changed: {report['files_changed']}
    - Services Impacted: {report['services_impacted']}
    """
)