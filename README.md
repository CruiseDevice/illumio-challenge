# Illumio challenge

### How to run the program:
1. git clone `https://github.com/CruiseDevice/illumio-challenge.git`
2. cd `illumio-challenge`
3. Run the script from the command line:
    ```sh
    python flow_log_analyzer.py log.txt lookup.csv output.csv
    ```
### This program does the following:
1. Reads the lookup table from a CSV file into dictionary.
2. Parses the flow log file line by line.
3. For each line, it extracts the destination port and protocol
4. It looks up the tag for the port/protocol combination in the lookup dictionary.
5. It counts the occurrences of each tag and each port/protocol combination.
6. Finally, it writes the results to the output CSV file.

### Assumptions:
1. The program only supports default log format and version 2 of flow logs.
2. The flow log file is in the format described in the AWS documentation.
3. The protocol field in the flow log is numeric (6 for TCP, 17 for UDP, 1 for ICMP)
4. The lookup table CSV file has headers 'dstport', 'protocol', and 'tag'

### Tests performed
1. Tested with the sample flow logs and lookup table provided in the description
2. Tested with emply flow log file and empty lookup table.
3. Tested with flow log entries that don't match any lookup table entry.
4. Tested with large file (upto 10MB) to ensure performance.

### Analysis
1. The program uses Python's built-in CSV module for reading and writing CSV files, which is efficient and reliable
2. It uses a dictionaty for the lookup table, providing O(1) lookup time.
3. The program processes the flow log file line by line, which allows it to handle large files without loading everything into memory at once.
