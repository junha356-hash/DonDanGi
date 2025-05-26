<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">프로필 정보 수정</span>
    </h1>
  </section>
  <div class="container-content d-flex justify-content-center align-items-center">
    <main>
      <div class="py-5 text-center" id="errorContainer">
        <img class="d-block mx-auto mb-4" src="@/assets/logo.png" width="150" height="150">
        <h2 class="fw-bold mb-5" style="font-size: 50px;">프로필 수정</h2>
      </div>

      <div class="row g-5" style="margin-bottom: 100px; max-width: 1200px;">
        <div class="col-lg-12">
          <h4>프로필 정보 수정</h4>
          <div v-if="errormsg" class="row">
            <p class="text-danger mb-2" v-for="err in errormsg" :key="err">{{ err }}</p>
          </div>
          <hr>

          <form class="mt-5" @submit.prevent="saveProfile">
            <div class="row g-4 profile-info">
              <div class="col-md-6">
                <label for="age" class="form-label">나이<span class="text-muted"> (0~100)</span></label>
                <input type="number" class="form-control" id="age" v-model.number="age" required />
              </div>

              <div class="col-md-6">
                <label for="gender" class="form-label">성별</label>
                <select class="form-select" id="gender" v-model="gender" required>
                  <option value="">성별 선택</option>
                  <option value="M">남성</option>
                  <option value="F">여성</option>
                </select>
              </div>

              <div class="col-md-6">
                <label for="risk_profile" class="form-label">투자성향</label>
                <select class="form-select" id="risk_profile" v-model="risk_profile" required>
                  <option value="">선택</option>
                  <option value="aggressive">공격적</option>
                  <option value="balanced">균형적</option>
                  <option value="defensive">방어적</option>
                </select>
              </div>

              <div class="col-md-6">
                <label for="liquid_assets" class="form-label">유동자산 (만원)</label>
                <input type="number" class="form-control" id="liquid_assets" v-model.number="liquid_assets" required />
              </div>

              <div class="col-md-6">
                <label for="annual_income" class="form-label">연봉 (만원)</label>
                <input type="number" class="form-control" id="annual_income" v-model.number="annual_income" required />
              </div>
            </div>

            <hr class="my-5">

            <div class="text-center">
              <button class="w-50 btn btn-primary btn-lg fs-4 fw-bold" type="submit">
                {{ isEdit ? '정보 수정' : '작성 완료' }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </main>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const token = localStorage.getItem('token')
const PROFILE_URL = 'http://127.0.0.1:8000/api/v1/user/profile/me/'

const age = ref('')
const gender = ref('')
const risk_profile = ref('')
const liquid_assets = ref('')
const annual_income = ref('')
const isEdit = ref(false)
const errormsg = ref([])

onMounted(async () => {
  const res = await fetch(PROFILE_URL, {
    headers: { Authorization: `Token ${token}` }
  })
  if (res.ok) {
    const data = await res.json()
    age.value = data.age
    gender.value = data.gender
    risk_profile.value = data.risk_profile
    liquid_assets.value = data.liquid_assets
    annual_income.value = data.annual_income
    isEdit.value = true
  }
})

const saveProfile = async () => {
  const formData = new FormData()
  formData.append('age', age.value)
  formData.append('gender', gender.value)
  formData.append('risk_profile', risk_profile.value)
  formData.append('liquid_assets', liquid_assets.value)
  formData.append('annual_income', annual_income.value)

  const res = await fetch(PROFILE_URL, {
    method: 'PUT',
    headers: {
      Authorization: `Token ${token}`
    },
    body: formData
  })

  if (res.ok) {
    alert('프로필이 저장되었습니다!')
    router.push({ name: 'profile' })
  } else {
    const data = await res.json()
    errormsg.value = Object.values(data).flat()
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
  font-size: 1.25rem; /* 1.25rem = 약 20px */
}

.profile-info strong {
  font-weight: 600;
}
</style>