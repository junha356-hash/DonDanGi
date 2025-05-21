<template>
    <div class="row justify-content-center">
        <!-- left -->
        <article class="container" data-aos="fade-left" data-aos-duration="700" data-aos-once="false" style="padding-top: 0px;">
          <div class="row">
            <div class="col">
              <h2 class="fw-bold">예적금 들어갈곳</h2>
            </div>
          </div>
        </article>

        <!-- left -->
        <article class="container justify-content-start"
        data-aos="fade-left" data-aos-duration="700" data-aos-once="false"
        >
        <div class="row justify-content-between">
          <div class="col-5" style="margin: auto 0;">
            <RouterLink :to="{ name: 'bank' }">
              <img src="../assets/bank.webp" alt="bank_img" style="width:100%;">
            </RouterLink>
          </div>
          <div class="col-6">
            <RouterLink :to="{ name: 'bank' }" class="text-decoration-none text-dark">
              <h1 class="my-3 fw-bold">주변 은행 찾기 서비스</h1>
              <p>내 위치 주변의 은행을 찾아보세요!</p>
              <br>
            </RouterLink>
          </div>
        </div>
        </article>
        
        <!-- left -->
        <article class="container" data-aos="fade-left" data-aos-duration="700" data-aos-once="false" style="padding-top: 0px;">
            <div class="row justify-content-between">
                <div class="col-7">
                  <RouterLink :to="{ name: 'gold_silver'}" class="text-decoration-none text-dark">
                    <h1 class="my-3 fw-bold">국제 금/은 시세 확인 서비스</h1>
                    <p>국제 금/은 시세를 확인해 보세요!</p>
                  </RouterLink>
                  <br>
                </div>
                <div class="col-5" style="margin: auto 0;">
                  <RouterLink :to="{ name: 'gold_silver'}">
                    <img src="../assets/gold_silver.webp" alt="gold_silver_img" style="width:100%;">
                  </RouterLink>
                </div>
            </div>
        </article>
        
        <!-- right -->
        <article class="container justify-content-start"
        data-aos="fade-right" data-aos-duration="700" data-aos-once="false"
        >
          <div class="row">
            <div class="col">
              <h2 class="fw-bold">커뮤니티 들어갈곳</h2>
            </div>
          </div>
        </article>

    </div>
</template>

<script setup>
</script>

<style scoped>
    h1, h2, h3, h4, h5 {
        text-wrap: wrap;
    }
    article {
        height: 500px;
        min-width:500px;
        max-width:1200px;
        width:100%;
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
        min-width:100%;
        margin-top: 0px;
    }
    .container-up h1,
    .container-up h2,
    .container-up h5 {
        word-wrap: break-word;
    }

    
</style>