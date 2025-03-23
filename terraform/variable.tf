# Terraform Variables File

variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
  default     = "2204702f-2344-4ad7-acc5-63b9daea47de"
}

variable "resource_group_name" {
  description = "Resource Group Name"
  type        = string
  default     = "myResourceGroupTR"
}

variable "location" {
  description = "Azure Region"
  type        = string
  default     = "East US"
}

variable "acr_name" {
  description = "Azure Container Registry Name"
  type        = string
  default     = "myacrTR202"
}

variable "app_service_name" {
  description = "App Service Name"
  type        = string
  default     = "my-fastapi-websocket-app"
}

variable "app_service_plan_name" {
  description = "App Service Plan Name"
  type        = string
  default     = "myAppServicePlan"
}

variable "app_insights_name" {
  description = "Application Insights Name"
  type        = string
  default     = "myAppInsights"
}
