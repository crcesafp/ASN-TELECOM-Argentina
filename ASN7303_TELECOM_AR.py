import requests

ASNS = [
    "AS7303"
]

prefixes = set()

for asn in ASNS:

    url = f"https://stat.ripe.net/data/announced-prefixes/data.json?resource={asn}"

    r = requests.get(url)

    data = r.json()

    for prefix in data['data']['prefixes']:
        prefixes.add(prefix['prefix'])

with open("ASN7303-Ar.txt", "w") as f:
    for p in sorted(prefixes):
        f.write(p + "\n")

print("Done.")
