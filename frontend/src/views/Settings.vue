<template>
<div class="AllPolls">
    <v-card
    class="mx-auto pa-3 ma-3"
            elevation="4"
            outlined
            width="65%">
        <v-row>
          <v-col cols="11">
              <v-text-field
                        ref="search"
                        v-model="request"
                        hide-details
                        label="Search"
                        single-line
              ></v-text-field>
          </v-col>
          <v-col cols="1">
              <v-btn
                    icon
                    @click="filter_polls"
                  >
                <v-icon>mdi-magnify</v-icon>
              </v-btn>
          </v-col>
        </v-row>
    </v-card>
</div>
</template>

<script>
export default {
name: "Settings"
}
</script>

<style scoped>

</style>