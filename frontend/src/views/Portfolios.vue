<template>
  <div>
    <h1>Portfolio</h1>
    <div v-for="investment in investments" :key="investment.id">
      <p>{{ investment.type }}: {{ investment.amount }} on {{ investment.date }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      investments: []
    }
  },
  created() {
    axios.get('/investments')
      .then(response => {
        this.investments = response.data
      })
  }
}
</script>
