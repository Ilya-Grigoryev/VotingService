<template>
    <div>
        <v-card class="mx-auto pa-3"
                elevation="6"
                outlined
                width="90%">
            <v-text-field
                v-model="name"
                :error-messages="nameErrors"
                label="Username"
                required clearable
                @input="$v.name.$touch()"
                @blur="$v.name.$touch()"
            ></v-text-field>
            <v-text-field
                type="password"
                v-model="password"
                :error-messages="passwordErrors"
                label="Password"
                required clearable
                @input="$v.password.$touch()"
                @blur="$v.password.$touch()"
            ></v-text-field>

            <v-btn
                    class="mr-4"
                    @click="submit"
                    width="25%">
              login
            </v-btn>
            <br>
            <ins style="color: gray; cursor: pointer;"
                 @click="$router.push('/register')">
                No account? Register now!
            </ins>
        </v-card>
  </div>
</template>

<script>
  import { required } from 'vuelidate/lib/validators'

  export default {
    name: "Login",
    components: {},
    props: [],

    validations: {
      name: { required },
      password: { required },
    },

    data: () => ({
      name: '',
      password: '',
    }),

    computed: {
      nameErrors () {
        const errors = []
        if (!this.$v.name.$dirty) return errors
        !this.$v.name.required && errors.push('Username is required.')
        return errors
      },
      passwordErrors () {
        const errors = []
        if (!this.$v.password.$dirty) return errors
        !this.$v.password.required && errors.push('Password is required')
        return errors
      },
    },

    methods: {
      submit () {
        this.$v.$touch()
        if (!this.$v.$invalid) {
            this.axios.post('http://localhost:8000/api/login/', {
                username: this.name,
                password: this.password
            }).then(response => {
                if (response.data.status === 200) {
                    localStorage.setItem('token', response.data.token)
                    this.$emit('login', {
                        token: response.data.token,
                        id: response.data.id,
                        email: response.data.email,
                        username: response.data.username,
                        first_name: response.data.first_name,
                        last_name: response.data.last_name,
                    });
                    this.$router.push('/');
                } else {
                    this.clear()
                    window.alert(response.data.description)
                }
            })
        }
      },
      clear () {
        this.$v.$reset()
        this.name = ''
        this.password = ''
      },
    },
  }
</script>

<style scoped>

</style>