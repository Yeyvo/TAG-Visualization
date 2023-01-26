## How to Use
### Install kafka (bitnami) in your k8s cluster
after you install helm use these commands:

`helm repo add bitnami https://charts.bitnami.com/bitnami`

`helm install my-release bitnami/kafka`
### Clone this repo
`git clone https://github.com/oubaydos/TAG-Visualization`
### Update cassandra url in deployment yaml files
Note: check this repo for a terraform script that creates a gcp VM with cassandra in port 9042
### apply the deployment files
`kubectl apply -f deployment`

and all is set
