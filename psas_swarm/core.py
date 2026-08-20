import torch
import torch.nn.functional as F
from google import genai
from google.colab import userdata

class PhaseShiftedAgentRouter:
    def __init__(self, model='gemini-3.6-flash', device=None):
        self.model = model
        self.device = device or torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.client = genai.Client(api_key=userdata.get("GEMINI_API_KEY"))

    def __call__(self, compressed_latents):
        # 1. Compute latent entropy & topological variance from the tensor
        probs = F.softmax(compressed_latents.float(), dim=-1)
        entropy = torch.distributions.Categorical(probs=probs).entropy().mean().item()
        
        # 2. Formulate phase-shifted verification prompt based on latent state metrics
        prompt = (
            f"Analyze compressed latent tensor of shape {tuple(compressed_latents.shape)} "
            f"exhibiting systemic entropy {entropy:.4f}. "
            "Evaluate topological validity, detect potential hallucination vectors, and output the Final Cognitive Routing State."
        )

        instruction = "You are the Phase-Shifted Agentic Swarm (PSAS) cognitive router. Enforce strict thermodynamic and logical consistency."
        
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=instruction,
                temperature=0.1
            )
        )
        return response.text

    def verify(self, prompt):
        # Backward-compatible helper for direct string prompts
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=genai.types.GenerateContentConfig(temperature=0.1)
        )
        return response.text
