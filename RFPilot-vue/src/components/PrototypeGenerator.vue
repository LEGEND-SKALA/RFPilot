<template>
    <div class="container mx-auto p-4">
      <h2 class="text-2xl font-bold mb-4">신청 양식 프로토타입 생성</h2>
      <p class="mb-4 text-gray-700">
        제안서 내용을 바탕으로 신청 양식에 맞춘 작성 가이드를 생성합니다.
      </p>
      <div class="bg-white p-6 rounded shadow">
        <p class="mb-2">기반 제안서: {{ fileName }}</p>
        <button
          @click="generatePrototype"
          class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          생성
        </button>
  
        <div v-if="prototype" class="mt-6">
          <h3 class="text-xl font-semibold mb-2">생성된 프로토타입</h3>
          <pre class="bg-gray-100 p-4 rounded overflow-x-auto">{{ prototype }}</pre>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const fileName = 'uploaded_proposal.pdf'; // 실제 로직에서는 props 또는 store에서 받아올 수 있음
  const prototype = ref('');
  
  const generatePrototype = async () => {
    // TODO: 실제 API 호출로 대체 필요
    prototype.value = `1. 사업 목적
  - ...
  
  2. 추진 일정
  - ...
  
  3. 예산 계획
  - ...`;
  };
  </script>
  
  <style scoped>
  pre {
    white-space: pre-wrap;
    word-wrap: break-word;
  }
  </style>
  