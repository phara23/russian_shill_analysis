import csv
import subprocess

def run_command(command):
    p = subprocess.Popen(command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return iter(p.stdout.readline, b'')


f = open('streamlined_tweets.csv')
csv_f = csv.reader(f)

ii = 1
for row in csv_f:
    if ii > 4:
        print(row[2])
        subprocess.call("aws comprehend detect-entities     --region us-west-2     --language-code \"en\"     --text \"" + str(row[2])+ "\" >> outputs/entities" + str(ii) +  ".json", shell=True)
        subprocess.call("aws comprehend detect-key-phrases     --region us-west-2     --language-code \"en\"     --text \"" + str(row[2])+ "\" >> outputs/key-phrases" + str(ii) + ".json", shell=True)
        subprocess.call("aws comprehend detect-sentiment     --region us-west-2     --language-code \"en\"     --text \"" + str(row[2])+ "\" >> outputs/sentiment" + str(ii) + ".json", shell=True)
    ii = ii + 1
