<template>
    <div class="result-container">
      <SidebarMenu />
  
      <section class="content">
        <h1 class="page-title">{{ title }}</h1>
  
        <div v-if="score !== null" class="score-box">
          <span>적합도 점수는</span>
          <strong class="score">{{ score }}점</strong>
          <span>입니다</span>
        </div>
  
        <div v-for="(section, index) in sections" :key="index" class="block">
          <h4>{{ section.label }}</h4>
          <img v-if="section.image" :src="section.image" class="section-image" />
          <textarea readonly :value="section.text" />
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  import SidebarMenu from './SidebarMenu.vue'
  
  const props = defineProps({
    title: String,
    score: Number,
    sections: {
      type: Array,
      default: () => [],
    },
  })
  </script>
  
  <style scoped>
  .result-container {
    display: flex;
    height: 100vh;
    font-family: 'Noto Sans KR', sans-serif;
  }
  
  .content {
    flex: 1;
    padding: 40px 60px;
  }
  
  .page-title {
    font-size: 32px;
    font-weight: 700;
    color: #1e2a39;
    margin-bottom: 24px;
  }
  
  .score-box {
    display: flex;
    align-items: baseline;
    gap: 8px;
    font-size: 18px;
    margin-bottom: 28px;
  }
  
  .score {
    font-size: 28px;
    font-weight: bold;
    color: #1e2a39;
  }
  
  .block {
    margin-bottom: 32px;
  }
  
  .block h4 {
    font-size: 16px;
    font-weight: 600;
    color: #1e2a39;
    margin-bottom: 12px;
  }
  
  textarea {
    width: 100%;
    height: 100px;
    padding: 14px;
    font-size: 14px;
    border: 1px solid #ddd;
    border-radius: 8px;
    resize: none;
  }
  
  .section-image {
    display: block;
    max-width: 200px;
    margin: 12px auto;
  }
  </style>