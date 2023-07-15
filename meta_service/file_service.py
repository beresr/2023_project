import os
#Constans: konstans változó, értéke nem vált.
#FOLDER_PATH = r"D:\Rita\Python\project\movies"

class FileService:
    #folder_path = r"D:\Rita\Python\project\movies"

    def __init__(self):
        #self.folder_path = folder_path
        ...
    def write_image(self):
        ...
    
    def writejson_data(self, json_path, data):
        import json
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def get_data_from_folder(self, folder_path):   ##általánosabban elérhető
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"A megadott folder: {folder_path} \n NEM létezik")
        
        temp = []
        for item in os.listdir(folder_path):
            temp.append(item[0:-4])

        return temp
        
        
        """try:
            movies = os.listdir(folder_path)
        except Exception as e:
            raise e
        
        return movies
        """


if __name__ == '__main__':
    from config import MOVIES_PATH
    test = FileService()

    movies = test.get_data_from_folder(MOVIES_PATH)
#print(movies)

for item in movies:
    ##itt egyesével letöltöm a metaadatot
    test.write_json_data