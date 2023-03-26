import csv
import json


def csv_to_json(csv_file_path, json_file_path, model_name):

    json_array = []

    # read csv file
    with open(csv_file_path, encoding='utf-8') as csv_file:
        # load csv file data using csv library's dictionary reader
        csv_reader = csv.DictReader(csv_file)

        # convert each csv row into python dict
        for row in csv_reader:

            # ID delete
            keys = row.keys()
            if 'id' in keys:
                del row['id']
            elif 'Id' in row.keys():
                del row['Id']

            # "TRUE", "FALSE" to bool
            if 'is_published' in keys:
                row['is_published'] = (row['is_published'].upper() == 'TRUE')

            # "Price" to int
            if 'price' in keys:
                row['price'] = int(row['price'])

            if 'location_id' in keys:
                row['location'] = [row['location_id']]
                del row['location_id']

            # add this python dict to json array
            json_array.append({"model": model_name, "fields": row})

    # convert python jsonArray to JSON String and write to file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json_string = json.dumps(json_array, indent=4, ensure_ascii=False)
        json_file.write(json_string)


csv_to_json('ad.csv', 'ad.json', 'ads.ad')
csv_to_json('category.csv', 'category.json', 'ads.category')
csv_to_json('location.csv', 'location.json', 'ads.location')
csv_to_json('user.csv', 'user.json', 'ads.user')
