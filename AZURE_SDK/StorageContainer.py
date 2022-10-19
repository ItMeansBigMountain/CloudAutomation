# REQUIREMENTS
    # Make sure you have AZ CLI installed
        # 'az login'
        # 'az account show'

    # pip install azure-storage-blob
    # pip install azure-mgmt-storage
    # pip install azure-identity


# DOCUMENTATION
    # https://portal.azure.com/#@affanfareedgmail.onmicrosoft.com/dashboard/private/97e74045-7a5d-4678-b2d0-edd065b4068e



import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob Storage v" + __version__ + " - Python quickstart sample")

    # Quick start code goes here

except Exception as ex:
    print('Exception:')
    print(ex)