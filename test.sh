#!/bin/bash
echo "--------post sample json file to server-----\n"
curl -v http://localhost:8080 -F datafile=@./tests/input.json
echo "--------get output json file from server-----\n"
curl -v -i http://127.0.0.1:8080/
echo "\n--------you can type http://127.0.0.1:8080/ on your browser to see the json output-----"
