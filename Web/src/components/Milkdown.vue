<template>
  <div id="milkdown"/>
</template>
<script>
import { Crepe } from '@milkdown/crepe'
import { replaceAll, getMarkdown } from '@milkdown/kit/utils'

import "@milkdown/crepe/theme/common/style.css"
import "@milkdown/crepe/theme/frame.css"

export default {
  data() {
    return {
      editor: null
    }
  },
  methods: {
    async init_milkdown() {
      let crepe = new Crepe({
        root: document.getElementById('milkdown'),
        defaultValue: 'Hello, Milkdown!',
      })

      await crepe.create()
      this.editor = crepe.editor
    },
    set_text(text) {
      this.editor.action(replaceAll(text))
    },
    get_text() {
      return this.editor.action(getMarkdown())
    },
  },
  async mounted() {
    await this.init_milkdown()
  }
}
</script>