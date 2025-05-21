<template>
    <section style="position:relative;" class="mb-5">
        <img src="@/assets/deposit_saving.webp" alt="main_img" data-aos="zoom-out" data-aos-duration="600">
        <h1 data-aos="fade-down" data-aos-duration="1500">예금/적금 비교</h1>
    </section>

    <div class="container-content" style="min-width: 1400px; min-height: 800px;"  v-if="store.products">
        <h1 class="fw-bold">예금/적금 조회</h1>
        <hr>
        <div class="row">
            <!-- 은행명 select -->
            <div class="col-3" style="position: relative;">
                <div class="d-flex flex-column flex-shrink-0 p-3" style="width: 100%; max-width: 280px;">
                    <p class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-decoration-none">
                        <svg class="bi pe-none me-2" width="40" height="32">
                        </svg>
                        <span class="fs-5 text-center fw-bold">은행명</span>
                    </p>
                    <hr style="border:2px black solid; margin-top: 10px;">
                    <select name="bank" id="bank" style="padding-left: 15px;" class="form-select"
                        v-model="selectedBank">
                        <option value="all" selected>전체</option>
                        <option v-for="bank in store.banks" :value="bank">{{ bank }}
                        </option>
                    </select>
                </div>

                <!-- 옵션 select -->
                <div class="d-flex flex-column flex-shrink-0 p-3" 
                    style="width: 100%; max-width: 280px;">
                    <p class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-decoration-none">
                        <svg class="bi pe-none me-2" width="40" height="32">
                        </svg>
                        <span class="fs-5 text-center fw-bold">기간</span>
                    </p>
                    <hr style="border:2px black solid; margin-top: 10px;">
                    <select name="trm" id="trm" style="padding-left: 15px;" class="form-select" v-model="selectedTrm">
                        <option disabled hidden selected value="">
                            기간 선택
                        </option>
                        <option value="1000">전체</option>
                        <option value="6">6달</option>
                        <option value="12">12달</option>
                        <option value="18">18달</option>
                        <option value="24">24달</option>
                        <option value="36">36달</option>
                    </select>
                </div>
            </div>

            <div class="ms-4 col-8 mt-4">
                <div class="row" style="height: 60px; border:2px gray solid;">
                    <div class="col-6 d-flex justify-content-center" 
                    :style="[{ backgroundColor: isSelected === 'deposit' ? '#0d6efd' : 'transparent' },
                    { color: isSelected === 'deposit' ? 'white' : 'black' }]"
                        @click="goBoard('deposit')">
                        <div class="d-flex align-items-center justify-content-center">
                            <p class="fs-3 fw-bold mb-0" style="text-decoration: none;">
                                예금
                            </p>
                        </div>
                    </div>

                    <div class="col-6 d-flex justify-content-center" style="border-left: 2px gray solid;" 
                    :style="[{ backgroundColor: isSelected === 'deposit' ? 'transparent' : '#0d6efd' },
                    { color: isSelected === 'deposit' ? 'black' : 'white' }]"
                        @click="goBoard('savings')">
                        <div class="d-flex align-items-center justify-content-center">
                            <p class="fs-3 fw-bold mb-0" style="text-decoration: none;">
                                적금
                            </p>
                        </div>
                    </div>
                </div>
                <RouterView :key="$route.fullPath" class="mt-5" v-if="store.filtered"/>
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted, watch } from 'vue';
import { RouterView, useRoute, useRouter } from 'vue-router';
import { useProductStore } from '@/stores/D_S'

const store = useProductStore()
const route = useRoute()
const router = useRouter()
const isSelected = ref(route.params.type)
const selectedBank = ref(route.params.bank)
const selectedTrm = ref(route.params.trm)

const goBoard = (type) => {
    isSelected.value = type
    router.push({ name: 'product', params: { 'type': type, 'bank': selectedBank.value, 'trm': selectedTrm.value } })
}

watch([selectedBank, selectedTrm], ([newBank, newTrm]) => {
    router.push({ name: 'product', params: { 'type': isSelected.value, 'bank': newBank, 'trm': newTrm } });
}, { immediate: true });

watch([isSelected, selectedBank, selectedTrm], ([newType, newBank, newTrm]) => {
    if (newType === 'deposit') {
        store.getDeposits(newBank, newTrm)
    } else {
        store.getSavings(newBank, newTrm)
    }
}, { immediate: true });

onMounted(() => {
    if (route.params.type === 'deposit') {
        store.getDeposits(route.params.bank, route.params.trm)
    } else {
        store.getSavings(route.params.bank, route.params.trm)
    }
});

watch(() => route.params, (newParams) => {
    isSelected.value = newParams.type
    selectedBank.value = newParams.bank
    selectedTrm.value = newParams.trm
}, { immediate: true });

</script>