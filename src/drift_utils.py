from scipy.stats import ks_2samp

def ks_drift_test(reference, current, alpha=0.05):
    """
    Perform KS test to detect data drift.

    Parameters:
        reference (array-like): baseline data
        current (array-like): new data
        alpha (float): significance level

    Returns:
        dict: KS statistic, p-value, drift flag
    """
    ks_stat, p_value = ks_2samp(reference, current)
    drift_detected = p_value < alpha

    return {
        "ks_statistic": ks_stat,
        "p_value": p_value,
        "drift_detected": drift_detected
    }
