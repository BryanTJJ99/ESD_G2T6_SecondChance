<template>
  <TopNavbar/>
  <Sidebar/>
  <div class="container-flex d-flex justify-content-center">
    <div ref="talkjs" style="width: 1000px; height: 700px" class="my-5">
      <i>Loading chat...</i>
      <ActionMenu class="action-menu"> 
          <Icon type="horizontalDots" /> 
      </ActionMenu>
  </div>
  </div>
  <Footer style="margin-left:4.5rem;"></Footer>
</template>

<script>
    import Talk from 'talkjs';
    import TopNavbar from "@/components/Navbar/TopNavbar.vue";
    import Sidebar from "@/components/Navbar/Sidebar.vue"
    import Footer from "@/components/Footer.vue";
    
    import { getAuth, onAuthStateChanged} from "firebase/auth";

    export default {
        components: {
            TopNavbar,
            Sidebar,
            Footer
        },
        data(){
          return {
            deptId: ''
          }
        },
        async mounted() {
          this.deptId = sessionStorage.getItem("deptId")

          this.checkuser()

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
  
        },
        methods: {
          checkuser(){
            const auth = getAuth();
            onAuthStateChanged(auth, (user) => {
                if (!user) {
                    console.log('user is not logged in')
                    window.location.href = `/`;
                }
            });
        },
        }
    }
</script>