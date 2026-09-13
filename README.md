#  Fraud Detection & Financial Risk Analytics

A rule-based data analytics project built using Python and **Pandas** to programmatically detect high-risk and anomalous financial transactions.

##  Automated Fraud Logic Applied
1. **High-Value Thresholding:** Filtered transactions where `Amount > 100,000` to catch sudden capital risk signals.
2. **Behavioral Deduplication:** Tracked repeated transaction profiles with identical user and amount parameters using `.duplicated()`.
3. **Automated Auditing:** Isolated anomalous entries and generated a programmatic operations file (`fraud_alert_report.csv`).

##  Tech Stack
* Python 3
* Pandas Library
* Python IDLE
