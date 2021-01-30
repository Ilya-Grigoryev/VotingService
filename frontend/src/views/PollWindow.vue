<template>
<div>
  <v-card  class="mx-auto pa-3 ma-3"
      elevation="4"
      outlined
      width="65%">
    <div>
    <v-app-bar
        v-if="image_url !== 'null' && image_url !== '/media/null'"
        :src="`http://localhost:8000${image_url}`"
        absolute
        dark
        prominent
      >
        <v-spacer></v-spacer>
      <v-btn   @click="$router.go(-1);"
               color="teal"
               depressed
               dark
               style="position: absolute; left: 10px;">
      <v-icon>mdi-arrow-left-bold-outline</v-icon>
      </v-btn>

    <v-btn
        v-if="voting.author.id === user.id && (voting.status === 'active' || voting.status === 'infinite')"
        @click="end_vote()"
        dark
        color="red darken-3"
        style="position: absolute; right: 90px;">
      Finish
      <v-divider vertical></v-divider>
      <v-icon> mdi-timer-off</v-icon>
    </v-btn>
      <v-btn
        v-if="voting.author.id !== user.id || !(voting.status === 'active' || voting.status === 'infinite')"
        dark
        disabled
        color="red darken-3"
        style="position: absolute; right: 90px;">
      Finish
      <v-divider vertical></v-divider>
      <v-icon> mdi-timer-off</v-icon>
    </v-btn>
    <v-dialog v-model="dialog" persistent max-width="800px">
    <template v-slot:activator="{ on, attrs }">
    <v-btn
        v-if="voting.author.id === user.id && voting.status === 'not started'"
        @click="rewrite_vote()"
        dark
        color="orange"
        style="position: absolute;
        right: 350px;"
        v-bind="attrs"
        v-on="on">
      <v-icon> mdi-pencil</v-icon>
    </v-btn>
      <v-btn
        v-if="voting.author.id !== user.id || voting.status !== 'not started'"
        dark
        disabled
        color="orange"
        style="position: absolute;
        right: 350px;"
        >
      <v-icon> mdi-pencil</v-icon>
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
                  <span class="headline">Edit vote</span>
                </v-card-title>
                <v-card-text>
                    <v-text-field
                    v-model="title"
                    :error-messages="titleErrors"
                    label="New title"
                    required clearable
                    :counter="50"
                    @input="$v.title.$touch()"
                    @blur="$v.title.$touch()"
                  ></v-text-field>

                  <v-text-field
                    v-model="description"
                    :error-messages="descriptionErrors"
                    label="New description"
                    required clearable
                    @input="$v.description.$touch()"
                    @blur="$v.description.$touch()"
                  ></v-text-field>

                  <v-radio-group
                    v-model="hours"
                    row>
                      <h3 class="mr-12">Duration:</h3>
                    <v-radio
                      label="1 hour"
                      :value="1"
                      selected
                    ></v-radio>
                    <v-radio
                      label="3 hours"
                      :value="3"
                    ></v-radio>
                    <v-radio
                      label="6 hours"
                      :value="6"
                    ></v-radio>
                    <v-radio
                      label="1 day"
                      :value="24"
                    ></v-radio>
                    <v-radio
                      label="1 week"
                      :value="24*7"
                    ></v-radio>
                    <v-radio
                      label="Infinite"
                      :value="24*7*4*10000000"
                    ></v-radio>
                  </v-radio-group>

                  <br>
                  <v-radio-group row>
                      <h3 class="mr-7">Options:   {{ options.length }}</h3>
                      <v-btn x-small @click="addOption">add option</v-btn>
                  </v-radio-group>
                  <v-list>
                      <v-list-item v-for="(option, ind) of options" :key="ind">
                          <v-text-field
                              v-model="options[ind]"
                              :error-messages="option.replace(/^\s+|\s+$/g, '') === '' ? ['Option is required.'] : []"
                              @input="$v.options.$each[ind].$touch()"
                              @blur="$v.options.$each[ind].$touch()"
                              label="Option"
                              required clearable
                          ></v-text-field>
                          <v-btn icon large @click="removeOption(ind)">
                              <v-icon color="red">mdi-close-box</v-icon>
                          </v-btn>
                      </v-list-item>
                  </v-list>

                  <v-row justify="space-between">
                      <v-col md="auto">
                          <h3 class="mr-7">Image:</h3>
                      </v-col>
                      <v-col>
                          <v-file-input accept="image/*"
                              label="Select image"
                              prepend-icon="mdi-camera"
                              outlined
                              dense
                              v-model="file"
                              @change="addFiles">
                          </v-file-input>
                      </v-col>
                  </v-row>
                  <v-img max-height="300"
                         contain
                         v-if="file"
                         :ref="'file'"
                         title="photo">
                  </v-img>

                  <v-btn
                    color="purple"
                    outlined
                    @click="save_changes">
                    Save
                  </v-btn>
                </v-card-text>
              </v-card>
            </v-dialog>
    <v-btn
        v-if="voting.author.id === user.id && voting.status === 'not started'"
        @click="start_vote()"
        dark
        color="teal"
        style="position: absolute; right: 220px;">
      Start
      <v-divider vertical></v-divider>
      <v-icon> mdi-timer</v-icon>
    </v-btn>
      <v-btn
        v-if="voting.author.id !== user.id || voting.status !== 'not started'"
        dark
        disabled
        color="teal"
        style="position: absolute; right: 220px;">
      Start
      <v-divider vertical></v-divider>
      <v-icon> mdi-timer</v-icon>
    </v-btn>


    <v-btn
        v-if="voting.author.id === user.id"
        @click="delete_vote()"
        dark
        color="red darken-3" style="position: absolute; right: 10px;">
      <v-icon> mdi-delete</v-icon>
    </v-btn>
    </v-app-bar>
      </div>
    <div>
        <v-app-bar
        v-if="image_url === 'null' && image_url === '/media/null'"
        :src="`https://sunnycrew.jp/wp-content/themes/dp-colors/img/post_thumbnail/noimage.png`"
        absolute
        white
        prominent
      >
        <v-spacer></v-spacer>
      <v-btn @click="$router.go(-1);"
               depressed
             dark
                color="teal"
               style="position: absolute; left: 10px;">
      <v-icon>mdi-arrow-left-bold-outline</v-icon>
      </v-btn>

    <v-btn
        v-if="voting.author.id === user.id && (voting.status === 'active' || voting.status === 'infinite')"
        @click="end_vote()"
        dark
        color="red darken-3"
        style="position: absolute; right: 90px;">
      Finish
      <v-divider vertical></v-divider>
      <v-icon> mdi-timer-off</v-icon>
    </v-btn>
      <v-btn
        v-else
        dark
        disabled
        color="red darken-3"
        style="position: absolute; right: 90px;">
      Finish
      <v-divider vertical></v-divider>
      <v-icon> mdi-timer-off</v-icon>
    </v-btn>
   <v-dialog v-model="dialog" persistent max-width="800px">
          <template v-slot:activator="{ on, attrs }">
              <v-btn
                  v-if="voting.author.id === user.id && voting.status === 'not started'"
                  @click="rewrite_vote()"
                  dark
                  color="orange"
                  style="position: absolute;
                  right: 350px;"
                  v-bind="attrs"
                  v-on="on">
                <v-icon> mdi-pencil</v-icon>
              </v-btn>
                <v-btn
                  v-else
                  dark
                  disabled
                  color="orange"
                  style="position: absolute;
                  right: 350px;"
                  >
                <v-icon> mdi-pencil</v-icon>
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
                        <span class="headline">Edit vote</span>
                      </v-card-title>
                      <v-card-text>
                          <v-text-field
                          v-model="title"
                          :error-messages="titleErrors"
                          label="New title"
                          required clearable
                          :counter="50"
                          @input="$v.title.$touch()"
                          @blur="$v.title.$touch()"
                        ></v-text-field>

                        <v-text-field
                          v-model="description"
                          :error-messages="descriptionErrors"
                          label="New description"
                          required clearable
                          @input="$v.description.$touch()"
                          @blur="$v.description.$touch()"
                        ></v-text-field>

                        <v-radio-group
                          v-model="hours"
                          row>
                            <h3 class="mr-12">Duration:</h3>
                          <v-radio
                            label="1 hour"
                            :value="1"
                            selected
                          ></v-radio>
                          <v-radio
                            label="3 hours"
                            :value="3"
                          ></v-radio>
                          <v-radio
                            label="6 hours"
                            :value="6"
                          ></v-radio>
                          <v-radio
                            label="1 day"
                            :value="24"
                          ></v-radio>
                          <v-radio
                            label="1 week"
                            :value="24*7"
                          ></v-radio>
                          <v-radio
                            label="Infinite"
                            :value="24*7*4*10000000"
                          ></v-radio>
                        </v-radio-group>

                        <br>
                        <v-radio-group row>
                            <h3 class="mr-7">Options:   {{ options.length }}</h3>
                            <v-btn x-small @click="addOption">add option</v-btn>
                        </v-radio-group>
                        <v-list>
                            <v-list-item v-for="(option, ind) of options" :key="ind">
                                <v-text-field
                                    v-model="options[ind]"
                                    :error-messages="option.replace(/^\s+|\s+$/g, '') === '' ? ['Option is required.'] : []"
                                    @input="$v.options.$each[ind].$touch()"
                                    @blur="$v.options.$each[ind].$touch()"
                                    label="Option"
                                    required clearable
                                ></v-text-field>
                                <v-btn icon large @click="removeOption(ind)">
                                    <v-icon color="red">mdi-close-box</v-icon>
                                </v-btn>
                            </v-list-item>
                        </v-list>

                        <v-row justify="space-between">
                            <v-col md="auto">
                                <h3 class="mr-7">Image:</h3>
                            </v-col>
                            <v-col>
                                <v-file-input accept="image/*"
                                    label="Select image"
                                    prepend-icon="mdi-camera"
                                    outlined
                                    dense
                                    v-model="file"
                                    @change="addFiles">
                                </v-file-input>
                            </v-col>
                        </v-row>
                        <v-img max-height="300"
                               contain
                               v-if="file"
                               :ref="'file'"
                               title="photo">
                        </v-img>

                        <v-btn
                          color="purple"
                          outlined
                          @click="save_changes">
                          Save
                        </v-btn>
                      </v-card-text>
                    </v-card>
            </v-dialog>
    <v-btn
        v-if="voting.author.id === user.id && voting.status === 'not started'"
        @click="start_vote()"
        dark
        color="teal"
        style="position: absolute; right: 220px;">
      Start
      <v-divider vertical></v-divider>
      <v-icon> mdi-timer</v-icon>
    </v-btn>
      <v-btn
        v-else
        dark
        disabled
        color="teal"
        style="position: absolute; right: 220px;">
      Start
      <v-divider vertical></v-divider>
      <v-icon> mdi-timer</v-icon>
    </v-btn>


    <v-btn
        v-if="voting.author.id === user.id"
        @click="delete_vote()"
        dark
        color="red darken-3" style="position: absolute; right: 10px;">
      <v-icon> mdi-delete</v-icon>
    </v-btn>
    </v-app-bar>
