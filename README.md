# Fraud Detection in Applications (Major Project)

This repository holds the updated framework for my Major Project as a Data Analyst Intern at Internee.pk.

### Project Objective:
The core target of this module is to analyze incoming user enrollment forms and automatically detect fraudulent behaviors, bot applications, or anomalous data entries.

Dashboard Overview
![Fraud Output Preview](Output%20(2).png)

### Extended Technical Architecture:
* **Python** (Backend Manipulation)
* **Pandas** (For text standardization using `.str.title()` and filtering logic)
* **Scikit-Learn (sklearn)** (Unsupervised Machine Learning Engine)
* **Isolation Forest Algorithm** (Contamination-based anomaly scoring)

### Analytical Insights:
* Programmed safety overrides to capture logical data errors (e.g., negative or impossible ages).
* Employed an unsupervised Isolation Forest model to isolate rapid clicks and spam bot registrations.
* Automatically generated clear visual anomaly classification alert tags.
