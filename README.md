# Tutorial - A simple SingularityNET service written in Python

_This example was adapted from: https://github.com/singnet/wiki/tree/master/tutorials/howToWritePythonService

-------------------------------

_Before following this tutorial, make sure you've installed_

* _Docker (https://www.docker.com/)_
* _Metamask (https://metamask.io)_

_You will need a private-public key pair to register your service in SNET. Generate them in Metamask before you start this tutorial._

-------------------------------

Run this tutorial from a bash terminal.

We'll use Python gRPC, for more details see https://grpc.io/docs/

In this tutorial we'll create a Python service and publish it in SingularityNET.

## Step 1 

Setup a `ubuntu:18.04` docker container using provided `Dockerfile`.

```
$ docker build --build-arg language=python -t snet_python_service https://github.com/blueskyinterfaces/snet-textecho.git#master:/Docker
$ docker run -p 7000:7000 -ti snet_python_service bash
```

From this point we follow the tutorial in the Docker container's prompt.

# cd /opt/singnet/tutorial

## Step 2

```
# ./buildProto.sh
```

## Step 3

To test our server locally (without using the blockchain)

```
# python3 server.py &
# python3 client.py "hello world"
```

You should have something like the following output:

```
# python3 server.py &
[1] 4217
# Server listening on 0.0.0.0:8105
python3 client.py "hello world"
You said hello world
```

At this point you have successfully built a gRPC Python service. The executables can 
be used from anywhere inside the container (they don't need anything from 
the installation directory) or outside the container if you have Python gRPC libraries installed.

The next steps in this tutorial will publish the service in SingularityNET.

## Step 4

Now you must follow the [howToPublishService](../howToPublishService/README.md)
tutorial to publish this service or use our script (next step).

You'll also need a `SNET CLI` identity (check step 3 from [howToPublishService](../howToPublishService/README.md#step-3)).

## Step 5

First, make sure you killed the `server` process started in Step 3.

Then
publish and start your service:

```
# ./publishAndStartService.sh PAYMENT_ADDRESS
```

Replace `PAYMENT_ADDRESS` by your public key (wallet).

Example:

```
# ./publishAndStartService.sh 0xA6E06cF37110930D2906e6Ae70bA6224eDED917B
```

This will start the `SNET Daemon` and your service. If everything goes well you will 
see the blockchain transaction logs and then the following messages 
(respectively from: your service and `SNET Daemon`):

```
[blockchain log]
Server listening on 0.0.0.0:7070
[daemon initial log]
INFO[0002] Blockchain is enabled: instantiate payment validation interceptor 
INFO[0002]                                               PaymentChannelStorageClient="&{ConnectionTimeout:5s RequestTimeout:3s Endpoints:[http://127.0.0.1:2379]}"
INFO[0002] Default payment handler registered            defaultPaymentType=escrow
DEBU[0002] starting daemon                              
```

You can double check if it has been properly published using

```
# snet organization list-services snet
```

Optionally you can un-publish the service

```
# snet service delete snet math-operations
```

Actually, since this is just a tutorial, you are expected to un-publish your
service as soon as you finish the tests.

Other `snet` commands and options (as well as their documentation) can be found 
[here](https://github.com/singnet/snet-cli).

## Step 6

You can test your service making requests in command line:

The `testServiceRequest.sh` script is set to use channel id `0`, if your
`SNET CLI` identity already had opened previous channels, you'll have to
set channel id manually at.

```
# ./testServiceRequest.sh hello world
[blockchain log]
    response:
        v: You said hello world
```
