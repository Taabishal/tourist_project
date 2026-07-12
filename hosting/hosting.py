from huggingface_hub import HfApi
import os

# Retrieve the Hugging Face token from Colab secrets
token = userdata.get("HFA_TOKEN")

# Initialize API client with the token
api = HfApi(token=token)

api.upload_folder(
    folder_path="tourism_project/deployment",     # the local folder containing your files
    repo_id="happy-face1/Toursim_pkg_pediction",          # the target repo
    repo_type="space",                      # dataset, model, or space
    path_in_repo="",                          # optional: subfolder path inside the repo
)

print("Deployment files successfully uploaded to Hugging Face Space!")