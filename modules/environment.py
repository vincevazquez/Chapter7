import os 

def run(**args):
    
    print "[*] In environment module."
    files = os.listdir(".")
    
    return str(os.environ)
