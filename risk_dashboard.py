def calculate_risk(depth, critical_services, files_changed, test_gap):
    # Weighted scoring system
    score = (
        depth * 0.35 +
        critical_services * 0.30 +
        files_changed * 0.20 +
        test_gap * 0.15
    )

    # Risk classification
    if score > 70:
        level = "HIGH"
    elif score > 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level