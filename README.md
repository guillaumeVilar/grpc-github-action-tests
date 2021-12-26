# grpc-github-action-tests

Test for both grpc and github action.  

The test setup consists of 2 docker containers based on python docker image.  
One of the container is acting as the gRPC server, the other one as client. 

## How to launch the containers? 
```
make start
```

## How to trigger the gRPC client action? 
```
make client
```

## Generate the python code from the protocol buffer definition 
```
pip3 install grpcio-tools
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. helloworld.proto
```