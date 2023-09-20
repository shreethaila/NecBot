from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('<b>Nec Bot</b>')

# chatbot = ChatBot(
#     'ChatBot for College Enquiry',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         {
#             'import_path': 'chatterbot.logic.BestMatch',
#             'default_response': "Hi there, Welcome to NEC Bot! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
#             'maximum_similarity_threshold': 0.90
#         }
#     ],
#     database_uri='sqlite:///database.sqlite3'   
# ) 
# trainer = ListTrainer(chatbot)
english_bot = ChatBot('English Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
english_trainer = ListTrainer(english_bot)

tamil_bot = ChatBot('Tamil Bot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
tamil_trainer = ListTrainer(tamil_bot)


english_conversation = [
"Hi",
"Helloo!",
"Hey",

"lolo",
"leleuuuuuu!",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

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
    
    "1.1",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1 Moodle <br> 1.1.2 Syllabus </b>",
    "1.1.1",
    "<b> 1.1.1 Moodle <br>The link to Moodle 👉 <a href=" 'http://lms.nec.edu.in/' ">Click Here</a> </b>",
    "1.1.2",
    "<b> 1.1.2 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://nec.edu.in/curriculum-syllabus/' ">Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Sports and Games<br> 1.2.2 Student Chapters <br> 1.2.3 Clubs</b>",
    "1.2.1",
    "<b > 1.2.1 Sports and Games<br>The link to Sports and Games👉 <a href=" 'https://nec.edu.in/facilities-2/sports-and-games/' ">Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2 Student Chapters<br>The link to IEEE Student Chapters👉<a href=" 'https://nec.edu.in/ieee-students-branch/' ">Click Here</a> </b>",
    "1.2.3",
    "<b > 1.2.3 Clubs <br>The link to Clubs👉 <a href=" 'https://nec.edu.in/extra-curricular/national-cadet-corps/' ">Click Here</a> </b>",

    "1.3",
    "<b > EXAMINATION <br>These are the top results:<br>  1.3.1 Examination Process <br> 1.3.2 Result </b>",
    "1.3.1",
    "<b > 1.3.1 Examination Process<br>The link to Examination Process👉 <a href=" 'https://nec.edu.in/wp-content/uploads/2023/03/Examination-Rule.pdf' ">Click Here</a> </b>",
    "1.3.2",
    "<b > 1.3.2 Result<br>The link to Result👉<a href=" 'https://nec.edu.in/exam-results/' ">Click Here</a> </b>",

    "1.4",
    "<b > PLACEMENTS These are the top results:<br> 1.4.1 Placements<br> 1.4.2 Our Recruiters <br> 1.4.3 Placement Statistics </b>",
    "1.4.1",
    "<b> 1.4.1 Placements<br>The link to Placements👉 <a href=" 'https://nec.edu.in/placement/#introduction' ">Click Here</a> </b>",
    "1.5.2",
    "<b> 1.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://nec.edu.in/placement/#recruiters' ">Click Here</a> </b>",
    "1.5.3",
    "<b > 1.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://nec.edu.in/placement/#place-batch' ">Click Here</a> </b>",

    # "2",
    # "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Portals & Administration<br>2.2  Change Personal Details<br>2.3  Examination </b>",
    
    # "2.1",
    # "<b > PORTALS & ADMINISTRATION These are the top results:<br> 2.1.1 Biometric Attendance System <br>2.1.2 Moodle </b>",
    # "2.1.1",
    # "<b> 2.1.1 Biometric Attendance<br>The link to Biometric Attendance👉<a href=" 'http://samay.fragnel.edu.in:1234/timeo/' ">Click Here</a> </b>",
    # "2.1.2",
    # "<b> 2.1.2 Moodle<br>The link to Moodle👉<a href=" 'http://gyan.fragnel.edu.in:2222/moodle' ">Click Here</a> </b>",

    # "2.2",
    # "<b > CHANGE PERSONAL DETAILS These are the top results:<br> <br> 2.2.1 Site Login <br> </b>",
    # "2.2.1",
    # "<b> 2.2.1 Site Login<br>The link to Site Login👉<a href=" 'http://www.frcrce.ac.in/index.php/component/users/?view=login&Itemid=437' ">Click Here</a> </b>",
   
    # "2.3",
    # "<b > EXAMINATION <br>These are the top results:<br> <br> 2.3.1 Notices<br> 2.3.2 Question Paper Archive </b>",
    # "2.3.1",
    # "<b> 2.3.1 Notices <br>The link to Notices 👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/crce-notices/110-examsection' ">Click Here</a> </b>",
    # "2.3.2",
    # "<b> 2.3.2 Question Paper Archive <br>The link to Archive👉<a href=" 'http://www.frcrce.ac.in/questionpaper/ArchUE.php' ">Click Here</a> </b>",
  
    # "3",
    # "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements </b> " ,

    # "3.1",
    # "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About CRCE<br> 3.1.2 Director's Address <br> 3.1.3 Principal's Address </b>",
    # "3.1.1",
    # "<b > 3.1.1 About CRCE<br>The link to About CRCE👉 <a href=" 'http://www.frcrce.ac.in/index.php/about-us/about-crce' ">Click Here</a> </b>",
    # "3.1.2",
    # "<b > 3.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'http://www.frcrce.ac.in/index.php/about-us/director' ">Click Here</a> </b>",
    # "3.1.3",
    # "<b > 3.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'http://www.frcrce.ac.in/index.php/about-us/principal-frcrce' ">Click Here</a> </b>",

    # "3.2",
    # "<b > NOTICES<br>These are the top results:<br> <br> 3.2.1 All Notices  </b>",
    # "3.2.1",
    # "<b > 3.2.1 All Notices <br>The link to All Notices👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/crce-notices' ">Click Here</a> </b>",

    # "3.3",
    # "<b > ABOUT US<br>These are the top results:<br> <br>3.3.1 Payment Details <br> 3.3.2 Online Payment Portal </b>",
    # "3.3.1",
    # "<b > 3.3.1 Payment Details<br>The link to Payment Details 👉 <a href=" 'http://frcrce.ac.in/attachments/article/248/NEFTForm.pdf' ">Click Here</a> </b>",
    # "3.3.2",
    # "<b > 3.3.2 Payment Portal <br>The link to Payment Portal👉<a href=" 'https://pay.fragnel.edu.in/CRCE/initPay.php' ">Click Here</a> </b>",

    # "3.4",
    # "<b > PLACEMENTS These are the top results:<br> <br>3.4.1 Placements<br> 3.4.2 Our Recruiters <br> 3.4.3 Placement Statistics </b>",
    # "3.4.1",
    # "<b> 3.4.1 Placements<br>The link to Placements👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/placements/campus-placement-overview' ">Click Here</a> </b>",
    # "3.4.2",
    # "<b> 3.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'http://www.frcrce.ac.in/index.php/students/placements/our-recruiters' ">Click Here</a> </b>",
    # "3.4.3",
    # "<b > 3.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/placements/placement-statistics' ">Click Here</a> </b>",

    # "4",
    # "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br>4.2 Programs We Offer <br>4.3 Student Bodies <br>4.4 Extra-Curricular </b>",
    
    # "4.1",
    # "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About CRCE<br> 4.1.2 Director's Address <br> 4.1.3 Principal's Address </b>",
    # "4.1.1",
    # "<b > 4.1.1 About CRCE<br>The link to About CRCE👉 <a href=" 'http://www.frcrce.ac.in/index.php/about-us/about-crce' ">Click Here</a> </b>",
    # "4.1.2",
    # "<b > 4.1.2 Director's Address <br>The link to Director's Address👉<a href=" 'http://www.frcrce.ac.in/index.php/about-us/director' ">Click Here</a> </b>",
    # "4.1.3",
    # "<b > 4.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'http://www.frcrce.ac.in/index.php/about-us/principal-frcrce' ">Click Here</a> </b>",

    # "4.2",
    # "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate<br> 4.2.3 Ph.D </b>",
    # "4.2.1",
    # "<b > 4.2.1 Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'http://www.frcrce.ac.in/index.php/admission/under-graduate' ">Click Here</a> </b>",
    # "4.2.2",
    # "<b > 4.2.2 Post-Graduate <br>The link to Post-Graduate👉<a href=" 'http://www.frcrce.ac.in/index.php/admission/post-graduate' ">Click Here</a> </b>",
    # "4.2.3",
    # "<b > 4.2.3 Ph.D <br>The link to Ph.D👉 <a href=" 'http://www.frcrce.ac.in/index.php/admission/phd' ">Click Here</a> </b>",

    # "4.3",
    # "<b > STUDENT BODIES <br>These are the top results:<br> <br>4.3.1 Students Council  <br> 4.3.2 Students Chapter <br> 4.3.3 Students Project Groups </b>",
    # "4.3.1",
    # "<b > 4.3.1 Students Council  <br>The link to Students Council  👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/students-council' ">Click Here</a> </b>",
    # "4.3.2",
    # "<b > 4.3.2 Students Chapter <br>The link to Students Chapter 👉<a href=" 'http://www.frcrce.ac.in/index.php/students/forums' ">Click Here</a> </b>",
    # "4.3.3",
    # "<b > 4.3.3 Students Project Groups <br>The link to Students Project Groups👉 <a href=" 'http://www.frcrce.ac.in/' ">Click Here</a> </b>",

    # "4.4",
    # "<b > EXTRA-CURRICULAR <br>These are the top results:<br> <br>4.4.1 Events  <br> 4.4.2 Institute Innovation Cell </b>",
    # "4.4.1",
    # "<b > 4.4.1 Events    <br>The link to Events   👉 <a href=" 'http://www.frcrce.ac.in/index.php/students/events-new' ">Click Here</a> </b>",
    # "4.4.2",
    # "<b > 4.4.2 Institute Innovation Cell <br>The link to Institute Innovation Cell 👉<a href=" 'https://crceiic.github.io/' ">Click Here</a> </b>",

]

tamil_conversation=[
    "வணக்கம்",
    "வந்தனம்"
]

english_trainer.train(english_conversation)
tamil_trainer.train(tamil_conversation)
