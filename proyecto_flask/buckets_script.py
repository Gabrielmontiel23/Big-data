import boto3

# Crear una sesión con boto3
s3 = boto3.client('s3')

# Listar los buckets
response = s3.list_buckets()

# Imprimir los nombres de los buckets
print("Buckets disponibles:")
for bucket in response['Buckets']:
    print(bucket['Name'])

