from flask import Flask, render_template

app = Flask(__name__)

# --- 프로젝트 데이터 정의 ---
# 각 프로젝트의 정보를 담고 있습니다.
# 여기에 새 프로젝트를 추가하거나 기존 프로젝트를 수정할 수 있습니다.
projects_data = [
    {
        "id": "media-art", # 프로젝트를 식별하는 고유 ID (URL에 사용됨)
        "title_ko": "미디어 아트", # 한글 제목
        "title_en": "media art", # 영문 제목 (프로젝트 박스에 표시)
        "thumb_img": "images/media_art_thumb.png", # 호버 시 나타날 썸네일 이미지 (static/images/ 경로)
        "type": "image", # 'image': 썸네일 이미지가 보임, 'text': 텍스트만 보임 (호버 시에도)
        "description": "이 미디어 아트 프로젝트는 첨단 기술과 예술적 감각을 융합하여 관람객에게 몰입형 경험을 제공합니다. 다양한 인터랙티브 요소를 통해 사용자의 참여를 유도하며, 시각적, 청각적 자극을 통해 새로운 차원의 예술적 사색을 이끌어냅니다.",
        "full_images": ["images/artwork_full_1.jpg"], # 상세 페이지용 이미지 목록
        "materials": "디지털 미디어, 인터랙티브 센서, 프로젝션 맵핑",
        "year": "2023"
    },
    {
        "id": "surrealist-photography",
        "title_ko": "초현실주의 사진",
        "title_en": "surrealist<br>photography", # <br> 태그로 제목 줄바꿈 가능
        "thumb_img": "images/photography_thumb.png", # 썸네일 이미지 경로
        "type": "image", # 'image'로 변경하여 호버 시 이미지 보임
        "description": "꿈과 현실의 경계를 허무는 초현실주의 사진 시리즈입니다. 일상적인 풍경에 비현실적인 요소를 더하여 상상력을 자극하고, 보는 이에게 새로운 시각적 경험을 선사합니다. 각각의 사진은 독립적인 이야기를 담고 있으면서도, 전체적으로는 하나의 거대한 내러티브를 형성합니다.",
        "full_images": ["images/photography_full_1.jpg"],
        "materials": "사진, 디지털 합성, Adobe Photoshop",
        "year": "2024"
    },
    {
        "id": "logo-design",
        "title_ko": "로고 디자인",
        "title_en": "logo design",
        "thumb_img": "images/logo_design_thumb.png", # 썸네일 이미지 경로
        "type": "image", # 'image'로 변경하여 호버 시 이미지 보임
        "description": "다양한 브랜드의 아이덴티티를 구축하기 위한 로고 디자인 작업물입니다. 클라이언트의 요구사항을 바탕으로 시장 조사, 컨셉 도출, 시안 제작 과정을 거쳐 브랜드의 핵심 가치를 시각적으로 표현합니다. 미니멀리즘부터 복잡한 일러스트레이션까지 폭넓은 스타일을 다룹니다.",
        "full_images": ["images/logo_design_full_1.jpg", "images/logo_design_full_2.jpg"],
        "materials": "Adobe Illustrator, 스케치",
        "year": "2024"
    }
    # 여기에 더 많은 프로젝트를 추가할 수 있습니다.
]

# --- Flask 라우팅 (URL 처리) ---

@app.route('/')
def index():
    """메인 포트폴리오 페이지를 렌더링합니다."""
    # projects_data를 index.html 템플릿으로 전달합니다.
    return render_template('index.html', projects=projects_data)

@app.route('/project/<project_id>')
def project_detail(project_id):
    """각 프로젝트의 상세 페이지를 렌더링합니다."""
    # projects_data 리스트에서 요청된 project_id와 일치하는 프로젝트를 찾습니다.
    project = next((p for p in projects_data if p['id'] == project_id), None)

    if project:
        # 해당 프로젝트를 찾으면 project_detail.html 템플릿에 전달하여 렌더링합니다.
        return render_template('project_detail.html', project=project)
    else:
        # 프로젝트를 찾지 못했을 경우 404 에러를 반환합니다.
        return "<h1>404 Not Found</h1><p>죄송합니다. 요청하신 프로젝트를 찾을 수 없습니다.</p><p><a href='/'>메인 페이지로 돌아가기</a></p>", 404

# --- 애플리케이션 실행 ---
if __name__ == '__main__':
    # Flask 애플리케이션을 개발 모드로 실행합니다.
    app.run(debug=True)