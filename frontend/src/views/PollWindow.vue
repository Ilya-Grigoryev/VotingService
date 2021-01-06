<template>
<div>
  <v-card
      class="mx-auto pa-3 ma-3"
      elevation="4"
      outlined
      width="65%">
    <Poll v-if="voting" v-bind="voting" :user="user"/>
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
      <v-col md="6">
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
      </v-col>
      <v-col md="6">
        <v-card class="">
          <v-img src="https://picsum.photos/id/11/500/300"></v-img>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</div>
</template>


<script>
    import Poll from "../components/Poll";

    export default {
      name: "PollWindow",
      props: ['user'],
      components: {
        Poll
      },
      data: () => ({
        voting: null,
        likes: 10,
        dislikes: 3,
        liked: false,
        disliked: false,
        comments: [
          {
            author: { name: 'noname', id: 0 },
            text: 'А у меня Ubuntu))'
          },
          {
            author: { name: 'lexa', id: 4 },
            text: 'Ubuntu это дистрибутив Linux'
          }
        ],
        comment: '',
      }),
      methods: {
        send_comment() {
          console.log(this.comment)
        },
        like() {
          this.liked = !this.liked
          this.dislikes -= this.disliked ? 1 : 0
          this.disliked = false
          this.likes += this.liked ? 1 : -1
        },
        dislike() {
          this.disliked = !this.disliked
          this.likes -= this.liked ? 1 : 0
          this.liked = false
          this.dislikes += this.disliked ? 1 : -1
        },
        get_poll() {
          this.axios.get(`http://localhost:8000/api/voting/${this.$route.params.id}/`)
          .then(response => {
            let vote = response.data
            let answers = []
            let voted_answer = -1
            for (let i = 0; i < vote.options.length; i++) {
              for (let j = 0; j < vote.options[i].users.length; j++)
                if (vote.options[i].users[j].id === this.user.id)
                  voted_answer = i

              answers.push({
                id: vote.options[i].id,
                text: vote.options[i].text,
                votes: vote.options[i].users.length
              })
            }
            let start = new Date(vote.start_date)
            let end = new Date(vote.end_date)
            this.voting = {
              id: vote.id,
              question: vote.title,
              description: vote.description,
              author: vote.user,
              start_date: start,
              end_date: end,
              answers: answers,
              multiple: false,
              voted_answer: voted_answer
            }
          })
        }
      },
      mounted() {
        this.get_poll()
      }
    }
</script>

<style scoped>

</style>