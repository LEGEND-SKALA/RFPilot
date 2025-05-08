<template>
    <div class="p-6">
      <h2 class="text-2xl font-bold mb-4">🎤 발표 음성 업로드</h2>
      <p class="mb-4 text-gray-700">
        발표 음성 파일을 업로드하면, 텍스트로 변환한 뒤 AI 심사위원의 반응을 시뮬레이션해드려요.
      </p>
  
      <div class="mb-4">
        <label class="block mb-2 font-semibold" for="voiceFile">음성 파일 업로드</label>
        <input type="file" id="voiceFile" @change="handleFileUpload" accept=".mp3,.wav" />
      </div>
  
      <button
        class="bg-purple-500 text-white px-4 py-2 rounded hover:bg-purple-600"
        :disabled="!voiceFile"
        @click="analyzeVoice"
      >
        심사위원 반응 시뮬레이션 출력
      </button>
  
      <div v-if="transcribedText" class="mt-6 p-4 border rounded bg-gray-50">
        <h3 class="font-semibold mb-2">📝 음성 텍스트화 결과</h3>
        <p class="text-gray-800 whitespace-pre-wrap">{{ transcribedText }}</p>
      </div>
  
      <div v-if="simulatedFeedback.length" class="mt-6 p-4 border rounded bg-gray-100">
        <h3 class="font-semibold mb-2">🤖 AI 심사위원 반응</h3>
        <ul class="list-disc ml-5 space-y-2 text-gray-800">
          <li v-for="(feedback, index) in simulatedFeedback" :key="index">
            {{ feedback }}
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const voiceFile = ref(null);
  const transcribedText = ref('');
  const simulatedFeedback = ref([]);
  
  function handleFileUpload(event) {
    voiceFile.value = event.target.files[0];
  }
  
  function analyzeVoice() {
    // 실제 whisper API 호출 및 분석은 백엔드 연동 필요
    transcribedText.value = `안녕하세요. 오늘 발표할 주제는 AI 기반 제안서 평가 시스템입니다. 먼저 문제점부터 설명드리겠습니다...`;
  
    simulatedFeedback.value = [
      '심사위원 1: 도입부가 명확해서 좋았습니다.',
      '심사위원 2: 핵심 기술 설명 부분에서 구체적인 사례가 부족했습니다.',
      '심사위원 3: 전체적으로 논리적인 흐름이 잘 구성되었습니다.'
    ];
  }
  </script>