<template>
  <Codemirror v-model="text" @focus="focus = true" @blur="focus = false" :extensions="extensions"/>
</template>
<script>
import { watch } from 'vue'
import { Codemirror } from 'vue-codemirror'
import { markdown } from '@codemirror/lang-markdown'
import lodash from "lodash"
export default {
  components: {
    Codemirror
  },
  data() {
    return {
      text: "",
      focus: true,
      extensions: [markdown()]
    }
  },
  methods: {
    set_code(text) {
      if (!this.focus) {
        this.text = text
      }
    }
  },
  mounted() {
    const update = lodash.throttle((newVal) => {
        this.$emit('set_milkdown', newVal, this.focus)
      }, 200)
    watch(() => this.text, (newVal, oldVal) => {
      update(newVal)
    })
  }
}
</script>
<style scoped>

</style>