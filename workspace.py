from azure.ai.ml import MLClientS

from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()

ml_client = MLClient(
    credential = credential,
    
)