<template>
    <ResultView
      title="음성 분석 및 평가 결과"
      :score="85"
      :sections="[
        { label: '요약', text: '어쩌구 저쩌구' },
        { label: 'AI 심사위원 평가', image: '/assets/judges.png', text: '어쩌구 하하 짱' }
      ]"
    />
  </template>
  
  <script setup>
  import ResultView from '../components/common/ResultView.vue'
  </script>