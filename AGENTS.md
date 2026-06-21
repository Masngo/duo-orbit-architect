name: Duo Orbit Architect Agent

trigger:
  event: merge_request

inputs:
  - repository_diff
  - changed_files
  - commit_metadata

analysis_pipeline:
  dependency_mapping:
    description: "Build dependency graph from changed files and imports"

  blast_radius_analysis:
    description: "Identify services impacted by the change"

  risk_scoring:
    description: "Compute risk score based on dependency depth, critical services, and test gaps"

rules:
  - if dependency_depth > 5:
      flag: high_risk
  - if touches_auth_module:
      increase_risk: 20
  - if test_coverage_missing:
      increase_risk: 15

outputs:
  merge_request_comment:
    format: markdown
    includes:
      - risk_score
      - risk_level
      - impacted_services
      - recommendations

  risk_report:
    format: json
    fields:
      - score
      - level
      - dependencies
      - blast_radius
      - suggested_actions