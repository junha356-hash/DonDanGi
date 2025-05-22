<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/community.jpg" alt="community_img" data-aos="zoom-out" data-aos-duration="800">
    <h1 data-aos="fade-down" data-aos-duration="1500">
      <span class="brand-name">프로필 수정</span>
    </h1>
  </section>
  <form @submit.prevent="saveProfile" enctype="multipart/form-data">
    <div style="margin-bottom: 16px;">
      <div v-if="previewUrl">
        <img :src="previewUrl" class="profile-img" alt="프로필 이미지 미리보기" />
      </div>
      <input type="file" accept="image/*" @change="onFileChange" />
    </div>
    <input v-model.number="age" type="number" placeholder="나이" required />
    <select v-model="gender" required>
      <option value="">성별 선택</option>
      <option value="M">남성</option>
      <option value="F">여성</option>
    </select>
    <select v-model="risk_profile" required>
      <option value="">투자성향 선택</option>
      <option value="aggressive">공격적</option>
      <option value="defensive">방어적</option>
      <option value="balanced">균형적</option>
    </select>
    <input v-model.number="liquid_assets" type="number" placeholder="유동자산(만원)" required />
    <input v-model.number="annual_income" type="number" placeholder="연봉(만원)" required />
    <button type="submit">{{ isEdit ? '수정' : '작성' }}</button>
  </form>

</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const image = ref(null)
const previewUrl = ref('')
const router = useRouter()
const userId = localStorage.getItem('user_pk')
const token = localStorage.getItem('token')

const age = ref('')
const gender = ref('')
const risk_profile = ref('')
const liquid_assets = ref('')
const annual_income = ref('')
const isEdit = ref(false)
const PROFILE_URL = 'http://127.0.0.1:8000/api/v1/user/profile/me/';

onMounted(async () => {
  const res = await fetch(PROFILE_URL, {
    headers: { 'Authorization': `Token ${token}` }
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

const onFileChange = (e) => {
  const file = e.target.files[0]
  image.value = file
  if (file) {
    previewUrl.value = URL.createObjectURL(file)
  }
}

const saveProfile = async () => {
  // 이미지 등 포함 시엔 FormData로!
  const formData = new FormData()
  formData.append('age', age.value)
  formData.append('gender', gender.value)
  formData.append('risk_profile', risk_profile.value)
  formData.append('liquid_assets', liquid_assets.value)
  formData.append('annual_income', annual_income.value)
  if (image.value) formData.append('image', image.value)

  const res = await fetch(PROFILE_URL, {
    method: 'PUT',
    headers: {
      'Authorization': `Token ${token}`
      // 'Content-Type'은 FormData일 때 직접 쓰지 않음!
    },
    body: formData
  })
  if (res.ok) {
    alert('프로필이 저장되었습니다!')
    router.push({ name: 'profile' })
  } else {
    alert('저장 실패!')
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
</style>