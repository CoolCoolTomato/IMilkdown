<template>
  <div class="tree-node" :class="status">
    <div class="title">
      <button @click="toggleNode" v-if="node[showChildren]">
        <Arrow size="20"/>
      </button>
      <div v-show="!node[showChildren]" style="width: 20px; height: 20px"/>
      <p>{{ node[text] }}</p>
    </div>
    <div class="children">
      <div>
        <tree-view
          v-for="c in node[children]"
          :node="c"
          :text="text"
          :children="children"
          :show-children="showChildren"
        />
      </div>
    </div>
  </div>
</template>

<script>

import Arrow from "@/components/Arrow.vue"

export default {
  components: {
    Arrow
  },
  props: {
    node: {
      type: Object,
      required: true
    },
    text: {
      type: String,
      required: true
    },
    children: {
      type: String,
      required: true
    },
    showChildren: {
      type: String,
    }
  },
  data() {
    return {
      status: "hide"
    }
  },
  methods: {
    toggleNode() {
      this.status = this.status === "show" ? "hide" : "show"
    }
  },
  mounted() {

  }
}
</script>

<style scoped>
.tree-node {
  padding-left: 10px;
}
.title {
  display: flex;
  align-items: center;
}
.title:hover {
  background-color: #E0E0E0;
}
.title button {
  border: none;
  cursor: pointer;
  padding: 0;
  display: flex;
  align-items: center;
  transition: 0.2s;
  background: none;
}
.show > .title > button {
  transform: rotateZ(90deg);
}
.hide > .title > button {
  transform: rotateZ(0deg);
}
.title p{
  margin: 0;
  user-select: none;
}
.children {
  overflow: hidden;
  transition: 0.3s;
  max-height: 0;
  display: flex;
  flex-direction: column-reverse;
}
.show > .children {
  max-height: 1000px;
}
.hide > .children {
  max-height: 0;
}
</style>