</div>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <Poll v-if="voting" v-bind="voting" :user="user"
          @start="(new_status) => (voting.status = new_status)"
          @end="voting.status = 'ended'"/>
    <br>
    <v-progress-linear
      color="cyan darken-2"
      rounded
      value="100"
    ></v-progress-linear>
    <br>
    <v-list-group style="border: 1px solid gray;">
          <template v-slot:activator>
            <v-list-item>
              <v-list-item-title><h3>Comments</h3></v-list-item-title>
            </v-list-item>
          </template>
          <v-list-item v-for="(comment, i) in comments" :key="i">
            <v-card class="px-3 ma-2" outlined width="100%" style="text-align: left;">
              <v-row justify="space-between">
                <v-col md="auto">
                  <strong style="color: #800080; cursor: pointer;"
                      @click="$router.push(`/profile/${comment.author.id}`)">
                    <u>{{ comment.author.name }}:</u>
                  </strong>
                </v-col>
                <v-col md="7">
                  {{ comment.text }}
                </v-col>
              </v-row>
            </v-card>
          </v-list-item>
          <br>
          <v-row justify="space-between" no-gutters class="px-6">
            <v-col md="10">
              <v-text-field
                      v-model="comment"
                      label="Comment"
                      outlined>
              </v-text-field>
            </v-col>
            <v-col md="2">
              <v-btn @click="send_comment()"
                     style="border: 2px solid #16b8fa;"
                     color="blue" icon x-large>
                <v-icon>mdi-send</v-icon>
              </v-btn>
            </v-col>
          </v-row>
        </v-list-group>

    <br>
    <v-progress-linear
      color="cyan darken-2"
      rounded
      value="100"
    ></v-progress-linear>
    <br>

    <v-row justify="space-between">
        <v-row justify="center">
          <v-col>
            <v-btn class="mx-2" :color="liked? 'green':'grey'" @click="like()">
              <v-icon dark>mdi-thumb-up</v-icon> <h2 class="ml-3">{{ likes }}</h2>
            </v-btn>
          </v-col>
          <v-col>
            <v-btn class="mx-2" :color="disliked? 'red':'grey'" @click="dislike()">
              <v-icon dark>mdi-thumb-down</v-icon> <h2 class="ml-3">{{ dislikes }}</h2>
            </v-btn>
          </v-col>
        </v-row>
    </v-row>
  </v-card>
