// UploadProposal.vue
<template>
  <div class="upload-proposal">
    <h2>제안서 업로드</h2>
    <form @submit.prevent="handleSubmit">
      <div>
        <label>기업명:</label>
        <input v-model="company" required />
      </div>
      <div>
        <label>서비스 설명:</label>
        <textarea v-model="description" required></textarea>
      </div>
      <div>
        <label>제안서 파일 업로드:</label>
        <input type="file" @change="handleFileChange" accept=".pdf,.docx,.hwp" required />
      </div>
      <div>
        <label>심사위원 수 선택:</label>
        <select v-model="panelCount">
          <option v-for="n in 3" :key="n" :value="n">{{ n }}명</option>
        </select>
      </div>
      <button type="submit">제안서 분석 시작</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const company = ref('');
const description = ref('');
const file = ref(null);
const panelCount = ref(1);

const handleFileChange = (e) => {
  file.value = e.target.files[0];
};

const handleSubmit = () => {
  if (!file.value) return alert('파일을 업로드해주세요.');

  // TODO: 파일 업로드 및 분석 요청 처리
  console.log({ company: company.value, description: description.value, file: file.value, panelCount: panelCount.value });

  // 분석 후 요약 페이지로 이동
  router.push('/summary');
};
</script>

<style scoped>
.upload-proposal {
  max-width: 600px;
  margin: auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>