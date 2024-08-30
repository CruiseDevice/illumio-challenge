import csv
import sys
from collections import defaultdict


def read_lookup_table(fpath):
    lookup_dict = {}
    with open(fpath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (int(row['dstport']), row['protocol'].lower())
            lookup_dict[key] = row['tag ']
            
    return lookup_dict


def read_log_file(log_file, lookup_dict, output_file):
    protocols_dict = {
        6: 'tcp',
        17: 'udp',
        1: 'icmp',        
    }
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)
    
    with open(log_file, 'r') as f:
        for line in f:
            fields = line.split()
            dstport = int(fields[6])
            protocol = protocols_dict.get(int(fields[7]))
            key = (dstport, protocol)
            tag = lookup_dict.get(key, 'Untagged')
            tag_counts[tag] += 1
            port_protocol_counts[key] += 1

    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Tag', 'Count'])
        for tag, count in tag_counts.items():
            writer.writerow([tag, count])
            
        writer.writerow([])
        writer.writerow([])
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in port_protocol_counts.items():
            writer.writerow([port, protocol, count])

def main():
    if len(sys.argv) != 4:
        print("Usage: python script.py <log_file> <lookup_file> <output_file>")
        sys.exit(1)
        
    
    log_file = sys.argv[1]
    lookup_file = sys.argv[2]
    output_file = sys.argv[3]

    lookup_dict = read_lookup_table(lookup_file)
    read_log_file(log_file, lookup_dict, output_file)
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    main()