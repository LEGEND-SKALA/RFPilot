import { createRouter, createWebHistory } from 'vue-router';

import UploadProposal from '../components/proposal/UploadProposal.vue';
import ProposalSummary from '../components/proposal/ProposalSummary.vue';
import LoadingPage from '../components/common/LoadingPage.vue';
import PrototypeGenerator from '../components/prototype/PrototypeGenerator.vue';
import EvaluationPage from '../components/evalutaion/EvaluationUpload.vue';
import ScriptUpload from '../components/script/ScriptUpload.vue';
import VoiceUpload from '../components/voice/VoiceUpload.vue';
import VoiceResult from '../components/voice/VoiceResult.vue';
import EvaluationResult from '../components/evalutaion/EvaluationResult.vue';
import PrototypeResult from '../components/prototype/PrototypeResult.vue';
import ScriptResult from '../components/script/ScriptResult.vue';


const routes = [
  { path: '/script-analysis', name: 'ScriptResult', component: ScriptResult },
  { path: '/prototype-result', name: 'PrototypeResult', component: PrototypeResult },
  { path: '/', name: 'UploadProposal', component: UploadProposal },
  { path: '/loading', name: 'LoadingPage', component: LoadingPage },  
  { path: '/summary', name: 'ProposalSummary', component: ProposalSummary },
  { path: '/prototype', name: 'PrototypeGenerator', component: PrototypeGenerator },
  { path: '/evaluation', name: 'EvaluationPage', component: EvaluationPage },
  { path: '/script', name: 'ScriptUpload', component: ScriptUpload },
  { path: '/voice', name: 'VoiceUpload', component: VoiceUpload },
  { path: '/evaluation-result', name: 'EvaluationResult', component: EvaluationResult },
  {
    path: '/voice-result',
    name: 'VoiceResult',
    component: VoiceResult
  }
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;