<template>
  <div>
    <h2>Add Investment</h2>
    <form @submit.prevent="addInvestment">
      <div>
        <label for="type">Type:</label>
        <input v-model="type" id="type" required />
      </div>
      <div>
        <label for="amount">Amount:</label>
        <input v-model="amount" id="amount" type="number" required />
      </div>
      <div>
        <label for="date">Date:</label>
        <input v-model="date" id="date" type="date" required />
      </div>
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      type: '',
      amount: '',
      date: ''
    }
  },
  methods: {
    async addInvestment() {
      const newInvestment = {
        type: this.type,
        amount: this.amount,
        date: this.date
      }
      await axios.post('/investments', newInvestment)
      this.$router.push('/')
    }
  }
}
</script>
