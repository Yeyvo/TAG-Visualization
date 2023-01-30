## How to Use
### Install kafka (bitnami) in your k8s cluster
after you install helm use these commands:

`helm repo add bitnami https://charts.bitnami.com/bitnami`

`helm install my-release bitnami/kafka`
### Clone this repo
`git clone the repo`
or

### Update cassandra url in deployment yaml files
Note: check this repo [Terraform Repo](https://github.com/oubaydos/terraform/tree/cassandra) for a terraform script that creates a gcp VM with cassandra in port 9042
### apply the deployment files
`kubectl apply -f deployment`

and all is set

## alternative 
`helm repo add bitnami https://charts.bitnami.com/bitnami`

`helm install my-release bitnami/kafka`

`
kubectl apply -f https://raw.githubusercontent.com/Yeyvo/TAG-Visualization/main/deployment/app-deployment.yaml; kubectl apply -f https://raw.githubusercontent.com/Yeyvo/TAG-Visualization/main/deployment/app-service.yaml; kubectl apply -f https://raw.githubusercontent.com/Yeyvo/TAG-Visualization/main/deployment/consumer-deployment.yaml; kubectl apply -f https://raw.githubusercontent.com/Yeyvo/TAG-Visualization/main/deployment/producer-deployment.yaml;
`

## How to build to convert the compose file 
`kompose convert -f docker-compose.yaml -o deployment/ --with-kompose-annotation=false --build local --push-image=True -v`
