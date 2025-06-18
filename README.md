# 🔐 Azure Flask Login Monitoring Lab 
## 📸 Demo Video

🎥 Watch the 10-minute demo here:  
**[▶️ YouTube Video Link]([https://youtu.be/HuYFQiQ1yaM)**

---
### 🔍 Function of Azure Flask Login Monitoring
   It combines Flask (web app) + Azure (hosting/platform) + Monitoring (security/usage insights):

#### ✅ 1. User Authentication Monitoring
You can track:
- Who is logging in (user IDs/emails)
- When they logged in (timestamp)
- From where (IP address, location)
How often they fail to log in (brute force detection)

#### 🛡️ 2. Security Auditing
Logging and alerting on:
 -Repeated failed logins
- Suspicious login patterns (e.g. multiple countries in short time)
- Admin login attempts
This helps in identifying security threats or account breaches.

#### 📈 3. Application Performance & Usage Monitoring
Using Azure tools (like Application Insights or Log Analytics), you can monitor:

- API calls to login endpoints
 -Time taken for login/auth flows
- Any errors during the login process (e.g., HTTP 401)

#### 🧰 4. How You Can verify It
-	A Flask web app deployed on Azure that logs login attempts
-	How Azure Monitor captures and analyzes security events
-	Real-time brute force detection using KQL queries
-	Automated alerting when suspicious activity occurs

---
## 📎 Files Included in this Repo

- `app.py` — The Flask application that handles login attempts.
- `test-app.http` — HTTP request file for testing login attempts (compatible with VS Code REST Client).
- `requirements.txt` — List of Python dependencies needed to run the app.
- `README.md` — Documentation of the lab steps, KQL query, and demo instructions.

## ✅ Lab Tasks & Steps

### ⚙️ Part 1: Deploy the Flask App to Azure

1. **Develop a Flask App with /login Route**  
   - Clone the GitHub Repository
           git clone https://github.com/ramymohamed10/25S_CST8919_Lab_2

   - Install Flask
     d:\25S_CST8919_Lab_2\25S_CST8919_Lab_2\.venv\Scripts\python.exe -m pip install flask
     
   - Create Project Files
     1. app.py – Your main Flask application.
     2. requirements.txt – Contains dependencies (e.g., flask).
     3. test-app.http – A file for testing login via HTTP requests using VS Code REST Client.
     
2. **Deployment Using Azure CLI**
        Follow these steps in the **VS Code terminal** to deploy your Flask app to Azure:
       1. **Login to Azure**
           ```bash
            az login
            ````
      
      2. **Create a Resource Group**
           ```bash
            az group create --name flask-lab-rg --location canadacentral
            ```
      3. **Create an App Service Plan**
           ```bash
         az appservice plan create --name flaskPlan --resource-group flask-lab-rg --sku FREE
         ```
      
      4. **Create the Web App**
          ```bash
         az webapp create --resource-group flask-lab-rg --plan flaskPlan --name <YOUR_WEBAPP_NAME> --runtime "PYTHON|3.10" --deployment-local-git
         ```

### 2. Set Deployment Remote and Push
    After creating the Web App, Azure will give you a Git deployment URL. Use the following commands to set the remote and push your code:
      ```bash
      git remote add azure <GIT_URL_FROM_PREVIOUS_COMMAND>
      git push azure master
      ````
![image](https://github.com/user-attachments/assets/e9a52003-9408-4391-af18-4ad9e8ef3305)

<img width="614" alt="image" src="https://github.com/user-attachments/assets/594f1ecb-784d-4512-9f07-6f650313cfb4" />


```bash
git push azure master
````
This means:

* Take the code in your local `master` branch and send it to the Azure remote repository.
* Azure receives your Flask app’s code.
* It runs a deployment process.
* Your app becomes live at:
  `https://<your-app-name>.azurewebsites.net`

---

### 🧪 Part 2: Enable Monitoring

1. **Create a Log Analytics Workspace**  
   - In the Azure Portal → Search: *Log Analytics Workspaces* → Create → Choose same region as your Web App.
     Run this command in the terminal to create a Log Analytics Workspace:

   ```bash
   az monitor log-analytics workspace create --resource-group flask-lab-rg --workspace-name flaskLogs --location canadacentral
![image](https://github.com/user-attachments/assets/53cf0431-257e-41b6-99eb-117d14140e75)

2. **Enable Diagnostic Logs**
   - Go to your Web App → **Monitoring > Diagnostic settings**
   - Create a new setting:
     - ✅ AppServiceConsoleLogs  
     - ✅ AppServiceHTTPLogs *(optional)*
     - ✅ Send to Log Analytics workspace (select the one you created)
           
         1. Go to **Azure Portal > Your Web App > Monitoring > Diagnostic settings**  
         2. Click **+ Add diagnostic setting** and configure as follows:
            - ✅ Enable **AppServiceConsoleLogs**  
            - ✅ (Optional) Enable **AppServiceHTTPLogs**  
            - 📤 **Send to Log Analytics Workspace**  
            - Select your workspace: **`flaskLogs`**

  This setup ensures:
      All your login attempts (and print/debug info) from Flask will appear in Log Analytics.
      You'll be able to query them using KQL in the next steps.
      
![image](https://github.com/user-attachments/assets/9d31acc2-9da9-4e50-aab3-8e37bfbc3d09)




3. **Test your app**
   - Create a file named `test-app.http` with login requests for success/failure.
   - Use the **REST Client** extension in VS Code to send requests and generate logs.
![image](https://github.com/user-attachments/assets/b2b07ad9-8d4e-4356-b2fe-fcfd3acc535a)

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
![image](https://github.com/user-attachments/assets/64ca0a9a-6ef2-4af2-aa53-1f30ba15a68a)

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


<img width="1250" alt="Screenshot 2025-06-18 alert2" src="https://github.com/user-attachments/assets/83e46d83-bd9f-49d5-9133-650ad55aa31f" />




![image](https://github.com/user-attachments/assets/815f41dc-d1a2-4e02-8502-ff868529a40a)
























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

