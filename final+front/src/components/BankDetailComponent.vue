<template>
  <div class="my-5">
    <h2 class="fw-bold">{{ bank.place_name }}</h2>
    <hr>
    <table class="table">
      <tbody class="table-group-divider">
        <tr>
          <th scope="row">상세 주소</th>
          <td class="border-left">{{ bank.address_name }}</td>
        </tr>
        <tr>
          <th scope="row">도로명 주소</th>
          <td>{{ bank.road_address_name || '없음' }}</td>
        </tr>
        <tr>
          <th scope="row">전화번호</th>
          <td>{{ bank.phone || '전화번호 없음' }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const props = defineProps({
  bank: {
    type: Object,
    required: true
  }
})
</script>

<style scoped>
th {
  width: 200px;
  padding-left: 20px;
  font-size: large;
}
td {
  font-size: large;
}
</style>
