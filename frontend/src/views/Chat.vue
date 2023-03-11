<template>
  <TopNavbar/>
  <Sidebar/>
  <div class="container-flex d-flex justify-content-center">
    <div ref="talkjs" style="width: 1000px; height: 700px" class="mt-5">
      <i>Loading chat...</i>
      <ActionMenu class="action-menu"> 
          <Icon type="horizontalDots" /> 
      </ActionMenu>
  </div>

  </div>
</template>

<script>
    import Talk from 'talkjs';
    import TopNavbar from "@/components/Navbar/TopNavbar.vue";
    import Sidebar from "@/components/Navbar/Sidebar.vue"

    export default {
        components: {
            TopNavbar,
            Sidebar
        },
        async mounted() {
          await Talk.ready
          const me = new Talk.User({
            id: 1,
            name: 'Tan Aloysius',
            email: 'aloysius@test.com',
          })
                
          const talkSession = new Talk.Session({
            appId: 'tiPNIXv3',
            me: me,
          });

          const other = new Talk.User({
            id: '654321',
            name: 'Sebastian',
            email: 'Sebastian@example.com',
          });

          const other2 = new Talk.User({
            id: 2,
            name: 'Analisa',
            email: 'Jesus@example.com',
          });

          const conversation2 = talkSession.getOrCreateConversation(
            Talk.oneOnOneId(me, other2)
          );
          
          conversation2.setParticipant(me)
          conversation2.setParticipant(other2)

          const inbox = talkSession.createInbox();
          inbox.select(conversation2)
          inbox.mount(this.$refs.talkjs);
  
        }
    }
</script>