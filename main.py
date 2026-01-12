#!/usr/bin/env python3
import json
import sys
from agent import InternHubAgent

def load_json_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found!")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Error: Invalid JSON in '{file_path}'!")
        sys.exit(1)

def get_user_input() -> tuple:
    print("\n" + "="*70)
    print("🚀 Welcome to InternHub AI Agent")
    print("="*70)
    print("\nChoose input method:")
    print("1. Use example JSON files (quick demo)")
    print("2. Enter data manually (interactive)")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == "1":
        return load_json_file("example_inputs/student_profile.json"), load_json_file("example_inputs/internship_jd.json")
    elif choice == "2":
        return get_manual_input()
    else:
        print("❌ Invalid choice!")
        sys.exit(1)

def get_manual_input() -> tuple:
    print("\n📋 Enter Student Profile Information:")
    print("-" * 50)
    
    name = input("Student Name: ").strip()
    skills_input = input("Skills (comma-separated, e.g., Python,React,ML): ").strip()
    interests_input = input("Interests (comma-separated, e.g., AI,Web Dev): ").strip()
    experience = input("Experience (e.g., Fresher, 6 months Python, 1 year): ").strip() or "Fresher"
    
    student_profile = {
        "name": name,
        "skills": [s.strip() for s in skills_input.split(",")],
        "interests": [i.strip() for i in interests_input.split(",")],
        "experience": experience
    }
    
    print("\n📝 Enter Internship Job Description:")
    print("-" * 50)
    
    role = input("Role Title (e.g., AI Engineering Intern): ").strip()
    requirements = input("Key Requirements (comma-separated or paragraph): ").strip()
    description = input("Role Description (brief): ").strip()
    
    internship_jd = {
        "role": role,
        "requirements": requirements,
        "description": description
    }
    
    return student_profile, internship_jd

def main():
    """Main function"""
    try:
        # Get input
        student_profile, internship_jd = get_user_input()
        
        # Initialize agent
        print("\n🤖 Initializing InternHub AI Agent...")
        agent = InternHubAgent()
        
        # Analyze match
        print("⏳ Analyzing internship match... (this may take a few seconds)")
        results = agent.analyze_match(student_profile, internship_jd)
        
        # Format and display output
        output = agent.format_output(results)
        print(output)
        
        # Save results to file
        output_file = "analysis_report.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(output)

        print(f"\n✅ Report saved to: {output_file}")
        
    except KeyboardInterrupt:
        print("\n\n❌ Process interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
