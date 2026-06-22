# risk_dashboard.py

import matplotlib.pyplot as plt


def calculate_risk(depth, critical_services, files_changed, test_gap):
    """
    Calculate overall risk score and risk level.
    """

    score = (
        depth * 0.35 +
        critical_services * 0.30 +
        files_changed * 0.20 +
        test_gap * 0.15
    )

    if score > 70:
        level = "HIGH"
    elif score > 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return round(score, 2), level


# Demo scenarios for hackathon presentation

SCENARIOS = {
    "low": {
        "depth": 20,
        "critical_services": 15,
        "files_changed": 2,
        "test_gap": 10,
        "services_impacted": 1
    },

    "medium": {
        "depth": 55,
        "critical_services": 60,
        "files_changed": 8,
        "test_gap": 40,
        "services_impacted": 4
    },

    "high": {
        "depth": 90,
        "critical_services": 95,
        "files_changed": 15,
        "test_gap": 75,
        "services_impacted": 7
    }
}


def generate_dashboard(scenario_name):

    data = SCENARIOS[scenario_name]

    score, level = calculate_risk(
        data["depth"],
        data["critical_services"],
        data["files_changed"],
        data["test_gap"]
    )

    factors = [
        "Dependency Depth",
        "Critical Services",
        "Files Changed",
        "Test Coverage Gap"
    ]

    values = [
        data["depth"],
        data["critical_services"],
        data["files_changed"],
        data["test_gap"]
    ]

    plt.figure(figsize=(10, 6))

    bars = plt.bar(factors, values)

    plt.title(
        f"Duo Orbit Architect - {scenario_name.upper()} Risk Analysis"
    )

    plt.ylabel("Risk Contribution")

    plt.figtext(
        0.5,
        0.01,
        (
            f"Risk Score: {score}/100 | "
            f"Risk Level: {level} | "
            f"Files Changed: {data['files_changed']} | "
            f"Services Impacted: {data['services_impacted']}"
        ),
        ha="center",
        fontsize=10
    )

    plt.tight_layout()

    filename = f"{scenario_name}_risk_dashboard.png"

    plt.savefig(filename)

    plt.close()

    print("\n" + "=" * 60)
    print(f"Scenario: {scenario_name.upper()}")
    print("=" * 60)
    print(f"Files Changed      : {data['files_changed']}")
    print(f"Services Impacted  : {data['services_impacted']}")
    print(f"Risk Score         : {score}")
    print(f"Risk Level         : {level}")

    if scenario_name == "high":
        print("Authentication Module Modified")
        print("Recommendation: Extensive testing required.")

    elif scenario_name == "medium":
        print("Recommendation: Additional integration testing.")

    else:
        print("Recommendation: Safe to merge.")

    print(f"\nGenerated: {filename}")


if __name__ == "__main__":

    generate_dashboard("low")
    generate_dashboard("medium")
    generate_dashboard("high")