<template>
    <div>
        <v-card v-if="profile"
          class="mx-auto pa-3 ma-3"
          elevation="4"
          outlined
          width="65%">
            <v-dialog v-model="dialog" persistent max-width="600px" v-if="Number($route.params.id) === user.id">
              <template v-slot:activator="{ on, attrs }">
                <v-btn large
                    icon outlined color="orange"
                    style="position: absolute; right: 10px;"
                    v-bind="attrs"
                    v-on="on">
                  <v-icon large
                      color="orange"
                      dense>
                      mdi-pencil-outline
                  </v-icon>
                </v-btn>
              </template>
              <v-card>
                <v-card-title>
                    <v-btn icon outlined color="red" style="position: absolute; right: 10px;"
                        @click="dialog = false">
                        <v-icon color="red">
                            mdi-close
                        </v-icon>
                    </v-btn>
                  <span class="headline">Edit profile</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-text-field
                        v-model="first_name"
                        :error-messages="first_nameErrors"
                        label="First name"
                        required clearable
                        @input="$v.first_name.$touch()"
                        @blur="$v.first_name.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="last_name"
                        :error-messages="last_nameErrors"
                        label="Last name"
                        required clearable
                        @input="$v.last_name.$touch()"
                        @blur="$v.last_name.$touch()"
                    ></v-text-field>
                    <v-text-field
                        @keydown.space="(event) => event.preventDefault()"
                        v-model="username"
                        :error-messages="usernameErrors"
                        label="Username"
                        :counter="20"
                        required clearable
                        @input="$v.username.$touch()"
                        @blur="$v.username.$touch()"
                    ></v-text-field>
                    <v-text-field
                        v-model="email"
                        :error-messages="emailErrors"
                        label="E-mail"
                        required clearable
                        @input="$v.email.$touch()"
                        @blur="$v.email.$touch()"
                    ></v-text-field>
                      <br><br>
                    <v-text-field
                        type="password"
                        v-model="password"
                        :error-messages="passwordErrors"
                        label="Password"
                        required clearable
                        @input="$v.password.$touch()"
                        @blur="$v.password.$touch()"
                    ></v-text-field>
                  </v-container>
                  <v-btn
                    color="purple"
                    outlined
                    @click="save_changes">
                    Save
                  </v-btn>
                </v-card-text>
              </v-card>
            </v-dialog>

            <v-row>
                <v-col md="3">
                    <v-avatar width="100%" height="auto" class="ml-3">
                        <img src="https://ishwortimilsina.com/images/icon_no_avatar.svg"
                             alt="John">
                    </v-avatar>
                </v-col>
                <v-col md="1" class="ma-0 pa-0">
                    <v-divider vertical></v-divider>
                </v-col>

                <v-col md="8">
                    <h2>{{ profile.first_name }} {{ profile.last_name }}</h2>
                    <strong style="color: gray; font-family: Roboto, sans-serif;">
                        @{{ profile.username }}
                    </strong>
                    <v-row>
                        <v-col style="font-family: Courier New, monospace">
                            <div>
                                Polls: <br>
                                <strong style="font-size: 25px;">{{ profile.polls_count }}</strong>
                            </div>
                        </v-col>
                        <v-col style="font-family: Courier New, monospace">
                            Votes: <br>
                            <strong style="font-size: 25px;">{{ profile.vote_count }}</strong>
                        </v-col>
                    </v-row>
                    <v-divider></v-divider>

                    <v-row style="font-size: 18px;">
                        <v-col md="3" style="font-family: Courier New, monospace;">
                            Email:
                        </v-col>
                        <v-col md="auto">
                            {{ profile.email }}
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        </v-card>
    </div>
</template>

<script>
    import { validationMixin } from 'vuelidate'
    import { required, maxLength, email } from 'vuelidate/lib/validators'

    export default {
        mixins: [validationMixin],
        validations: {
            first_name: { required },
            last_name: { required },
            username: { required, maxLength: maxLength(20) },
            email: { required, email },
            password: { required }
        },
        name: "Profile",
        props: ['user', 'id'],
        data: () => ({
            first_name: '',
            last_name: '',
            username: '',
            email: '',
            password: '',
            profile: null,
            dialog: false,
        }),
        methods: {
            save_changes() {
                this.$v.$touch()
                if (!this.$v.$invalid) {
                    this.axios.post(`http://localhost:8000/api/user/${this.$route.params.id}/`,
                        {
                            first_name: this.first_name,
                            last_name: this.last_name,
                            username: this.username,
                            email: this.email,
                            password: this.password
                        },
                        {
                        headers: { Authorization: `Token ${this.user.token}` }
                        }
                    ).then(response => {
                        if (response.data.status === 200) {
                            this.profile.first_name = this.first_name
                            this.profile.last_name = this.last_name
                            this.profile.username = this.username
                            this.profile.email = this.email
                            this.password = ''
                            this.dialog = false
                        }
                        else window.alert(response.data.description)
                    })
                }
            },
            loadProfile() {
                this.axios.get(`http://localhost:8000/api/user/${this.$route.params.id}/`)
                .then(response => {
                    this.profile = response.data
                    this.first_name = this.profile.first_name
                    this.last_name = this.profile.last_name
                    this.username = this.profile.username
                    this.email = this.profile.email
                })
            }
        },
        computed: {
          first_nameErrors () {
            const errors = []
            if (!this.$v.first_name.$dirty) return errors
            !this.$v.first_name.required && errors.push('First name is required.')
            return errors
          },
          last_nameErrors () {
            const errors = []
            if (!this.$v.last_name.$dirty) return errors
            !this.$v.last_name.required && errors.push('Last name is required.')
            return errors
          },
          usernameErrors () {
            const errors = []
            if (!this.$v.username.$dirty) return errors
            !this.$v.username.maxLength && errors.push('Username must be at most 20 characters long.')
            !this.$v.username.required && errors.push('Username is required.')
            return errors
          },
          emailErrors () {
            const errors = []
            if (!this.$v.email.$dirty) return errors
            !this.$v.email.email && errors.push('Must be valid e-mail.')
            !this.$v.email.required && errors.push('E-mail is required.')
            return errors
          },
          passwordErrors () {
            const errors = []
            if (!this.$v.password.$dirty) return errors
            !this.$v.password.required && errors.push('Password is required')
            return errors
          }
        },
        mounted() {
            this.loadProfile()
        }
    }
</script>

<style scoped>

</style>