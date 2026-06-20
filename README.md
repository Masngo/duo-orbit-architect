🚀 Duo Orbit Architect: Blast-Radius AI Engine
An AI-powered GitLab Duo Agent that uses Knowledge Graph intelligence to analyze Merge Requests, identify architectural impact, assess regression risk, and recommend testing strategies before code reaches production.

📖 Overview
Modern software systems are highly interconnected. A seemingly small code change can affect multiple services, APIs, workflows, and downstream dependencies.
Duo Orbit Architect: Blast-Radius AI Engine helps developers understand the true impact of code changes before they are merged.
The solution analyzes Merge Requests (MRs), leverages GitLab Knowledge Graph relationships to identify affected components, evaluates testing coverage, calculates risk levels, and generates actionable recommendations to reduce regressions.
Instead of manually tracing dependencies across a codebase, developers receive an automated blast-radius assessment directly within their GitLab workflow.

🎯 Elevator Pitch
An autonomous GitLab Duo Agent that leverages Knowledge Graph intelligence to map dependencies, identify regression risks, and generate testing recommendations whenever a Merge Request is opened.

❓ The Problem
During code reviews, developers often struggle to answer critical questions:
What systems are affected by this change?
How far does the impact propagate?
Are existing tests sufficient?
Is this change safe to merge?
What downstream services could break?
Manual dependency analysis is time-consuming, difficult to scale, and prone to oversight.
As applications become increasingly distributed, understanding architectural impact before deployment becomes essential.

💡 The Solution
Duo Orbit Architect introduces architectural awareness into the Merge Request review process.
The agent:
Detects modified files
Identifies downstream dependencies
Maps impacted services and APIs
Evaluates testing coverage
Calculates blast-radius risk scores
Generates reviewer recommendations
Produces concise architectural summaries
This enables teams to make informed merge decisions and reduce production regressions.

⚙️ Key Features
Architectural Impact Analysis
Automatically determines which services, APIs, modules, and workflows are affected by a change.
Dependency Mapping
Uses Knowledge Graph relationships to identify downstream dependencies.
Blast-Radius Detection
Measures how widely a code change propagates through the system.
Risk Assessment
Calculates risk levels based on affected components and dependency breadth.
Test Coverage Evaluation
Identifies testing gaps within impacted systems.
Merge Request Summaries
Provides concise AI-generated impact reports.
Actionable Recommendations
Suggests testing strategies and review actions before approval.

🏗️ Architecture
Merge Request
      ↓
GitLab Duo Agent
      ↓
Knowledge Graph Analysis
      ↓
Dependency Mapping
      ↓
Blast-Radius Engine
      ↓
Risk Assessment
      ↓
Test Coverage Evaluation
      ↓
Recommendations & Report


🔄 Agent Workflow
Step 1 – Detect Changes
The agent identifies files modified within a Merge Request.
Step 2 – Knowledge Graph Query
Relationships between services, modules, APIs, and files are retrieved.
Step 3 – Dependency Analysis
Downstream dependencies are mapped.
Step 4 – Blast-Radius Calculation
The scope of impact is evaluated.
Step 5 – Risk Scoring
A risk score is generated based on:
Number of impacted components
Dependency depth
Service criticality
Testing coverage
Step 6 – Recommendations
The agent generates actionable next steps for reviewers.

🧪 Example Analysis
Sample MR #2 – High Risk Authentication Change
Merge Request
Title
feat: introduce JWT refresh token validation

Files Changed
src/auth.py
src/token_manager.py


Blast-Radius Assessment
Impacted Components
Changed File
Impacted Components
Risk
auth.py
Login API, Session Service
High
token_manager.py
Authentication Workflow
High


Downstream Services
Login API
Session Service
User Service
Authentication Workflow

Risk Score
Risk Level: HIGH
Risk Score: 75/100


Test Coverage Assessment
Component
Existing Tests
Missing Tests
Login API
Yes
No
Session Service
Partial
Yes
Token Refresh Flow
No
Yes


