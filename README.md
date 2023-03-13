### URL Shortener implementation built using the Serverless Framework and AWS technologies. The project leverages the following AWS services:

* API Gateway
* Lambda
* DynamoDB


### Installation and Deployment

Install Python 3.x (3.8 was used during implementation) and pip if they're not already installed. You can download the latest version of Python from the official website: https://www.python.org/downloads/.

Install the required Python packages using pip:

`pip install -r requirements.txt
`

This command installs all the Python packages required by your project. Make sure to include a requirements.txt file in your project that lists all the required packages and their versions.

Install Node.js and npm if they're not already installed. You can download the latest version of Node.js from the official website: https://nodejs.org/.

Install the Serverless Framework using npm:

`npm install -g serverless
`

This command installs the latest version of the Serverless Framework globally on your system.

Configure your AWS credentials for Serverless Framework:


`serverless config credentials --provider aws --key <your_aws_access_key> --secret <your_aws_secret_key>
`

Replace <your_aws_access_key> and <your_aws_secret_key> with your actual AWS access key and secret key. This command stores your AWS credentials in the Serverless Framework configuration file, so you don't have to enter them every time you deploy your project.

Usage
Navigate to the root directory of your Serverless project in the terminal.

Deploy your project to AWS using the Serverless Framework:

`serverless deploy
`

This command deploys your project to AWS Lambda and sets up any required AWS resources, such as API Gateway or S3 buckets. Once the deployment is complete, the Serverless Framework outputs the URL of your Lambda function and any other relevant information.

Contributing
If you would like to contribute to this project, please follow these guidelines:

Fork the repository and clone it to your local machine.
Create a new branch for your feature or bug fix.
Write tests for your changes and make sure they pass.
Submit a pull request with a clear description of your changes and why they are necessary.