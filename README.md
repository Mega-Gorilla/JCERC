# JCERC - Japan Common University Entrance Exam Reasoning Challenge

Japanese follows English. / 日本語の記述は英語に続きます．

A new dataset of genuine high school level, multiple-choice science questions from the 2024 Common University Entrance Examination (Japan), assembled to encourage research in advanced question-answering. We pose this dataset, based on the 2024 Common University Entrance Examination (Japan), as a challenge to the community.

2024年度大学入学共通テストに出題された、高校レベルの理科の多肢選択問題を集めた新しいデータセットです。2024年大学入学共通テストに基づくこのデータセットは、LLMを評価するために作成されました。

## Description / 内容

This dataset consists of JSON files that transcribe the question texts and answers from the 2024 University Entrance Examination.

このデータセットは2024年度大学共通テストの問題文をおよび回答を書き起こしたJsonファイルで構成されています。

### JSON Structure / Jsonファイルの構造

The JSON files provide the text of the question "stem," as well as the "context" necessary to answer the question. Additionally, they include various "choices" for the answers, along with corresponding labels (1, 2, 3, 4). The files also contain the "answerKey" indicating the correct answer and the "score" representing the points for the question. The "id" refers to the question number, for instance, "JCUE_kokugo_2024_1_1_1" indicates University Entrance Examination 2024 - Question 1 - Subquestion 1 - Answer Option 1.

Jsonファイルには質問の文"stem"および問題を解答するのに必要な"context"が提供され、さらに様々な回答の"choices"、およびそれらに対応するラベル(1,2,3,4)が含まれています。そのほかに、回答を示す"anserKey"とその問題の点数を示す"socre"が含まれます。またidは、問題番号を指し、"JCUE_kokugo_2024_1_1_1"の場合、2024粘度大学共通テスト-問題番号1-設問1-解答番号1を示しています。

```
{
        "id": "JCUE_kokugo_2024_1_1_1",
        "question": {
            "stem": "これは、日本語における漢字の問題です。\r\nカタカナの「ケイサイ」を漢字変換した時、同じ漢字を含む設問を解答せよ。",
            "context": "",
            "choices": [
                {
                    "text": "名著に「ケイハツ」される",
                    "label": "1"
                },
                {
                    "text": "連絡事項を「ケイシュツ」する",
                    "label": "2"
                },
                {
                    "text": "方針転換の「ケイキ」になる",
                    "label": "3"
                },
                {
                    "text": "一族の「ケイズ」を作る",
                    "label": "4"
                }
            ]
        },
        "answerKey": "2",
        "score": "2"
    }
```

### problem_to_json.py

This Python file provides an editor for creating the aforementioned JSON data files. The editor allows you to input the necessary information into the UI and add data in the specified format to the designated JSON file.

このpyファイルは、上記Jsonデータファイルを作成するためのエディターを提供しています。
このエディターは、UIに必要情報を入力することで、設定したJsonファイルに上記フォーマットのデータを追加することができます。

# Collaboration / 協力

This dataset is currently a solo project by Me. We are actively seeking volunteers to collaborate and contribute to this project!

このデータセットは、猩々博士が１人で製作しており、有志にて協力してくれる方を募集中です！！