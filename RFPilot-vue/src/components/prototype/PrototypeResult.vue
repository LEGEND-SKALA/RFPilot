<!-- PrototypeResult.vue -->
<template>
    <div class="result-container">
      <SidebarMenu />
  
      <section class="content">
        <h1>프로토타입</h1>
  
        <button class="download-button">생성된 프로토타입 파일 다운로드</button>
  
        <div class="block">
          <h4>요약</h4>
          <textarea readonly>어쩌구 저쩌구</textarea>
        </div>
  
        <div class="block">
          <h4>AI 심사위원 평가</h4>
          <img src="../assets/judges.png" alt="Judging Robots" class="judges" />
          <textarea readonly>어쩌구 저쩌구 하하하 짱</textarea>
        </div>
      </section>
    </div>
  </template>
  
  <script setup>
  import SidebarMenu from './common/SidebarMenu.vue'
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
  
  .content h1 {
    font-size: 28px;
    margin-bottom: 24px;
    color: #1e2a39;
  }
  
  .download-button {
    background-color: #1e2a39;
    color: white;
    padding: 10px 18px;
    border: none;
    border-radius: 8px;
    margin-bottom: 32px;
    font-size: 0.95rem;
    cursor: pointer;
  }
  
  .block {
    margin-bottom: 32px;
  }
  
  .block h4 {
    font-size: 16px;
    margin-bottom: 12px;
    color: #1e2a39;
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
  
  .judges {
    margin: 12px 0;
    width: 200px;
  }
  </style>