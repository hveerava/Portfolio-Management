<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email:</label>
        <input v-model="email" id="email" type="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex'

export default {
  setup() {
    const email = ref('')
    const password = ref('')
    const router = useRouter()
    const store = useStore()

    const login = async () => {
      try {
        const response = await axios.post('/auth/login', { email: email.value, password: password.value })
        store.commit('setToken', response.data.access_token)
        store.dispatch('fetchInvestments')
        router.push('/')
      } catch (error) {
        console.error('Invalid login', error)
      }
    }

    return { email, password, login }
  }
}
</script>
