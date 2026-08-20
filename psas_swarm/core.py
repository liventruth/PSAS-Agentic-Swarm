import time
from google import genai
from google.colab import userdata

class PhaseShiftedAgentRouter:
    def __init__(self, model='gemini-2.5-flash'):
        self.model = model
        self.client = genai.Client(api_key=userdata.get("GEMINI_API_KEY"))

    def _agent_alpha(self, prompt):
        instruction = "You are a strict physics and mathematics engine. Do not speculate. Rely strictly on thermodynamic and material constraints."
        response = self.client.models.generate_content(
            model=self.model, contents=prompt,
            config=genai.types.GenerateContentConfig(system_instruction=instruction, temperature=0.0)
        )
        return response.text

    def _agent_beta(self, prompt):
        instruction = "You are a theoretical lateral-thinking architect. Look for edge cases, acoustic topological mapping, and alternative geometric interpretations."
        response = self.client.models.generate_content(
            model=self.model, contents=prompt,
            config=genai.types.GenerateContentConfig(system_instruction=instruction, temperature=0.8)
        )
        return response.text

    def _agent_gamma(self, prompt):
        instruction = "You are an adversarial logic filter. Find logical fallacies or impossible physics constraints in the prompt."
        response = self.client.models.generate_content(
            model=self.model, contents=prompt,
            config=genai.types.GenerateContentConfig(system_instruction=instruction, temperature=0.4)
        )
        return response.text

    def verify(self, prompt):
        print("[*] Initiating Phase-Shifted Swarm...")
        alpha_state = self._agent_alpha(prompt)
        time.sleep(2)
        beta_state = self._agent_beta(prompt)
        time.sleep(2)
        gamma_state = self._agent_gamma(prompt)
        time.sleep(2)

        print("[*] Swarm complete. Engaging Interference Engine...")
        interference_prompt = (
            "Evaluate these three cognitive frequencies:\n\n"
            f"[Alpha]: {alpha_state}\n\n[Beta]: {beta_state}\n\n[Gamma]: {gamma_state}\n\n"
            "DIRECTIVE: Calculate Consensus Delta. Apply Destructive Interference to sever logic branches that violate Gamma or Alpha. Output the Final Verifiable Truth State."
        )
        response = self.client.models.generate_content(
            model=self.model, contents=interference_prompt,
            config=genai.types.GenerateContentConfig(temperature=0.1)
        )
        return response.text
