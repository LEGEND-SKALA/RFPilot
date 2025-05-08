<template>
  <div class="p-6">
    <h2 class="text-2xl font-bold mb-4">📊 자료적합도 평가</h2>
    <p class="mb-4 text-gray-700">
      업로드한 발표 자료를 기반으로, 제안서와의 연관성을 AI 심사위원이 평가합니다.
    </p>

    <div class="mb-4">
      <label class="block mb-2 font-semibold" for="presentationFile">발표 자료 업로드</label>
      <input type="file" id="presentationFile" @change="handleFileUpload" accept=".pdf,.pptx,.docx" />
    </div>

    <button
      class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
      :disabled="!presentationFile"
      @click="evaluateRelevance"
    >
      평가 시작
    </button>

    <div v-if="evaluationResult" class="mt-6 p-4 border rounded bg-gray-50">
      <h3 class="font-semibold mb-2">📄 평가 결과</h3>
      <ul class="list-disc ml-5 space-y-1 text-gray-800">
        <li v-for="(result, idx) in evaluationResult" :key="idx">{{ result }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const presentationFile = ref(null);
const evaluationResult = ref(null);

function handleFileUpload(event) {
  presentationFile.value = event.target.files[0];
}

function evaluateRelevance() {
  // 임시 결과 시뮬레이션
  evaluationResult.value = [
    '기술 항목 적합도: 85%',
    '일정 계획 일치도: 90%',
    '예산 계획 연관성: 78%',
    '전체 평가: 높은 관련성'
  ];
}
</script>