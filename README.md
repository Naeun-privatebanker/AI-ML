# Private Banker, Naeun AI/ML

나만의 은행원, 나은 AI/ML 소스코드

## About Naeun

Naeun is an AI banker service to prevent the elderly from being victimized by mis-selling and help them respond after the fact.<br>
To prevent financial damage to the elderly due to mis-selling, the service strengthens the crisis management capabilities of elderly consumers through financial technology specialized for the elderly.
<br><br>
나은(Naeun)은 불완전판매로 인한 고령층의 피해를 사전 방지하고 사후 대응을 돕기 위한 AI 은행원 서비스입니다. <br>
불완전판매로 인한 고령층의 금융피해를 방지하기 위해 노인 전용 금융 기술을 통해 고령소비자의 위기관리 능력을 강화합니다.

## Tech Architecture

![Tech Stack](https://github.com/Naeun-privatebanker/AI-ML/assets/68212300/f3349510-2aac-4de2-8ca7-1794d07a1460)

## How to Run on Local

로컬에서 작동시키는 방법

#### 1. Clone this Repository

```bash
git clone https://github.com/Naeun-privatebanker/AI-ML
```

#### 2. Create `settings.py` file and add `file1.pdf` on `AI-ML/env`

```python
CONFIG_GLOBAL = {
    'google-api-key': {YOUR_GEMINI_API_KEY},
}

CONFIG_DESC = {
    'prompt': {GEMINI_PROMPT_FOR_DESC}
}

CONFIG_CAUTION = {
    'prompt': {GEMINI_PROMPT_FOR_CAUTION}
}
```

- The pdf file is a prospectus from [DART](https://dart.fss.or.kr/)

#### 3. Install packages required

```bash
pip install -r requirements.txt
```

#### 4. Move to `/AI-ML` and Run the app

```bash
uvicorn main:app --port 8000 --reload
```