Recommendations
Add integration tests for token refresh workflows.
Validate expired token handling.
Review session creation and renewal logic.
Perform authentication regression testing.
Verify downstream service compatibility.

🧠 How GitLab Technology Is Used
This project was designed specifically around GitLab's AI and repository intelligence vision.
GitLab Duo Agent Platform
Provides the foundation for intelligent workflow automation.
GitLab Knowledge Graph
Enables dependency-aware impact analysis through relationship mapping.
GitLab Merge Requests
Serves as the primary review workflow where insights are delivered.
By combining repository intelligence with architectural awareness, Duo Orbit Architect transforms Merge Requests into intelligent architectural reviews.

🖥️ Prototype Dashboard
The project includes a Streamlit-based prototype dashboard that allows users to:
Submit Merge Request JSON
Analyze impacted services
Calculate blast radius
Generate risk scores
Visualize dependency graphs
Display recommendations

📥 Sample Merge Request Input
{
  "title": "feat: introduce JWT refresh token validation",
  "author": "developer1",
  "branch": "feature/jwt-refresh",
  "files": [
    "src/auth.py",
    "src/token_manager.py"
  ]
}


📊 Example Output
Merge Request Details
---------------------

Title:
feat: introduce JWT refresh token validation

Author:
developer1

Branch:
feature/jwt-refresh

Risk Level:
HIGH

Risk Score:
75/100

Impacted Components:
- Login API
- Session Service
- User Service
- Authentication Workflow

Recommendations:
- Add integration tests
- Validate expired token handling
- Review session workflows


🏆 Accomplishments
Built a GitLab Duo Agent focused on architectural impact analysis.
Created a structured blast-radius assessment workflow.
Developed risk-based Merge Request reporting.
Simulated Knowledge Graph-driven dependency mapping.
Designed realistic low-risk, high-risk, and critical-risk scenarios.
Demonstrated AI-assisted code review workflows.

📚 What We Learned
Through this project we gained deeper understanding of:
GitLab Duo Agents
Knowledge Graph-driven software intelligence
Dependency analysis methodologies
Risk assessment strategies
Architectural review workflows
Developer experience design

⚠️ Challenges We Faced
Avoiding Speculative Dependencies
Rather than inferring relationships, the design prioritizes Knowledge Graph-based dependency awareness.
Simplifying Complex Architecture
Presenting architectural impact in a concise and actionable format required balancing depth with usability.
Reviewer Experience
The output needed to be immediately understandable during code review.

🔮 Future Enhancements
Planned improvements include:
Interactive dependency visualization
Historical regression prediction
CI/CD impact analysis
Security impact assessment
Service ownership mapping
AI-generated integration tests
Multi-repository dependency analysis
Merge approval recommendations
GitLab API integration
Real-time webhook processing

🛠️ Technology Stack
GitLab Duo Agent Platform
GitLab Knowledge Graph
GitLab Merge Requests
Python
Streamlit
NetworkX
Matplotlib
Markdown

🚀 Running the Prototype
Install Dependencies
pip install streamlit networkx matplotlib

Launch Dashboard
streamlit run app.py


🎬 Demonstration Flow
Problem (20 Seconds)
Explain the challenge of understanding architectural impact during code reviews.
Architecture (40 Seconds)
Walk through the GitLab Duo Agent and Knowledge Graph workflow.
Live Demo (60 Seconds)
Show:
Low-Risk MR
High-Risk MR
Critical-Risk MR
Display risk scores, impacted services, and recommendations.
Future Vision (20 Seconds)
Present upcoming enhancements and roadmap.

🧭 Hackathon Information
Hackathon: GitLab Transcend Hackathon 2026
Track: Showcase Track

👤 Author
Masango Dewheretsoko

📄 License
This project was developed as a hackathon demonstration and educational prototype.

🌟 Final Summary
Duo Orbit Architect transforms Merge Requests into intelligent architectural reviews by combining GitLab Duo Agents with Knowledge Graph-driven dependency analysis.
By identifying blast radius, assessing risk, evaluating testing coverage, and generating actionable recommendations, the solution helps teams reduce regressions, improve review quality, and ship software with greater confidence.

