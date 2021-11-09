#!/bin/bash

# not needed for now

for i in {1..10}
do
	docker run --net="host" publisher
done
