<template>
  <div id="main">
    <tree-view :node="nodes" text="name" children="sub_nodes" show-children="is_folder"/>
  </div>
</template>

<script>
import nodeApi from "@/api/nodeApi.js"
import TreeView from "@/components/TreeView.vue"

export default {
  components: {
    TreeView
  },
  data() {
    return {
      nodes: {}
    }
  },
  methods: {
    get_nodes(){
      nodeApi.get_nodes({
        path: "W:/code/Python/Imilkdown/Server"
      }).then(res => {
        this.nodes = res.nodes
        console.log(this.nodes)
      }).catch(error => {
        console.log(error)
      })
    }
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

</style>