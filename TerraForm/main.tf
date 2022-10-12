# 1. Specify the version of the AzureRM Provider to use
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.0.1"
    }
  }
}



# Configure Azure RESOURCE MANAGEMENT provider
provider "azurerm" {
  features {}
}



# DEPLOY A RESOURCE GROUP
resource "azurerm_resource_group" "rg" {
    name = "terraform-demo"
    location = "centralus"
}
