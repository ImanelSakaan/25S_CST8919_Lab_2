# 🔐 Azure Flask Login Monitoring Lab 

## 📘 Scenario
As a cloud security engineer, your task is to secure a basic Flask web application. The app must log login attempts, detect brute-force login behavior, and trigger an automatic alert if suspicious activity is found.

---
## 📎 Files Included in this Repo

- `app.py` — The Flask application that handles login attempts.
- `test-app.http` — HTTP request file for testing login attempts (compatible with VS Code REST Client).
- `requirements.txt` — List of Python dependencies needed to run the app.
- `README.md` — Documentation of the lab steps, KQL query, and demo instructions.

## ✅ Lab Tasks & Steps

### ⚙️ Part 1: Deploy the Flask App to Azure

1. **Create a Python Flask app**  
   - Implement a `/login` route.
   - Log successful and failed login attempts using `logging`.

2. **Deploy to Azure Web App**
   - Use Azure CLI to create a resource group, App Service Plan, and a Web App.
   - Deploy the app using ZIP deploy or GitHub Actions.

---

### 🧪 Part 2: Enable Monitoring

1. **Create a Log Analytics Workspace**  
   - In the Azure Portal → Search: *Log Analytics Workspaces* → Create → Choose same region as your Web App.

2. **Enable Diagnostic Logs**
   - Go to your Web App → **Monitoring > Diagnostic settings**
   - Create a new setting:
     - ✅ AppServiceConsoleLogs  
     - ✅ AppServiceHTTPLogs *(optional)*
     - ✅ Send to Log Analytics workspace (select the one you created)

3. **Test your app**
   - Create a file named `test-app.http` with login requests for success/failure.
   - Use the **REST Client** extension in VS Code to send requests and generate logs.

---

### 🔍 Part 3: Query Logs with KQL

1. **Open Log Analytics > Logs**
2. **Run this KQL query** to detect failed logins:

```kql
AppServiceConsoleLogs
| where TimeGenerated > ago(1h)
| where Message contains "Failed login attempt"
| project TimeGenerated, Message
| order by TimeGenerated desc
```
3. **Verify that failed login attempts are displayed.**

### 🚨 Part 4: Create an Alert Rule

1. Go to **Azure Monitor > Alerts > + Create > Alert Rule**

2. **Scope**  
   - Select the **Log Analytics Workspace** connected to your Web App.

3. **Condition**  
   - Use your **KQL query** from Part 3  
   - **Measure**: Table rows  
   - **Threshold**: Greater than 5  
   - **Aggregation granularity**: 5 minutes  
   - **Frequency of evaluation**: 1 minute

4. **Action Group**  
   - Create a **new action group**  
   - Add an **email notification** action

5. **Finalize the Alert**  
   - **Name** your alert (e.g., `BruteForceLoginAlert`)  
   - Set **Severity** to 2 or 3  
   - Click **Save**






























## Objective

In this lab, you will:
- Create a simple Demo Python Flask app
- Deploy a the app to Azure App Service
- Enable diagnostic logging with Azure Monitor
- Use Kusto Query Language (KQL) to analyze logs
- Create an alert rule to detect suspicious activity and send it to your email
---
## Scenario
As a cloud security engineer, you're tasked with securing a simple web application. The app logs login attempts. You must detect brute-force login behavior and configure an automatic alert when it occurs.

## Tasks

### Part 1: Deploy the Flask App to Azure
1. Develop a Python Flask app with a `/login` route that logs both successful and failed login attempts.
2. Deploy the app using **Azure Web App**.

### Part 2: Enable Monitoring
1. Create a **Log Analytics Workspace** in the same region.
2. In your Web App, go to **Monitoring > Diagnostic settings**:
   - Enable:
     - `AppServiceConsoleLogs`
     - `AppServiceHTTPLogs` (optional)
   - Send to the Log Analytics workspace.
3. Interact with the app to generate logs (e.g., failed `/login` attempts).


You must test your app using a .http file (compatible with VS Code + REST Client) and include that file in your GitHub repo as test-app.http.

### Part 3: Query Logs with KQL
1. Create a KQL query to find failed login attempts.
2. Test it

### Part 4: Create an Alert Rule
1. Go to Azure Monitor > Alerts > + Create > Alert Rule.
2. Scope: Select your Log Analytics Workspace.
3. Condition: Use the query you created in the last step.
4. Set:
    - Measure: Table rows
    - Threshold: Greater than 5
    - Aggregation granularity: 5 minutes
    - Frequency of evaluation: 1 minute
    - Add an Action Group to send an email notification.
    - Name the rule and set Severity (2 or 3).
    - Save the alert.

## Submission
### GitHub Repository
- Initialize a Git repository for your project.
- Make **frequent commits** with meaningful commit messages.
- Push your code to a **public GitHub repository**.
- Include  **YouTube demo link in the README.md**.

Include a `README.md` with:
  - Briefly describe what you learned during this lab, challenges you faced, and how you’d improve the detection logic in a real-world scenario.
  - Your KQL query with explanation

- **A link to a 5-minute YouTube video demo** showing:
  - App deployed
  - Log generation and inspection in Azure Monitor
  - KQL query usage
  - Alert configuration and triggering

You must test your app using a .http file (compatible with VS Code + REST Client) and include that file in your GitHub repo as test-app.http.


---

## Submission Instructions

Submit your **GitHub repository link** via Brightspace.

**Deadline**: Wednesday, 18 June 2025

---

