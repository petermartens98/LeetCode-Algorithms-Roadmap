class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            at_index = email.index('@')
            local_name = email[:at_index]
            domain_name = email[at_index:]
            if '+' in local_name:
                local_name = local_name[:local_name.index('+')]
            local_name = local_name.replace('.', '')
            unique_emails.add(local_name + domain_name)
        return len(unique_emails)
