import oci
import time
import json
import requests

# replace with the location of your oci config file
CONFIG_FILENAME = "~/.oci/config"
config = oci.config.from_file(CONFIG_FILENAME, profile_name="TEST")

auth = oci.signer.Signer(
  tenancy=config['tenancy'],
  user=config['user'],
  fingerprint=config['fingerprint'],
  private_key_file_location=config['key_file'],
  pass_phrase=config['pass_phrase'])

# Initialize some constants
CLOUD_ENV_URL = "https://aiservicepreprod.us-ashburn-1.oci.oraclecloud.com"
COMPARTMENT_ID = "YOUR_COMPARYMENY_ID"

headers = { 'Content-Type': 'application/json', 'User-Agent': 'any-user' }

### **STEP 1:** Creating a Project


PROJECT_URL = f"{CLOUD_ENV_URL}/20210101/projects"

payload = { "displayName": "Sample Project",
                 "compartmentId": COMPARTMENT_ID,
                 "description" : "SAMPLE PROJECT FOR ANOMALY DETECTION" }

session = requests.Session()
create_project_res = session.request("POST", PROJECT_URL, headers=headers, data=json.dumps(payload),
                                             allow_redirects=True, auth=auth)
create_project_json = json.loads(create_project_res.text)
print(create_project_res.text)
project_id = create_project_json["id"]

# This loop waits for project to be created (upto 10 mins)
timeout = time.time() + 60 * 10
while True:
    view_project_res = session.request("GET", f"{PROJECT_URL}/{project_id}", headers=headers,
                                       allow_redirects=True, auth=auth)
    view_project_json = json.loads(view_project_res.text)
    if time.time() > timeout:
        print("TIMEOUT")
        break
    elif view_project_json["lifecycleState"] == "ACTIVE":
        print("SUCCESS")
        break
    elif view_project_json["lifecycleState"] == "CREATING":
        print("Still creating...")
    elif view_project_json["lifecycleState"] == "FAILED":
        print("FAILED...")
        break
    time.sleep(10)


### **STEP 2:** Creating the DataAsset


DATA_ASSET_URL = f"{CLOUD_ENV_URL}/20210101/dataAssets"
BUCKET_NAME = "Your bucket name of the object"
NAME_SPACE = "Your namespace of the object"
OBJECT_FILE_NAME = "Your object file name in Oracle OCI Object Storage"

dataasset_payload = {
  "displayName": "Sample dataAsset",
  "compartmentId": COMPARTMENT_ID,
  "projectId": project_id,
  "description": "oracle object storage data asset",
  "dataSourceDetails": {
    "dataSourceType": "ORACLE_OBJECT_STORAGE",
    "bucketName": BUCKET_NAME,
    "namespace": NAME_SPACE,
    "objectName": OBJECT_FILE_NAME
  }
}

session = requests.Session()
create_dataasset_res = session.request("POST", DATA_ASSET_URL, headers=headers, data=json.dumps(dataasset_payload),
                                             allow_redirects=True, auth=auth)
create_dataasset_json = json.loads(create_dataasset_res.text)
print(create_dataasset_res.text)
dataasset_id = create_dataasset_json["id"]

# This loop waits for dataasset to be created (upto 10 mins)
timeout = time.time() + 60 * 10
while True:
    view_dataasset_res = session.request("GET", f"{DATA_ASSET_URL}/{dataasset_id}", headers=headers,
                                       allow_redirects=True, auth=auth)
    view_dataasset_json = json.loads(view_dataasset_res.text)
    if time.time() > timeout:
        print("TIMEOUT")
        break
    elif view_dataasset_json["lifecycleState"] == "ACTIVE":
        print("SUCCESS")
        break
    elif view_dataasset_json["lifecycleState"] == "CREATING":
        print("Still creating...")
    elif view_dataasset_json["lifecycleState"] == "FAILED":
        print("FAILED...")
        break
    time.sleep(10)


### **STEP 3:** Creating the Train Model

TRAIN_URL = f"{CLOUD_ENV_URL}/20210101/models"

