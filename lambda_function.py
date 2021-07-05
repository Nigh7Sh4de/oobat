import json
import random

f = open("google-large.txt", "r")
lines = f.readlines()


def lambda_handler():
    i = random.randint(0,len(lines))

    return {
        'statusCode': 200,
        'body': json.dumps({'word': lines[i].strip()})
    }

if __name__ == "__main__":
    print(lambda_handler())