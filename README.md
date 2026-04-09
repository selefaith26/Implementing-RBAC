# Implementing RBAC
## Access Control Mechanisms Assignment - Part 2
### Grand Canyon University
# Ortasele Aisuan
---

## Overview

This program implements a Role-Based Access Control (RBAC) system in Python.
It manages a list of users, assigns each user a specific role, and controls
access to a protected text file based on what each role is permitted to do.

RBAC is one of the most widely used access control models in organizations
because permissions are assigned to roles rather than individuals, making
access management simple and scalable. When a user's job changes, only
their role needs to be updated — not every individual permission
(Pfleeger, Pfleeger, & Coles-Kemp, 2024).

---

## Files Included

| File | Purpose |
|---|---|
| rbac.py | Main program — run this |
| company_data.py | Defines the protected file name and initial content |
| protected.txt | Created automatically when the program runs |
| README.md | This file |

---

## How to Run

**Step 1 — Make sure Python is installed**
```
python --version
```

**Step 2 — Put both files in the same folder**
- rbac.py
- company_data.py

**Step 3 — Run the program**
```
python rbac.py
```

No libraries to install. Standard library only.

---

## The Six Roles

| Role | Read | Write | Delete | Manage | Audit |
|---|---|---|---|---|---|
| admin | YES | YES | YES | YES | NO |
| manager | YES | YES | YES | NO | NO |
| editor | YES | YES | NO | NO | NO |
| viewer | YES | NO | NO | NO | NO |
| auditor | YES | NO | NO | NO | YES |
| guest | NO | NO | NO | NO | NO |

---

## Pre-Loaded Users

| Username | Role |
|---|---|
| alice | admin |
| bob | manager |
| carol | editor |
| dave | viewer |
| eve | auditor |
| frank | guest |

---

## Menu Options

When you run the program you will see an interactive menu:

```
  ROLE-BASED ACCESS CONTROL SYSTEM
  ----------
  1. Show all users and roles
  2. Add a new user
  3. Read file
  4. Write to file
  5. Delete file
  6. Exit
```

- Option 1 — displays all roles, permissions, and current users
- Option 2 — add a brand new user and assign them a role
- Option 3 — attempt to read the protected file as a specific user
- Option 4 — attempt to write to the protected file as a specific user
- Option 5 — attempt to delete the protected file as a specific user
- Option 6 — exit the program

The program will print GRANTED if the user has permission
or DENIED if they do not.

---

## Why the File is Created Automatically

The protected.txt file is created automatically by the program
the first time it runs rather than being created manually beforehand.
This is an intentional security design decision — if the file were
created separately, it would exist on the system with no access controls
around it. By having the program create it at runtime, the file and the
RBAC protection are in place from the exact same moment
Acm, & Nist. (1999).

---

## Academic References

Pfleeger, C., Lawrence Pfleeger, S., & Coles-Kemp, L. (2024). Security in computing (6th ed.). Pearson.

Acm, & Nist. (1999). Proceedings Fourth ACM Workshop on Role-Based Access Control. 160. 

Coronado, A. S. (2013). Computer Security: Principles and Practice, Second Edition. Journal of Information Privacy & Security, 9(2), 62–65. https://doi-org.lopes.idm.oclc.org/10.1080/15536548.2013.10845680

Bello, A. J., Diyan, M., & Asghar, I. (2025). Zero Trust Implementation for Legacy Systems using Dynamic Microsegmentation, Role-Based Access Control (RBAC), and Attribute-Based Access Control (ABAC). 2025 4th International Conference on Computing and Information Technology (ICCIT), Computing and Information Technology (ICCIT), 2025 4th International Conference On, 181–189. https://doi-org.lopes.idm.oclc.org/10.1109/ICCIT63348.2025.10989392


---

## Disclaimer

This project is for educational purposes only as part of a university
course assignment at Grand Canyon University.
