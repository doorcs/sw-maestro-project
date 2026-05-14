# soma17th-ai21-fe

AI·SW 마에스트로 17기 AI-21팀 프론트엔드입니다.  
AI 투자 어시스턴트 채팅 웹앱으로, 반도체·제약 섹터 분석과 투자 용어 설명 기능을 제공합니다.
백엔드 API 서버와 연동하여 동작하며, 단독으로는 실행되지 않습니다.

## 로컬 실행 절차

### 사전 준비

- Node.js 20 이상
- 백엔드 API 서버가 로컬에서 실행 중이어야 합니다 (`http://127.0.0.1:8000` 기본값)

### 설치 및 실행

```bash
# 1. 레포지토리 클론
git clone <repo-url>
cd soma17th-ai21-fe

# 2. 의존성 설치
npm install

# 3. 환경 변수 설정
cp .env.example .env
# .env 파일을 열어 VITE_API_BASE_URL을 백엔드 서버 주소로 설정

# 4. 개발 서버 실행
npm run dev
```

브라우저에서 `http://localhost:5173`으로 접속합니다.

### 환경 변수

| 변수명              | 설명                 | 기본값                  |
| ------------------- | -------------------- | ----------------------- |
| `VITE_API_BASE_URL` | 백엔드 API 서버 주소 | `http://127.0.0.1:8000` |

## Docker 빌드 및 실행 절차

### 사전 준비

- Docker 설치 필요

### 빌드

```bash
docker build -t soma17th-ai21 .
```

### 실행

```bash
docker run -p 3000:3000 soma17th-ai21
```

브라우저에서 `http://localhost:3000`으로 접속합니다.

백엔드 API 서버 주소를 지정하려면 환경 변수를 함께 전달합니다.

```bash
docker run -p 3000:3000 -e VITE_API_BASE_URL=http://<백엔드-주소>:8000 soma17th-ai21
```
