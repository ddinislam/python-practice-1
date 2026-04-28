import os
import csv
import json

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        """Проверка наличия файла данных."""
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder='output'):
        """Создание папки для результатов."""
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        """Загрузка 10,000 строк из CSV."""
        print("Loading data...")
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = [row for row in reader]
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

    def preview(self, n=5):
        """Вывод первых 5 строк (student_id, age, gender, country, GPA)."""
        print(f"First {n} rows:")
        print("-" * 50)
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
        print("-" * 50)

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = []

    def analyse(self):
        """Вариант D: Поиск ТОП-10 по финальному экзамену."""
        valid_students = []
        for s in self.students:
            try:
                s['final_exam_score'] = float(s['final_exam_score'])
                s['GPA'] = float(s['GPA'])
                valid_students.append(s)
            except (ValueError, KeyError):
                continue

        sorted_students = sorted(valid_students, key=lambda x: x['final_exam_score'], reverse=True)
        self.result = sorted_students[:10]
        return self.result

    def run_extra_logic(self):
        """Lambda, Filter, Map (требование Практики 5)."""
        top_gpa = list(filter(lambda s: float(s['GPA']) >= 4.0, self.valid_data_helper()))
        print(f"Students with 4.0 GPA: {len(top_gpa)}")


        countries = list(map(lambda s: s['country'], self.students[:5]))
        print(f"Sample countries: {countries}")
        print("-" * 50)

    def valid_data_helper(self):
        """Помощник для безопасного перевода в float."""
        res = []
        for s in self.students:
            try:
                s['GPA'] = float(s['GPA'])
                res.append(s)
            except: continue
        return res

    def print_results(self):
        print("TOP 10 STUDENTS BY EXAM SCORE (Variant D):")
        for i, s in enumerate(self.result, 1):
            print(f"{i}. ID: {s['student_id']} | Score: {s['final_exam_score']} | GPA: {s['GPA']} | Major: {s['major']}")
        print("-" * 50)

class ResultSaver:
    def __init__(self, data, path):
        self.data = data
        self.path = path

    def save(self):
        """saving in JSON."""
        try:
            with open(self.path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=4)
            print(f"Successfully saved to {self.path}")
        except Exception as e:
            print(f"Save error: {e}")

def main():
    csv_file = 'global_university_students_performance_habits_10000.csv'
    
    fm = FileManager(csv_file)
    if not fm.check_file():
        return
    fm.create_output_folder()

    dl = DataLoader(csv_file)
    data = dl.load()
    if not data: return
    dl.preview()

    analyser = DataAnalyser(data)
    analyser.run_extra_logic()
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save()

if __name__ == "__main__":
    main()