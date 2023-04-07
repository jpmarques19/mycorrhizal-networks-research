import csv

with open('datasets/MycorrhizalFungusNetworks_doi_10_5061_dryad_7ts20_v1/01_SampleData.txt', 'r') as txt_file:
    with open('datasets/MycorrhizalFungusNetworks_doi_10_5061_dryad_7ts20_v1/01_SampleData.csv', 'w', newline='') as csv_file:
        # Create a CSV writer object
        csv_writer = csv.writer(csv_file)

        # Write the headers to the CSV file
        headers = txt_file.readline().strip().split('\t')
        csv_writer.writerow(headers)

        # Write the remaining lines to the CSV file
        for line in txt_file:
            csv_writer.writerow(line.strip().split('\t'))
