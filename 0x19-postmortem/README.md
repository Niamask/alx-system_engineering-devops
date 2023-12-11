# Postmortem: User Login Outage

![alt text](https://miro.medium.com/v2/resize:fit:1200/0*vPHtjDvBL8eUxP6B.jpg)

# Issue Summary
On Friday, December 8, 2023, from 10:45 AM to 11:30 AM, our user login system experienced an outage. During this period, approximately 85% of users were unable to log in to the platform. The outage caused significant disruption to user workflows and productivity.
# Timeline
- 10:45 AM: Monitoring alerts triggered, indicating a spike in failed login attempts.
- 10:50 AM: Engineering team on-call is notified and begins investigating the issue.
- 10:55 AM: Initial investigation focuses on the authentication service, assuming overloaded servers are causing the issue.
- 11:00 AM: Authentication service logs show normal server behavior, eliminating initial hypothesis.
- 11:10 AM: Investigation shifts to the user database, suspecting corruption or synchronization issues.
- 11:20 AM: Database logs reveal a recent update script encountered an error during execution, leaving the user table partially corrupted.
- 11:25 AM: A rollback script is deployed, restoring the database to a stable state.
- 11:30 AM: User login functionality is restored.
# Root cause and resolution
The root cause of the outage was a bug in a recently deployed update script that corrupted the user table in the database. The script was intended to add a new field to the table, but due to a programming error, it introduced data inconsistencies, preventing the user login process from completing successfully.

To resolve the issue, the engineering team rolled back the update script and successfully restored the database to its pre-update state. This restored the user table data and allowed the login functionality to work as expected.
# Corrective and preventative measures
- Improved Code Review: Implement a more rigorous code review process to identify and address potential bugs before deployment. This includes unit testing, code coverage analysis, and peer review.
- Automated Rollback Script: Develop automated rollback scripts for critical database updates. These scripts should be tested regularly to ensure their effectiveness in case of unexpected issues.
- Enhanced Monitoring and Alerting: Improve monitoring capabilities for database health and performance metrics. This will enable faster detection of anomalies and potential problems.
- Incident Response Training: Conduct regular training sessions for the engineering team on incident response procedures. This will improve their ability to quickly diagnose and resolve issues, minimizing downtime and user impact.
