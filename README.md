# Camerge Service

[Camerge](https://github.com/LukasForst/camerge) as a service.

We're not exactly sure how this is going to be deployed, for that reason we have modules:

- [common](common) contains all business logic
- [backend](backend) FastAPI for deployment in Docker on VM
- [cloud_function](cloud_function) deployment using Google Cloud Function
- [frontend](frontend) SPA for management

Env setup:

1. `make venv` creates `venv`
2. `make install-deps` install dependencies
3. `source venv/bin/activate` activates python environment

Python 3.11 should be used.