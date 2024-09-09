import csv
from functools import reduce

def mapper(namafile):
    mapped_values = []
    with open(namafile, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            nilai = float(row["Nilai"])
            mapped_values.append((nilai, 1))
    return mapped_values

def reducer_sum(values):
    total_sum = reduce(lambda x, y: x + y[0], values, 0)
    total_count = reduce(lambda x, y: x + y[1], values, 0)
    return total_sum, total_count

def reducer_rata2(sum_count_pair):
    total_sum, total_count = sum_count_pair
    rata2 = total_sum / total_count
    return rata2

def main():
    mapped_values = mapper('C:/Users/afifa/OneDrive/Documents/nilaimahasiswa/nilai.csv')

    sum_count_pair = reducer_sum(mapped_values)
    print(f"Total nilai dari {sum_count_pair[1]} mahasiswa : {sum_count_pair[0]}")

    rata2 = reducer_rata2(sum_count_pair)
    print(f"Rata-rata nilai dari {sum_count_pair[1]} mahasiswa: {rata2}")

if __name__ == "__main__":
    main()