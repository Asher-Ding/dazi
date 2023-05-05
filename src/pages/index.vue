<template>
	<view class="content">
		<Navbar></Navbar>
		<Chatpage></Chatpage>
		<Bulletin></Bulletin>
		<Sendbox></Sendbox>
	</view>
</template>

<script>
import Navbar from 'components/navbar.vue'
import Chatpage from 'components/chatpage.vue'
import Bulletin from 'components/card/bulletin.vue'
import Sendbox from 'components/sendbox.vue'

export default {
	name: 'Index',
	components: {
		Navbar,
		Chatpage,
		Bulletin,
		Sendbox
	},
	data() {
		return {
			messages: [
				{ text: "Hi there!", isMine: false },
				{ text: "Hey! What's up?", isMine: true }
			],
			newMessageText: ''
		};
	},
	onLoad() {

	},
	methods: {
		toggleMenu() {
			console.log('toggleMenu')
		},
		sendMessage() {
			this.messages.push({
				text: this.newMessageText,
				isMine: true
			})
			this.newMessageText = ""
		}
	}
}
</script>

<style></style>
