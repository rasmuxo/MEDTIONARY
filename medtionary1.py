import difflib
import colorama
from colorama import Fore, Style

# Initialize colorama for colored text
colorama.init()

# Dictionary of medical terms and their definitions
medical_dictionary = {
    "anatomy": "The branch of science that deals with the structure of organisms.",
    "blood pressure": "The force exerted by circulating blood against the walls of the blood vessels.",
    "diagnosis": "The identification of the nature of an illness or other problem by examination of the symptoms.",
    "fever": "A temporary increase in body temperature, often due to an illness or infection.",
    "hospital": "An institution providing medical and surgical treatment and nursing care for sick or injured people.",
    "immunization": "The process by which an individual's immune system becomes fortified against an agent (known as an immunogen).",
    "joint": "The point where two or more bones meet in the body, allowing for movement and flexibility.",
    "kidney": "A vital organ that filters waste products from the blood and regulates fluid and electrolyte balance.",
    "lungs": "The primary organs of respiration in humans, responsible for taking in oxygen and expelling carbon dioxide.",
    "medication": "A substance used to treat, cure, or prevent a disease or medical condition.",
    "nurse": "A healthcare professional trained to care for individuals, families, and communities to maintain or recover optimal health.",
    "oxygen": "A chemical element that is essential for life and is used by the body to produce energy.",
    "pulse": "The rhythmic beating of the heart, which can be felt in various parts of the body, such as the wrist or neck.",
    "radiology": "The medical specialty that uses imaging techniques, such as X-rays, to diagnose and treat diseases and injuries.",
    "surgery": "The branch of medicine that uses operative techniques to treat injuries, diseases, or other medical conditions through incisions in the body.",
    "thermometer": "An instrument used to measure temperature, often used to monitor fever or changes in body heat.",
    "ultrasound": "A diagnostic medical imaging technique that uses high-frequency sound waves to create images of the inside of the body.",
    "vaccination": "The administration of a vaccine to stimulate an individual's immune system to produce immunity to a specific disease.",
    "x-ray": "A form of electromagnetic radiation that can pass through most objects, used in medical imaging to visualize the inside of the body.",
    "allergy": "An abnormal immune system response to substances that are usually harmless, resulting in symptoms such as sneezing, itching, or hives.",
    "bronchitis": "An inflammation of the lining of the bronchial tubes, often caused by infections or irritants.",
    "cholesterol": "A waxy, fat-like substance found in the cells of the body and in certain foods; high levels can increase the risk of heart disease.",
    "diabetes": "A chronic condition that affects how the body processes glucose (sugar) and can lead to high blood sugar levels.",
    "eczema": "A chronic skin condition characterized by redness, itching, and inflammation of the skin.",
    "flu": "A contagious respiratory illness caused by influenza viruses, resulting in symptoms such as fever, cough, and body aches.",
    "gastroenteritis": "An inflammation of the stomach and intestines, often causing symptoms like diarrhea and vomiting.",
    "hypertension": "High blood pressure, a condition in which the force of the blood against the artery walls is consistently too high.",
    "insomnia": "A sleep disorder characterized by difficulty falling asleep or staying asleep, leading to inadequate sleep and daytime fatigue.",
    "jaundice": "A yellowing of the skin and the whites of the eyes, often due to liver or gallbladder problems.",
    "liver": "A vital organ responsible for detoxifying chemicals, metabolizing drugs, and producing bile for digestion.",
    "malaria": "A mosquito-borne infectious disease characterized by fever, chills, and flu-like symptoms.",
    "neurology": "The branch of medicine that deals with the anatomy, functions, and disorders of the nervous system.",
    "obesity": "Excessive accumulation of body fat, often associated with health problems such as heart disease and diabetes.",
    "pneumonia": "An inflammatory lung condition characterized by fever, cough, and difficulty breathing, often caused by infection.",
    "quarantine": "The isolation of individuals who may have been exposed to a contagious disease to prevent its spread.",
    "respiratory": "Relating to the organs and structures involved in breathing, such as the lungs and airways.",
    "stroke": "A sudden interruption of blood supply to the brain, leading to damage of brain tissue and neurological symptoms.",
    "tumor": "An abnormal mass or lump of cells that may be benign (noncancerous) or malignant (cancerous).",
    "urinary": "Relating to the organs and structures involved in the production and elimination of urine.",
    "virus": "A microscopic infectious agent that replicates inside living cells and can cause diseases in humans and animals.",
    "wound": "An injury to the body, typically involving a break in the skin, often requiring medical attention.",
    "anesthesia": "A medical technique used to induce a temporary loss of sensation or consciousness during surgery or medical procedures.",
    "biopsy": "The removal of a small sample of tissue for examination under a microscope to diagnose diseases or conditions.",
    "cancer": "A group of diseases characterized by uncontrolled cell growth and the potential to invade or spread to other parts of the body.",
    "depression": "A mood disorder characterized by persistent feelings of sadness, hopelessness, and a lack of interest or pleasure in daily activities.",
    "epidemic": "The widespread occurrence of a disease in a specific geographic area or population during a particular period of time.",
    "fertility": "The ability to conceive and produce offspring; often used to refer to the ability to become pregnant or impregnate.",
    "genes": "The segments of DNA that contain the instructions for building and maintaining the structures and functions of the body.",
    "heart attack": "A sudden and often fatal event in which the blood supply to the heart muscle is blocked, typically by a blood clot.",
    "infection": "The invasion and multiplication of microorganisms, such as bacteria, viruses, or fungi, in the body.",
    "laboratory": "A facility equipped for scientific research, experimentation, and analysis of substances and specimens.",
    "migraine": "A recurrent, throbbing headache often accompanied by nausea, vomiting, and sensitivity to light and sound.",
    "nutrition": "The process of obtaining and using the nutrients necessary for health and growth through the consumption of food.",
    "obstetrics": "The branch of medicine that deals with pregnancy, childbirth, and the postpartum period.",
    "pandemic": "An epidemic that has spread across a large geographic area and affected a significant portion of the population.",
    "quarantine": "The isolation of individuals who may have been exposed to a contagious disease to prevent its spread.",
    "radiation": "The emission and transmission of energy in the form of electromagnetic waves or particles.",
    "surgery": "The branch of medicine that uses operative techniques to treat injuries, diseases, or other medical conditions through incisions in the body.",
    "thyroid": "A butterfly-shaped gland in the neck that produces hormones regulating metabolism and energy levels.",
    "ulcer": "An open sore or lesion on the skin or mucous membranes, often accompanied by pain and inflammation.",
    "vaccine": "A biological preparation that stimulates the immune system to develop immunity to a specific disease, often by containing weakened or inactive pathogens.",
    "wound": "An injury to the body, typically involving a break in the skin, often requiring medical attention.",
    "anesthesia": "A medical technique used to induce a temporary loss of sensation or consciousness during surgery or medical procedures.",
    "biopsy": "The removal of a small sample of tissue for examination under a microscope to diagnose diseases or conditions.",
    "cancer": "A group of diseases characterized by uncontrolled cell growth and the potential to invade or spread to other parts of the body.",
    "depression": "A mood disorder characterized by persistent feelings of sadness, hopelessness, and a lack of interest or pleasure in daily activities.",
    "epidemic": "The widespread occurrence of a disease in a specific geographic area or population during a particular period of time.",
    "fertility": "The ability to conceive and produce offspring; often used to refer to the ability to become pregnant or impregnate.",
    "genes": "The segments of DNA that contain the instructions for building and maintaining the structures and functions of the body.",
    "heart attack": "A sudden and often fatal event in which the blood supply to the heart muscle is blocked, typically by a blood clot.",
    "infection": "The invasion and multiplication of microorganisms, such as bacteria, viruses, or fungi, in the body.",
    "laboratory": "A facility equipped for scientific research, experimentation, and analysis of substances and specimens.",
    "migraine": "A recurrent, throbbing headache often accompanied by nausea, vomiting, and sensitivity to light and sound.",
    "nutrition": "The process of obtaining and using the nutrients necessary for health and growth through the consumption of food.",
    "obstetrics": "The branch of medicine that deals with pregnancy, childbirth, and the postpartum period.",
    "pandemic": "An epidemic that has spread across a large geographic area and affected a significant portion of the population.",
    "radiation": "The emission and transmission of energy in the form of electromagnetic waves or particles.",
    "surgery": "The branch of medicine that uses operative techniques to treat injuries, diseases, or other medical conditions through incisions in the body.",
    "thyroid": "A butterfly-shaped gland in the neck that produces hormones regulating metabolism and energy levels.",
    "ulcer": "An open sore or lesion on the skin or mucous membranes, often accompanied by pain and inflammation.",
    "vaccine": "A biological preparation that stimulates the immune system to develop immunity to a specific disease, often by containing weakened or inactive pathogens.",
    "anatomy": "The branch of science that deals with the structure of organisms.",
    "blood pressure": "The force exerted by circulating blood against the walls of the blood vessels.",
    "diagnosis": "The identification of the nature of an illness or other problem by examination of the symptoms.",
    "fever": "A temporary increase in body temperature, often due to an illness or infection.",
    "hospital": "An institution providing medical and surgical treatment and nursing care for sick or injured people.",
    "immunization": "The process by which an individual's immune system becomes fortified against an agent (known as an immunogen).",
    "joint": "The point where two or more bones meet in the body, allowing for movement and flexibility.",
    "kidney": "A vital organ that filters waste products from the blood and regulates fluid and electrolyte balance.",
    "lungs": "The primary organs of respiration in humans, responsible for taking in oxygen and expelling carbon dioxide.",
    "medication": "A substance used to treat, cure, or prevent a disease or medical condition.",
    "nurse": "A healthcare professional trained to care for individuals, families, and communities to maintain or recover optimal health.",
    "oxygen": "A chemical element that is essential for life and is used by the body to produce energy.",
    "pulse": "The rhythmic beating of the heart, which can be felt in various parts of the body, such as the wrist or neck.",
    "radiology": "The medical specialty that uses imaging techniques, such as X-rays, to diagnose and treat diseases and injuries.",
    "surgery": "The branch of medicine that uses operative techniques to treat injuries, diseases, or other medical conditions through incisions in the body.",
    "thermometer": "An instrument used to measure temperature, often used to monitor fever or changes in body heat.",
    "ultrasound": "A diagnostic medical imaging technique that uses high-frequency sound waves to create images of the inside of the body.",
    "vaccination": "The administration of a vaccine to stimulate an individual's immune system to produce immunity to a specific disease.",
    "x-ray": "A form of electromagnetic radiation that can pass through most objects, used in medical imaging to visualize the inside of the body.",
    "allergy": "An abnormal immune system response to substances that are usually harmless, resulting in symptoms such as sneezing, itching, or hives.",
    "bronchitis": "An inflammation of the lining of the bronchial tubes, often caused by infections or irritants.",
    "cholesterol": "A waxy, fat-like substance found in the cells of the body and in certain foods; high levels can increase the risk of heart disease.",
    "diabetes": "A chronic condition that affects how the body processes glucose (sugar) and can lead to high blood sugar levels.",
    "eczema": "A chronic skin condition characterized by redness, itching, and inflammation of the skin.",
    "flu": "A contagious respiratory illness caused by influenza viruses, resulting in symptoms such as fever, cough, and body aches.",
    "gastroenteritis": "An inflammation of the stomach and intestines, often causing symptoms like diarrhea and vomiting.",
    "hypertension": "High blood pressure, a condition in which the force of the blood against the artery walls is consistently too high.",
    "insomnia": "A sleep disorder characterized by difficulty falling asleep or staying asleep, leading to inadequate sleep and daytime fatigue.",
    "jaundice": "A yellowing of the skin and the whites of the eyes, often due to liver or gallbladder problems.",
    "liver": "A vital organ responsible for detoxifying chemicals, metabolizing drugs, and producing bile for digestion.",
    "malaria": "A mosquito-borne infectious disease characterized by fever, chills, and flu-like symptoms.",
    "neurology": "The branch of medicine that deals with the anatomy, functions, and disorders of the nervous system.",
    "obesity": "Excessive accumulation of body fat, often associated with health problems such as heart disease and diabetes.",
    "pneumonia": "An inflammatory lung condition characterized by fever, cough, and difficulty breathing, often caused by infection.",
    "respiratory": "Relating to the organs and structures involved in breathing, such as the lungs and airways.",
    "stroke": "A sudden interruption of blood supply to the brain, leading to damage of brain tissue and neurological symptoms.",
    "tumor": "An abnormal mass or lump of cells that may be benign (noncancerous) or malignant (cancerous).",
    "urinary": "Relating to the organs and structures involved in the production and elimination of urine.",
    "virus": "A microscopic infectious agent that replicates inside living cells and can cause diseases in humans and animals.",
    "wound": "An injury to the body, typically involving a break in the skin, often requiring medical attention.",
}

