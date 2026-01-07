# 실사 모델 다운로드 가이드 (일본 배경/사물/풍경 특화) 🗾

## 🎯 현재 문제
- **japaneseDollLikeness** 모델은 애니메이션/일러스트 전용입니다
- **일본 거리, 건물, 전통 건축물, 자연 풍경, 실내 사물** 등 실사 배경 이미지를 원하시면 실사 전용 모델이 필요합니다
- 🎬 스토리 동영상에는 **배경과 사물**이 가장 중요합니다 (얼굴/인물 불필요)

## 📥 추천 실사 모델 (배경/사물/풍경 특화) 🏯

### 1. Realistic Vision V5.1 (가장 추천!) ⭐⭐⭐⭐⭐
- **다운로드 링크**: https://civitai.com/models/4201/realistic-vision-v51
- **크기**: ~2.1GB (pruned 버전 추천)
- **특징**: 
  - ✅ **배경/풍경/사물 사진 품질 최고** (일본 장면 완벽)
  - ✅ 일본 거리, 신사, 전통 건축물, 자연 풍경 모두 뛰어남
  - ✅ 일본 전통 사물 (제등, 돌등, 도리이, 다다미, 쇼지문 등)
  - ✅ 키워드만 입력해도 사실적인 배경 생성
  - ✅ **사람 없는 풍경 완벽** (스토리 배경에 최적)
  - ✅ 빠른 생성 속도, macOS/MPS 지원 우수
- **다운로드 파일명**: `realisticVisionV51_v51VAE.safetensors` 또는 `realisticVisionV60B1_v51VAE.safetensors`
- **예시 프롬프트**: 
  - "Japanese traditional street, Kyoto, old wooden buildings, stone pavement"
  - "Japanese shrine interior, tatami floor, shoji screen, natural light"
  - "Japanese countryside, rice fields, mountains, sunset"
  - "Traditional Japanese room, kotatsu, tea set, window view"

### 2. Deliberate V2 (시네마틱 배경/분위기) ⭐⭐⭐⭐⭐
- **다운로드 링크**: https://civitai.com/models/4823/deliberate
- **크기**: ~2.1GB
- **특징**: 
  - ✅ **영화 같은 분위기의 배경** (스토리텔링 최적)
  - ✅ 드라마틱한 조명, 안개, 비, 계절감 표현 우수
  - ✅ 감정 전달에 최적화된 풍경 (슬픔, 기쁨, 향수 등)
  - ✅ 일본 전통 분위기 (시대극, 역사물)
  - ✅ **macOS에서도 빠른 생성**
- **다운로드 파일명**: `deliberate_v2.safetensors`
- **예시 프롬프트**:
  - "Japanese temple in morning fog, cinematic lighting, peaceful"
  - "Old Japanese village, dramatic sunset, nostalgic atmosphere"
  - "Rain falling on traditional Japanese roof, cinematic, melancholic"

### 3. DreamShaper 8 (다목적 실사) ⭐⭐⭐⭐
- **다운로드 링크**: https://civitai.com/models/4384/dreamshaper
- **크기**: ~2GB
- **특징**: 
  - ✅ 배경/사물 모두 우수, **가장 빠른 생성 속도**
  - ✅ 일본 현대/전통 장면 모두 잘 표현
  - ✅ 실내 사물 (가구, 소품) 디테일 좋음
  - ✅ macOS 최적화 우수
- **다운로드 파일명**: `dreamshaper_8.safetensors`
- **예시**: "Japanese living room, modern minimalist, window, plants"

### 4. SDXL Base 1.0 (초고해상도, 고급 사용자용) ⭐⭐⭐⭐
- **다운로드 링크**: https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0
- **크기**: ~6.9GB
- **특징**: 
  - ✅ SDXL (차세대 모델) - **해상도 최고** (1024x1024)
  - ✅ 건축물 디테일, 나무결, 돌 질감 등 초정밀
  - ⚠️ **생성 속도 느림** (macOS에서 2-3배 시간)
  - ⚠️ VRAM/메모리 많이 사용
