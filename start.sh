#!/bin/bash

# Directory containing files
DIRECTORY="networks"
ORIGINAL_NETWORKS="intradomain_wl.json intradomain.json routers_wl.json routers.json webserver_wl.json webserver.json"
EXTEND_NETWORKS="datacenter_wl.json datacenter.json fattree_wl.json fattree.json"

# Array of elements
OLLAMA_MODELS="llama2:7b llama2:13b mistral:7b-instruct-v0.2-q8_0 gemma2:27b llama3.1:8b"
GPT_MODELS="gpt-4o-mini"

# Python script to call
OLLAMA_SCRIPT="src/network_model_ollama.py"
OPENAI_SCRIPT="src/network_model_openai.py"

# Outer loop: Iterate over files in the directory
for file in $EXTEND_NETWORKS; do
    relative_file="${DIRECTORY}/${file}"
    
    echo "Processing file: $relative_file"
    # Inner loop: Iterate over array elements
    for element in $OLLAMA_MODELS; do
        echo "  Passing element: $element"
        
        # Pass arguments to the Python script
        # "network name", "model code"
        python3 "$OLLAMA_SCRIPT" "$relative_file" "$element"
    done
done

# Outer loop: Iterate over files in the directory
for file in $EXTEND_NETWORKS; do
    relative_file="${DIRECTORY}/${file}"
    
    echo "Processing file: $relative_file"
    
    # Inner loop: Iterate over array elements
    for element in $GPT_MODELS; do
        echo "  Passing element: $element"
        
        # Pass arguments to the Python script
        # "network name", "model code"
        python3 "$OPENAI_SCRIPT" "$relative_file" "$element"
    done
done