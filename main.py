import argparse
import subprocess
import sys

def run_script(script_name, query_text=None):
    if query_text:
        subprocess.run(['python', script_name, query_text])
    else:
        subprocess.run(['python', script_name])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run different parts of the project.')
    parser.add_argument('script', choices=['populate', 'query'], help='Script to run: populate or query')
    parser.add_argument('query_text', nargs='?', help='The query text for the query script')
    
    args = parser.parse_args()

    if args.script == 'populate':
        run_script('populate_database.py')
    elif args.script == 'query':
        if not args.query_text:
            print("Error: The query_text argument is required for the query script.")
            sys.exit(1)
        run_script('query_data.py', args.query_text)
