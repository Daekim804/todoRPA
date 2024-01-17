import requests

# Notion API 토큰 설정
api_token = 'tszdt2iw3NM6L2xAOaMNTEmGbMvuAN7U9oaydXBSTbb'  # Notion 개발자 대시보드에서 발급받은 API 토큰을 여기에 입력하세요

# 페이지 ID 및 블록 데이터 설정
page_id = '4-45eeff50ce584b099c0881d0fc3c8969'  # 블록을 추가하려는 페이지의 ID를 여기에 입력하세요
api_url = f'https://api.notion.com/v1/pages/4-45eeff50ce584b099c0881d0fc3c8969/children'

headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

block_data = {
    'object': 'block',
    'type': 'paragraph',
    'paragraph': {
        'text': [
            {
                'type': 'text',
                'text': {
                    'content': '새로운 블록 내용',
                },
            },
        ],
    },
}

# API 요청 보내기
response = requests.post(api_url, headers=headers, json=block_data)

# 응답 확인
if response.status_code == 200:
    print('블록이 성공적으로 추가되었습니다.')
else:
    print(f'블록 추가에 실패했습니다. 상태 코드: {response.status_code}')
