import json
import os


def get_schema() -> list:
    """Get the schema definition of the form data"""
    return [
        {
            "name": "First Name",
            "type": "string",
            "required": True,
            "description": "User name, between 3 and 20 characters long",
            "value": None,
        },
        {
            "name": "Last Name",
            "type": "string",
            "required": True,
            "description": "User name, between 3 and 20 characters long",
            "value": None,
        },
        {
            "name": "Age",
            "type": "number",
            "required": True,
            "description": "Age, please enter a positive integer",
            "value": None,
        },
        {
            "name": "email",
            "type": "string",
            "required": False,
            "description": "Email address to receive notifications",
            "value": None,
        }
    ]


def ensure_form_file_exists(file_path: str) -> bool:
    """
    Ensure the form data file exists, create it if it doesn't
    """
    try:
        if not os.path.exists(file_path):
            print(
                f"Form data file does not exist: {file_path}, creating new file")
            # Ensure directory exists
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            # Create empty form data
            empty_form_data = get_schema()
            # Write empty data to file
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(empty_form_data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error creating form data file: {e}")
        return False


def get_user_data_tool() -> str:
    """
    Get user information from the JSON file
    """
    file_path = "./form_data.json"
    try:
        if not ensure_form_file_exists(file_path):
            return get_schema()

        with open(file_path, 'r', encoding='utf-8') as f:
            form_data = json.load(f)
            return json.dumps(form_data, indent=2)
            # return form_data
    except json.JSONDecodeError:
        return (f"JSON format error: {file_path}")
    except Exception as e:
        return (f"Error reading form data: {e}")


def update_user_data_tool(field_name: str, field_value: str) -> str:
    """
    Update user information in the JSON file

    Args:
        field_name (str): Form field name
        field_value (str): Form field value

    Returns:
        Updated field data
    """
    file_path = "./form_data.json"
    try:
        # Ensure file exists
        if not ensure_form_file_exists(file_path):
            return

        with open(file_path, 'r+', encoding='utf-8') as f:
            form_data = json.load(f)
            # Find the field to update
            for field in form_data:
                if field['name'] == field_name:
                    # Convert value according to field type
                    if field['type'] == 'number':
                        try:
                            field['value'] = int(field_value)
                        except ValueError:
                            try:
                                field['value'] = float(field_value)
                            except ValueError:
                                return (f"Warning: Cannot convert '{field_value}' to number type, keeping original string")
                                # field['value'] = field_value
                    else:  # string or other types
                        field['value'] = field_value
                    break
            f.seek(0)
            json.dump(form_data, f, ensure_ascii=False, indent=2)
            f.truncate()
        return f"Form data update successful: {field_name} = {field_value}"
    except Exception as e:
        return (f"Error updating form data: {e}")
