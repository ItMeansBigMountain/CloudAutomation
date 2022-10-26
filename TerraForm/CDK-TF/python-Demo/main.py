# *********************************************************
# CREATES EC-2 INSTANCE 
# DOCUMENTATION : https://www.terraform.io/cdktf
# *********************************************************







#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # define resources here


app = App()
MyStack(app, "python-Demo")

app.synth()
