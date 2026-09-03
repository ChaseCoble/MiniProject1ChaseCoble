### INF601 - Advanced Programming in Python
### Chase Coble
### Mini Project 1
 
 
# Practice API Wrapper Class
 
Completion of a wrapper class for use with a given API.
 
## Description
 
My specific focus on this project will be learning TDD (Test-Driven Development) techniques along with learning how to effectively utilize Claude code. Tests are written by hand, code written by agent. 
 
## Getting Started
 
### Dependencies
 
* requests
 
### Installing
 
* Download src
 
### Executing program
 
* API Token must be exported to terminal environment
* (For Linux) ``` export "PRACTICE_API_TOKEN"=<YOUR API TOKEN> ```
* ```python3 client.py```
 
## Help

## Authors
Chase Coble 

## Version History
* 1.0
    * Full test suite passed and project completed.
* 0.11
    * Integration tests for error handling written by me
* 0.10
    * Integration tests for CRUD written by me, passed by claude
* 0.9
    * Claude writes to pass error handling unit tests
* 0.8
    * Error handling tests written by me
* 0.7
    * Delete Unit test written by me, passed by Claude
* 0.6
    * Claude wrote update to pass tests
* 0.5
    * Wrote the unit tests for update_post
* 0.4
    * Refactored unit tests to use pytest.fixture after identifying excessive duplicated code
* 0.3
    * Removed accidentally tracked .pyc and pycache files
* 0.2
    * Unit test written and passed for get_post
* 0.1
    * Initial Release
 
## License
 
This project is unlicensed

## Acknowledgments
 Full API Reference in the [API Documentation](https://practice.fhsucyber.com/docs)

##AI Usage

All tests are written by me, as well as exceptions.py. Claude modified client.py to pass the tests I wrote, while I also confirmed the test harness manually as well. 

