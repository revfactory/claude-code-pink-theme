# Claude Code Pink Theme 🌸

Claude Code 공식 문서를 핑크 테마로 꾸민 한국어 웹사이트입니다.

## 📋 프로젝트 개요

이 프로젝트는 Anthropic의 Claude Code AI 코딩 어시스턴트 문서를 핑크 색상 팔레트로 재디자인하고 한국어로 번역한 웹사이트입니다. 원본 문서의 모든 기능과 내용을 유지하면서 더욱 아름답고 친숙한 인터페이스를 제공합니다.

## ✨ 주요 기능

- 🎨 **핑크 테마 디자인**: 따뜻하고 친근한 핑크 색상 팔레트
- 🇰🇷 **한국어 지원**: 완전한 한국어 번역 및 현지화
- 📱 **반응형 디자인**: 모든 디바이스에서 최적화된 경험
- 🔍 **직관적인 네비게이션**: 쉽고 빠른 정보 탐색
- 💻 **상호작용 요소**: 호버 효과와 애니메이션

## 🎨 테마 색상

```css
--primary-pink: #FF69B4
--light-pink: #FFB6C1
--pale-pink: #FFC0CB
--deep-pink: #FF1493
--hot-pink: #FF69B4
--rose: #FFE4E1
--blush: #FFF0F5
```

## 📁 프로젝트 구조

```
claude-code-pink-theme/
├── index.html                     # 메인 홈페이지
├── styles.css                     # 핑크 테마 스타일시트
├── fetch_website.py               # 원본 문서 가져오기 스크립트
├── *.html                         # 각종 문서 페이지들
├── claude-code-*.md              # 마크다운 문서들
└── README.md                      # 이 파일
```

### 주요 페이지들

- **index.html**: 메인 홈페이지
- **overview.html**: Claude Code 개요
- **installation.html**: 설치 가이드
- **cli-usage.html**: CLI 사용법
- **common-tasks.html**: 일반 작업
- **advanced-features.html**: 고급 기능
- **ide-integration.html**: IDE 통합
- **github-actions.html**: GitHub Actions
- **security.html**: 보안
- **troubleshooting.html**: 문제 해결

## 🚀 로컬 실행

### 1. 저장소 클론

```bash
git clone https://github.com/revfactory/claude-code-pink-theme.git
cd claude-code-pink-theme
```

### 2. 웹 서버 실행

#### Python을 사용하는 경우:
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

#### Node.js를 사용하는 경우:
```bash
npx serve .
```

#### PHP를 사용하는 경우:
```bash
php -S localhost:8000
```

### 3. 브라우저에서 접속

http://localhost:8000 으로 접속하여 웹사이트를 확인할 수 있습니다.

## 🛠️ 개발

### 문서 업데이트

원본 Claude Code 문서에서 최신 내용을 가져오려면:

```bash
python fetch_website.py
```

### 스타일 수정

`styles.css` 파일에서 핑크 테마 색상과 레이아웃을 수정할 수 있습니다.

## 📖 Claude Code란?

Claude Code는 Anthropic이 개발한 AI 기반 코딩 어시스턴트입니다:

- 🤖 **스마트 코드 편집**: 컨텍스트를 이해하고 지능적인 코드 수정
- 🔍 **코드 아키텍처 분석**: 복잡한 시스템 구조 이해 및 설명
- 🧪 **테스트 자동화**: 테스트 작성, 실행, 디버깅 지원
- 🌿 **Git 워크플로우**: 커밋, PR 생성, 머지 충돌 해결
- 🔒 **엔터프라이즈 보안**: 세밀한 권한 제어
- 🚀 **IDE 통합**: VS Code, JetBrains IDE 지원

## 🤝 기여

이 프로젝트에 기여하고 싶으시다면:

1. 이 저장소를 포크합니다
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성합니다

## 📄 라이센스

이 프로젝트는 원본 Claude Code 문서의 라이센스를 따릅니다.

## 🔗 관련 링크

- [Claude Code 공식 문서](https://docs.anthropic.com/en/docs/claude-code)
- [Anthropic](https://www.anthropic.com)
- [Claude](https://claude.ai)

---

💖 **Made with Pink Love** by revfactory