from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connection_string = "safariGermain"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "my-container"
container_client = blob_service_client.get_container_client(container_name)

blob_name = "my-blob.txt"

blob_client = container_client.get_blob_client(blob_client)

data = b"hello, azure blob storage"

blob_client.upload_blob(data)

print("blobs in the container")

blob_list = container_client.list_blobs()

for blob in blob_list:
    print("\t", blob.name)

downloaded_blob = blob_client.download_blob()
blob_contents = downloaded_blob.readall()

print("download blob contents", blob_contents.decode("utf-8"))