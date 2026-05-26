| **![](data:image/jpeg;base64...)** | |
| --- | --- |
| **Title**: AWS and Aptible Security Incident Management Policy | **Policy #**: |
| **Effective Date**: | **Last Revised**: |

1. **Scope**

This Policy applies to all AWS accounts, AWS-hosted systems, AWS services, AWS-related data environments, Aptible accounts, Aptible-hosted systems, Aptible-related data environments owned, operated, managed, or used by Millie, Inc. (“Company”), and all Company personnel. For purposes of this Policy, the term “personnel” includes all licensed professionals and staff who perform services on behalf of Company.

This Policy applies in addition to Company’s Security Incident Management Policy, Breach Notification Policy, Contingency Planning Policy, Safeguards Policy, Encryption Policy, Password Management Policy, Remote Access Policy, and Risk Management Policy.

1. **Policy**
2. It is Company’s policy to ensure the prompt reporting of and response to security incidents involving AWS and/or Aptible systems in order to prevent the occurrence of similar incidents in the future and safeguard Company’s PHI.
3. This Policy governs the reporting, investigation and management of actual and suspected AWS and/or Aptible security incidents that may compromise the security, confidentiality, integrity, or availability of PHI or Company systems.
4. AWS and/or Aptible security incidents may include, but are not limited to:
   1. Unauthorized access to an AWS account, IAM user, IAM role, access key, Aptible account;
   2. Loss, theft, or disclosure of an AWS or Aptible password, credential, access key, secret,
   3. token, or other access control mechanism;
   4. Unauthorized creation, modification, deletion, or public exposure of AWS resources;
   5. Unauthorized access to or disclosure of PHI stored or processed in AWS-hosted or Aptible-hosted systems;
   6. Public exposure of S3 buckets, databases, backups, logs, or other storage resources;
   7. Unusual AWS activity, including suspicious CloudTrail, CloudWatch, GuardDuty, or other monitoring alerts;
   8. Unauthorized changes to security groups, network access controls, encryption settings, or logging settings;
   9. Suspected malware, ransomware, denial of service, or other compromise affecting AWS-hosted systems; or
   10. Any AWS or Aptible event that could compromise the integrity, confidentiality, or availability of PHI or Company systems.
5. **Procedure**
6. Incident Reporting.
   1. All personnel shall promptly report to the Chief Security Officer, any observed or suspected AWS or Aptible security incident, security weakness, violation of Company security policies, or event that could compromise the integrity, confidentiality, or availability of PHI.
   2. If the AWS or Aptible security incident could be considered a Breach of HIPAA, the Chief Security Officer shall immediately notify the Chief Security Officer.
   3. Any personnel member who is uncertain as to whether a particular AWS or Aptible event is reportable should contact his or her supervisor or Chief Security Officer.
   4. Personnel shall not attempt to resolve a suspected AWS or Aptible security incident without authorization from the Chief Security Officer.
7. Initial Investigation.
   1. Upon learning of a suspected AWS or Aptible security incident, the Chief Security Officer shall conduct a preliminary investigation within 24 hours of the reported incident to determine whether a bona fide security event has occurred.
   2. The preliminary investigation may include review of available AWS and application records, including:

* CloudTrail logs;
* CloudWatch logs;
* GuardDuty findings;
* IAM users, roles, policies, and credential reports;
* S3 bucket policies, access logs, and public access settings;
* Security group and network access settings;
* Database access logs via Aptible;
* Backup and snapshot records via Aptible; and
* Application audit logs.
  1. If a security incident is verified, the Chief Security Officer shall promptly determine the nature and scope of the incident and shall promptly report the matter to the CEO and others as appropriate and required.

1. Response Priorities.

Regardless of the nature and scope of the incident, Company’s response shall be based upon the following order of priorities, as applicable:

* Protection of human life and safety;
* Protection of PHI against unauthorized disclosure, destruction, or modification;
* Prevention or mitigation of damage to Company’s systems and assets;
* Containment of unauthorized access or activity within AWS and Aptible systems;
* Preservation of security logs and records necessary for investigation;
* Notification of any third parties that may be adversely affected by the event, provided that such notification shall not be made unless and until approved by General Counsel;
* Minimizing disruption of Company’s computing resources and processes; and
* Reporting the incident to applicable law enforcement agencies and insurance carriers, provided that such notification shall not be made unless and until approved by the Chief Legal Officer.

