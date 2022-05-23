import json

with open('./data/ntas.geojson') as f:
    data = json.load(f)

ntas = data['features']

docs = []
for nta in ntas:
    props = nta['properties']
    doc = {
        u'geometry': nta['geometry'],
        u'neighborhood': props['ntaname'],
        u'ntacode': props['ntacode'],
        u'boro': props['boro_name']
    }
    docs.append(doc)

