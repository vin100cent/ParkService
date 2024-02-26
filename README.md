# Park Microservice

A microservice that provides information about American National Parks.

## About

This program uses a ZeroMQ message queue to communicate with a separate program that makes requests for information about American National Parks. The program uses the National Park Service API to retrieve information about the parks and returns it to the requesting program.

**Features**
Random park: the program retrieves a list of all parks from the nps API and selects a random park from the list.
Get park by id: the program retrieves a park from the NPS API by its id.


![UML Sequence Diagram](https://github.com/vin100cent/ParkService/blob/main/SequenceDiagram.png)


## Setup

**Example Directory**
```bash
/park_service_microservice
|-- /venv
|-- /src
|   |-- ParkService.py
|   |-- ZmqSocket.py
|   |-- NpsApiHandler.py
|   |-- TestClient.py
|-- /tests
|   |-- test_park_service.py
|-- requirements.txt
|-- .env
|-- .gitignore
|-- README.md
```

1. Clone Repository

2. Get an API Key from the [NPS get started site](https://www.nps.gov/subjects/developer/get-started.htm)

3. Setup Environment 

Install and read documentation [ZeroMQ](https://zeromq.org/languages/python/)

Other packages needed are "requests" and "python-dotenv", I'd recommend placing necessary packages inside a requirements.txt and installing with

```zsh
pip3 install -r requirements.txt
```

place api key in .env 
```zsh
NPS_API_KEY=YOUR_KEY_GOES_HERE
```

Run the server ParkService.py then the Client file (TestClient.py is provided or use your own)


## How to Request and Receive data 




