terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.27.0"
    }
  }
}


# NOTE: CREATE provider.tf AND DROP THIS IN THERE TO SAFE KEEP SENSITIVE DATA
#provider "azurerm" {
#  features {}
#  subscription_id   = "xxxx"
#  tenant_id         = "xxxx"
#  client_id         = "xxxx"
#  client_secret     = "xxxx"
#}
provider "azurerm" {
  features {}
}

module "name" {
  source = "./modules/deploy-keyvault"
}

module "name" {
  source = "./modules/deploy-kubernetesCluster"
}

module "name" {
  source = "./modules/deploy-resourceGroup"
}

module "name" {
  source = "./modules/deploy-storageContainer"
}

module "name" {
  source = "./modules/deploy-virtualMachines"
}