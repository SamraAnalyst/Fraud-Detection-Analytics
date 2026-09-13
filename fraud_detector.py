Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

======= RESTART: C:/Users/AL RAHMAN LAPTOP/Desktop/Fraud_Project/Fraud.py ======
--- Data Successfully Loaded ---
  TransactionID  UserID  Amount    CardCountry    Status
0        TXN101  USR_01     250       Pakistan  Approved
1        TXN102  USR_02   15000            USA  Approved
2        TXN103  USR_03  999999  International   Pending
3        TXN104  USR_01     250       Pakistan  Approved
4        TXN105  USR_04     450             UK  Approved

🚨 [ALERT] High-Risk Transactions Found:
  TransactionID  UserID  Amount    CardCountry   Status
2        TXN103  USR_03  999999  International  Pending
5        TXN106  USR_03  999999  International  Pending

🚨 [ALERT] Suspicious Duplicate Transactions Found:
  TransactionID  UserID  Amount    CardCountry    Status
0        TXN101  USR_01     250       Pakistan  Approved
2        TXN103  USR_03  999999  International   Pending
3        TXN104  USR_01     250       Pakistan  Approved
5        TXN106  USR_03  999999  International   Pending

🎉 Success: Fraud report generated as 'fraud_alert_report.csv'!
>>> 
= RESTART: C:/Users/AL RAHMAN LAPTOP/Desktop/Fraud_Project/Fraud.py
--- Data Successfully Loaded ---
  TransactionID  UserID  Amount    CardCountry    Status
0        TXN101  USR_01     250       Pakistan  Approved
1        TXN102  USR_02   15000            USA  Approved
2        TXN103  USR_03  999999  International   Pending
3        TXN104  USR_01     250       Pakistan  Approved
4        TXN105  USR_04     450             UK  Approved

 [ALERT] High-Risk Transactions Found:
  TransactionID  UserID  Amount    CardCountry   Status
2        TXN103  USR_03  999999  International  Pending
5        TXN106  USR_03  999999  International  Pending

 [ALERT] Suspicious Duplicate Transactions Found:
  TransactionID  UserID  Amount    CardCountry    Status
0        TXN101  USR_01     250       Pakistan  Approved
2        TXN103  USR_03  999999  International   Pending
3        TXN104  USR_01     250       Pakistan  Approved
5        TXN106  USR_03  999999  International   Pending

 Success: Fraud report generated as 'fraud_alert_report.csv'!
