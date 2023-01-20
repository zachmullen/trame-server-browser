<script lang="ts">
import { Server, ServerSchemes } from "../schema";

export default {
  props: {
    servers: {
      type: Array as () => Server[],
      required: true,
    },
    tableHeight: {
      type: Number,
      default: 500,
    },
  },
  data() {
    return {
      addDialogOpen: false,
      selectedServers: [],
      headers: [
        {
          text: "Configuration",
          value: "name",
        },
        {
          text: "Server",
          value: "url",
        },
        {
          text: "",
          value: "actions",
          sortable: false,
        },
      ],
      timeout: 60,
    };
  },
  methods: {
    editServer(server: Server) {
      console.log(server);
    },
    getScheme(server: Server): string {
      return ServerSchemes[server.type];
    },
  },
};
</script>

<template>
  <div>
    <v-toolbar color="#424242" dense elevation="0">
      <v-btn @click="$emit('loadServers')" class="px-1 mr-3" text dark small>
        <v-icon class="mr-1">mdi-server-plus</v-icon>
        Load Servers
      </v-btn>
      <v-btn
        @click="$emit('saveServers')"
        class="px-1 mr-3"
        text
        dark
        small
        :disabled="!selectedServers.length"
      >
        <v-icon class="mr-1">mdi-content-save</v-icon>
        Save Servers
      </v-btn>
      <v-btn @click="$emit('fetchServers')" class="px-1 mr-3" text dark small>
        <v-icon class="mr-1">mdi-refresh</v-icon>
        Fetch Servers
      </v-btn>
      <v-spacer />
      <v-btn @click="addDialogOpen = true" small rounded color="primary">
        <v-icon small class="mr-1">mdi-plus-circle</v-icon>
        Add Server
      </v-btn>
    </v-toolbar>
    <v-data-table
      class="server-list-data-table"
      v-model="selectedServers"
      :headers="headers"
      :items="servers"
      item-key="name"
      show-select
      :height="tableHeight"
    >
      <template v-slot:no-data>
        <v-container>
          <v-row>
            <v-col class="pt-5">
              <v-icon large>mdi-information-outline</v-icon>
              <div class="mt-3 text-h5">No servers found</div>
              <div class="mt-3 text-subtitle-1 font-italic">
                You may load or fetch existing servers or click "Add Server" to
                get started.
              </div>
            </v-col>
          </v-row>
        </v-container>
      </template>
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template v-slot:item.url="{ item: server }">
        <div>{{ getScheme(server) }}://{{ server.host }}:{{ server.port }}</div>
      </template>
      <!-- eslint-disable-next-line vue/valid-v-slot -->
      <template v-slot:item.actions="{ item: server }">
        <v-btn color="primary" @click="editServer(server)" icon>
          <v-icon>mdi-pencil</v-icon>
        </v-btn>
      </template>
    </v-data-table>
    <v-toolbar color="#f5f5f5" elevation="0" height="80">
      <v-col style="max-width: 140px">
        <v-text-field
          type="number"
          outlined
          hide-details
          label="Timeout (s)"
          v-model="timeout"
          dense
        />
      </v-col>
      <v-spacer />
      <v-btn class="mr-3" @click="$emit('close')">Close</v-btn>
      <v-btn color="primary" :disabled="selectedServers.length !== 1">
        <v-icon class="mr-1">mdi-connection</v-icon>
        Connect
      </v-btn>
    </v-toolbar>
  </div>
</template>

<style scoped></style>

<style lang="scss">
.server-list-data-table {
  border-bottom: 1px solid #e5e5e5;

  th {
    background-color: #eee;
    border-right: 1px solid #ddd;

    &:last-child {
      border-right: none;
    }
  }
}
</style>
