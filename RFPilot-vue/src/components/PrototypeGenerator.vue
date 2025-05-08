<template>
  <div class="container">
    <Header />
    <div class="header">
      <!-- <img src="../assets/logo.png" alt="RFPilot Logo" class="logo" /> -->
      <h1 class="title">프로토 타입 생성하기</h1>
    </div>

    <p class="description">
      업로드된 파일의 양식에 맞게 프로토 타입을 생성해드릴게요!
    </p>

    <img src="../assets/robot-basic.png" alt="AI Robot" class="robot" />

    <input
        type="file"
        ref="fileInput"
        @change="handleFileChange"
        style="display: none"
        accept=".pdf,.doc,.docx,.hwp"
      />

      <!-- 업로드 버튼 -->
      <button class="upload-button" @click="triggerFileInput">
        <span>{{ uploadedFileName || "파일 업로드 하기" }}</span>
      </button>

      <!-- 생성하기 버튼: 파일이 업로드된 경우에만 표시 -->
      <button
        v-if="uploadedFileName"
        class="generate-button"
        @click="goToSummary"
      >
        생성하기
      </button>
  </div>
</template>

<script setup>
import Header from './common/Header.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const fileInput = ref(null)
const uploadedFileName = ref('')
const router = useRouter()

const triggerFileInput = () => {
  fileInput.value?.click()
}

const handleFileChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    uploadedFileName.value = file.name
  }
}

const goToSummary = () => {
  router.push('/') // 반드시 라우터에 이 경로 등록되어 있어야 함
}
</script>

<style scoped>
.container {
  text-align: center;
  padding: 60px 20px;
  background-color: #ffffff;
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}

.logo {
  width: 120px;
}

.title {
  font-size: 1.8rem;
  font-weight: bold;
  color: #1e2a39;
}

.description {
  margin-top: 24px;
  font-size: 1rem;
  color: #333;
}

.robot {
  width: 180px;
  margin: 40px auto;
  display: block;
}

.upload-button {
  background-color: #1e2a39;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
  margin-bottom: 40px;
}
</style>