- **다운로드 파일명**: `sd_xl_base_1.0.safetensors`
- **추천**: 고사양 Mac 또는 최종 고품질 출력용

## 📂 설치 방법

1. **모델 파일 다운로드**
   - 위 링크에서 `.safetensors` 파일 다운로드
   - **추천**: Realistic Vision V5.1 (배경 품질 최고)

2. **파일 이동**
   ```bash
   # 다운로드한 파일을 SD WebUI 모델 폴더로 이동
   mv ~/Downloads/realisticVisionV51_v51VAE.safetensors \
      /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/
   ```

3. **현재 모델 폴더 확인**
   ```bash
   ls -lh /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/
   ```

## 🗾 일본 배경/사물 프롬프트 예시 (얼굴 없음)

### 🏘️ 전통 거리/마을
```
Japanese traditional street, Kyoto style, old wooden buildings, stone pavement, 
lanterns, morning light, photorealistic, 8k, highly detailed, no people
```
```
Old Japanese village, traditional houses, narrow alley, stone walls, 
peaceful atmosphere, golden hour, realistic photography
```

### 🏯 신사/사찰/건축물
```
Japanese shrine, torii gate, stone lanterns, autumn leaves, 
moss-covered stones, peaceful atmosphere, natural lighting, photorealistic
```
```
Buddhist temple interior, wooden pillars, tatami floor, shoji screen, 
incense smoke, soft light, traditional architecture, highly detailed
```
```
Japanese castle, traditional architecture, stone walls, moat, 
blue sky, clouds, landscape photography, 8k
```

### 🌸 자연 풍경 (계절별)
```
# 봄 (벚꽃)
Japanese cherry blossom trees, sakura petals falling, traditional path, 
spring season, pink flowers, peaceful, photorealistic

# 여름 (논밭)
Japanese rice fields, summer, green paddy, mountains in background, 
blue sky, rural landscape, realistic photography

# 가을 (단풍)
Japanese autumn forest, red and orange maple leaves, traditional bridge, 
peaceful stream, fall colors, cinematic lighting

# 겨울 (설경)
Japanese village in snow, traditional houses with snow-covered roofs, 
winter landscape, cold atmosphere, white scenery, realistic
```

### 🌃 도시 풍경
```
Tokyo street at night, neon signs, rain reflections on pavement, 
urban landscape, city lights, cinematic lighting, photorealistic, detailed
```
```
Japanese convenience store exterior, night, vending machines, 
street lights, urban scene, realistic photography
```

### 🏠 실내 사물/배경
```
Traditional Japanese room, tatami floor, shoji screen, sliding door, 
natural light through window, minimalist interior, photorealistic
```
```
Japanese tea ceremony room, matcha bowl, bamboo whisk, wooden table, 
traditional atmosphere, soft lighting, highly detailed objects
```
```
Japanese izakaya interior, wooden counter, sake bottles, lanterns, 
warm lighting, cozy atmosphere, realistic, no people
```

### 🎋 전통 사물 (클로즈업)
```
Japanese stone lantern, moss-covered, garden setting, 
detailed texture, natural lighting, macro photography, 8k
```
```
Japanese paper lantern (chochin), red and white, traditional design, 
hanging, soft glow, night scene, photorealistic
```
```
Traditional Japanese tea set, ceramic cups, teapot, wooden tray, 
tatami background, soft natural light, product photography
```

### 🌊 자연 배경
```
Japanese beach at sunset, torii gate in water, orange sky, 
peaceful ocean, dramatic lighting, landscape photography
```
```
Japanese mountain range, misty morning, forest, hiking trail, 
nature landscape, realistic, atmospheric
```

### 🎎 문화 사물
```
Japanese daruma doll, red, traditional decoration, 
wooden shelf, soft lighting, product shot, highly detailed
```
```
Japanese folding fan (sensu), traditional pattern, 
elegant design, close-up, artistic lighting, 8k
```

