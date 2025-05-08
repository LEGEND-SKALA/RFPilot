<!-- src/components/common/ResultSection.vue -->
<template>
    <div class="result-block">
      <h4 class="title">{{ title }}</h4>
      <img v-if="image" :src="image" alt="Related visual" class="image" />
      <textarea readonly class="content">{{ content }}</textarea>
    </div>
  </template>
  
  <script setup>
  defineProps({
    title: String,
    content: String,
    image: String, // optional
  })
  </script>
  
  <style scoped>
  .result-block {
    margin-bottom: 32px;
  }
  
  .title {
    font-size: 16px;
    margin-bottom: 12px;
    color: #1e2a39;
  }
  
  .image {
    width: 60%;
    margin: 12px auto;
    display: block;
  }
  
  .content {
    width: 100%;
    height: 100px;
    padding: 14px;
    font-size: 14px;
    border: 1px solid #ddd;
    border-radius: 8px;
    resize: none;
  }
  </style>