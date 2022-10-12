# RESOURCE TAG FROM main.tf
output "resource_group_name" {
  value = azurerm_resource_group.example_rg.name
}
output "resource_group_name" {
  value = azurerm_resource_group.example_rg2.name
}

