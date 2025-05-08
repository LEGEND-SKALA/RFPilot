import { createRouter, createWebHistory } from 'vue-router';

import UploadProposal from '../components/UploadProposal.vue';
import ProposalSummary from '../components/ProposalSummary.vue';
import PrototypeGenerator from '../components/PrototypeGenerator.vue';
import EvaluationPage from '../components/EvaluationUpload.vue';
import ScriptUpload from '../components/ScriptUpload.vue';
import VoiceUpload from '../components/VoiceUpload.vue';

const routes = [
  { path: '/script-analysis', name: 'ScriptResult', component: ScriptResult },
  { path: '/prototype-result', name: 'PrototypeResult', component: PrototypeResult },
  { path: '/', name: 'UploadProposal', component: UploadProposal },
  { path: '/summary', name: 'ProposalSummary', component: ProposalSummary },
  { path: '/prototype', name: 'PrototypeGenerator', component: PrototypeGenerator },
  { path: '/evaluation', name: 'EvaluationPage', component: EvaluationPage },
  { path: '/script', name: 'ScriptUpload', component: ScriptUpload },
  { path: '/voice', name: 'VoiceUpload', component: VoiceUpload },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;