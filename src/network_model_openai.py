from openai import OpenAI
import sys
import json
import csv
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python network_model.py <network_name> <model_name>")
        sys.exit(1)

    network_file = sys.argv[1]
    model_code = sys.argv[2]

    network_name = network_file.split("/")[1].split(".")[0]
    directory_path = f"outputs/{network_name}_{model_code}"

    # Check if the directory exists
    if not os.path.exists(directory_path):
        # Create the directory
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")

    # Open and read the network file
    with open(network_file, 'r') as file:
        network = json.load(file)
        
    # print(network['network'])
    
    # Open the task file
    with open('tasks/tasks.csv', mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')  
        tasks = [row for row in csv_reader]
    
    with open('labels.csv', mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=',') 
        network_labels = [row for row in csv_reader]
    
    network_label = next((item for item in network_labels if item["network"] == network['network']), None)

    prompt_template = ""
    with open('prompt_template', 'r') as file:
        prompt_template = file.read()
    
    client = OpenAI()

    for row in tasks:
        results = []
        for i in range(10):
            result = {'ID':row['ID'], 'topic':row['topic'], 'result':""}
            if row['ID'] == 'T11':
                task = row['task'].format(x1=network_label["x1_neg"], x2=network_label["x2_neg"])
            else:
                task = row['task'].format(x1=network_label["x1_pos"], x2=network_label["x2_pos"])
            prompt = prompt_template.format(network=network, task=task)
            
            if model_code == "o1-preview":
                response = client.chat.completions.create(
                        model=model_code, 
                        messages=[
                            {
                                "role":"user",
                                "content": prompt
                            }
                        ]
                    )
            else:    
                response = client.chat.completions.create(
                        model=model_code, 
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant to answer users' questions on a given networking structure."},                        
                            {
                                "role":"user",
                                "content": prompt
                            }
                        ],
                        temperature=1.2
                    )
            result["result"]=response.choices[0].message.content
            results.append(result)
        with open(f"outputs/{network_name}_{model_code}/{row['ID']}.txt", 'w') as file:
            for r in results:
                file.write(str(r))
                file.write('\n')