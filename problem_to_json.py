import flet as ft
import json
import string

def main(page: ft.Page):
    page.title = "Question Data Form"
    
    # 入力フィールドを含むコンテナ
    form_container = ft.ListView(expand=True)

    # テキストフィールドの作成
    txt_id = ft.TextField(label="ID", width=page.window_width - 40)
    txt_stem = ft.TextField(label="Question Stem", width=page.window_width - 40,multiline=True)
    txt_context = ft.TextField(label="Question context", width=page.window_width - 40,multiline=True)
    txt_num_choices = ft.TextField(label="Number of Choices", width=page.window_width - 40, value="4")
    txt_choices = []
    txt_answer_key = ft.TextField(label="Answer Key (e.g., A)", width=page.window_width - 40)

    # JSONを表示するためのテキスト
    txt_json_output = ft.Text(value="", size=20)

    # Update Choicesボタン
    btn_update_choices = ft.ElevatedButton(text="Update Choices", on_click=lambda e: update_choices())

    # Submitボタン
    btn_submit = ft.ElevatedButton(text="Generate JSON", on_click=lambda e: generate_json())

    # フォームのウィジェットをコンテナに追加
    form_container.controls.extend([txt_id, txt_stem,txt_context, btn_update_choices, txt_num_choices, txt_answer_key, btn_submit, txt_json_output])
    page.add(form_container)

    def update_choices():
        nonlocal txt_choices
        # 現存する選択肢フィールドをクリア
        for choice in txt_choices:
            form_container.controls.remove(choice)
        txt_choices.clear()

        # txt_num_choices のインデックスを見つける
        num_choices_index = form_container.controls.index(txt_num_choices) + 1

        # 新しい選択肢フィールドを作成
        num_choices = int(txt_num_choices.value)
        for i in range(num_choices):
            label = string.ascii_uppercase[i]
            choice = ft.TextField(label=f"Choice {label}", width=page.window_width - 40)
            txt_choices.append(choice)
            # txt_num_choices の直後に新しい選択肢フィールドを挿入
            form_container.controls.insert(num_choices_index + i, choice)

        page.update()


    import os

    def generate_json():
        # 入力データを基にJSONデータを構築
        data = {
            "id": txt_id.value,
            "question": {
                "stem": txt_stem.value,
                "context": txt_context.value,
                "choices": [{"text": choice.value, "label": label} for choice, label in zip(txt_choices, string.ascii_uppercase[:len(txt_choices)])],
            },
            "answerKey": txt_answer_key.value
        }

        # JSON形式の文字列に変換
        json_str = json.dumps(data, indent=4)

        # JSONをテキストウィジェットに表示
        txt_json_output.value = json_str

        # ファイル名をIDから生成
        filename = f"{txt_id.value}.json"

        # JSONデータをファイルに保存
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_str)

        # ページを更新し、保存したファイル名を通知
        txt_json_output.value += f"\n\nJSON data saved to {filename}"
        page.update()


    # 初期の選択肢フィールドを作成
    update_choices()

# アプリを実行
ft.app(target=main)
