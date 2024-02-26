# Park Microservice

A microservice that provides information about American National Parks.

## About

This program uses a ZeroMQ message queue to communicate with a separate program that makes requests for information about American National Parks. The program uses the National Park Service API to retrieve information about the parks and returns it to the requesting program.

### Architecture

```UML Diagram
 ________________________       ____________________       _________________      _______
|Program making a request|     |ZeroMQ Message Queue|     |Park microservice|    |NPS API|
 ------------------------       --------------------       -----------------      -------
         |                              |                      |                      |
         |---send request-------------->|                      |                      |
         |                              |---forward request--->|                      |
         |                              |                      |---API request------->|
         |                              |                      |<--API response-------|
         |                              |<--forward response---|                      |
         |<--receive response-----------|                      |                      |
         |                              |                      |                      |

```

### The NPS API

## How to use the program

**Setup**

1. Setup ZeroMQ
   - Install ZeroMQ
   - Install the ZeroMQ library for python
2. Clone the repository
3. Install packages.
   - zmq
   - requests
4. Read the documentation for the NPS API and get an API key

**Features**
Random park: the program retrieves a list of all parks from the nps API and selects a random park from the list.
Get park by id: the program retrieves a park from the NPS API by its id.