print(Fore.LIGHTGREEN_EX + r'''
ooo        ooooo oooooooooooo oooooooooo.   ooooooooooooo ooooo   .oooooo.   ooooo      ooo       .o.       ooooooooo.   oooooo   oooo 
`88.       .888' `888'     `8 `888'   `Y8b  8'   888   `8 `888'  d8P'  `Y8b  `888b.     `8'      .888.      `888   `Y88.  `888.   .8'  
 888b     d'888   888          888      888      888       888  888      888  8 `88b.    8      .8"888.      888   .d88'   `888. .8'   
 8 Y88. .P  888   888oooo8     888      888      888       888  888      888  8   `88b.  8     .8' `888.     888ooo88P'     `888.8'    
 8  `888'   888   888    "     888      888      888       888  888      888  8     `88b.8    .88ooo8888.    888`88b.        `888'     
 8    Y     888   888       o  888     d88'      888       888  `88b    d88'  8       `888   .8'     `888.   888  `88b.       888      
o8o        o888o o888ooooood8 o888bood8P'       o888o     o888o  `Y8bood8P'  o8o        `8  o88o     o8888o o888o  o888o     o888o     
''' + Style.RESET_ALL)

print("Welcome to the MEDTIONARY!")
while True:
    term = input("What can I define for you today?\nEnter a medical term: ").lower()

    if term in medical_dictionary:
        definition = medical_dictionary[term]
        print(f"Definition of '{term}': {definition}")
    else:
        # Find the most similar term in the dictionary
        best_match = difflib.get_close_matches(term, medical_dictionary.keys(), n=1, cutoff=0.6)
        if best_match:
            suggestion = best_match[0]
            response = input(f"Did you mean '{suggestion}'? (yes/no): ").lower()
            if response == 'yes':
                definition = medical_dictionary[suggestion]
                print(f"Definition of '{suggestion}': {definition}")
            elif response == 'no':
                print("Alright. Have a wonderful day!")
                break
            else:
                print("Sorry, I didn't quite get that... Could you answer with a 'yes' or 'no'?")
        else:
            print("I'm sorry, I don't have information on that term.")

    another_term = input("Do you want to look up another term? (yes/no): ").lower()
    if another_term == 'no':
        print("Alright. Have a wonderful day!")
        break

