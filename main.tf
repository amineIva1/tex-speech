# main.tf

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "example" {
  name     = "example-resource-group"
  location = "West US"
}

resource "azurerm_container_registry" "example" {
  name                     = "example-acr"
  resource_group_name      = azurerm_resource_group.example.name
  location                 = azurerm_resource_group.example.location
  sku                      = "Basic"
  admin_enabled            = true
}

resource "azurerm_container_group" "example" {
  name                = "example-container-group"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name

  container {
    name   = "example-container"
    image  = "${azurerm_container_registry.example.login_server}/<image-name>:<tag>"
    cpu    = "1.0"
    memory = "1.5"

    ports {
      port     = 80
      protocol = "TCP"
    }
  }

  os_type = "Linux"

  dns_name_label = "<aci-dns-name-label>"
}