</div>
</template>


<script>
    import Poll from "../components/Poll";
    import { validationMixin } from 'vuelidate'
    import { required, maxLength } from 'vuelidate/lib/validators'


    export default {
      name: "PollWindow",
      props: ['user'],
      components: {
        Poll
      },
      mixins: [validationMixin],

        validations: {
          title: {required, maxLength: maxLength(50)},
          description: {required},
          $each: {
            option: {required, maxLength: maxLength(50)}
          },
          options: {
            required,
            $each: {required}
          }
        },
      data: () => ({
        menu1: false,
        menu2: false,
        changed_voting: null,
        dialog: false,
        voting: null,
        likes: 0,
        dislikes: 0,
        liked: false,
        disliked: false,
        comments: [],
        comment: '',
        image_url: 'null',
        title: '',
        description: '',
        hours: 1,
        options: [''],
        file: null,
        reader: null,
      }),
      methods: {
        addFiles() {
          this.reader = new FileReader();
          this.reader.onloadend = () => {
            let fileData = this.reader.result
            let imgRef = this.$refs.file
            imgRef.src = fileData
          }
          this.reader.readAsDataURL(this.file);
        },
        addOption() {
          if (this.options.length < 7)
            this.options.push('')
        },
        removeOption(ind) {
          if (this.options.length > 1)
            this.options.splice(ind, 1)
        },
        save_changes() {
          let option_error = false
          for (let option of this.options) {
            if (option.replace(/^\s+|\s+$/g, '') === '') {
              option_error = true
              break
            }
          }
          if (this.title.length > 50 || this.title.replace(/^\s+|\s+$/g, '') === ''
              || this.description.replace(/^\s+|\s+$/g, '') === ''
              || option_error) {
            console.log('invalid')
            return
          }
          let formData = new FormData();
          formData.append('file', this.file)
          formData.append('title', this.title)
          formData.append('description', this.description)
          formData.append('hours', this.hours)
          formData.append('options', this.options)
          this.axios.post(
              'http://localhost:8000/api/voting/',
              formData,
              {
                headers: { Authorization: `Token ${this.user.token}`}
              }
          ).then(response => {
            if (response.data.status === 200) {
              this.$router.push('/all-polls')
            } else window.alert(response.data.description)
          })
        },
        delete_vote() {
          this.axios.post(
                  `http://localhost:8000/api/delete_poll/`,
                  {
                    "poll_id": this.$route.params.id,
                  },
                  {
                    headers: { Authorization: `Token ${this.user.token}` }
                  }
          ).then(response => {
            if (response.data.status === 200)
              this.$router.go(-1)
            else
              window.alert(response.data.description)
          })
        },
        end_vote(){
            this.axios.post(`http://localhost:8000/api/end_poll/`,
                {
                    poll_id: this.voting.id,
                },
                { headers: { Authorization: `Token ${this.user.token}` } }
            ).then(response => {
                if (response.data.status === 200) {
                    this.voting.status = 'ended'
                    this.get_poll()
                }
                else
                    window.alert(response.data.description)

            })
        },
        rewrite_vote(){
          console.log('rewriting...')
        },
        start_vote(){
          console.log('start')
          this.axios.post(`http://localhost:8000/api/start_poll/`,
                {
                    poll_id: this.voting.id,
                },
                {
                    headers: { Authorization: `Token ${this.user.token}` }
                }
          ).then(response => {
                if (response.data.status === 200) {
                    if (this.voting.end_date) {
                        this.voting.status = 'active'
                    }
                    else
                        this.voting.status = 'infinite'
                    this.get_poll()
                    this.voting.visibleResults = true
                }
                else
                    window.alert(response.data.description)

          })
        },
        send_comment() {
          this.axios.post(
                  'http://localhost:8000/api/comments/',
                  {
                    "user_id": this.user.id,
                    "voting_id": this.voting.id,
                    "text": this.comment
                  },
                  {
                    headers: {Authorization: `Token ${this.user.token}`}
                  }
          ).then(response => {
            if (response.data.status === 200) {
              this.comments.push(response.data.comment)
              this.comment = ''
            }
          })
        },
        like() {
          this.liked = !this.liked
          this.dislikes -= this.disliked ? 1 : 0
          this.disliked = false
          this.likes += this.liked ? 1 : -1
          this.axios.post(
                  'http://localhost:8000/api/likes/',
                  {
                    "user_id": this.user.id,
                    "voting_id": this.voting.id
                  },
                  {
                    headers: {Authorization: `Token ${this.user.token}`}
                  }
          )
        },
        dislike() {
          this.disliked = !this.disliked
          this.likes -= this.liked ? 1 : 0
          this.liked = false
          this.dislikes += this.disliked ? 1 : -1
          this.axios.post(
                  'http://localhost:8000/api/dislikes/',
                  {
                    "user_id": this.user.id,
                    "voting_id": this.voting.id
                  },
                  {
                    headers: {Authorization: `Token ${this.user.token}`}
                  }
          )
        },
        get_poll() {
          this.axios.get(`http://localhost:8000/api/voting/${this.$route.params.id}/`)
          .then(response => {
            this.changed_voting = response.data
            let vote = response.data
            let answers = []
            let voted_answer = -1
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
            let start = new Date(vote.start_date)
            start.setHours(start.getHours()-3)
              let end
              if (vote.end_date) {
                  end = new Date(vote.end_date)
                  end.setHours(end.getHours() - 3)
              } else
                  end = null
            this.voting = {
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
            }
            this.likes = vote.likes.length
            this.dislikes = vote.dislikes.length
            for (let like of vote.likes) {
              if (like.user_id === this.user.id)
                this.liked = true
            }
            for (let dislike of vote.dislikes) {
              if (dislike.user_id === this.user.id)
                this.disliked = true
            }
            this.comments = vote.comments
            this.image_url = vote.image_url
          })
        }
      },
      computed: {
            titleErrors () {
                const errors = []
                if (!this.$v.title.$dirty) return errors
                !this.$v.title.maxLength && errors.push('Title must be at most 50 characters long.')
                !this.$v.title.required && errors.push('Title is required.')
                return errors
            },
            descriptionErrors () {
                const errors = []
                if (!this.$v.description.$dirty) return errors
                !this.$v.description.required && errors.push('Description is required.')
                return errors
            }
        },
      mounted() {
        this.get_poll()
      }
    }
</script>

<style scoped>

</style>