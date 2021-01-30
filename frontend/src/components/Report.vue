<template>
    <div class="vue-report">
        <v-list two-line>
        <v-list-item-group
          v-model="selected"
          active-class="teal--text"
          multiple

        >
          <template v-for="(report, index) in reports">
            <v-list-item :key="report.title">
              <template v-slot:default="{ active }">
                <v-list-item-content>
                  <v-list-item-title v-text="report.title"></v-list-item-title>
                </v-list-item-content>

                <v-list-item-action>
                  <v-list-item-action-text v-text="report.action"></v-list-item-action-text>

                  <v-dialog v-model="dialog" persistent max-width="700px">
                      <template v-slot:activator="{ on, attrs }">
                          <v-btn
                              icon
                              v-if="!active"
                              color="grey lighten-1"
                              style="position: relative; "
                              v-bind="attrs"
                              v-on="on">
                              <v-icon>mdi-message</v-icon>
                            </v-btn>
                        <v-btn
                              icon
                              v-else
                              color="red darken-3"
                              style="position: relative; "
                              v-bind="attrs"
                              v-on="on">
                              <v-icon> mdi-message-alert</v-icon>
                            </v-btn>
                      </template>
                    <v-card class="mx-auto pa-3"
                    elevation="4"
                    outlined
                    width="100%">

                    <v-btn
                        @click="$router.go(0);"
                        icon
                        large
                        depressed
                        color="red"
                        style="position: absolute; right: 20px;"
                    >
                      <v-icon>mdi-close-circle-outline</v-icon>
                    </v-btn>
                      <br>
                    <v-text-field v-model="report.title" label="Title"></v-text-field>
                      <v-text-field v-model="report.subtitle" label="Subtitle"></v-text-field>
                      <v-list-item v-for="(message, i) in messages" :key="i">
                        <v-card class="px-3 ma-2" outlined width="100%" style="text-align: left;">
                          <v-row justify="space-between">
                            <v-col md="auto">
                              <strong style="color: #800080; cursor: pointer;">
                                <u>{{ message.author.name }}:</u>
                              </strong>
                            </v-col>
                            <v-col md="7">
                              {{ message.text }}
                            </v-col>
                          </v-row>
                        </v-card>
                      </v-list-item>
                      <br>
                      <v-row justify="space-between" no-gutters class="px-6">
                        <v-col md="10">
                          <v-text-field
                                  v-model="message"
                                  label="Message.."
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
          </v-dialog>

                </v-list-item-action>
              </template>
            </v-list-item>

            <v-divider
              v-if="index < reports.length - 1"
              :key="index"
            ></v-divider>
          </template>
        </v-list-item-group>
      </v-list>
    </div>
</template>

<script>

    export default{
        name: 'Report',
        props: {
            author: {
                type: Object,
                required: true
            },
            user: {
                type: Object,
                required: true
            },
            id: {
                type: Number,
                required: true
            },
            title: {
                type: String,
                required: true
            },
            subtitle: {
                type: String,
                required: true
            },
        },
        data(){
            return {
                visibleResults: JSON.parse(this.showResults),
                time: {h: 0, m: 0, s: 0},
                interval: null,
                finalResults: false,
                messages: [],
                selected: [],
                reports: [
                  {
                  action: '15 min',
                  subtitle: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
                  title: 'Ali Connors',
                },
                {
                  action: '2 hr',
                  subtitle: `Wish I could come, but I'm out of town this weekend.`,
                  title: 'me, Scrott, Jennifer',
                },
                {
                  action: '6 hr',
                  subtitle: 'Do you have Paris recommendations? Have you ever been?',
                  title: 'Sandra Adams',
                },
                {
                  action: '12 hr',
                  subtitle: 'Have any ideas about what we should get Heidi for her birthday?',
                  title: 'Trevor Hansen',
                },
                {
                  action: '18hr',
                  headline: 'Recipe to try',
                  subtitle: 'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
                  title: 'Britta Holt',
                },
              ],
            }
        },
        computed: {

        },
        methods: {
          send_message(){
              this.axios.post(
                          'http://localhost:8000/api/messages/',
                          {
                            "user_id": this.user.id,
                            "title": this.report.title,
                            "text": this.report.subtitle,
                            "action": this.report.action,
                          },
                          {
                            headers: {Authorization: `Token ${this.user.token}`}
                          }
                  ).then(response => {
                    if (response.data.status === 200) {
                      this.messages.push(response.data.report)
                      this.report = ''
                    }
                  })
            },
        },
        mounted() {
        }
    }

</script>

<style>
    .vue-report{
      font-family: 'Avenir', Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      color: #2c3e50;
    }
</style>