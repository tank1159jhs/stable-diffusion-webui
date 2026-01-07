#!/bin/bash
# Realistic Vision V6.0 B1 모델 테스트

echo "🎨 Realistic Vision V6.0 B1 모델 테스트"
echo "========================================"
echo ""

# 1. SD WebUI 실행 확인
echo "1️⃣  SD WebUI 실행 확인..."
if curl -s http://127.0.0.1:7860/sdapi/v1/sd-models > /dev/null 2>&1; then
    echo "   ✅ SD WebUI 실행 중"
else
    echo "   ❌ SD WebUI가 실행되지 않았습니다!"
    echo "   터미널에서 실행: cd /Users/systemi/stable-diffusion-webui && ./webui.sh --api --listen --port 7860"
    exit 1
fi

# 2. 현재 로드된 모델 확인
echo ""
echo "2️⃣  현재 로드된 모델:"
curl -s http://127.0.0.1:7860/sdapi/v1/sd-models | python3 -c "
import sys, json
data = json.load(sys.stdin)
for model in data:
    print(f\"   📦 모델: {model['model_name']}\")
    print(f\"   📂 경로: {model['filename']}\")
"

# 3. 테스트 이미지 생성
echo ""
echo "3️⃣  테스트 이미지 생성 중..."
echo "   프롬프트: Japanese traditional street, Kyoto, photorealistic"

curl -s -X POST http://127.0.0.1:7860/sdapi/v1/txt2img \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Japanese traditional street, Kyoto style, old wooden buildings, stone pavement, morning light, photorealistic, 8k, highly detailed, no people",
    "negative_prompt": "anime, cartoon, illustration, 2D, drawn, people, person, face",
    "steps": 20,
    "sampler_name": "DPM++ 2M",
    "cfg_scale": 7.0,
    "width": 768,
    "height": 512,
    "seed": -1
  }' | python3 -c "
import sys, json, base64, os
data = json.load(sys.stdin)
if 'images' in data and data['images']:
    image_data = base64.b64decode(data['images'][0])
    output_path = '/Users/systemi/storymaker/output/test_realistic_vision.png'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as f:
        f.write(image_data)
    print(f'   ✅ 테스트 이미지 생성 완료!')
    print(f'   📂 저장 위치: {output_path}')
else:
    print('   ❌ 이미지 생성 실패')
    print(f'   응답: {data}')
"

echo ""
echo "========================================"
echo "✅ 테스트 완료!"
echo ""
echo "📝 다음 단계:"
echo "   1. /Users/systemi/storymaker/output/test_realistic_vision.png 이미지 확인"
echo "   2. 실사 일본 거리가 생성되었는지 확인"
echo "   3. Storymaker 실행: cd /Users/systemi/storymaker && streamlit run app.py"
