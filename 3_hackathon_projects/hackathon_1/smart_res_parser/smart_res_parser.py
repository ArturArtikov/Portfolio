class SmartResParser:
    def __init__(self):
        pass

    def parse_resume(
            self,
            file_path
    ):
        return {
            "first_name": "",
            "last_name": "",
            "middle_name": "",
            "birth_date": "",
            "birth_date_year_only": False,
            "country": "",
            "city": "",
            "about": "",
            "key_skills": "",
            "salary_expectations_amount": "",
            "salary_expectations_currency": "",
            "photo_path": "",
            "gender": "",
            "resume_name": "",
            "source_link": "",
            "contactItems": [],
            "educationItems": [],
            "experienceItems": [],
            "languageItems": []
        }
