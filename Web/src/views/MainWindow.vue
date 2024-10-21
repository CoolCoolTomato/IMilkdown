<template>
  <div id="main">
    <div style="display: flex; height: 100%">
      <splitpanes class="default-theme">
        <pane max-size="20">
          <tree-view :node="nodes" text="name" children="sub_nodes" show-children="is_folder"/>
        </pane>
        <pane>
          <div id="editor">
            <div id="text">
              <Codemirror @set_milkdown="set_milkdown" ref="codemirror"/>
            </div>
            <div id="markdown">
              <Milkdown @set_codemirror="set_codemirror" ref="milkdown"/>
            </div>
          </div>
        </pane>
      </splitpanes>
    </div>
  </div>
</template>

<script>
import nodeApi from "@/api/nodeApi.js"
import TreeView from "@/components/TreeView.vue"
import Milkdown from "@/components/Milkdown.vue"
import Codemirror from "@/components/CodeMirror.vue"
import { Splitpanes, Pane } from 'splitpanes'
import 'splitpanes/dist/splitpanes.css'

export default {
  components: {
    Codemirror,
    TreeView,
    Milkdown,
    Splitpanes,
    Pane
  },
  data() {
    return {
      nodes: {},
      editor_text: "",
      milkdown_text: ""
    }
  },
  methods: {
    get_nodes(){
      nodeApi.get_nodes({
        path: "C:/Users/liuqiukai/Desktop/articles"
      }).then(res => {
        this.nodes = res.nodes
      }).catch(error => {
        console.log(error)
      })
    },
    set_codemirror(text) {
      this.$refs.codemirror.set_code(text)
    },
    set_milkdown(text, focus) {
      this.$refs.milkdown.set_text(text, focus)
    },
  },
  mounted() {
    this.get_nodes()
  }
}
</script>
<style>
#main {
  width: 100%;
  height: 100vh;
  background: #EEEEEE;
}
#editor {
  width: 100%;
  height: 100%;
  display: grid;
  grid-template-columns: 1fr 1fr;
}
#text {
  overflow-y: scroll;
}
#text textarea {
  width: 100%;
  height: 100%;
  resize: none;
  border: none;
  padding: 0;
  box-shadow: none;
  font-size: 20px;
}
#text textarea:focus {
  border: none;
  box-shadow: none;
}
#markdown {
  overflow-y: scroll;
}
</style>