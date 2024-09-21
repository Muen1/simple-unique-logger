import os
import json

class UniqueInt:
    def __init__(self):
        self.unique_integers = set()

    def process_file(self, input_file_path, output_file_path):
        with open(input_file_path, 'r') as file:
            for line in file:
                self.read_next_item_from_file(line)
        
        sorted_unique_integers = sorted(self.unique_integers)
        with open(output_file_path, 'w') as file:
            for integer in sorted_unique_integers:
                file.write(f"{integer}\n")

    def read_next_item_from_file(self, line):
        try:
            line = line.strip()
            if line and line.replace('-', '').isdigit():
                self.unique_integers.add(int(line))
        except ValueError:
            pass

if __name__ == "__main__":
    input_dir = "/dsa/hw01/sample_inputs/"
    output_dir = "/dsa/hw01/sample_results/"
    for input_file in os.listdir(input_dir):
        if input_file.endswith(".txt"):
            input_file_path = os.path.join(input_dir, input_file)
            output_file_path = os.path.join(output_dir, f"{input_file}_results.txt")
            unique_int = UniqueInt()
            unique_int.process_file(input_file_path, output_file_path)

