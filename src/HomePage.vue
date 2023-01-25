<script lang="ts">
import { defineComponent, reactive } from "vue";
import { ServerBrowser } from "./components";
import { Server } from "./schema";

export default defineComponent({
  name: "HomePage",
  components: { ServerBrowser },
  setup() {
    const servers = reactive<Server[]>([]);

    function addServer(server: Server) {
      servers.push(server);
    }

    function updateServer(oldServer: Server, newServer: Server) {
      console.log(oldServer, newServer);
    }

    return {
      servers,
      addServer,
      updateServer,
    };
  },
});
</script>

<template>
  <div id="app">
    <v-app>
      <server-browser
        :servers="servers"
        @add="addServer"
        @update="updateServer"
      />
    </v-app>
  </div>
</template>

<style scoped>
.container-1 {
  margin: 10px;
  padding: 10px;
  width: 400px;
  background-color: black;
}
.container-2 {
  margin: 10px;
  padding: 10px;
  border: 1px dashed black;
  width: 700px;
}
</style>
