import re

from PyPDF2 import PdfReader
from docx import Document

from pyresparser import ResumeParser


def resume_result_wrapper(resume):
    parser = ResumeParser(resume)
    print(parser.get_extracted_data())
    return parser.get_extracted_data()


def get_text_from_file(file_path):
    text = 'This PDF-file is not readable'
    if file_path.endswith('.pdf'):
        try:
            text = str()
            reader = PdfReader(file_path)
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                text += page.extract_text()
            return text
        except Exception:
            return text

    elif file_path.endswith('.docx'):
        try:
            text = str()
            source = Document(file_path)
            paras = source.paragraphs
            for i in range(len(paras)):
                text += paras[i].text
            return text
        except Exception:
            return text

    else:
        return text


def extract_contact_info(resume_lines):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    phone_pattern = r"\+?[0-9\s\-\(\)]{7,}"
    linkedin_pattern = r"\b(?:https?:\/\/)?(?:www\.)?(linkedin\.com\/[^\s,]*)"
    github_pattern = r"\b(?:https?:\/\/)?(?:www\.)?(github\.com\/[^\s,]*|[a-zA-Z0-9-]+\.github\.io\/?[^\s,]*)"

    email, phone, linkedin, github = None, None, None, None

    for line in resume_lines:
        if not email:
            email_match = re.search(email_pattern, line)
            if email_match:
                email = email_match.group(0)

        if not phone:
            phone_match = re.search(phone_pattern, line)
            if phone_match:
                phone = phone_match.group(0)

        if not linkedin:
            linkedin_match = re.search(linkedin_pattern, line)
            if linkedin_match:
                linkedin = linkedin_match.group(0)

        if not github:
            github_match = re.search(github_pattern, line)
            if github_match:
                github = github_match.group(0)

        if email and phone and linkedin and github:
            break

    return email, phone, linkedin, github


class SmartResParser:
    def __call__(
            self,
            file_path
    ):
        res = {
            "resume_id": "",
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

        pyresparser_result = resume_result_wrapper(file_path)
        contact_info = extract_contact_info(get_text_from_file(file_path))

        if contact_info[0] or pyresparser_result['email']:
            res['contactItems'].append({
                "resume_contact_item_id": len(res['contactItems']),
                "value": contact_info[0] or pyresparser_result['email'],
                "comment": "",
                "contact_type": "Email"
            })
        if contact_info[1] or pyresparser_result['mobile_number']:
            res['contactItems'].append({
                "resume_contact_item_id": len(res['contactItems']),
                "value": contact_info[1] or pyresparser_result['mobile_number'],
                "comment": "",
                "contact_type": "Телефон"
            })
        if contact_info[3]:
            res['contactItems'].append({
                "resume_contact_item_id": len(res['contactItems']),
                "value": contact_info[3],
                "comment": "",
                "contact_type": "Github"
            })

        if pyresparser_result['name']:
            res['first_name'] = pyresparser_result['name'].split(' ')[0]
            res['last_name'] = pyresparser_result['name'].split(' ')[-1]
            res['middle_name'] = pyresparser_result['name'].split(' ')[2] \
                if len(pyresparser_result['name'].split(' ')) > 2 else ""

        res['key_skills'] = pyresparser_result['skills'] or ""

        if pyresparser_result['degree']:
            for degree in pyresparser_result['degree']:
                res['educationItems'].append({
                    "resume_education_item_id": len(res['educationItems']),
                    "year": "",
                    "organization": pyresparser_result['college_name'],
                    "faculty": "",
                    "specialty": degree,
                    "result": "",
                    "education_type": "",
                    "education_level": ""
                })

        if pyresparser_result['designation']:
            for designation in pyresparser_result['designation']:
                res['experienceItems'].append({
                    "resume_experience_item_id": len(res['experienceItems']),
                    "starts": "",
                    "ends": "",
                    "employer": designation,
                    "city": "",
                    "url": "",
                    "position": "",
                    "description": pyresparser_result['experience'] or "",
                    "order": len(res['experienceItems'])
                })

        return res
