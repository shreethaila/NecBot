from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import spacy
spacy.load('en_core_web_sm')

chatbot = ChatBot('<b>Nec Bot</b>')

english_bot = ChatBot(
    'English Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to NEC Bot! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.6
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
english_trainer = ListTrainer(english_bot)

tamil_bot = ChatBot(
    'Tamil Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "வணக்கம், NEC Bot க்கு வரவேற்கிறோம்! 👋 உங்களுக்கு ஏதேனும் உதவி தேவைப்பட்டால், நான் எப்போதும் இங்கே இருக்கிறேன். மேலே சென்று ஏதேனும் வினவல்களின் எண்ணை எழுதவும். 😃✨<b><br><br> பின்வரும் எந்த பயனர் குழுவைச் சேர்ந்தவர்? <br><br>1.&emsp;மாணவர் பிரிவு விசாரணை.</br>2.&emsp;ஆசிரியப் பிரிவு விசாரணை. </br>3.&emsp;பெற்றோர் பிரிவு விசாரணை.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
tamil_trainer = ListTrainer(tamil_bot)


english_conversation = [
"Hi",
"Helloo!",
"Hey",


"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br><br>",

"Great",
"Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br><br>",

"good",
"Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br><br>",

"fine",
"Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br><br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"What do you do?",
"I am made to give Information about National Engineering college.",

"What else can you do?",
"I can help you know more about National Engineering college",
    
    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3 Examination <br>1.4 Placements </b>",

    "student",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3 Examination <br>1.4 Placements </b>",
    
    "1.1",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1 Moodle <br> 1.1.2 Syllabus </b>",

     "curricular",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1 Moodle <br> 1.1.2 Syllabus </b>",

    "1.1.1",
    "<b> 1.1.1 Moodle <br>The link to Moodle 👉 <a href=" 'http://lms.nec.edu.in/' ">Click Here</a> </b>",

    "moodle",
    "<b> 1.1.1 Moodle <br>The link to Moodle 👉 <a href=" 'http://lms.nec.edu.in/' ">Click Here</a> </b>",

    "1.1.2",
    "<b> 1.1.2 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://nec.edu.in/curriculum-syllabus/' ">Click Here</a> </b>",

     "syllabus",
    "<b> 1.1.2 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://nec.edu.in/curriculum-syllabus/' ">Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Sports and Games<br> 1.2.2 Student Chapters <br> 1.2.3 Clubs</b>",

    "extra curriculars",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Sports and Games<br> 1.2.2 Student Chapters <br> 1.2.3 Clubs</b>",
    
    "1.2.1",
    "<b > 1.2.1 Sports and Games<br>The link to Sports and Games👉 <a href=" 'https://nec.edu.in/facilities-2/sports-and-games/' ">Click Here</a></b>",

    "sports",
    "<b > 1.2.1 Sports and Games<br>The link to Sports and Games👉 <a href=" 'https://nec.edu.in/facilities-2/sports-and-games/' ">Click Here</a></b>",

    "1.2.2",
    "<b > 1.2.2 Student Chapters<br>The link to IEEE Student Chapters👉<a href=" 'https://nec.edu.in/ieee-students-branch/' ">Click Here</a> </b>",
     "student chapters",
    "<b > 1.2.2 Student Chapters<br>The link to IEEE Student Chapters👉<a href=" 'https://nec.edu.in/ieee-students-branch/' ">Click Here</a> </b>",

    "1.2.3",
    "<b > 1.2.3 Clubs <br>The link to Clubs👉 <a href=" 'https://nec.edu.in/extra-curricular/national-cadet-corps/' ">Click Here</a> </b>",

     "clubs",
    "<b > 1.2.3 Clubs <br>The link to Clubs👉 <a href=" 'https://nec.edu.in/extra-curricular/national-cadet-corps/' ">Click Here</a> </b>",

    "1.3",
    "<b > EXAMINATION <br>These are the top results:<br>  1.3.1 Examination Process <br> 1.3.2 Result </b>",

     "examination",
    "<b > EXAMINATION <br>These are the top results:<br>  1.3.1 Examination Process <br> 1.3.2 Result </b>",

    "1.3.1",
    "<b > 1.3.1 Examination Process<br>The link to Examination Process👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">Click Here</a> </b>",

     "examination process",
    "<b > 1.3.1 Examination Process<br>The link to Examination Process👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">Click Here</a> </b>",

    "1.3.2",
    "<b > 1.3.2 Result<br>The link to Result👉<a href=" 'https://nec.edu.in/exam-results/' ">Click Here</a> </b>",

     "results",
    "<b > 1.3.2 Result<br>The link to Result👉<a href=" 'https://nec.edu.in/exam-results/' ">Click Here</a> </b>",

    "1.4",
    "<b > PLACEMENTS These are the top results:<br> 1.4.1 Placements<br> 1.4.2 Our Recruiters <br> 1.4.3 Placement Statistics </b>",

     "placements",
    "<b > PLACEMENTS These are the top results:<br> 1.4.1 Placements<br> 1.4.2 Our Recruiters <br> 1.4.3 Placement Statistics </b>",

     "could you please tell me about the placements",
    "<b > PLACEMENTS These are the top results:<br> 1.4.1 Placements<br> 1.4.2 Our Recruiters <br> 1.4.3 Placement Statistics </b>",

    "1.4.1",
    "<b> 1.4.1 Placements<br>The link to Placements👉 <a href=" 'https://nec.edu.in/placement/#introduction' ">Click Here</a> </b>",
    "1.4.2",
    "<b> 1.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://nec.edu.in/placement/#recruiters' ">Click Here</a> </b>",

    "recruiters",
    "<b> 1.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://nec.edu.in/placement/#recruiters' ">Click Here</a> </b>",

    "1.4.3",
    "<b > 1.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://nec.edu.in/placement/#place-batch' ">Click Here</a> </b>",
    "placement statistics",
    "<b > 1.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://nec.edu.in/placement/#place-batch' ">Click Here</a> </b>",

    "2",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Portals & Administration<br>2.2  Examination </b>",
    
    "2.1",
    "<b > PORTALS & ADMINISTRATION These are the top results:<br> 2.1.1 ERP <br>2.1.2 Moodle </b>",
    "2.1.1",
    "<b> 2.1.1 ERP<br>The link to ERP👉<a href=" 'https://erp.nec.edu.in/erp/' ">Click Here</a> </b>",
    "erp",
    "<b> 2.1.1 ERP<br>The link to ERP👉<a href=" 'https://erp.nec.edu.in/erp/' ">Click Here</a> </b>",
    "2.1.2",
    "<b> 2.1.2 Moodle<br>The link to Moodle👉<a href=" 'http://lms.nec.edu.in/' ">Click Here</a> </b>",

   
   
    "2.2",
    "<b > EXAMINATION <br>These are the top results:<br>  2.2.1 Examination Process <br> 2.2.2 Result </b>",

     "examination",
    "<b > EXAMINATION <br>These are the top results:<br>  2.2.1 Examination Process <br> 2.2.2 Result </b>",

    "2.2.1",
    "<b > 2.2.1 Examination Process<br>The link to Examination Process👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">Click Here</a> </b>",

     "examination process",
    "<b > 2.2.1 Examination Process<br>The link to Examination Process👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">Click Here</a> </b>",

    "2.2.2",
    "<b > 2.2.2 Result<br>The link to Result👉<a href=" 'https://nec.edu.in/exam-results/' ">Click Here</a> </b>",

     "results",
    "<b > 2.2.2 Result<br>The link to Result👉<a href=" 'https://nec.edu.in/exam-results/' ">Click Here</a> </b>",
  
    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Admission <br>3.3 Scholarship <br>3.4 Placements <br>3.5 Fee Payment </b> " ,

   
    "3.1",
    "<b > 3.1 About NEC<br>The link to About NEC👉 <a href="' https://nec.edu.in/about-us/' ">Click Here</a> </b>",
     "about",
    "<b > 3.1 About NEC<br>The link to About NEC👉 <a href="' https://nec.edu.in/about-us/' ">Click Here</a> </b>",

    "3.2",
    "<b > 3.2 Admission <br>The link to Admission👉<a href=" 'https://nec.edu.in/admission/' ">Click Here</a> </b>",

    "admission",
    "<b > 3.2 Admission <br>The link to Admission👉<a href=" 'https://nec.edu.in/admission/' ">Click Here</a> </b>",


    "3.3",
    "<b > 3.3 Scholarship <br>The link to Scholarship👉 <a href=" 'https://nec.edu.in/scholarship-2/' ">Click Here</a> </b>",
    "scholarship",
    "<b > 3.3 Scholarship <br>The link to Scholarship👉 <a href=" 'https://nec.edu.in/scholarship-2/' ">Click Here</a> </b>",
     "3.4",
    "<b > 3.4 Placements <br>The link to Scholarship👉 <a href=" 'https://nec.edu.in/placement/#introduction' ">Click Here</a> </b>",
     "3.5",
    "<b > 3.5 Fee Payment <br>The link to Scholarship👉 <a href=" 'https://nec.edu.in/online-fee-payment-erp/' ">Click Here</a> </b>",
     "fee payment",
    "<b > 3.5 Fee Payment <br>The link to Scholarship👉 <a href=" 'https://nec.edu.in/online-fee-payment-erp/' ">Click Here</a> </b>"

]

tamil_conversation=[
    "வணக்கம்",
"ஹலோ!",
"ஏய்",


"எப்படி இருக்கிறீர்கள்?",
"நான் நன்றாக இருக்கிறேன்.</br> <br>எந்த வினவல்களின் எண்ணையும் எழுதுங்கள். br>3.&emsp;பெற்றோர் பிரிவு விசாரணை.</br>4.&emsp;பார்வையாளர் பிரிவு விசாரணை.</br>",

"நன்று",
"எந்த வினவலின் எண்ணையும் எழுதுங்கள். br>4.&emsp;பார்வையாளர் பிரிவு விசாரணை.</br>",

"நல்ல",
"எந்த வினவல்களின் எண்ணையும் எழுதவும். br>",

"நன்று",
"எந்த வினவல்களின் எண்ணையும் எழுதவும். br>",

"நன்றி",
"உங்கள் வரவேற்கிறோம் 😄",

"நன்றி",
"உங்கள் வரவேற்கிறோம் 😄",

"வருகிறேன்",
"வருகைக்கு நன்றி!..",

"நீ என்ன செய்கிறாய்?",
"நேஷனல் இன்ஜினியரிங் கல்லூரியைப் பற்றிய தகவல்களைத் தருவதற்காக நான் உருவாக்கப்பட்டுள்ளேன்.",

"வேறு என்ன செய்ய முடியும்?",
"நேஷனல் இன்ஜினியரிங் கல்லூரியைப் பற்றி மேலும் தெரிந்துகொள்ள நான் உங்களுக்கு உதவ முடியும்",

"1",
    "<b>மாணவர் <br>பின்வருபவை மாணவர் தொடர்பான அடிக்கடி தேடப்படும் சொற்கள். கீழே உள்ள விருப்பங்களிலிருந்து ஒன்றைத் தேர்ந்தெடுக்கவும்: <br> <br> 1.1 பாடத்திட்டங்கள் <br>1.2 கூடுதல் பாடத்திட்டங்கள்<br>1.3 தேர்வு <br>1.4 இடங்கள் </b>",

    "மாணவர்",
    "<b>மாணவர் <br>பின்வருபவை மாணவர் தொடர்பான அடிக்கடி தேடப்படும் சொற்கள். கீழே உள்ள விருப்பங்களிலிருந்து ஒன்றைத் தேர்ந்தெடுக்கவும்: <br> <br> 1.1 பாடத்திட்டங்கள் <br>1.2 கூடுதல் பாடத்திட்டங்கள்<br>1.3 தேர்வு <br>1.4 இடங்கள் </b>",
    
    "1.1",
    "<b> பாடத்திட்டம் <br> இவையே சிறந்த முடிவுகள்: <br> <br> 1.1.1 Moodle <br> 1.1.2 பாடத்திட்டம் </b>",

     "பாடத்திட்டம்",
    "<b> பாடத்திட்டம் <br> இவையே சிறந்த முடிவுகள்: <br> <br> 1.1.1 Moodle <br> 1.1.2 பாடத்திட்டம் </b>",

    "1.1.1",
    "<b> 1.1.1 Moodle <br>மூடுலுக்கான இணைப்பு 👉 <a href=" 'http://lms.nec.edu.in/' ">இங்கே கிளிக் செய்யவும்</a> </b>",

    "மூடில்",
    "<b> 1.1.1 Moodle <br>மூடுலுக்கான இணைப்பு 👉 <a href=" 'http://lms.nec.edu.in/' ">இங்கே கிளிக் செய்யவும்</a> </b>",

    "1.1.2",
    "<b> 1.1.2 பாடத்திட்டம்<br>பாடத்திட்டத்திற்கான இணைப்பு 👉 <a href=" 'https://nec.edu.in/curriculum-syllabus/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,

     "பாடத்திட்டங்கள்",
    "<b> 1.1.2 பாடத்திட்டம்<br>பாடத்திட்டத்திற்கான இணைப்பு 👉 <a href=" 'https://nec.edu.in/curriculum-syllabus/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,
"1.2",
    "<b>கூடுதல் பாடத்திட்டம்<br>இவை சிறந்த முடிவுகள்: <br> <br> 1.2.1 விளையாட்டு மற்றும் விளையாட்டு<br> 1.2.2 மாணவர் அத்தியாயங்கள் <br> 1.2.3 கிளப்கள்</b>",

    "கூடுதல் பாடத்திட்டங்கள்",
    "<b>கூடுதல் பாடத்திட்டம்<br>இவை சிறந்த முடிவுகள்: <br> <br> 1.2.1 விளையாட்டு மற்றும் விளையாட்டு<br> 1.2.2 மாணவர் அத்தியாயங்கள் <br> 1.2.3 கிளப்கள்</b>",
    
    "1.2.1",
    "<b > 1.2.1 விளையாட்டு மற்றும் விளையாட்டுகள்<br>விளையாட்டு மற்றும் விளையாட்டுகளுக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/facilities-2/sports-and-games/' ">கிளிக் செய்யவும் இதோ</a></b>",

    "விளையாட்டு",
    "<b > 1.2.1 விளையாட்டு மற்றும் விளையாட்டுகள்<br>விளையாட்டு மற்றும் விளையாட்டுகளுக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/facilities-2/sports-and-games/' ">கிளிக் செய்யவும் இதோ</a></b>",

    "1.2.2",
    "<b> 1.2.2 மாணவர் அத்தியாயங்கள்<br>IEEE மாணவர் அத்தியாயங்களுக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/ieee-students-branch/' ">இங்கே கிளிக் செய்யவும்</a> </b>",
     "மாணவர் அத்தியாயங்கள்",
    "<b> 1.2.2 மாணவர் அத்தியாயங்கள்<br>IEEE மாணவர் அத்தியாயங்களுக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/ieee-students-branch/' ">இங்கே கிளிக் செய்யவும்</a> </b>",

    "1.2.3",
    "<b > 1.2.3 கிளப்கள் <br>கிளப்களுக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/extra-curricular/national-cadet-corps/' ">இங்கே கிளிக் செய்யவும்</a > </b>",

     "கிளப்புகள்",
    "<b > 1.2.3 கிளப்கள் <br>கிளப்களுக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/extra-curricular/national-cadet-corps/' ">இங்கே கிளிக் செய்யவும்</a > </b>",

    "1.3",
    "<b> தேர்வு <br>இவையே சிறந்த முடிவுகள்:<br> 1.3.1 தேர்வு செயல்முறை <br> 1.3.2 முடிவு </b>",

     "தேர்வு",
    "<b> தேர்வு <br>இவையே சிறந்த முடிவுகள்:<br> 1.3.1 தேர்வு செயல்முறை <br> 1.3.2 முடிவு </b>",

    "1.3.1",
    "<b > 1.3.1 தேர்வுச் செயல்முறை<br>தேர்வு செயல்முறைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">இங்கே கிளிக் செய்யவும்</a> </b>",

     "தேர்வு செயல்முறை",
    "<b > 1.3.1 தேர்வுச் செயல்முறை<br>தேர்வு செயல்முறைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">இங்கே கிளிக் செய்யவும்</a> </b>",

    "1.3.2",
    "<b > 1.3.2 முடிவு<br>முடிவுக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/exam-results/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,

     "முடிவுகள்",
    "<b > 1.3.2 முடிவு<br>முடிவுக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/exam-results/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,
    "1.4",
    "<b> இடங்கள் இவையே சிறந்த முடிவுகள்:<br> 1.4.1 இடங்கள்<br> 1.4.2 எங்கள் பணியமர்த்துபவர்கள் <br> 1.4.3 வேலை வாய்ப்பு புள்ளிவிவரங்கள் </b>",

     "வேலையிடங்கள்",
    "<b> இடங்கள் இவையே சிறந்த முடிவுகள்:<br> 1.4.1 இடங்கள்<br> 1.4.2 எங்கள் பணியமர்த்துபவர்கள் <br> 1.4.3 வேலை வாய்ப்பு புள்ளிவிவரங்கள் </b>",

    "1.4.1",
    "<b> 1.4.1 இடங்கள்<br>இடுப்புகளுக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/placement/#introduction' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,
    "1.4.2",
    "<b> 1.4.2 எங்கள் ஆட்சேர்ப்பாளர்கள்<br>தேர்வு செய்பவர்களுக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/placement/#recruiters' ">இங்கே கிளிக் செய்யவும்</a> </b> ",

    "ஆட்சேர்ப்பு செய்பவர்கள்",
    "<b> 1.4.2 எங்கள் ஆட்சேர்ப்பாளர்கள்<br>தேர்வு செய்பவர்களுக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/placement/#recruiters' ">இங்கே கிளிக் செய்யவும்</a> </b> ",

    "1.4.3",
    "<b > 1.4.3 வேலை வாய்ப்பு புள்ளி விவரங்கள்<br> வேலை வாய்ப்பு புள்ளி விவரத்திற்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/placement/#place-batch' ">இங்கே கிளிக் செய்யவும்</a> < /b>",
    "வேலையிடல் புள்ளியியல்",
    "<b > 1.4.3 வேலை வாய்ப்பு புள்ளி விவரங்கள்<br> வேலை வாய்ப்பு புள்ளி விவரத்திற்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/placement/#place-batch' ">இங்கே கிளிக் செய்யவும்</a> < /b>",

    "2",
    "<b>FACULTY<br>பின்வருவது ஆசிரியர் தொடர்பான அடிக்கடி தேடப்படும் சொற்கள். கீழே உள்ள விருப்பங்களிலிருந்து ஒன்றைத் தேர்ந்தெடுக்கவும்:</br></br>2.1 போர்டல்கள் & நிர்வாகம்<br>2.2 தேர்வு </b>",
    
    "2.1",
    "<b> போர்ட்டல்கள் & நிர்வாகம் இவையே சிறந்த முடிவுகள்:<br> 2.1.1 ERP <br>2.1.2 Moodle </b>",
    "2.1.1",
    "<b> 2.1.1 ERP<br>ERPக்கான இணைப்பு👉<a href=" 'https://erp.nec.edu.in/erp/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,
    "ஈஆர்பி",
    "<b> 2.1.1 ERP<br>ERPக்கான இணைப்பு👉<a href=" 'https://erp.nec.edu.in/erp/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,
    "2.1.2",
    "<b> 2.1.2 Moodle<br>மூடுலுக்கான இணைப்பு👉<a href=" 'http://lms.nec.edu.in/' ">இங்கே கிளிக் செய்யவும்</a> </b>",

   
   
    "2.2",
    "<b> தேர்வு <br>இவை சிறந்த முடிவுகள்:<br> 2.2.1 தேர்வு செயல்முறை <br> 2.2.2 முடிவு </b>",

     "தேர்வு",
    "<b> தேர்வு <br>இவை சிறந்த முடிவுகள்:<br> 2.2.1 தேர்வு செயல்முறை <br> 2.2.2 முடிவு </b>",

    "2.2.1",
    "<b > 2.2.1 தேர்வுச் செயல்முறை<br>தேர்வு செயல்முறைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">இங்கே கிளிக் செய்யவும்</a> </b>",

     "தேர்வு செயல்முறை",
    "<b > 2.2.1 தேர்வுச் செயல்முறை<br>தேர்வு செயல்முறைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">இங்கே கிளிக் செய்யவும்</a> </b>",

    "2.2.2",
    "<b> 2.2.2 முடிவு<br>முடிவுக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/exam-results/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,

     "முடிவுகள்",
    "<b> 2.2.2 முடிவு<br>முடிவுக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/exam-results/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,
    "3",
    "<b> பெற்றோர் <br>பின்வருபவை பெற்றோர் தொடர்பான அடிக்கடி தேடப்படும் சொற்கள். கீழே உள்ள விருப்பங்களில் இருந்து ஒன்றைத் தேர்ந்தெடுக்கவும்: <br> <br> 3.1 எங்களைப் பற்றி <br>3.2 சேர்க்கை <br>3.3 உதவித்தொகை <br>3.4 இடங்கள் <br>3.5 கட்டணம் செலுத்துதல் </b> " ,

   
    "3.1",
    "<b > 3.1 NEC பற்றி<br>NEC பற்றிய இணைப்பு👉 <a href="' https://nec.edu.in/about-us/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,
     "பற்றி",
    "<b > 3.1 NEC பற்றி<br>NEC பற்றிய இணைப்பு👉 <a href="' https://nec.edu.in/about-us/' ">இங்கே கிளிக் செய்யவும்</a> </b>" ,

    "3.2",
    "<b > 3.2 சேர்க்கை <br>சேர்க்கைக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/admission/' ">இங்கே கிளிக் செய்யவும்</a> </b>",

    "சேர்க்கை",
    "<b > 3.2 சேர்க்கை <br>சேர்க்கைக்கான இணைப்பு👉<a href=" 'https://nec.edu.in/admission/' ">இங்கே கிளிக் செய்யவும்</a> </b>",


    "3.3",
    "<b > 3.3 உதவித்தொகை <br>உதவித்தொகைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/scholarship-2/' ">இங்கே கிளிக் செய்யவும்</a> </b>",
    "உதவித்தொகை",
    "<b > 3.3 உதவித்தொகை <br>உதவித்தொகைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/scholarship-2/' ">இங்கே கிளிக் செய்யவும்</a> </b>",
     "3.4",
    "<b > 3.4 இடங்கள் <br>உதவித்தொகைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/placement/#introduction' ">இங்கே கிளிக் செய்யவும்</a> </b>",
     "3.5",
    "<b > 3.5 கட்டணம் செலுத்துதல் <br>உதவித்தொகைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/online-fee-payment-erp/' ">இங்கே கிளிக் செய்யவும்</a> </ b>",
     "கட்டணம் செலுத்துதல்",
    "<b > 3.5 கட்டணம் செலுத்துதல் <br>உதவித்தொகைக்கான இணைப்பு👉 <a href=" 'https://nec.edu.in/online-fee-payment-erp/' ">இங்கே கிளிக் செய்யவும்</a> </ b>"


]

english_trainer.train(english_conversation)
tamil_trainer.train(tamil_conversation)

corpus_trainer = ChatterBotCorpusTrainer(english_bot)
corpus_trainer.train("chatterbot.corpus.english")