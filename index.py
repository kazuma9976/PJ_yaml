import yaml
import pandas as pd

# 1. YAMLファイルの読み込み
def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# 2. YAMLデータをフラット化してリスト化
def flatten_user_data(yaml_data):
    user_list = []
    for user in yaml_data['sample_data']['users']:
        flat_user = {
            'Name': user['name'],
            'Age': user['age'],
            'Email': user['email'],
            'City': user['address']['city'],
            'Zipcode': user['address']['zipcode']
        }
        user_list.append(flat_user)
    return user_list

# 3. データをExcelに書き込み
def write_to_excel(user_list, output_file_path):
    df = pd.DataFrame(user_list)
    df.to_excel(output_file_path, index=False)

# メイン処理
if __name__ == "__main__":
    # YAMLファイルのパス
    yaml_file_path = 'users.yaml'  # 読み込むYAMLファイル
    excel_file_path = 'users.xlsx'  # 書き出すExcelファイル

    # 1. YAMLファイルをロード
    yaml_data = load_yaml(yaml_file_path)

    # 2. YAMLデータをフラット化
    user_list = flatten_user_data(yaml_data)

    # 3. フラット化したデータをExcelに書き込む
    write_to_excel(user_list, excel_file_path)

    print(f"YAMLファイルがExcelファイル '{excel_file_path}' に変換されました。")
