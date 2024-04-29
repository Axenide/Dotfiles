#!/bin/bash

if systemctl status ollama | grep -q "running"; then
  echo "True"
else
  echo "False"
fi
