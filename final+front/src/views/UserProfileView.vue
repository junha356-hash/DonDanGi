<template>
  <section class="mb-5" style="position:relative;">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500" class="text-center fw-bold">
      <span class="brand-name">{{ profile?.username || '' }}님의 프로필</span>
    </h1>
  </section>

  <div class="container my-5">
    <div v-if="profile">
      <!-- 프로필 이미지 -->
      <div v-if="profile.image" class="text-center mb-4">
        <img :src="imageUrl(profile.image)" class="profile-img" alt="프로필 이미지" />
      </div>

      <!-- 프로필 정보 -->
      <div class="card p-4 shadow-sm profile-info">
        <h2 class="mb-4 text-center">{{ profile.username }}님의 정보</h2>
        <p>👤 <strong>나이:</strong> {{ profile.age }}세</p>
        <p>👫 <strong>성별:</strong> {{ profile.gender === 'M' ? '남성' : '여성' }}</p>
        <p>📊 <strong>투자성향:</strong>
          {{
            profile.risk_profile === 'aggressive' ? '공격적' :
              profile.risk_profile === 'balanced' ? '균형적' :
                profile.risk_profile === 'defensive' ? '방어적' : profile.risk_profile
          }}
        </p>
        <p>💰 <strong>유동자산:</strong> {{ profile.liquid_assets }}만원</p>
        <p>💼 <strong>연봉:</strong> {{ profile.annual_income }}만원</p>

        <div class="text-end mt-4">
          <button class="btn btn-primary" @click="goEdit">프로필 수정</button>
        </div>
      </div>
    </div>

    <!-- 프로필이 없는 경우 -->
    <div v-else class="text-center">
      <p class="mb-3">프로필 정보가 없습니다.</p>
      <button class="btn btn-success" @click="goEdit">프로필 작성</button>
    </div>
  </div>

<div v-if="userStore.depositList.length || userStore.savingList.length" class="mt-5">
  <div class="row">
    <!-- 상품 카드 (왼쪽) -->
    <div class="col-md-5 mb-4">
      <div class="card shadow-sm">
        <div class="card-body">
          <h4 class="card-title mb-4 fw-bold">
            <i class="bi bi-stars"></i> 내가 추가한 상품
          </h4>
          <!-- 예금 -->
          <div v-if="userStore.depositList.length" class="mb-4">
            <h5 class="fw-semibold text-primary mb-2">
              <i class="bi bi-piggy-bank"></i> 예금 <span class="fs-6 text-muted">(최대 3개 비교)</span>
            </h5>
            <ul class="list-group">
              <li v-for="item in userStore.depositList" :key="item.fin_prdt_cd"
                  class="list-group-item d-flex align-items-center justify-content-between border-0 px-0 py-2">
                <div class="form-check flex-grow-1">
                  <input type="checkbox"
                    class="form-check-input"
                    :checked="selectedProducts.includes(item)"
                    @change="handleCheck(item)"
                    :disabled="!selectedProducts.includes(item) && selectedProducts.length >= 3"
                    :id="'deposit-' + item.fin_prdt_cd"
                  >
                  <label class="form-check-label ms-2" :for="'deposit-' + item.fin_prdt_cd">
                    <span class="fw-semibold">{{ item.fin_prdt_nm }}</span>
                    <span class="text-secondary ms-1">({{ item.kor_co_nm }})</span>
                  </label>
                </div>
                <span class="badge bg-gradient text-bg-light text-danger fs-6 px-2">
                  {{ getBestDepositRate(item) !== null ? getBestDepositRate(item) + '%' : 'N/A' }}
                </span>
                  <button
                  class="btn btn-outline-danger btn-sm ms-2"
                  @click="removeProduct('deposit', item.fin_prdt_cd)"
                  title="내 목록에서 삭제"
                >
                  <i class="bi bi-x-circle"></i>
                </button>
              </li>
            </ul>
          </div>
          <!-- 적금 -->
          <div v-if="userStore.savingList.length">
            <h5 class="fw-semibold text-success mb-2">
              <i class="bi bi-cash-coin"></i> 적금 <span class="fs-6 text-muted">(최대 3개 비교)</span>
            </h5>
            <ul class="list-group">
              <li v-for="item in userStore.savingList" :key="item.fin_prdt_cd"
                  class="list-group-item d-flex align-items-center justify-content-between border-0 px-0 py-2">
                <div class="form-check flex-grow-1">
                  <input type="checkbox"
                    class="form-check-input"
                    :checked="selectedSavings.includes(item)"
                    @change="handleSavingCheck(item)"
                    :disabled="!selectedSavings.includes(item) && selectedSavings.length >= 3"
                    :id="'saving-' + item.fin_prdt_cd"
                  >
                  <label class="form-check-label ms-2" :for="'saving-' + item.fin_prdt_cd">
                    <span class="fw-semibold">{{ item.fin_prdt_nm }}</span>
                    <span class="text-secondary ms-1">({{ item.kor_co_nm }})</span>
                  </label>
                </div>
                <span class="badge bg-gradient text-bg-light text-danger fs-6 px-2">
                  {{ getBestSavingRate(item) !== null ? getBestSavingRate(item) + '%' : 'N/A' }}
                </span>
                  <button
                  class="btn btn-outline-danger btn-sm ms-2"
                  @click="removeProduct('saving', item.fin_prdt_cd)"
                  title="내 목록에서 삭제"
                >
                  <i class="bi bi-x-circle"></i>
                </button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
   
    <!-- 그래프 (오른쪽) -->
    <div class="col-md-7 d-flex flex-column align-items-center justify-content-center">
      <div v-if="selectedProducts.length >= 2" class="w-100 mb-4">
        <h3 style="text-align: center;">예금 금리 비교</h3>
        <BarGraph :products="selectedProducts" :getBestRate="getBestDepositRate" />
      </div>
      <hr>
      <div v-if="selectedSavings.length >= 2" class="w-100">
        <h3 style="text-align: center;">적금 금리 비교</h3>
        <BarGraph :products="selectedSavings" :getBestRate="getBestSavingRate" />
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import BarGraph from '@/components/BarGraph.vue' // BarGraph 컴포넌트 경로에 맞게 import!

