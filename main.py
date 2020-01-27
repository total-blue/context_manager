import datetime
class OpenerCounter:
    def __enter__(self):
        self.enter_time = datetime.datetime.now()
        print('Entry time ', self.enter_time)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit_time = datetime.datetime.now()
        print('Exit time ', self.exit_time)
        self.res = self.exit_time - self.enter_time
        print('Spent: ', self.res)

if __name__ == '__main__':
    with OpenerCounter():
        documents = [
                     {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
                     {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
                     {"type": "invoice", "number": "11-2"},
                     {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
                     ]

        directories = {
                      '1': ['2207 876234', '11-2', '5455 028765'],
                      '2': ['10006', '5400 028765', '5455 002299'],
                      '3': []
                       }

        def find_person_by_number(number):
            founded = False
            for line in documents:
                if line['number'] == number:
                    print(line['name'])
                    founded = True
            if not founded:
                print(f'invalid doc number {number}')

        def show_docs():
            for line in documents:
                person = ' '.join(list(line.values()))
                print(person)

        def find_shelf_by_number(number):
            founded = False
            for key in directories:
                if number in directories[key]:
                    print(key)
                    founded = True
            if not founded:
                print(f'invalid shelf number {number}')

        def add_doc_dir(doc_number, type, name, shelf_number):
            if not shelf_number in directories.keys():
                directories[shelf_number] = []
            documents.append({'type': type, 'number': doc_number, 'name': name})
            directories[shelf_number].append(doc_number)

        def del_doc_dir(number):
            for i in range(len(documents)):
                if documents[i]['number'] == number:
                    del documents[i]
                    break

        def move_doc(doc_number, shelf_number):
            if not shelf_number in directories.keys():
                directories[shelf_number] = []
                print(f'shelf {shelf_number} created')
            doc_founded = False
            for shelf in directories.keys():
                if doc_number in directories[shelf]:
                    directories[shelf].pop(directories[shelf].index(doc_number))
                    doc_founded = True
                    break
            if not doc_founded:
                print(f'invalid doc number {doc_number}')
            if not shelf_number in directories.keys():
                directories[shelf_number] = []
            directories[shelf_number].append(doc_number)

        def add_shelf(shelf_number):
            if not shelf_number in directories.keys():
                directories[shelf_number] = []
            else:
                print(f'shelf {shelf_number} already exist!')

        def show_names():
            names=[]
            for doc in documents:
                try:
                    names.append(doc['name'])
                except KeyError:
                    names.append('noname')
            print(names)


        def handler():
            command = input('enter your command: ')
            if command == 'p':
                doc_number = input('number? ')
                find_person_by_number(doc_number)
            elif command == 'l':
                show_docs()
            elif command == 's':
                shelf_number = input('number? ')
                find_shelf_by_number(shelf_number)
            elif command == 'a':
                doc_number = input('document number? ')
                type = input('type? ')
                name = input('name? ')
                shelf_number = input('shelf_number? ')
                add_doc_dir(doc_number, type, name, shelf_number)
            elif command == 'm':
                doc_number = input('doc number? ')
                shelf_number = input('shelf number? ')
                move_doc(doc_number, shelf_number)
            elif command == 'as':
                shelf_number = input('shelf number? ')
                add_shelf(shelf_number)
            elif command == 'sn':
                show_names()
            elif command == 'exit':
                global Flag
                Flag = False

        Flag = True
        while Flag:
            handler()
