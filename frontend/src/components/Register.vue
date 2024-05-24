<template>
  <div>
    <h2>Register</h2>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input v-model="username" id="username" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input v-model="email" id="email" type="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input v-model="password" id="password" type="password" required />
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const username = ref('')
    const email = ref('')
    const password = ref('')
    const router = useRouter()

    const register = async () => {
      try {
        await axios.post('/auth/register', { username: username.value, email: email.value, password: password.value })
        router.push('/login')
      } catch (error) {
        console.error('Registration error', error)
      }
    }

    return { username, email, password, register }
  }
}
</script>
