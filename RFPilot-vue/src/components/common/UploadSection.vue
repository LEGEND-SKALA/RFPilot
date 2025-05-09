<template>
    <div class="container">
      <Header />
  
      <div class="header">
        <h1 class="title">{{ title }}</h1>
      </div>
  
      <p class="description">{{ description }}</p>
  
      <img src="../../assets/robot-basic.png" alt="AI Robot" class="robot" />
  
      <input
        type="file"
        ref="fileInput"
        @change="handleFileChange"
        style="display: none"
        :accept="accept"
      />
  
      <button class="upload-button" @click="triggerFileInput">
        <span>{{ uploadedFileName || "파일 업로드 하기" }}</span>
      </button>
  
      <button
        v-if="uploadedFileName"
        class="generate-button"
        @click="goToNext"
      >
        {{ actionText }}
      </button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import Header from './Header.vue'
  
  const props = defineProps({
    title: String,
    description: String,
    actionText: {
      type: String,
      default: '생성하기',
    },
    accept: {
      type: String,
      default: '.pdf,.doc,.docx,.hwp,.txt,.wav,.mp3',
    },
    nextRoute: {
      type: String,
      default: '/',
    },
    onProcess: Function
  })
  
  const fileInput = ref(null)
  const uploadedFileName = ref('')
  const router = useRouter()
  
  const triggerFileInput = () => {
    fileInput.value?.click()
  }
  
  const uploadedFile = ref(null)

  const handleFileChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      uploadedFile.value = file
      uploadedFileName.value = file.name
    }
  }

  const goToNext = async () => {
    if (props.onProcess && uploadedFile.value) {
      await props.onProcess(uploadedFile.value)
    }
  }
  </script>
  
  <style scoped>
  .container {
    text-align: center;
    padding: 60px 20px;
    background-color: #ffffff;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .header {
    margin-top: 20px;
    margin-bottom: 12px;
  }
  
  .title {
    font-size: 1.8rem;
    font-weight: bold;
    color: #1e2a39;
  }
  
  .description {
    margin-top: 16px;
    font-size: 1rem;
    color: #333;
    line-height: 1.6;
    max-width: 480px;
  }
  
  .robot {
    width: 200px;
    margin: 40px 0;
  }
  
  .upload-button {
    background-color: #1e2a39;
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1rem;
    margin-bottom: 20px;
  }
  
  .generate-button {
    background-color: #f4f4f4;
    color: #1e2a39;
    padding: 12px 24px;
    border: 1px solid #ccc;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.2s ease;
  }
  
  .generate-button:hover {
    background-color: #e0e0e0;
  }
  </style>