from groq import Groq
from config import API_CONFIG
import json

class InternHubAgent:
    def __init__(self):
        self.client = Groq(api_key=API_CONFIG["api_key"])
        self.model = API_CONFIG["model"]
    
    def call_groq_api(self, prompt: str) -> str:
        try:
            message = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model=self.model,
                temperature=API_CONFIG["temperature"],
                max_tokens=API_CONFIG["max_tokens"],
            )
            return message.choices[0].message.content
        except Exception as e:
            return f"❌ Error calling Groq API: {str(e)}"
    
    def analyze_match(self, student_profile: dict, internship_jd: dict) -> dict:

        
        # Extract data
        student_skills = ", ".join(student_profile.get("skills", []))
        student_interests = ", ".join(student_profile.get("interests", []))
        student_experience = student_profile.get("experience", "Fresher")
        
        jd_requirements = internship_jd.get("requirements", "")
        jd_description = internship_jd.get("description", "")
        jd_role = internship_jd.get("role", "Intern")
        
        # 1. MATCH PERCENTAGE PROMPT
        match_prompt = f"""
        Analyze the internship match between a student and a job role.
        
        STUDENT PROFILE:
        - Skills: {student_skills}
        - Interests: {student_interests}
        - Experience: {student_experience}
        
        JOB REQUIREMENTS:
        - Role: {jd_role}
        - Requirements: {jd_requirements}
        - Description: {jd_description}
        
        Please provide ONLY:
        1. A match percentage (0-100%)
        2. A one-line match summary
        
        Format: "MATCH: 85% | Summary: Strong Python skills match the backend requirements"
        """
        
        match_response = self.call_groq_api(match_prompt)
        
        # 2. SKILL GAP PROMPT
        gap_prompt = f"""
        Identify skill gaps for this student applying to this internship.
        
        STUDENT SKILLS: {student_skills}
        JOB REQUIREMENTS: {jd_requirements}
        
        Please provide:
        1. Skills the student has that match (list 3-4)
        2. Critical skills missing (list 3-4)
        3. Nice-to-have skills to learn
        
        Keep it concise and actionable.
        """
        
        gap_response = self.call_groq_api(gap_prompt)
        
        # 3. RECOMMENDATION PROMPT
        recommendation_prompt = f"""
        Write a brief recommendation (2-3 sentences) on whether this student should apply to this {jd_role} role.
        
        STUDENT: {student_profile.get('name', 'Student')} with skills in {student_skills}
        ROLE: {jd_role}
        REQUIREMENTS: {jd_requirements}
        EXPERIENCE: {student_experience}
        
        Be honest and encouraging. Consider their potential to grow.
        """
        
        recommendation_response = self.call_groq_api(recommendation_prompt)
        
        # 4. TAILORED RESUME PROMPT
        resume_prompt = f"""
        Generate a brief tailored resume summary for this job application.
        
        STUDENT NAME: {student_profile.get('name', 'Your Name')}
        SKILLS: {student_skills}
        INTERESTS: {student_interests}
        EXPERIENCE: {student_experience}
        JOB ROLE: {jd_role}
        JOB REQUIREMENTS: {jd_requirements}
        
        Create a 4-5 line resume summary that:
        1. Highlights relevant skills
        2. Shows alignment with JD
        3. Uses industry keywords from the JD
        4. Is ATS-optimized (simple formatting, clear keywords)
        
        Format as a professional summary section.
        """
        
        resume_response = self.call_groq_api(resume_prompt)
        
        # 5. CONFIDENCE SCORE PROMPT
        confidence_prompt = f"""
        Calculate an ATS (Applicant Tracking System) match score (0-100) for this candidate.
        
        STUDENT PROFILE: {json.dumps(student_profile)}
        JOB REQUIREMENTS: {jd_requirements}
        
        Consider:
        - Keyword matches (40%)
        - Skill alignment (40%)
        - Experience level (20%)
        
        Provide ONLY the score and 2-3 factors affecting the score.
        Format: "ATS SCORE: 78/100 | Factors: Strong Python match, Missing DevOps, Good ML foundation"
        """
        
        confidence_response = self.call_groq_api(confidence_prompt)
        
        # Return comprehensive results
        return {
            "match_summary": match_response,
            "skill_gaps": gap_response,
            "recommendation": recommendation_response,
            "tailored_resume": resume_response,
            "confidence_score": confidence_response,
        }
    
    def format_output(self, results: dict) -> str:
        """
        Format all results into a readable output
        """
        output = f"""
╔════════════════════════════════════════════════════════════════╗
║           🤖 InternHub AI Agent - Analysis Report              ║
╚════════════════════════════════════════════════════════════════╝

📊 INTERNSHIP MATCH ANALYSIS
{'-' * 64}
{results['match_summary']}

🎯 SKILL GAP ANALYSIS
{'-' * 64}
{results['skill_gaps']}

💡 RECOMMENDATION
{'-' * 64}
{results['recommendation']}

📄 TAILORED RESUME SUMMARY
{'-' * 64}
{results['tailored_resume']}

🔐 ATS & CONFIDENCE SCORE
{'-' * 64}
{results['confidence_score']}

{'-' * 64}
Generated by InternHub AI Agent (Powered by Groq + Mixtral)
"""
        return output
