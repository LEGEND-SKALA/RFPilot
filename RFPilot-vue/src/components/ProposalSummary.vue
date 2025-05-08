<template>
  <div class="result-container">
    
    <aside class="sidebar">
      <Header></Header>
      <div class="menu">
        <h3>다른 기능 해보기</h3>
        <ul>
          <li @click="goTo('prototype')">
            <span class="star">⭐</span>
            <div>
              <strong>프로토타입 생성</strong>
              <p>신청 양식에 대한 프로토타입을 생성합니다.</p>
            </div>
          </li>
          <li @click="goTo('evaluation')">
            <span class="star">⭐</span>
            <div>
              <strong>자료 적합도 평가</strong>
              <p>RFP에 해당하는 자료가 적합한지 평가받습니다.</p>
            </div>
          </li>
          <li @click="goTo('script')">
            <span class="star">⭐</span>
            <div>
              <strong>발표 스크립트 평가</strong>
              <p>발표 스크립트 파일을 업로드해 평가받습니다.</p>
            </div>
          </li>
          <li @click="goTo('voice')">
            <span class="star">⭐</span>
            <div>
              <strong>발표 음성 평가</strong>
              <p>자신의 발표 음성 파일을 업로드해 평가받습니다.</p>
            </div>
          </li>
          <li @click="goTo('')">
            <span class="star">⭐</span>
            <div>
              <strong>첫 화면으로 돌아가기</strong>
              <p>첫 업로드 화면으로 돌아갑니다.</p>
            </div>
          </li>
        </ul>
      </div>
    </aside>

    <!-- Main Content -->
    <section class="content">
      <h1>분석 결과</h1>

      <div class="block">
        <h4>제안서 요약</h4>
        <textarea readonly>어쩌구 저쩌구</textarea>
      </div>

      <div class="block">
        <h4>AI 심사위원 평가</h4>
        <img src="../assets/judges.png" alt="Judging Robots" class="judges" />
        <textarea readonly>어쩌구 저쩌구 하하하 짱</textarea>
      </div>

      <div class="block">
        <h4>트렌드 기반 기능 제안</h4>
        <textarea readonly>어쩌구 저쩌구</textarea>
      </div>
    </section>
  </div>
</template>

<script setup>
import Header from './common/Header.vue'
import { useRouter } from 'vue-router'
const router = useRouter()

const goTo = (target) => {
  router.push(`/${target}`)
}

</script>

<style scoped>
.result-container {
  display: flex;
  height: 100vh;
  font-family: 'Noto Sans KR', sans-serif;
}

.sidebar {
  width: 300px;
  padding: 30px;
  background-color: #f9fafb;
  border-right: 1px solid #ddd;
}

.logo {
  width: 140px;
  margin-bottom: 20px;
}

.menu h3 {
  margin-bottom: 16px;
  font-size: 18px;
  font-weight: bold;
}

.menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu li {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  cursor: pointer;
}

.menu li div {
  display: flex;
  flex-direction: column;
}

.menu li strong {
  font-size: 15px;
  font-weight: 600;
}

.menu li p {
  font-size: 13px;
  color: #666;
  margin: 4px 0 0;
}

.content {
  flex: 1;
  padding: 10px 60px;
}

.content h1 {
  font-size: 32px;
  margin-bottom: 32px;
  color: #1e2a39;
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
  padding-left: 50px;
  padding-right: 50px;
  justify-content: space-between;
  margin: 12px 0;
  width: 50%;
}
</style>
