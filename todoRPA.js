const { Client } = require("@notionhq/client");

// Notion API 키와 페이지 ID 초기화
const notion = new Client({ auth: "secret_tszdt2iw3NM6L2xAOaMNTEmGbMvuAN7U9oaydXBSTbb" });
const pageId = "45eeff50ce584b099c0881d0fc3c8969";

async function addBlockToPage() {
    try {
      const response = await notion.blocks.children.append({
        block_id: pageId,
        children: [
          {
            object: 'block',
            type: 'heading_2',
            heading_2: {
              rich_text: [
                {
                  type: 'text',
                  text: {
                    content: '새로운 제목',
                  },
                },
              ],
            },
          },
          {
            object: 'block',
            type: 'paragraph',
            paragraph: {
              rich_text: [
                {
                  type: 'text',
                  text: {
                    content: '새로운 단락 내용입니다.',
                    link: null,
                  },
                  annotations: {
                    color: 'blue',
                  },
                },
              ],
            },
          },
          // 추가하고 싶은 다른 블록들을 여기에 포함시킬 수 있습니다.
        ],
      });
  
      console.log("블록이 성공적으로 추가되었습니다:", response);
    } catch (error) {
      console.error("블록을 추가하는 데 실패했습니다:", error.body);
    }
  }
  
  addBlockToPage();