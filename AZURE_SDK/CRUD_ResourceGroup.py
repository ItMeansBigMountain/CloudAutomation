# REQUIREMENTS
    # Make sure you have AZ CLI installed
        # 'az login'
        # 'az account show'

    # pip install azure-mgmt-resource
    # pip install azure-identity





from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient



# AUTHORIZATION
credential = AzureCliCredential()
subscription_id =  "e928ce0b-aa60-4e05-a8c2-a9eb05266c69"


# INIT RESOURCE MANAGER CLIENT
resourceManagement_client = ResourceManagementClient(credential, subscription_id)









# CREATE/UPDATE PARAMS 
resource_name = "automation-testing" 
resource_params = {
    "managedBy" : None ,  #The ID of the resource that manages this resource group.
    "location" : "centralus" ,
    "tags" : {} ,
}









# # CREATE resource group
# resourceManagement_client.resource_groups.create_or_update(
#     resource_name  ,
#     resource_params
# )





# READ resource group
# found = False
# for resource in resourceManagement_client.resource_groups.list():
#     if resource.name == resource_name:
#         found = True
# if found:
#     print("RG '" + resource_name + "' found!")
# else:
#     print("RG \'" + resource_name + "\' NOT found!")





# UPDATE resource group
# resourceManagement_client.resource_groups.create_or_update(
#     resource_name  ,
#     resource_params
# )





# DELETE resource group
# deletion_operation = resourceManagement_client.resource_groups.begin_delete(resource_name)
# print("deleting \'" + resource_name + "\' ...")
# deletion_operation.wait()
# print("done!")