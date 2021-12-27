#!/bin/bash


for i in {1..3}
do
	docker run --net="host" subscriber i
done
