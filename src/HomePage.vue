<script lang="ts">
import { defineComponent } from "vue";
import { ServerBrowser } from "./components";
import { ServerType } from "./schema";

export default defineComponent({
  name: "HomePage",
  components: { ServerBrowser },
  setup() {
    return {
      servers: [
        {
          name: "My ParaView server",
          host: "paraview.org",
          port: 1111,
          type: ServerType.ClientServer,
          waitTime: 0,
          startupCommand: "",
        },
      ],
    };
  },
});
</script>

<template>
  <div id="app">
    <v-app>
      <server-browser :servers="servers" />
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
