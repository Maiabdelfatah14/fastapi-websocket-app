
# CI/CD Pipeline for WebSocket Service




## Project Details:
 
 This project automates the deployment of a FastAPI WebSocket service using a complete CI/CD pipeline. The pipeline builds, secures, and deploys the application on Azure using GitHub Actions, Terraform, and Docker. 




## Tools Used

- FastAPI : Framework for building the WebSocket service.

-  Docker : Containerization of the WebSocket service .

- Azure Services 

   1- Azure App Service: Hosts the WebSocket container.

  2- Azure Container Registry (ACR): Stores the Docker images.

  3- Azure Monitor: Tracks application performance.

  4-  Azure Key Vault: Manages secrets securely.
    
  5- Azure Private Link & NSGs: Ensures secure WebSocket communication.

- Terraform : Infrastructure as Code (IaC) to provision Azure resources.

-  GitHub Actions : Automates CI/CD pipeline for deployment.

- Trivy : Security scanning for container vulnerabilities , checks for CRITICAL and HIGH severity issues.
### note 
✅ exit 0 → The pipeline continues, even if vulnerabilities are found.

⚠️ exit 1 → The pipeline would fail if vulnerabilities exist (not used in this setup)
## Getting Started 🚀

- Download The Code

```bash
 git clone https://github.com/Maiabdelfatah14/webSocket-.git
```
- Set Up Azure CLI Authentication
```bash
  az login
  ```
- If using a Service Principal, run:
```bash
az login --service-principal -u "<AZURE_CLIENT_ID>" -p "<AZURE_CLIENT_SECRET>" --tenant "<AZURE_TENANT_ID>"
 ```

 ### Build the Infrastructure
 - Set Up Terraform
 ```bash
 terraform --version
```
- Ensure Terraform is installed, then initialize and apply the infrastructure:
```bash
terraform init
```
```bash
terraform apply -auto-approve -var "subscription_id=${{ secrets.AZURE_SUBSCRIPTION_ID }}"
```
- output 

![1.png](https://github.com/Maiabdelfatah14/fastapi-websocket-app/blob/main/ScreenShots/1.png?raw=true)

### Now you can check your Azure account, and you will see the following resources created:

- Resource Group named "myResourceGroupTR".
- Virtual Network named "my-vnet".
- Subnet for Private Link.
- Network Security Group (NSG) for WebSocket traffic.
- Security Rules:   
   => Allow WebSocket traffic and Deny all inbound traffic.
- Azure Container Registry (ACR) named "myacrTR202".
- App Service Plan for hosting the Web App.
- Linux Web App named "my-fastapi-websocket-app".
- Private Endpoint for securing the Web App.
- Application Insights for monitoring.
- Auto-scaling Configuration for the App Service.
- Monitor Alerts:     
   => WebSocket failure alerts ,Latency alerts and Downtime alerts.


![2.png](https://github.com/Maiabdelfatah14/fastapi-websocket-app/blob/main/ScreenShots/2-.png?raw=true)


### then , can access app from browser

🌍 Application URL:
```bash
https://my-fastapi-websocket-app.azurewebsites.net/
 ```
📌 WebSocket Endpoint:
```bash
wss://my-fastapi-websocket-app.azurewebsites.net/ws
 ```



## Contributors:
 
➡️ [ maiabdelfata14](https://github.com/Maiabdelfatah14)


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
