# main.tf

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resource-group"
  location = "West US"
}

resource "azurerm_container_group" "example" {
  name                = "example-container-group"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  container {
    name   = "example-container"
    image  = "nginx:latest"
    cpu    = "1.0"
    memory = "1.5"

    ports {
      port     = 80
      protocol = "TCP"
    }
  }
}
