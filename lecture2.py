import csv

cities_per_state = {}
states_per_city = {}
population_buckets = {}

def read_csv_file():
  with open("cities.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
      state_id = row["state_id"]
      city = row["city"]

      if state_id not in cities_per_state:
        cities_per_state[state_id] = []

      cities_per_state[state_id].append(city)

      if city not in states_per_city:
        states_per_city[city] = []

      states_per_city[city].append(state_id)

      population = int(float(row["population"]))
      population_formatted = f"{population:,}"
      city_info = f"{city} {state_id} ({population_formatted})"

      if population <= 10:
        population_buckets[10].append(city_info)
      elif population <= 100:
        population_buckets[100].append(city_info)
      elif population <= 1000:
        population_buckets[1000].append(city_info)
      elif population <= 10000:
        population_buckets[10000].append(city_info)
      elif population <= 100000:
        population_buckets[100000].append(city_info)
      elif population <= 1000000:
        population_buckets[1000000].append(city_info)
      elif population <= 10000000:
        population_buckets[10000000].append(city_info)
      elif population <= 100000000:
        population_buckets[100000000].append(city_info)
      else:
        raise Exception("Too Big Pop")

def main():
  population_buckets[10] = []
  population_buckets[100] = []
  population_buckets[1000] = []
  population_buckets[10000] = []
  population_buckets[100000] = []
  population_buckets[1000000] = []
  population_buckets[10000000] = []
  population_buckets[100000000] = []
  read_csv_file()

  while True:
    # state_id = input("Enter 2 Letter State: ").upper()

    # print(cities_per_state[state_id])

    # city = input("City: ")
    # print(states_per_city[city])

    pop = int(input("Enter pop cap: "))
    print(population_buckets[pop])

if __name__ == "__main__":
  main()