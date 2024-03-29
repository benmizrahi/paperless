# Paperless
Made With Love ❤️ from  :israel: :israel:      

[Paperless](https://github.com/Plarium-Repo/paperless.git) is a tool that extends the capabilities of [Papermill](https://papermill.readthedocs.io/) by providing the ability to run Papermill via [Google Cloud Dataproc Serverless](https://cloud.google.com/dataproc-serverless/docs).   

[![ICON](https://skillicons.dev/icons?i=gcp,py&perline=3)](https://skillicons.dev) 

## Overview

Papermill is a powerful tool for parameterizing and executing Jupyter Notebooks. However, by default papermill dosn't support [Jupyter Kernel Gateway](https://jupyter-kernel-gateway.readthedocs.io/en/latest/) - it was impossible to run spark notebook vs Google Cloud Dataproc Serverless environment with Papermill tool - this is where Paperless helps.

Paperless bridges the gap between Papermill and Google Cloud Dataproc Serverless interactive mode, allowing you to seamlessly integrate the two and harness the power of serverless execution for your Jupyter Notebooks.

## Features

- **Serverless Execution:** Run Papermill on Google Cloud Dataproc without managing the underlying infrastructure.

- **Scalability:** Leverage the scalability of Google Cloud Dataproc for processing multiple Notebooks concurrently.

- **Cost-Effective:** Pay only for the resources you consume during the execution, optimizing costs for your notebook parameterization tasks.

Pricing model is much more cost-effective considering other platofrms and technologies 

![https://cloud.google.com/dataproc-serverless/pricing](./images/pricing_model.png)
*resource*: https://cloud.google.com/dataproc-serverless/pricing

## Getting Started

### Prerequisites

Before using Paperless, make sure you have the following:

- A Google Cloud Platform (GCP) project
- Access to Google Cloud Dataproc  [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=dataproc)
- Papermill installed locally or in your environment


### Step 1: Install Google Cloud SDK

To authenticate your application using Application Default Credentials (ADC) with `gcloud` -
If you haven't already installed the Google Cloud SDK, you can download and install it from the [Google Cloud SDK documentation](https://cloud.google.com/sdk/docs/install).

### Step 2: Authenticate with `gcloud`

Open a terminal and run the following command to authenticate your Google Cloud SDK with your Google Cloud Platform (GCP) account:

```bash
gcloud auth login

gcloud auth application-default login 
```

### Step 3: Install Paperless 

```bash
pip install paperless
```

### Step 4: Create sessionTemplates For Paperless

Parameters and details can be found in [GCP Docs](https://cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

```bash
 gcloud compute instance-templates create paperless-interactive --<extra params...>
``` 

You can change parameters as you need based on the jobs needs - check the docs for that.


### Step 5: Test Executtion:

Paperless excepts && supports all list or arguments exists in original [Papermill](https://papermill.readthedocs.io/) package -
the minimum needed for testing:

```bash
 paperless <input_path> <output_path> ...
``` 
An extra parameter that is special for Paperless: --template_name
Example:

```bash
 paperless ./resources/spark.ipynb ./resources/spark-out.ipynb --template_name paperless-interactive

```

You're all set, enjoy :)

----

### Local development:

```bash

# Create a new directory for your project
git clone https://github.com/Plarium-Repo/paperless.git && cd paperless

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate

# On macOS and Linux
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install the command line
python setup.py install 

# Execute example
paperless ./resources/spark.ipynb ./resources/spark-out.ipynb

```

---
[MIT License](LICENSE)

[Contribution](CONTRIBUTION)

[Code Of Conduct](CODE_OF_CONDUCT)