const userStore = useUserStore()
const router = useRouter()
const profile = ref(null)
const selectedProducts = ref([])
const selectedSavings = ref([])

const imageUrl = (img) => {
  if (!img) return ''
  return `http://127.0.0.1:8000${img.startsWith('/') ? img : '/' + img}?v=${Date.now()}`
}

onMounted(async () => {
  const token = localStorage.getItem('token')
  const res = await fetch('http://127.0.0.1:8000/api/v1/user/profile/me/', {
    headers: { 'Authorization': `Token ${token}` }
  })
  if (res.ok) {
    profile.value = await res.json()
  }
  await userStore.fetchMyProducts()
})

const goEdit = () => {
  router.push({ name: 'profileSetup' })  // profileSetup 라우터 이름을 맞춰주세요!
}

const logout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('username')
  router.push({ name: 'MainPage' })
}

// 3개까지 체크 가능, 해제시 다시 선택 가능
const handleCheck = (product) => {
  if (selectedProducts.value.includes(product)) {
    selectedProducts.value = selectedProducts.value.filter(p => p !== product)
  } else {
    if (selectedProducts.value.length < 3) {
      selectedProducts.value.push(product)
    } else {
      alert("3개까지만 선택할 수 있습니다!")
    }
  }
}

const handleSavingCheck = (item) => {
  if (selectedSavings.value.includes(item)) {
    selectedSavings.value = selectedSavings.value.filter(p => p !== item)
  } else if (selectedSavings.value.length < 3) {
    selectedSavings.value.push(item)
  } else {
    alert("적금은 3개까지만 선택할 수 있습니다!")
  }
}

const getBestDepositRate = (item) => {
  if (!item.options || item.options.length === 0) return null
  return Math.max(...item.options.map(opt => opt.intr_rate ?? 0))
}

const getBestSavingRate = (item) => {
  if (!item.options || item.options.length === 0) return null
  return Math.max(...item.options.map(opt => opt.intr_rate ?? 0))
}

const removeProduct = async (type, fin_prdt_cd) => {
  await userStore.removeMyProduct(type, fin_prdt_cd)
  // 성공 후 새로고침(최신 상태 반영)
  await userStore.fetchMyProducts()
  // 혹시 체크 상태도 반영 원하면 선택 배열에서 제거
  if (type === 'deposit') {
    selectedProducts.value = selectedProducts.value.filter(p => p.fin_prdt_cd !== fin_prdt_cd)
  } else if (type === 'saving') {
    selectedSavings.value = selectedSavings.value.filter(p => p.fin_prdt_cd !== fin_prdt_cd)
  }
}

</script>

<style scoped>
.profile-img {
  width: 120px;
  height: 120px;
  object-fit: cover;
  border-radius: 50%;
  border: 3px solid #ddd;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.07);
  margin-bottom: 16px;
}
.profile-info p {
  font-size: 1.25rem;
}
.profile-info strong {
  font-weight: 600;
}
</style>
