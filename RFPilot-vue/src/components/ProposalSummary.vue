<template>
    <div class="max-w-4xl mx-auto p-6 space-y-8">
      <section>
        <h2 class="text-2xl font-bold mb-2">📄 제안서 요약</h2>
        <p class="bg-gray-100 p-4 rounded">{{ summary }}</p>
      </section>
  
      <section>
        <h2 class="text-2xl font-bold mb-2">🤖 AI 심사위원 목록</h2>
        <ul class="space-y-2">
          <li v-for="(reviewer, index) in reviewers" :key="index" class="bg-white p-3 shadow rounded">
            <strong>{{ reviewer.role }}</strong>: {{ reviewer.criteria }}
          </li>
        </ul>
      </section>
  
      <section>
        <h2 class="text-2xl font-bold mb-2">📊 제안 적합도 점수</h2>
        <ul class="grid grid-cols-2 gap-4">
          <li v-for="(score, key) in scores" :key="key" class="bg-blue-50 p-4 rounded shadow">
            <div class="font-semibold">{{ key }}</div>
            <div class="text-lg">{{ score }}점</div>
          </li>
        </ul>
      </section>
  
      <section>
        <h2 class="text-2xl font-bold mb-2">✨ 트렌드 기반 기능 제안</h2>
        <p class="bg-gray-100 p-4 rounded">{{ trendSuggestion }}</p>
      </section>
    </div>
  </template>
  
  <script setup>
  const summary = `이 제안서는 AI를 활용한 스마트 물류 시스템 구축 방안을 설명합니다. 기술 구성과 개발일정, 예산안이 포함되어 있습니다.`;
  
  const reviewers = [
    { role: '기술 전문가', criteria: 'AI 모델 구조의 실현 가능성과 기술력 검토' },
    { role: '사업 총괄', criteria: '일정과 예산의 현실성 평가' },
    { role: '시장 분석가', criteria: '목표 대비 시장 적합성 분석' },
  ];
  
  const scores = {
    기술: 82,
    일정: 90,
    예산: 78,
    목표: 85,
  };
  
  const trendSuggestion = `최근 정부과제의 기술 동향과 비교해, 자동화 물류 시스템 외에도 AI 기반 수요 예측 모듈을 추가하는 것이 경쟁력 확보에 도움이 됩니다.`;
  </script>
  
  <style scoped>
  ul {
    list-style: none;
    padding: 0;
  }
  </style>
  