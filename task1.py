import PyPDF2


def extract_pdf_info(pdf_file_path):
    pdf_info = {}  # Создаем пустой словарь для хранения информации

    with open(pdf_file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        page = pdf_reader.pages[0]  # Извлекаем первую (и единственную) страницу
        text = page.extract_text()  # Извлекаем текст с страницы

        lines = text.split('\n')  # Разделяем текст на строки по символу новой строки
        print(lines)
        for line in lines:
            if line == 'REMARK: LOT# : 1':
                key, value, key1, value1 = 'REMARK:', '', 'LOT#', '1'
                pdf_info[key[:-1]] = value
                pdf_info[key1[:-1]] = value1
                continue
            if line.count(':') == 1:
                key, value = map(str.strip, line.split(":"))  # Разделяем строку на ключ и значение
                pdf_info[key] = value  # Добавляем пару ключ-значение в словарь
                continue
            if line.count(':') == 2:
                try:
                    temp_list = line.split(':', 1)
                    value, key1, value1 = temp_list[1].split()
                    pdf_info[temp_list[0]] = value
                    pdf_info[key1[:-1]] = value1
                except ValueError:
                    value = '1'
                    key1, value1 = 'Notes', 'inspection notes'
                    pdf_info[temp_list[0]] = value
                    pdf_info[key1] = value1
                continue
    return pdf_info


pdf_file_path = 'test_task.pdf'
result_dict = extract_pdf_info(pdf_file_path)

for key, value in result_dict.items():
    print(f"{key}: {value}")
