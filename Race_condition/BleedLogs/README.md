# 🚩 Lab 0x01: BleedLogs v1.0

> **Vulnerability Class:** Race Condition (TOCTOU)\
> **Target System:** LogVault™ Enterprise Audit Console\
> **Difficulty:** Easy

------------------------------------------------------------------------

## 🧬 Overview

BleedLogs v1.0 is a high-fidelity offensive security lab simulating
real-world flaws in concurrent web applications.

This lab demonstrates how improper handling of: - Shared memory -
Asynchronous execution - File system access

can lead to critical vulnerabilities such as: - Unauthorized Data
Access - Path Traversal - Race Condition Exploitation

------------------------------------------------------------------------

## 📖 Executive Summary

Modern backend systems often process multiple requests simultaneously
for performance. When validation logic is separated from execution
logic, timing flaws can be exploited.

BleedLogs shows how attackers can: - Abuse concurrency - Manipulate
shared state - Bypass validation mechanisms

------------------------------------------------------------------------

## 🛠️ Technical Specifications

-   **Framework:** Python Flask (WSGI-based)
-   **Server Mode:** Multi-threaded
-   **Vulnerability Type:** TOCTOU (Time-of-Check to Time-of-Use)
-   **Attack Vector:** Global shared state manipulation
-   **Objective:** Retrieve the hidden `flag.txt` outside the logs
    directory

------------------------------------------------------------------------

## 🔬 Root Cause Analysis

### Race Window Breakdown

1.  **Check Phase**
    -   The application validates a safe file (e.g., `system.log`)
2.  **Race Window**
    -   A global variable is updated during request handling
3.  **Use Phase**
    -   The application reads a modified path (e.g., `../../flag.txt`)
        without re-validation

------------------------------------------------------------------------

## 🎯 Attack Surface

  Component       Description
  --------------- ------------------------
  `/view?file=`   Entry point
  Global State    Shared across requests
  File System     Target of traversal

------------------------------------------------------------------------

## 🧪 Lab Objectives

-   Analyze application behavior
-   Identify race condition vulnerability
-   Intercept and modify HTTP requests
-   Execute concurrent requests
-   Retrieve `flag.txt`

------------------------------------------------------------------------

## 🧰 Suggested Tools

-   Burp Suite
-   OWASP ZAP
-   curl
-   Python scripts

------------------------------------------------------------------------

## 🚀 Deployment Instructions

### 1. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 2. Run the Lab

``` bash
python app.py
```

### 3. Access

http://127.0.0.1:5000/

------------------------------------------------------------------------

## 🧠 Exploitation Notes

-   Focus on timing and concurrency
-   Single request exploitation will fail
-   Race condition is the key

------------------------------------------------------------------------

## 🧬 Real-World Impact

-   Sensitive file disclosure
-   Privilege escalation
-   Data leakage

------------------------------------------------------------------------

## ⚖️ Ethics

For educational use only. Do not test against systems without
authorization.

------------------------------------------------------------------------

## 🧠 Author

**Besh0x79**\
**Module:** 0x01 - Race Condition

------------------------------------------------------------------------

## 🔥 Final Note

> The vulnerability is not in the code alone, but in the time between
> its operations.
