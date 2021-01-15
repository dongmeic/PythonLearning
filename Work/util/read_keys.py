import json

def read_api_key(path):
	with open(path, 'r') as f:
		keys = json.load(f)
	return keys['google_maps']['APIKEY']
