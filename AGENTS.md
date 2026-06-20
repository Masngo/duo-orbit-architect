# Duo Orbit Architect Agent

trigger: merge_request

analysis:
  - dependency_mapping
  - blast_radius_analysis
  - risk_scoring

output:
  - merge_request_comment
  - risk_report