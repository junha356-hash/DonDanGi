<template>
  <section style="position:relative;" class="mb-5 ">
    <img src="@/assets/bank.webp" alt="main_img"
    data-aos="zoom-out" data-aos-duration="600">
    <h1 data-aos="fade-down" data-aos-duration="1500">주변 은행 찾기</h1>
  </section>
    <div class="row container-content mx-auto" id="section">
        <h1 class="fw-bold">&nbsp;&nbsp;주변 은행 찾기</h1>
        <hr style="margin-top: 20px;  margin-bottom: 20px;">
        <div class="my-3 row gy-3">
            <form class="input-group py-0 my-0" @submit.prevent="searchBank">
                <select name="inputProv"
                    v-model="inputProv"
                    @change="inputProvEvent"
                    class="form-select" required
                >
                <option disabled hidden selected value="">
                    도/광역시 선택
                </option>
                <option v-for="prov in store.province" 
                :value="prov">{{ prov }}</option>
                </select>
                                        
                <select name="inputCityEvent"  
                    v-model="inputCity" 
                    @change="inputCityEvent"
                    class="form-select" required
                >
                <option disabled hidden selected value="">
                    시/구 선택
                </option>
                <option v-for="city in store.city[inputProv]"
                    :value="city">{{ city }}</option>
                </select>
                            
                <select name="inputBankEvent"
                    v-model="inputBank"
                    @change="inputBankEvent"
                    class="form-select" required
                    >
                <option disabled hidden selected value="">
                    은행명 선택
                </option>
                <option v-for="bank in store.bankList"
                    :value="bank">{{ bank }}</option>
                </select>
                <button class="btn btn-primary">검색</button>
            </form>
        </div>
        
        <!-- 지도 표시 -->
        <div class="my-3">
            <div id="map"
                style="width:100%; border:1px whitesmoke solid;">
            </div>
        </div>
        <div v-if="isBankDetailVisible">
            <BankDetailComponent v-show="isBankDetailVisible" :bank="selectedBank"/>
        </div>
    </div>
</template>

<script setup>
    import { ref, onMounted } from "vue"
    import { useBankStore } from "@/stores/bank"
    import BankDetailComponent from "@/components/BankDetailComponent.vue";

    const store = useBankStore()
    const inputProv = ref("")
    const inputCity = ref("")
    const inputBank = ref("")
    const map = ref(null)
    const flags = ref([])
    const isBankDetailVisible = ref(false)
    const selectedBank = ref(null)

    const inputProvEvent = (event) => {
        inputProv.value = event.target.value
    }
    const inputCityEvent = (event) => {
        inputCity.value = event.target.value
    }
    const inputBankEvent = (event) => {
        inputBank.value = event.target.value
    }

    let currentInfowindow = null

    // 수정 필 
    const SearchMyBanks = async (data, status) => {
        if (status === kakao.maps.services.Status.OK) {
            resetFlag()
            const bounds = new kakao.maps.LatLngBounds()
            for (let i = 0 ; i < data.length ; i++) {
                setFlag(data[i])
                bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x))
            }
            map.value.setBounds(bounds)
            updateFlag(data)
        } else if(status === kakao.maps.services.Status.ZERO_RESULT) {
            window.alert("검색 결과가 없습니다.")
        }
    }

    const searchResultText = ref("")

    const searchBank = function () {
        const searchAPI = new kakao.maps.services.Places(map.value)
        resetFlag()        
        searchAPI.keywordSearch(
            `${inputProv.value} ${inputCity.value} ${inputBank.value}`,
            (data, status) => {
                if (status === kakao.maps.services.Status.OK) {
                    searchResultText.value = ""
                } else {
                    searchResultText.value = "No result"
                }

                SearchMyBanks(data, status)
            },
            {
                useMapBounds: false,
            }
        )
    }

    const resetFlag = () => {
        for (const flag of flags.value) {
            if (flag.marker) {
                flag.marker.setMap(null)
            }
        }
        flags.value = []
    }

    const setFlag = function (bank) {
        const flag = new kakao.maps.Marker({
            map: map.value,
            position: new kakao.maps.LatLng(bank.y, bank.x),
        })

        flags.value.push({
            marker: flag,
            bank_name: bank.place_name,
        })

        kakao.maps.event.addListener(flag, "click", function () {
            if (currentInfowindow) {
                currentInfowindow.close()
            }

            const infowindow = new kakao.maps.InfoWindow({
                zIndex: 1,
                content: `<div style="padding:5px;font-size:12px;font-weight:bold;">${bank.place_name}</div>`,
            })
            infowindow.open(map.value, flag)
            currentInfowindow = infowindow

            selectedBank.value = bank
            isBankDetailVisible.value = true
        })
    }

onMounted(() => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((position) => {
      const lat = position.coords.latitude
      const lng = position.coords.longitude
      const userLoc = new kakao.maps.LatLng(lat, lng)

      const options = {
        center: userLoc,
        level: 5,
      }
      map.value = new kakao.maps.Map(document.getElementById("map"), options)

      const ps = new kakao.maps.services.Places()
      ps.categorySearch("BK9", (data, status) => {
        SearchMyBanks(data, status)
      }, {
        location: userLoc,
        radius: 4000,
        sort: kakao.maps.services.SortBy.DISTANCE
      })
    }, () => {
      // 위치 허용 거부 시 fallback
      const fallbackCenter = new kakao.maps.LatLng(37.5665, 126.9780)  // 서울 시청
      map.value = new kakao.maps.Map(document.getElementById("map"), {
        center: fallbackCenter,
        level: 5,
      })
    })
  }
})
</script>

<style scoped>
    #section{
        min-width: 800px;
        max-width: 1200px;        
    }
    #map {
    height:400px;
    }

</style>