## 💡 프롬프트 작성 팁 (배경/사물 최적화)

### ✅ 추가하면 좋은 키워드
- **품질 향상**: `photorealistic`, `8k`, `highly detailed`, `realistic photography`
- **사람 제거**: `no people`, `empty`, `uninhabited`, `deserted`
- **조명 효과**: `natural lighting`, `golden hour`, `soft light`, `dramatic lighting`
- **분위기**: `peaceful`, `nostalgic`, `cinematic`, `atmospheric`
- **시점**: `landscape photography`, `architectural photography`, `product shot`

### ❌ 피해야 할 키워드
- 사람 관련: `person`, `people`, `face`, `portrait`, `character`
- 애니메이션 관련: `anime`, `cartoon`, `illustration`, `2D`
- 저품질: `low quality`, `blurry`, `pixelated`

## ⚙️ Storymaker 설정 변경 (자동 전환)

모델을 다운로드한 후, `modules/sd_models.py`를 수정하여 스타일별로 다른 모델을 사용하도록 설정할 수 있습니다.

### 예시: 스타일별 모델 자동 선택 (배경 특화)
```python
# 스타일별 모델 매핑 (배경/풍경 최적화)
STYLE_MODEL_MAP = {
    "realistic": "realisticVisionV51_v51VAE.safetensors",      # 일반 실사 배경
    "cinematic": "deliberate_v2.safetensors",                  # 영화 같은 배경
    "anime": "japaneseDollLikeness.safetensors",               # 애니메이션 배경
    "semi-realistic": "dreamshaper_8.safetensors"              # 중간 스타일
}
```

## 🎨 사용 예시 (일본 배경)

### Before (japaneseDollLikeness 모델)
```
대본: "京都の古い街並み" (교토의 오래된 거리)
스타일: realistic
→ 애니메이션 스타일 배경 생성 ❌
```

### After (Realistic Vision V5.1 모델)
```
대본: "京都の古い街並み" (교토의 오래된 거리)
스타일: realistic
→ 실사 일본 거리 사진 생성 ✅
```

## 🎬 실전 예시: 스토리 동영상

**씬 1**: 老人の記憶 (노인의 기억)
- 대본: "昔々、京都の小さな村に住んでいた"
- 배경: 교토 전통 마을 풍경 (Realistic Vision V5.1)
- 결과: 실사 일본 전통 마을 ✅

**씬 2**: 桜の季節 (벚꽃 계절)
- 대본: "春になると、桜が満開になりました"
- 배경: 벚꽃 거리 풍경
- 결과: 실사 벚꽃 사진 ✅

**씬 3**: 夕暮れの海 (황혼의 바다)
- 대본: "夕方、海辺を歩いていました"
- 배경: 일본 해변 석양
- 결과: 시네마틱 바다 풍경 ✅

## ⚠️ 주의사항

- 각 모델 파일은 **5GB 내외**입니다 (저장 공간 확인)
- **첫 실행 시 로딩 시간**이 오래 걸릴 수 있습니다 (1-2분)
- **macOS/MPS** 환경에서는 약간 느릴 수 있습니다

## 🚀 빠른 시작 (Realistic Vision V5.1)

```bash
# 1. CivitAI에서 다운로드 (브라우저)
# https://civitai.com/models/4201/realistic-vision-v51

# 2. 파일 이동
cd ~/Downloads
mv realisticVisionV51_v51VAE.safetensors \
   /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/

# 3. 확인
ls -lh /Users/systemi/stable-diffusion-webui/models/Stable-diffusion/

# 4. SD WebUI 재시작 (터미널에서)
cd /Users/systemi/stable-diffusion-webui
./webui.sh --port 7861
```

## 📞 문제 해결

- **다운로드 링크 안 열림**: CivitAI 회원가입 필요 (무료)
- **파일 크기 큼**: 용량 부족 시 1개만 다운로드
- **로딩 느림**: 정상 (macOS는 CUDA보다 느림)