1. Containment.

As appropriate, the Chief Security Officer shall take reasonable steps to contain the AWS security incident. Such steps may include:

* Disabling or restricting compromised AWS or Aptible users, roles, access keys, tokens, or credentials;
* Rotating passwords, access keys, secrets, database credentials, or encryption keys;
* Requiring additional authentication or MFA reset for affected accounts;
* Removing unauthorized IAM policies, permissions, or resources;
* Restricting public or unauthorized access to S3 buckets, databases, backups, logs, or other storage resources;
* Enabling or restoring AWS logging and monitoring where disabled;
* Isolating affected compute resources, containers, databases, or networks;
* Restricting security group, firewall, or network access;
* Taking snapshots or backups necessary to preserve evidence; and
* Coordinating with third-party vendors, including hosting, infrastructure, monitoring, or security vendors, as necessary.

1. Investigation and Breach Review.
   1. The Chief Security Officer shall investigate the AWS security incident to determine:

* The date and time of the incident and discovery;
* The AWS and/or Aptible accounts, systems, services, and data affected;
* Whether PHI was accessed, acquired, used, disclosed, altered, or destroyed;
* The type and amount of PHI involved, if any;
* The person or system responsible for the incident, if known;
* Whether credentials, secrets, or access controls were compromised;
* Whether logging or monitoring was disabled or altered;
* Whether third parties or Business Associates were involved; and
* What steps have been taken or should be taken to mitigate risk.
  1. If PHI may have been involved, the Chief Security Officer shall determine whether a Breach occurred and whether notification is required under Company’s Breach Notification Policy.

1. Remediation and Recovery.
   1. Following containment and investigation, Company shall take reasonable steps to remediate the incident and restore affected systems. Such steps may include:

* Rebuilding affected systems from trusted sources;
* Restoring data or systems from validated backups;
* Patching or reconfiguring affected resources;
* Removing unauthorized resources, software, code, or access;
* Updating IAM policies, security groups, S3 policies, logging settings, or monitoring rules;
* Reviewing and updating vendor access;
* Re-training personnel, where appropriate; and
* Implementing additional administrative, physical, or technical safeguards.
  1. The Chief Security Officer shall coordinate recovery efforts with Company personnel and third-party service providers as needed. Recovery activities shall be conducted in a manner designed to preserve PHI, restore business operations, and reduce the risk of recurrence.

1. Log.
   1. The Chief Security Officer shall be responsible for maintaining a written record of all reported AWS security incidents and the details and events relating to the response process, including, as applicable:

* The type of incident;
* The date of the incident;
* The date the incident was reported to Chief Security Officer;
* If applicable, the date the incident was reported to Company by its Business Associate;
* The manner in which the incident was identified;
* The AWS accounts, services, systems, and data involved;
* Copies of relevant security audit logs and records;
* All internal and external discussions, unless privileged;
* All actions taken to contain, investigate, remediate, and recover from the incident;
* Any actions taken to mitigate harm;
* Any third-party, vendor, law enforcement, insurance, or regulatory notifications; and
* Any corrective actions implemented to reduce the likelihood of a similar incident.

1. Post-Incident Review.
   1. Following resolution of an AWS security incident, the Chief Security Officer shall review the incident and determine whether additional safeguards, procedures, training, monitoring, or risk management activities are appropriate.
   2. Material findings shall be incorporated into Company’s risk management process and, where appropriate, reported to leadership.
2. Confidentiality.

Personnel shall not discuss any events pertaining to a specific AWS security incident with other individuals, including other personnel, except as permitted under this Policy or as directed by the Chief Security Officer, Chief Privacy Officer, Chief Compliance Officer, General Counsel, or Chief Executive Officer.

1. **References**

* 45 C.F.R. §§ 164.308(a)(5), 164.308(a)(6), 164.308(a)(7), 164.312, and 164.400-164.414
* Company Security Incident Management Policy
* Company Breach Notification Policy
* Company Contingency Planning Policy
* Company Safeguards Policy
* Company Encryption Policy
* Company Password Management Policy
* Company Remote Access Policy
* Company Risk Management Policy
