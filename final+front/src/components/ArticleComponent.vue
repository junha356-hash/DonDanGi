<template>
  <div class="row justify-content-center">
    <!-- right -->
    <article class="container" data-aos="fade-left" data-aos-duration="700" data-aos-once="false"
      style="padding-top: 0px;">
      <div class="row justify-content-between">
        <div class="col-7">
          <RouterLink :to="{ name: 'product', params: { type: 'deposit', bank: 'shinhan', trm: '12' } }"
            class="text-decoration-none text-dark">
            <h1 class="my-3 fw-bold">예금/적금 비교</h1>
            <p>예적금 정보를 손쉽게 비교해 보세요!</p>
          </RouterLink>
          <br>
        </div>
        <div class="col-5" style="margin: auto 0;">
          <RouterLink :to="{ name: 'product', params: { type: 'deposit', bank: 'shinhan', trm: '12' } }">
            <img src="../assets/deposit_saving.webp" alt="deposit_saving_img" style="width:100%;">
          </RouterLink>
        </div>
      </div>
    </article>

    <!-- left -->
    <article class="container justify-content-start" data-aos="fade-left" data-aos-duration="700" data-aos-once="false">
      <div class="row justify-content-between">
        <div class="col-5" style="margin: auto 0;">
          <RouterLink :to="{ name: 'search' }">
            <img src="../assets/Video.jpg" alt="Video_img" style="width:100%;">
          </RouterLink>
        </div>
        <div class="col-6">
          <RouterLink :to="{ name: 'search' }" class="text-decoration-none text-dark">
            <h1 class="my-3 fw-bold">검색 기업 영상</h1>
            <p>검색한 기업의 정보를 찾아보세요!</p>
            <br>
          </RouterLink>
        </div>
      </div>
    </article>

    <!-- right -->
    <article class="container" data-aos="fade-left" data-aos-duration="700" data-aos-once="false"
      style="padding-top: 0px;">
      <div class="row justify-content-between">
        <div class="col-7">
          <RouterLink :to="{ name: 'exchange' }" class="text-decoration-none text-dark">
            <h1 class="my-3 fw-bold">국제 환율 계산</h1>
            <p>국제 환율을 손쉽게 알아보세요!</p>
          </RouterLink>
          <br>
        </div>
        <div class="col-5" style="margin: auto 0;">
          <RouterLink :to="{ name: 'exchange' }">
            <img src="../assets/exchange.jpg" alt="exchange_img" style="width:100%;">
          </RouterLink>
        </div>
      </div>
    </article>

    <!-- left -->
    <article class="container justify-content-start" data-aos="fade-left" data-aos-duration="700" data-aos-once="false">
      <div class="row justify-content-between">
        <div class="col-5" style="margin: auto 0;">
          <RouterLink :to="{ name: 'gold_silver' }">
            <img src="../assets/gold_silver.webp" alt="gold_silver_img" style="width:100%;">
          </RouterLink>
        </div>
        <div class="col-6">
          <RouterLink :to="{ name: 'gold_silver' }" class="text-decoration-none text-dark">
            <h1 class="my-3 fw-bold">국제 금/은 시세</h1>
            <p>국제 금/은의 시세를 한눈에 살펴보세요!</p>
            <br>
          </RouterLink>
        </div>
      </div>
    </article>

    <!-- right -->
    <article class="container" data-aos="fade-left" data-aos-duration="700" data-aos-once="false"
      style="padding-top: 0px;">
      <div class="row justify-content-between">
        <div class="col-7">
          <RouterLink :to="{ name: 'bank' }" class="text-decoration-none text-dark">
            <h1 class="my-3 fw-bold">주변 은행 찾기</h1>
            <p>내 주변의 은행을 쉽게 찾아보세요!</p>
          </RouterLink>
          <br>
        </div>
        <div class="col-5" style="margin: auto 0;">
          <RouterLink :to="{ name: 'bank' }">
            <img src="../assets/bank.webp" alt="bank_img" style="width:100%;">
          </RouterLink>
        </div>
      </div>
    </article>

    <!-- left -->
    <article class="container justify-content-start" data-aos="fade-left" data-aos-duration="700" data-aos-once="false">
      <div class="row justify-content-between">
        <div class="col-5" style="margin: auto 0;">
          <RouterLink :to="{ name: 'home' }">
            <img src="../assets/community.jpg" alt="community_img" style="width:100%;">
          </RouterLink>
        </div>
        <div class="col-6">
          <RouterLink :to="{ name: 'home' }" class="text-decoration-none text-dark">
            <h1 class="my-3 fw-bold">커뮤니티 바로가기</h1>
            <p>금융 관련 지식을 다른 사람들과 함께 나누세요!</p>
            <br>
          </RouterLink>
        </div>
      </div>
    </article>

    <!-- right -->
    <article class="container" data-aos="fade-left" data-aos-duration="700" data-aos-once="false"
      style="padding-top: 0px;">
      <div class="row justify-content-between">
        <div class="col-7">
          <RouterLink :to="{ name: 'recommend' }" class="text-decoration-none text-dark">
            <h1 class="my-3 fw-bold">AI 금융 상품 추천</h1>
            <p>AI가 제공하는 프로필, 목적 기반으로 사용자 맞춤 금융 상품 추천 기능을 체험해 보세요!</p>
          </RouterLink>
          <br>
        </div>
        <div class="col-5" style="margin: auto 0;">
          <RouterLink :to="{ name: 'recommend' }">
            <img src="../assets/recommend.jpg" alt="recommend_img" style="width:100%;">
          </RouterLink>
        </div>
      </div>
    </article>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
h1,
h2,
h3,
h4,
h5 {
  text-wrap: wrap;
}

article {
  height: 500px;
  min-width: 500px;
  max-width: 1200px;
  width: 100%;
  align-items: center;
  padding-top: 50px;
  padding-bottom: 50px;
  /* display: flex; */
  justify-content: space-between;
  margin-top: 50px;
  margin-bottom: 30px;
  overflow: visible;
  box-sizing: border-box
}

article img {
  width: 370px;
  max-width: 100%;
  height: 350px;
  object-fit: fill;
  border-radius: 40px;
}

.container-up {
  min-height: 750px;
  max-height: 800px;
  margin-top: 50px;
  margin-bottom: 0px;
  padding-bottom: 50px;
}

.container-up img {
  width: 100%;
  min-height: 100%;
  height: 400px;
  min-width: 100%;
  margin-top: 0px;
}

.container-up h1,
.container-up h2,
.container-up h5 {
  word-wrap: break-word;
}
</style>