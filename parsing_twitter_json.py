import json 





def main():
	with open("streamtest1.txt", 'r') as json_file:
		data = str(json_file.read())
		print(data)
		print("****************************AFTER STRIPPING***************************")
		stripped_data = data.split('_json=', 1)[1]
		print(stripped_data)

		json_obj = json.loads(stripped_data)
		print(json_obj['created_at'])




main()


