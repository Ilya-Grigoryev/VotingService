<template>
    <div>
        <v-btn width="65%"
               color="teal"
               elevation="10"
               @click="$router.push('/new-poll')"
               v-if="Number(this.$route.params.id) === user.id">
          add new poll
        </v-btn>
        <v-card v-if="profile"
          class="mx-auto pa-3 ma-3"
          elevation="4"
          outlined
          width="65%">
            <v-dialog v-model="dialog" persistent max-width="600px" v-if="Number(this.$route.params.id) === user.id">
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

            <v-row justify="space-around">
                <v-col md="3">
                    <div class="ml-5">
                        <input v-if="Number(this.$route.params.id) === user.id"
                            type="file"
                            accept="image/*"
                            ref="file"
                            class="d-none"
                            @change="onFileChanged">
                        <v-avatar style="border: 3px solid #3d365c;"
                                width="100%" height="100%">
                            <img v-if="file"
                                    style="max-width: 300px;
                                           max-height: 300px;"
                                   ref="image"
                                   title="photo">
                            <img v-else-if="profile.avatar === 'null'"
                                 style="max-width: 300px;
                                        max-height: 300px;"
                                 src="https://ishwortimilsina.com/images/icon_no_avatar.svg">
                            <img v-else
                                 style="max-width: 300px;
                                        max-height: 300px;"
                                 :src="`http://localhost:8000${profile.avatar}`">
                            <v-btn v-if="Number(this.$route.params.id) === user.id"
                                   fab @click="onButtonClick"
                                   @mouseover="mouseover=true" @mouseleave="mouseover=false"
                                   :style="`position: absolute;
                                          width: 100%; height: 100%;
                                          opacity: ${mouseover ? 0.5 : 0}`">
                                <v-icon size="70">mdi-camera-outline</v-icon>
                            </v-btn>
                        </v-avatar>
                    </div>
                </v-col>
                <v-col md="1" class="ma-0 pa-0">
                    <v-divider vertical></v-divider>
                </v-col>

                <v-col md="max">
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
          <br>
    <v-expansion-panels>
      <v-expansion-panel>
        <v-expansion-panel-header>
         <h3 class="ml-5">Polls</h3>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-expansion-panels>
      <v-expansion-panel>
        <v-expansion-panel-header>
         <h3 class="ml-5">Active</h3>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-list-item v-for="(voting, index) in voting_list_polls_active" :key="index">
            <v-card  class="mx-auto pa-3 ma-3"
                    elevation="4"
                    outlined
                    width="95%">
                      <v-btn icon depressed color="teal" style="position: absolute; right: 10px;">
                        <v-icon @click="$router.push(`/poll/${voting.id}/`)">mdi-arrow-expand-all</v-icon>
                      </v-btn>
                    <Poll v-bind="voting" :user="user"/>
            </v-card>
          </v-list-item>
        </v-expansion-panel-content>
      </v-expansion-panel>
      <v-expansion-panel>
        <v-expansion-panel-header>
         <h3 class="ml-5">Ended</h3>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-list-item v-for="(voting, index) in voting_list_polls_ended" :key="index">
            <v-card  class="mx-auto pa-3 ma-3"
                    elevation="4"
                    outlined
                    width="95%">
                      <v-btn icon depressed color="teal" style="position: absolute; right: 10px;">
                        <v-icon @click="$router.push(`/poll/${voting.id}/`)">mdi-arrow-expand-all</v-icon>
                      </v-btn>
                    <Poll v-bind="voting" :user="user"/>
            </v-card>
          </v-list-item>
        </v-expansion-panel-content>
      </v-expansion-panel>

        </v-expansion-panels>
        </v-expansion-panel-content>
      </v-expansion-panel>
            <v-expansion-panel>
        <v-expansion-panel-header>
         <h3 class="ml-5">Votes</h3>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-list-item v-for="(voting, index) in voting_list_votes" :key="index">
            <v-card class="mx-auto pa-3 ma-3"
                    elevation="4"
                    outlined
                    width="95%">
                      <v-btn icon depressed color="teal" style="position: absolute; right: 10px;">
                        <v-icon @click="$router.push(`/poll/${voting.id}/`)">mdi-arrow-expand-all</v-icon>
                      </v-btn>
                    <Poll v-bind="voting" :user="user"/>
            </v-card>
          </v-list-item>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>

        </v-card>
    </div>
</template>

<script>
    import { validationMixin } from 'vuelidate'
    import { required, maxLength, email } from 'vuelidate/lib/validators'
    import Poll from '../components/Poll.vue'

    export default {
        mixins: [validationMixin],
        validations: {
            first_name: { required },
            last_name: { required },
            username: { required, maxLength: maxLength(20) },
            email: { required, email },
            password: { required },
        },
        components: {
            Poll
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
            voting_list_votes: [],
            voting_list_polls_active: [],
            voting_list_polls_ended: [],
            mouseover: false,
            file: null,
        }),
        methods: {
            onButtonClick() {
                this.$refs.file.click()
            },
            onFileChanged(e) {
                if (!e.target.files[0])
                    return
                this.file = e.target.files[0]
                this.reader = new FileReader();
                this.reader.onloadend = () => {
                    let fileData = this.reader.result
                    let imgRef = this.$refs.image
                    imgRef.src = fileData
                }
                this.reader.readAsDataURL(this.file);
                this.load_new_avatar()
            },
            load_new_avatar() {
                let formData = new FormData();
                formData.append('file', this.file)
                this.axios.post(
                    `http://localhost:8000/api/user/${this.user.id}/new_avatar/`,
                    formData,
                    {
                        headers: {Authorization: `Token ${this.user.token}`}
                    }
                ).then(response => {
                    if (response.data.status === 200) {
                        this.profile.avatar = response.data.avatar
                        this.$emit('change-avatar', this.profile.avatar)
                    } else window.alert(response.data.description)
                })
            },
            save_changes() {
                this.$v.$touch()
                if (!this.$v.$invalid) {
                    this.axios.post(`http://localhost:8000/api/user/${Number(this.$route.params.id)}/`,
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
                this.axios.get(`http://localhost:8000/api/user/${Number(this.$route.params.id)}/`)
                .then(response => {
                    this.profile = response.data
                    this.first_name = this.profile.first_name
                    this.last_name = this.profile.last_name
                    this.username = this.profile.username
                    this.email = this.profile.email
                })
            },
            get_voting_list() {
              this.axios.get('http://localhost:8000/api/voting/')
              .then(response => {
                this.voting_list_votes = []
                this.voting_list_polls_active = []
                this.voting_list_polls_ended = []
                let data = response.data
                for (let vote of data) {
                  let answers = []
                  let voted_answer = -1
                  let user_voted_answer = -1
                  for (let i = 0; i < vote.options.length; i++) {
                    for (let j = 0; j < vote.options[i].users.length; j++)
                      if (vote.options[i].users[j].user.id === this.user.id)
                        voted_answer = i

                    answers.push({
                      id: vote.options[i].id,
                      text: vote.options[i].text,
                      votes: vote.options[i].users.length
                    })
                  }
                  for (let i = 0; i < vote.options.length; i++)
                    for (let j = 0; j < vote.options[i].users.length; j++)
                      if (vote.options[i].users[j].user.id === Number(this.$route.params.id))
                        user_voted_answer = i

                  let start = new Date(vote.start_date)
                  let end = new Date(vote.end_date)
                  if (user_voted_answer !== -1) {
                    this.voting_list_votes.unshift({
                      id: vote.id,
                      question: vote.title,
                      description: vote.description,
                      author: vote.user,
                      start_date: start,
                      end_date: end,
                      answers: answers,
                      multiple: false,
                      voted_answer: voted_answer,
                      status: vote.status
                    })
                  }
                  if (vote.user.id === Number(this.$route.params.id)) {
                    if (vote.status === 'active') {
                      this.voting_list_polls_active.unshift({
                        id: vote.id,
                        question: vote.title,
                        description: vote.description,
                        author: vote.user,
                        start_date: start,
                        end_date: end,
                        answers: answers,
                        multiple: false,
                        voted_answer: voted_answer,
                        status: 'active'
                      })
                    }
                    if (vote.status === 'ended') {
                      this.voting_list_polls_ended.unshift({
                        id: vote.id,
                        question: vote.title,
                        description: vote.description,
                        author: vote.user,
                        start_date: start,
                        end_date: end,
                        answers: answers,
                        multiple: false,
                        voted_answer: voted_answer,
                        status: 'ended'
                      })
                    }

                  }
                }
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
            this.get_voting_list()
            this.loadProfile()
        },
        watch:{
            $route (){
                this.get_voting_list()
                this.loadProfile()
            }
        }
    }
</script>

<style scoped>

</style>