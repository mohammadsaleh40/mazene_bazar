import os
os.system("nohup python3 sar_khati/main1.py &> output1.txt 2>&1 &")
os.system("nohup python3 sar_khati/main2.py &> output2.txt 3>&4 &")