import pandas as pd
pd.options.display.float_format = '{:,}'.format


def gather_salary_data(dataset="datasets/ds_salaries.csv"):   
    data = pd.read_csv(dataset)
    # drop redundant columns
    data = data.drop(["Unnamed: 0", "salary", "salary_currency"], axis=1)

    for i, xp in enumerate(data['experience_level']):
        if data['experience_level'][i] == 'EN':
            data['experience_level'][i] = 'Entry Level'
        elif data['experience_level'][i] == 'MI':
            data['experience_level'][i] = 'Mid Level'
        elif data['experience_level'][i] == 'SE':
            data['experience_level'][i] = 'Senior Level'
        else:
            data['experience_level'][i] = 'Executive Level'

    for i, emp in enumerate(data['employment_type']):
        if data['employment_type'][i] == "CT":
            data['employment_type'][i] = "Contract"
        elif data['employment_type'][i] == "FT":
            data['employment_type'][i] = "Full-time"
        elif data['employment_type'][i] == "FL":
            data['employment_type'][i] = "Freelance"
        else:
            data['employment_type'][i] = "Part-time"
        
    for i, size in enumerate(data['company_size']):
        if data['company_size'][i] == "L":
            data['company_size'][i] = "Large"
        elif data['company_size'][i] == "M":
            data['company_size'][i] = "Medium"
        else:
            data['company_size'][i] = "Small"
    return data

