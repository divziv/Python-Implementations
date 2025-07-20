import pandas as pd

def search_excel_for_substring(file_path, column_name, substring):
    # Read the Excel file
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

    # Print column names to verify
    print("Column names:", df.columns)

    # Check if the column exists
    if column_name not in df.columns:
        print(f"Column '{column_name}' not found in the Excel sheet.")
        return None

    # Filter rows where the specified column contains the substring
    filtered_rows = df[df[column_name].astype(str).str.contains(substring, case=False, na=False)]

    # Sort the filtered rows first alphabetically, then by length within each group
    sorted_rows = filtered_rows.sort_values(by=[column_name], key=lambda col: col.str.lower()).sort_values(by=[column_name], key=lambda col: col.str.len(), kind='stable')

    return sorted_rows

def main():
    # Prompt user for file path and substring
    print("Enter the path to the Excel file. Use capslock for drive name, double backslashes (\\\\) for Windows paths.")
    file_path = input("File path: ").strip()
    column_name = 'Directory'  # Ensure this matches exactly
    substring = input("Enter the substring to search for: ").strip()

    # Get the filtered and sorted rows
    result = search_excel_for_substring(file_path, column_name, substring)

    # Print the result
    if result is not None:
        print(result)
    else:
        print("No results found or an error occurred.")

if __name__ == '__main__':
    main()
