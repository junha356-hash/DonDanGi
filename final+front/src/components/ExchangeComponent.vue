<template>
  <div class="row mt-5 px-4 justify-content-center">
    <div class="converter row shadow rounded p-4 bg-white" style="max-width: 1300px; min-height:600px;">
      <div class="col-10">
        <div>
          <select v-model="CountrySelection" class="form-select fs-5 fw-semibold mb-4 px-3 py-2">
            <option disabled hidden selected value="">
              국가를 선택해주세요.
            </option>
            <option v-for="country in CountryList" :key="country" :value="country">
              {{ country }}
            </option>
          </select>
        </div>
      </div>
      <!-- 한국 국기 + 교환 이미지 + 선택한 국가 국기 -->

      <div class="col-2 d-flex align-items-center justify-content-center" v-if="CountrySelection">
        <!-- <img :src="flagSrc" alt="Country Flag" class="img-fluid rounded shadow-sm border" style="max-width: 100px;" /> -->
      </div>

      <div class="mt-4 text-start row">
        <div class="input-group align-items-center mb-3">
          <span class="input-group-text fs-6 fw-bold text-center bg-light" style="min-width: 100px;">To</span>
          <input type="number" v-model.number="KRW" @input="Paychanged(Math.floor((KRW / rate) * 100) / 100)" placeholder="KRW" class="form-control fs-5 px-3 py-2" />
          <span class="input-text-addon fw-bold fs-5">원</span>
        </div>
        <div class="input-group align-items-center">
          <span class="input-group-text fs-6 fw-bold text-center bg-light" style="min-width: 100px;">From</span>
          <input type="number" v-model.number="payment" @input="KRWChanged(Math.floor((payment * rate) * 100) / 100)" placeholder="Money" class="form-control fs-5 px-3 py-2" />
          <span class="input-text-addon fw-bold fs-5">{{ currencyName }}</span>
        </div>
      </div>

      <div id="board-list" class="mt-5" v-if="CountrySelection">
        <div class="container">
          <table class="table table-bordered text-center align-middle">
            <thead class="table-light">
              <tr>
                <th scope="col" class="fs-6">환율</th>
                <th scope="col" class="fs-6">
                  <span class="text-success">
                    <u>1 {{ currencyName }} 당 {{ Math.floor(basePrice * 100) / 100 }} 원</u>
                  </span>
                </th>
              </tr>
              <tr>
                <th scope="col" class="fs-6">기준일</th>
                <th scope="col" class="fs-6">✔ &nbsp;&nbsp; {{ date }}</th>
              </tr>
            </thead>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import axios from 'axios'

const API_KEY = 'AD6715YFHJNKZLU2'

const CountryList = ref([
  '미국', '일본', '영국', '중국', '호주', '캐나다', '스위스', '뉴질랜드',
  '싱가포르', '홍콩', '노르웨이', '스웨덴', '덴마크', '브라질', '인도', '러시아',
  '남아프리카', '멕시코', '유럽연합'
])

const CurrencyType = {
  미국: 'USD', 일본: 'JPY', 영국: 'GBP', 중국: 'CNY', 호주: 'AUD',
  캐나다: 'CAD', 스위스: 'CHF', 뉴질랜드: 'NZD', 싱가포르: 'SGD', 홍콩: 'HKD',
  노르웨이: 'NOK', 스웨덴: 'SEK', 덴마크: 'DKK', 브라질: 'BRL', 인도: 'INR',
  러시아: 'RUB', 남아프리카: 'ZAR', 멕시코: 'MXN', 유럽연합: 'EUR'
}

const CountrySelection = ref('')
const KRW = ref(0)
const payment = ref(0)
const rate = ref(null)
const basePrice = ref(null)
const currencyName = ref('')
const date = ref('')

watch(CountrySelection, async (CountryChanged) => {
  if (CountryChanged) {
    const currency = CurrencyType[CountryChanged]
    try {
      const { data } = await axios.get('https://www.alphavantage.co/query', {
        params: {
          function: 'CURRENCY_EXCHANGE_RATE',
          from_currency: currency,
          to_currency: 'KRW',
          apikey: API_KEY
        }
      })
      const result = data['Realtime Currency Exchange Rate']
      rate.value = parseFloat(result['5. Exchange Rate'])
      basePrice.value = rate.value
      currencyName.value = result['1. From_Currency Code']
      date.value = result['6. Last Refreshed']
      KRW.value = 0
      payment.value = 0
    } catch (err) {
      console.error('Alpha Vantage 환율 조회 실패:', err)
    }
  }
})

const Paychanged = (value) => {
  payment.value = value
}

const KRWChanged = (value) => {
  KRW.value = value
}
</script>

<style scoped>
.converter {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
}
.input-group {
  position: relative;
}
.input-text-addon {
  position: absolute;
  right: 40px;
  top: 50%;
  transform: translateY(-50%);
  font-weight: bold;
  font-size: 20px;
  pointer-events: none;
}
.form-control {
  padding-right: 60px;
}
.table {
  font-size: 15px;
}
</style>
