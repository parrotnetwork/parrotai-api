import requests
from typing import Dict, Any

class ParrotAPI:
    """A Python wrapper for interacting with the Parrot API.

    Attributes:
        api_key (str): The API key used for authentication.
        base_url (str): The base URL for the Parrot API.
        headers (dict): The headers to include in API requests.
    """
    
    def __init__(self, api_key: str) -> None:
        """Initialize the ParrotAPI with an API key.
        
        Args:
            api_key: A valid API key as a string.
        """
        self.api_key = api_key
        self.base_url = "http://api.joinparrot.ai/v1"
        self.headers = {"Authorization": api_key}

    def refresh_token(self, refresh_token: str) -> Dict[str, Any]:
        """Refresh the API token using a refresh token.
        
        Args:
            refresh_token: The refresh token as a string.
        
        Returns:
            A dictionary with the new token information.
        """
        url = f"{self.base_url}/user/refresh_token"
        payload = {"refresh_token": refresh_token}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def get_user_profile(self) -> Dict[str, Any]:
        """Retrieve the user's profile information.
        
        Returns:
            A dictionary containing the user's profile information.
        """
        url = f"{self.base_url}/user/me"
        response = requests.post(url, headers=self.headers)
        return response.json()

    def get_task_history(self) -> Dict[str, Any]:
        """Retrieve the user's task history.
        
        Returns:
            A dictionary containing the user's task history.
        """
        url = f"{self.base_url}/user/history"
        response = requests.post(url, headers=self.headers)
        return response.json()

    def create_config(self, rotation: str = "square", steps: int = 100, negative_prompt: str = "") -> Dict[str, Any]:
        """Helper function to create a configuration for the create_sdxl_task.
        
        Args:
            rotation: The orientation of the image ('square', 'landscape', 'portrait').
            steps: The number of steps for the image generation process.
            negative_prompt: Aspects to avoid in the generated image.
        
        Returns:
            A configuration dictionary for the image task.
        """
        return {
            "rotation": rotation,
            "steps": steps,
            "negative_prompt": negative_prompt
        }

    def create_sdxl_task(self, prompt: str, rotation: str = "square", steps: int = 100, negative_prompt: str = "") -> Dict[str, Any]:
        """Create an SDXL-turbo image task with a prompt and configuration.
        
        Args:
            prompt: Description of the image to be generated.
            rotation: Image rotation preference.
            steps: Number of generation steps.
            negative_prompt: Negative aspects to avoid in the image.
        
        Returns:
            A dictionary with the task creation response.
        """
        config = self.create_config(rotation, steps, negative_prompt)
        url = f"{self.base_url}/user/create_sdxl_task"
        payload = {"prompt": prompt, "config": config}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def create_sd_task(self, prompt: str, rotation: str = "square", steps: int = 100, negative_prompt: str = "") -> Dict[str, Any]:
        """Create an SD1.5 image task with a prompt and configuration.
        
        Args:
            prompt: Description of the image to be generated.
            rotation: Image rotation preference.
            steps: Number of generation steps.
            negative_prompt: Negative aspects to avoid in the image.
        
        Returns:
            A dictionary with the task creation response.
        """
        config = self.create_config(rotation, steps, negative_prompt)
        url = f"{self.base_url}/user/create_sd_task"
        payload = {"prompt": prompt, "config": config}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def create_lora_trainer_task(self, prompt: str, images: List[str]) -> Dict[str, Any]:
        """Create a LORA training task with the given prompt and images.

        Args:
            prompt: The text prompt for fine-tuning.
            images: A list of URLs pointing to images for fine-tuning.

        Returns:
            A dictionary containing the task ID and other response data.
        """
        url = f"{self.base_url}/user/create_lora_trainner_task"
        payload = {"prompt": prompt, "images": images}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def submit_feedback(self, task_id: str, rating: float, feedback: str) -> Dict[str, Any]:
        """Submit feedback for a completed task.

        Args:
            task_id: The unique identifier of the task.
            rating: A numeric rating value for the task outcome.
            feedback: Textual feedback about the task.

        Returns:
            A dictionary indicating the status of the feedback submission.
        """
        url = f"{self.base_url}/user/feedback"
        payload = {"task_id": task_id, "rating": rating, "feedback": feedback}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()