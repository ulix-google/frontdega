#!/bin/bash
# Run this script to create a Remote Forwarding SSH tunnel originating at the 
# edge node (i.e. the Raspberry Pi at home) and connecting to the remote proxy 
# node (i.e. the GCP VM running the NGINX proxy). The script loads environment
# variables from the edge/.env file, so ensure that the appropriate values
# are set before running this script.

# Load the environment variables.
# -a: Each variable or function that is created or modified is given the export
# attribute and marked for export to the environment of subsequent commands.
set -a            
source .env
# Turn off -a setting.
set +a

# Create Remote Forwarding SSH tunnel with:
# -N: Do not execute a remote command.  This is useful for just forwarding 
# ports.
# -T: Disable pseudo-terminal allocation.
ssh -N -T -R $PROXY_PORT:$LOCAL_HOST:$LOCAL_PORT $PROXY_USER@$PROXY_HOST
