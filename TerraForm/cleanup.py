import os

print("cleaning up terraform initialization...")


try:
    os.system("rm -r .terraform")
    os.system("rm .terraform.lock.hcl")
    os.system("rm terraform.tfstate")
    os.system("rm terraform.tfstate.backup")
    print("Done!")

except Exception as e:
    print("ERROR: "  + e)