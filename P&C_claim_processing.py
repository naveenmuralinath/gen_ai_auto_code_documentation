# claims_processing.py

class Claim:
    """
    Represents an insurance claim.
    Attributes:
        claim_id (str): Unique identifier for the claim.
        policy_id (str): Associated policy ID.
        claim_amount (float): Amount of the claim.
        status (str): Status of the claim ('Pending', 'Approved', 'Rejected').
    """
    def __init__(self, claim_id, policy_id, claim_amount):
        self.claim_id = claim_id
        self.policy_id = policy_id
        self.claim_amount = claim_amount
        self.status = "Pending"

    def approve_claim(self):
        """
        Approves the claim and updates its status.
        """
        self.status = "Approved"

    def reject_claim(self):
        """
        Rejects the claim and updates its status.
        """
        self.status = "Rejected"


class Policy:
    """
    Represents an insurance policy.
    Attributes:
        policy_id (str): Unique identifier for the policy.
        policy_holder (str): Name of the policyholder.
        premium_amount (float): Annual premium amount.
    """
    def __init__(self, policy_id, policy_holder, premium_amount):
        self.policy_id = policy_id
        self.policy_holder = policy_holder
        self.premium_amount = premium_amount

    def update_premium(self, new_premium):
        """
        Updates the premium amount of the policy.
        Args:
            new_premium (float): New premium amount.
        """
        self.premium_amount = new_premium


def process_claim(claim, policy):
    """
    Processes a claim based on the associated policy details.
    Args:
        claim (Claim): The claim to be processed.
        policy (Policy): The policy associated with the claim.
    Returns:
        str: Result of claim processing.
    """
    if claim.claim_amount <= policy.premium_amount * 10:
        claim.approve_claim()
        return f"Claim {claim.claim_id} approved for policy {policy.policy_id}."
    else:
        claim.reject_claim()
        return f"Claim {claim.claim_id} rejected for policy {policy.policy_id}."