param_fap = 0.01 # Model parameter: False Acceptance Percentage, have to be in range [0.01, 0.05]
param_trainingFac = 0.7 # Model parameter: Training Fraction, a percentage to split data into training and test, value range [0.7, 0.9]

train_payload = {
  "compartmentId": COMPARTMENT_ID,
  "displayName": "Test model",
  "description": "Creating a model test",
  "projectId": project_id,
  "modelCreationDetails": {
    "modelType": "ANOMALY_MULTIVARIATE",
    "fap": param_fap,
    "trainingFraction": param_trainingFac,
    "dataAssets": [ dataasset_id ]
  }
}

session = requests.Session()
create_train_res = session.request("POST", TRAIN_URL, headers=headers, data=json.dumps(train_payload),
                                             allow_redirects=True, auth=auth)
create_train_json = json.loads(create_train_res.text)
print(create_train_res.text)
model_id = create_train_json["id"]

# This loop waits for train to be created (upto 15 mins) depending on your training data size u might want to wait longer
timeout = time.time() + 60 * 15
while True:
    view_train_res = session.request("GET", f"{TRAIN_URL}/{model_id}", headers=headers,
                                       allow_redirects=True, auth=auth)
    view_train_json = json.loads(view_train_res.text)
    if time.time() > timeout:
        print("TIMEOUT")
        break
    elif view_train_json["lifecycleState"] == "ACTIVE":
        print("SUCCESS")
        break
    elif view_train_json["lifecycleState"] == "CREATING":
        print("Still creating...")
    elif view_train_json["lifecycleState"] == "FAILED":
        print("FAILED")
        break
    time.sleep(10)


### **STEP 4:** Deploying the Model

DEPLOY_URL = f"{CLOUD_ENV_URL}/20210101/modelDeployments"
deploy_payload = {
  "compartmentId": COMPARTMENT_ID,
  "displayName": "Anomaly Multivariate Model Shared Deployment",
  "description": "E2E Testing MSET Model Shared Deployment",
  "modelId": model_id,
  "config": { "sku": "SHARED", "coreCount": "1" }
}

session = requests.Session()
create_deploy_res = session.request("POST", DEPLOY_URL, headers=headers, data=json.dumps(deploy_payload),
                                             allow_redirects=True, auth=auth)
create_deploy_json = json.loads(create_deploy_res.text)
print(create_deploy_res.text)
deploy_id = create_deploy_json["id"]

# This loop waits for deploy to be created (upto 15 mins)
timeout = time.time() + 60 * 15
while True:
    view_deploy_res = session.request("GET", f"{DEPLOY_URL}/{deploy_id}", headers=headers,
                                       allow_redirects=True, auth=auth)
    view_deploy_json = json.loads(view_deploy_res.text)
    if time.time() > timeout:
        print("TIMEOUT")
        break
    elif view_deploy_json["lifecycleState"] == "ACTIVE":
        print("SUCCESS")
        break
    elif view_deploy_json["lifecycleState"] == "CREATING":
        print("Still creating...")
    elif view_deploy_json["lifecycleState"] == "FAILED":
        print("FAILED")
        break
    time.sleep(10)


### **STEP 5:** Detection with the Model

DETECT_URL = f"{CLOUD_ENV_URL}/20210101/modelDeployments/{deploy_id}/actions/detectAnomalies"

data_payload = {
  "requestType": "INLINE",
  "columnLabels": [ "sensor1", "sensor2", "sensor3", "sensor4", "sensor5", "sensor6", "sensor7", "sensor8", "sensor9", "sensor10" ],
  "data": [
    {
      "timestamp": "2020-10-01T09:22:59.000Z",
      "value": [ 0.8885, 0.975, 1.25, 0.01, 0, 0.8885, 0.975, 1.25, 0.01, -21654546980 ]
    }
  ]
}

session = requests.Session()
detect_res = session.request("POST", DETECT_URL, headers=headers, data=json.dumps(data_payload), allow_redirects=True, auth=auth)
print(detect_res.json())
print(detect_res.headers)
