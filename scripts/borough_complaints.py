import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',required=True,'the input csv file')
    parser.add_argument('-s',required=True,'start date')
    parser.add_argument('-e',required=True,'end date')
    parser.add_argument('-o','output file')

    

