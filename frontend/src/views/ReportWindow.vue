<template>
    <div>
        <v-card width="65%"
                v-if="report"
        class="mx-auto ma-3 pa-3">
            <v-app-bar outlined elevation="0">
                <v-btn @click="$router.go(-1);"
                       color="teal"
                       depressed
                       dark
                       style="position: absolute; left: 10px;">
                  <v-icon>mdi-arrow-left-bold-outline</v-icon>
                </v-btn>
                <h2 style="margin: auto"> {{ report.title }} </h2>
            </v-app-bar>
            <br>
        <v-row justify="space-around">
            <v-col md="max">
                <h3> {{ report.description }} </h3>
            </v-col>
            <v-col md="auto">
                <v-img max-width="300px"
                   v-if="report.image !== 'null' && report.image !== '/media/null'"
                   :src="`http://localhost:8000${report.image}`">
                </v-img>
            </v-col>
        </v-row>
        </v-card>
        <v-btn width="65%"
               class="mx-auto ma-3 pa-1"
               color="teal"
               elevation="10"
               @click="close_report"
               v-if="report.status === 'open' && !user.is_admin">
            problem solved!
        </v-btn>
        <v-card width="65%"
                v-if="messages[0] != null"
                class="mx-auto ma-3 pa-1">
            <div v-for="(message, index) in messages" :key="index">
                <div class="container" v-if="message.user.id === user.id">
                    <v-row justify="start">
                        <v-col md="auto">
                            <b style="color: #800080; cursor: pointer;"
                            @click="$router.push(`/profile/${message.user.id}`)">
                                {{ message.user.name }}
                            </b>
                            <br>
                            <img v-if="message.user.avatar === 'null' || message.user.avatar === '/media/null'"
                                 src="https://ishwortimilsina.com/images/icon_no_avatar.svg">
                            <img v-else :src="`http://localhost:8000${message.user.avatar}`">
                        </v-col>
                        <v-col md="auto">
                            <v-divider
                              vertical
                            ></v-divider>
                        </v-col>
                        <v-col md="max">
                            <p>{{ message.text }}</p>
                        </v-col>
                    </v-row>
                </div>

                <div class="container darker" v-else>
                    <v-row justify="start">
                        <v-col md="max">
                            <p>{{ message.text }}</p>
                        </v-col>
                        <v-col md="auto">
                            <v-divider
                              vertical
                            ></v-divider>
                        </v-col>
                        <v-col md="auto">
                            <b style="color: #800080; cursor: pointer;"
                            @click="$router.push(`/profile/${message.user.id}`)">
                                {{ message.user.name }}
                            </b>
                            <br>
                            <img v-if="message.user.avatar === 'null' || message.user.avatar === '/media/null'"
                                 src="https://ishwortimilsina.com/images/icon_no_avatar.svg">
                            <img v-else :src="`http://localhost:8000${message.user.avatar}`">
                        </v-col>
                    </v-row>
                </div>
            </div>
        </v-card>
        <v-card width="65%"
                class="mx-auto"
                v-if="report.status === 'open'">
            <br>
            <v-row justify="space-between" no-gutters class="px-6">
                <v-col md="10">
                  <v-text-field
                          @keydown.enter="send_message()"
                          v-model="new_message"
                          label="Message"
                          outlined>
                  </v-text-field>
                </v-col>
                <v-col md="2">
                  <v-btn @click="send_message()"
                         style="border: 2px solid #16b8fa;"
                         color="blue" icon x-large>
                    <v-icon>mdi-send</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
        </v-card>
    </div>
</template>

<script>
    export default{
        name: 'Report',
        props: ['user', 'id'],
        data: () => ({
            report: {
                title: '',
                description: '',
                image: 'null',
            },
            messages: [],
            new_message: '',
        }),
        methods: {
            getReport() {
                this.axios.get(`http://localhost:8000/api/reports/${this.$route.params.id}/`,
                  {
                      headers: { Authorization: `Token ${this.user.token}` }
                  })
                .then(response => {
                    if (response.data.status === 403)
                        this.$router.push('/reports')
                  this.report = response.data
                })
            },
            getMessages() {
                this.axios.get(`http://localhost:8000/api/report/${this.$route.params.id}/`,
                    {
                        headers: { Authorization: `Token ${this.user.token}` }
                    })
                .then(response => {
                    this.messages = response.data
                })
            },
            send_message() {
                if (!this.new_message) return
                this.axios.post(`http://localhost:8000/api/report/${this.$route.params.id}/`,
                    {
                        report_id: Number(this.$route.params.id),
                        text: this.new_message,
                    },
                    {
                        headers: { Authorization: `Token ${this.user.token}` }
                    }
                ).then(response => {
                    this.messages.push(response.data)
                    this.new_message = ''
                })
            },
            close_report() {
                this.axios.delete(`http://localhost:8000/api/reports/${this.$route.params.id}/`,
                    {
                        headers: { Authorization: `Token ${this.user.token}` }
                    }
                ).then(response => {
                    if (response.data.status === 200) {
                        this.report.status = 'closed'
                    }
                })
            },
        },
        mounted() {
            this.getReport()
            this.getMessages()
        }
    }
</script>

<style scoped>
    .container {
      border: 2px solid #dedede;
      background-color: #f1f1f1;
      border-radius: 5px;
      margin: 10px 0;
    }
    .darker {
      border-color: #aaa;
      background-color: #ccc;
    }
    .container::after {
      content: "";
      clear: both;
      display: table;
    }
    .container img {
      float: left;
      max-width: 60px;
      width: 100%;
      margin-right: 20px;
      border-radius: 50%;
    }
    .container img.right {
      float: right;
      margin-left: 20px;
      margin-right:0;
    }
</style>