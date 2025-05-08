<template>
    <div class="p-6">
      <h2 class="text-2xl font-bold mb-4">📝 발표 스크립트 업로드</h2>
      <p class="mb-4 text-gray-700">
        발표 스크립트를 업로드하면, 구조적 분석(문제-해결-기대효과 등)을 기반으로 평가를 받을 수 있어요.
      </p>
  
      <div class="mb-4">
        <label class="block mb-2 font-semibold" for="scriptFile">스크립트 파일 업로드</label>
        <input type="file" id="scriptFile" @change="handleScriptUpload" accept=".txt,.docx" />
      </div>
  
      <button
        class="bg-indigo-500 text-white px-4 py-2 rounded hover:bg-indigo-600"
        :disabled="!scriptFile"
        @click="analyzeScript"
      >
        스크립트 평가 결과 보기
      </button>
  
      <div v-if="analysisResult" class="mt-6 p-4 border rounded bg-gray-50">
        <h3 class="font-semibold mb-2">📄 구조 분석 결과</h3>
        <ul class="list-disc ml-5 space-y-1 text-gray-800">
          <li>문제 제기: {{ analysisResult.problem }}</li>
          <li>해결 방안: {{ analysisResult.solution }}</li>
          <li>기대 효과: {{ analysisResult.impact }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const scriptFile = ref(null);
  const analysisResult = ref(null);
  
  function handleScriptUpload(event) {
    scriptFile.value = event.target.files[0];
  }
  
  function analyzeScript() {
    // 실제 분석 API 연동 시 이 부분을 수정
    analysisResult.value = {
      problem: '기존 제품 대비 기술적 한계 존재',
      solution: 'AI 기반 제안서 분석 자동화 도구 제시',
      impact: '평가 효율 향상 및 객관성 확보 가능'
    };
  }
  </script>