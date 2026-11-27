# AMC Website

AMC의 공개 홈페이지입니다. `main`의 루트 정적 파일을 GitHub Pages로 게시합니다.

URL: https://ai-makers-community.github.io/website/

빌드 의존성·외부 폰트·분석 도구·회원 데이터 수집이 없습니다. `.nojekyll`로 정적 HTML을 제공합니다. 문서 검사는 기본 Linux 실행기와 읽기 전용 토큰을 사용합니다.

변경은 PR로 제출하고 공개 동의·권리·개인정보·링크를 확인한 뒤 병합합니다. 행사 일정·신청·연락처는 실제 확정 전 만들지 않습니다. 사례는 개별 공개 승인 후 추가합니다. 커스텀 도메인과 AWS 로고를 사용하지 않습니다.

## 커밋 개인정보 보호

커밋 작성자와 committer는 GitHub noreply 이메일을 사용합니다. 웹 편집·자동 초기화는 이메일 노출 여부를 먼저 확인합니다. CLI squash 병합 시 `gh pr merge --squash --author-email 3435720+serithemage@users.noreply.github.com`을 사용하고 병합 후 메타데이터를 검증합니다. 문서 검사는 전체 가져온 이력의 이메일도 확인합니다.
