# risk_scenarios.py

def generate_risk_report(scenario):

    scenarios = {
        "low": {
            "files_changed": 2,
            "services_impacted": 1,
            "risk_score": 20,
            "risk_level": "LOW",
            "summary": "Minimal blast radius detected.",
            "recommendation": "Safe to merge after standard review."
        },

        "medium": {
            "files_changed": 8,
            "services_impacted": 4,
            "risk_score": 55,
            "risk_level": "MEDIUM",
            "summary": "Multiple services impacted.",
            "recommendation": "Additional integration testing recommended."
        },

        "high": {
            "files_changed": 15,
            "services_impacted": 7,
            "risk_score": 85,
            "risk_level": "HIGH",
            "summary": "Authentication module modified with significant downstream impact.",
            "recommendation": "Conduct extensive testing before approval."
        }
    }

    return scenarios.get(scenario.lower())


if __name__ == "__main__":

    for scenario in ["low", "medium", "high"]:

        report = generate_risk_report(scenario)

        print("\n" + "=" * 50)
        print(f"SCENARIO: {scenario.upper()}")
        print("=" * 50)

        for key, value in report.items():
            print(f"{key}: {value}")