<template>
  <div id="milkdown"/>
</template>
<script>
import { Crepe } from '@milkdown/crepe'
import { replaceAll, getMarkdown } from '@milkdown/kit/utils'
import { listener, listenerCtx } from '@milkdown/kit/plugin/listener'

import lodash from "lodash"
import "@milkdown/crepe/theme/common/style.css"
import "@milkdown/crepe/theme/frame.css"

export default {
  data() {
    return {
      editor: null,
    }
  },
  methods: {
    async init_milkdown() {
      let crepe = new Crepe({
        root: document.getElementById('milkdown'),
        defaultValue: '',
      })
      crepe.editor.use(listener)
      await crepe.create()
      this.editor = crepe.editor
    },
    set_text(text, focus) {
      if (focus) {
        this.editor.action(replaceAll(text))
      }
    },
    get_text() {
      return this.editor.action(getMarkdown())
    },
  },
  async mounted() {
    await this.init_milkdown()
    const update = lodash.throttle((markdown) => {
      this.$emit('set_codemirror', markdown)
    }, 200)
    this.editor.action((ctx) => {
      ctx.get(listenerCtx).markdownUpdated((ctx, markdown, prevMarkdown) => {
        update(markdown)
      })
    })
  },
}
</script>