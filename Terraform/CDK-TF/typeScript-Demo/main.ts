// *********************************************************

// CREATES EC-2 INSTANCE 

// DOCUMENTATIONS
// https://www.terraform.io/cdktf
// https://www.terraform.io/cdktf/concepts/providers

// *********************************************************






import { Construct } from "constructs";
import { App, TerraformOutput, TerraformStack } from "cdktf";


import { AwsProvider } from "./.gen/providers/aws/provider";
import { Instance } from "./.gen/providers/aws/instance";



const region = "us-east-1"





class MyStack extends TerraformStack {
  constructor(scope: Construct, name: string) {
    super(scope, name);


    // PROVIDER
    const cloudProvider = new AwsProvider(this, "aws", {
      region: region,
    });


    // RESOURCES
    const ec2 = new Instance(this, "Hello", {
      ami: "ami-2757f631",
      instanceType: "t2.micro",
    });


    // OUTPUT
    const output = new TerraformOutput(this, "id", { value: ec2.id })





  }
}

const app = new App();
new MyStack(app, "typeScript-Demo");
app.synth();
