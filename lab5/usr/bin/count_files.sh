#!/bin/bash

DIR="/etc"
COUNT=$(find $DIR -type f | wc -l)

echo "Number of files in $DIR: $COUNT"
