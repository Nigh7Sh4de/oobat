import json
import random
f = open("result.json", "r")
data = json.load(f)

def lambda_handler():
    i = random.randint(0,len(data))
    result = data[i]
    print(result)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

if __name__ == "__main__":
    print(lambda_handler())