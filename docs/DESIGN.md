# AMC 홈페이지 디자인

## 방향

파란색을 AMC의 중심 색으로 유지하고, 서로 다른 분야의 경험이 연결되는 메이커 작업판을 첫 화면의 핵심 그래픽으로 사용합니다. 한글 제목과 참여 안내를 먼저 읽을 수 있게 하고 SHARE·MAKE·CONNECT, 참여 절차, 운영 원칙, 공개 사례 순으로 정보를 배치합니다.

## 구성

- 색상: cobalt #244bdd, ink #1d2b48, paper #f6f8fc, mint #c7e6dd, peach #f8d8c5. 배경과 색 대비를 구분하고 파란색은 주요 행동과 브랜드에 사용합니다.
- 서체: 한글은 Apple SD Gothic Neo / Malgun Gothic 시스템 서체, 영문 표지는 Avenir Next 계열입니다. 외부 폰트 요청은 없습니다.
- 레이아웃: 데스크톱은 소개와 작업판의 비대칭 2열, 활동 3열입니다. 800px 이하에서는 본문을 세로 배치하고 540px 이하에서 활동·참여·기록 영역을 한 열로 구성합니다.
- 그래픽: 로컬 SVG와 CSS로 제작했습니다. 이미지·폰트·스크립트 CDN, 분석 도구, 새 런타임 의존성이 없습니다. 그래픽 속 대화와 문서는 활동 방식을 설명하는 장식이며 실제 사례나 회원 기록이 아닙니다.
- 접근성: 한글 lang, 의미 있는 제목 단계, 본문 바로가기, 키보드 포커스, 44px 이상의 주요 링크/버튼, 줄어든 모션 설정, 장식 SVG의 aria-hidden을 적용합니다.
- 공개 경계: 행사 일정·신청·연락처를 임의로 만들지 않습니다. 초대 링크·회원 정보는 게시하지 않습니다. 정책 초안과 사례 미등록 상태를 유지합니다.

## Exa로 찾은 디자인 스킬과 검수 참고 자료

2026-11-28 Exa 검색으로 아래 원문을 찾고 읽었습니다. 실행 스크립트나 외부 플러그인을 설치하지 않고 지침을 적용했습니다.

- [Anthropic Frontend Design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md): 주제에 맞는 시각 방향, 서체·여백·정보 계층, 반응형 화면 검토.
- [Vercel Web Interface Guidelines](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/references/command.md): 의미 있는 HTML, 포커스, 터치 영역, 앵커·모션·반응형 검수 참고.

현재 게시 방식은 GitHub Pages의 main 루트 정적 파일입니다. 변경은 PR과 Documents 검사를 거칩니다.
