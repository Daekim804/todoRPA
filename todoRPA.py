import requests

def create_notion_block(token, block_id, children):
    create_url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    data = {"children": children}

    response = requests.post(create_url, headers=headers, json=data)
    return response.json()

# 사용 예시
notion_token = "secret_tszdt2iw3NM6L2xAOaMNTEmGbMvuAN7U9oaydXBSTbb"
block_id = "45eeff50ce584b099c0881d0fc3c8969"

children = [
    {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [{"type": "text", "text": {"content": "Lacinato kale"}}]
        },
    },
    {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
                        "link": {"url": "https://en.wikipedia.org/wiki/Lacinato_kale"}
                    }
                }
            ]
        },
    }
]

result = create_notion_block(notion_token, block_id, children)
print(result)
