#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from soda.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        for key in company_list.keys():
            company_dict = company_list[key]
            name = company_dict['name']
            company = Company.objects.filter(name=name)
            if company:
                company = company[0]
                company.description = company_dict['description']
                company.img = company_dict['img']
                company.links = company_dict['links']
            else:
                company = Company(name=company_dict['name'], description=company_dict['description'], img=company_dict['img'],links=company_dict['links'])
            company.save()
        print str(len(Company.objects.all())) + " company data has been inserted."

company_list = {}
# company_list['counsyl'] = {'name':'Counsyl', "description":"Counsyl is a technology company that strives to give millions of men and women access to vital information about their bodies so they can confidently make choices about their lives. Counsyl integrates sophisticated technology with custom automation in its CLIA-certified, CAP-accredited and NYS CLEP-permitted medical laboratory.", 'img':"http://counsyl.files.wordpress.com/2014/04/github-logo2.png", 'links':'https://www.counsyl.com/careers/software-engineering-intern-2015/'}
company_list['affirm'] = {'name': 'Affirm', 'description' : 'Affirm lets shoppers pay for purchases across multiple months with transparent, fairly-priced fees built into every payment, and boosts conversion and basket size for eTailers at less than the cost of credit cards.','img': 'https://d1qb2nb5cznatu.cloudfront.net/startups/i/178430-585fa2c6225328beaedec4ce1ac8c924-medium_jpg.jpg?buster=1392918465', 'links': 'https://jobs.lever.co/affirm/41093734-0492-4f7e-b5ab-7fe53f2143e7/apply'}
company_list['quora'] = {'name':'Quora','description':'Quora is a question-and-answer website where questions are created, answered, edited and organized by its community of users','img':'http://www.joshhannah.com/wp-content/uploads/quora-logo.png','links':'https://jobs.lever.co/quora/c6456987-4af5-4db0-984e-b8489ffdcf0a/apply'}
company_list['box'] = {'name':'Box', 'description':"Box Inc. (formerly Box.net) is an online file sharing and personal cloud content management service for businesses. The company adopted a freemium business model, and provides up to 10 GB of free storage for personal accounts.", 'img':"http://8.mshcdn.com/wp-content/uploads/2009/02/box-logo-blue-background-300x181.png", 'links':"https://jobs.lever.co/box/c0aba64f-7d5d-4e52-b1eb-03460b0f34a6/apply"}
company_list['arista'] = {'name':'Arista', "description":"Arista Networks (previously Arastra) is a computer networking company headquartered in Santa Clara, California, USA. The company designs and sells multilayer network switches to deliver software-defined networking (SDN) solutions for large datacenter, cloud computing, high-performance computing and high-frequency trading environments.", 'img':"http://media.glassdoor.com/sqll/295128/arista-networks-squarelogo.png", 'links':"http://www.arista.com/en/careers/engineering"}
company_list['stripe'] = {'name':'Stripe', "description":"Stripe is a company that provides a way for individuals and businesses to accept payments over the Internet. Co-founded by brothers Patrick and John Collison, the company has received $130 million in funding.", 'img':"https://stripe.com/img/open-graph/logo.png?2", 'links':"https://stripe.com/jobs/positions/engineer/#engineering"}
company_list['ea'] = {'name':'EA', 'description':"Electronic Arts, Inc. (EA), also known as EA Games, is an American developer, marketer, publisher and distributor of video games headquartered in Redwood City, California, U.S. Founded and incorporated on May 28, 1982 by Trip Hawkins, the company was a pioneer of the early home computer games industry and was notable for promoting the designers and programmers responsible for its games.", 'img':"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQx6kyVodp_6YRGGH_myDzvvN5RMpSIBozUZH8mJjmombiYcIuT", 'links':"http://ea.avature.net/university"}
company_list['mongodb'] = {'name':"MongoDB", 'description':"MongoDB is a cross-platform document-oriented database. Classified as a NoSQL database, MongoDB eschews the traditional table-based relational database structure in favor of JSON-like documents with dynamic schemas (MongoDB calls the format BSON), making the integration of data in certain types of applications easier and faster.", 'img':"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTx6TxNovLD8X24W4HV8dbxBylmg8R_8KDeXVR63wEjyoyWe_kf", 'links':"http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qX79VfwS&j=oG2vZfwW"}
company_list['square'] = {'name':"Square", 'description':"Square, Inc. is a financial services, merchant services aggregator and mobile payments company based in San Francisco, California. The company markets several software and hardware products and services, including Square Register and Square Order. The company was founded in 2009 by Jack Dorsey and Jim McKelvey and launched its first app and service in 2010.", 'img':"https://pbs.twimg.com/profile_images/458796011356311552/2D5G8yIo.png", 'links':"http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q8Z9VfwV&page=Apply&j=o2XdZfwV"}
company_list['spacex'] = {'name':"SpaceX", 'description':"Space Exploration Technologies Corporation (SpaceX) is a space transport services company headquartered in Hawthorne, California. It was founded in 2002 by former PayPal entrepreneur and Tesla Motors CEO Elon Musk.", 'links':"https://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qz49Vfwr&j=obTMZfwz&nl=0", 'img':'http://kxxv.images.worldnow.com/images/4067143_G.jpg'}
company_list['nest'] = {'name':'Nest','description':'We reinvent unloved but important home products, like the thermostat and smoke alarm. The company focuses on delighting customers with simple, beautiful and thoughtful hardware, software and services. ','links':'http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=Apply&c=qW69VfwQ&j=oS7wZfwe', 'img':'http://rightstartups.com/wp-content/uploads/Nest-Labs.jpg'}
company_list['jawbone'] = {'name':'Jawbone', 'description':'Jawbone is a privately held consumer technology and wearable products company headquartered in San Francisco, California. It develops and sells wearable technology such as the Jawbone UP and UP24 wristbands and portable audio devices, including the Jambox and Big Jambox wireless speakers.', 'links':"https://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qPb9VfwO&amp;cs=919aVfwZ&amp;j=orRJZfwK&amp;jvprefix=https%3a%2f%2fjawbone.com&amp;jvresize=%2fcareers%2fjobvite_frame_resize&amp;page=Apply&page=Apply&j=orRJZfwK", 'img':"https://d3osil7svxrrgt.cloudfront.net/static/www/logos/jawbone/jawbone-logo-display.png"}
company_list['etsy'] = {'name':'Etsy','description':"Etsy is an e-commerce website focused on handmade or vintage items and supplies, as well as unique factory-manufactured items under Etsy's new guidelines, released in October 2013. These items cover a wide range, including art, photography, clothing, jewelry, food, bath and beauty products, quilts, knick-knacks, and toys.",'links':'http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qmZ9Vfw9&amp;j=oMwPZfwQ&amp;page=Apply&page=Apply&j=oMwPZfwQ', 'img':'http://www.brandsoftheworld.com/sites/default/files/styles/logo-thumbnail/public/122010/etsy-thumb.png'}
company_list['rocketfuel'] = {'name':'RocketFuel','description':"Rocket Fuel is a provider of a programmatic media-buying platform that utilizes artificial intelligence (AI), big data, and predictive modeling to autonomously real-time bid (RTB) on digital media ad impressions across web, video, mobile, and social media.",'links':'http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qK29VfwA&jvprefix=http%3a%2f%2frocketfuel.com&cs=9Sq9Vfw6&jvresize=http%3a%2f%2frocketfuel.com%2fframeresize.htm&page=Apply&j=o7hRZfwY', 'img':'http://allfacebook.com/files/2013/01/RocketFuelLogo.jpg'}
company_list['yelp'] = {'name':'Yelp','description':"Yelp is a multinational corporation headquartered in San Francisco, California. It develops, hosts and markets Yelp.com and the Yelp mobile app, which publish crowd-sourced reviews about local businesses.",'links':'http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q6X9VfwR&jvprefix=http%3a%2f%2fwww.yelp.com&cs=924aVfwV&jvresize=http%3a%2f%2fwww.yelp.com%2fhtml%2fjobvite.html&nl=0&page=Apply&j=oFOmWfwv', 'img':'http://static01.nyt.com/images/2009/03/03/timestopics/yelp-395.jpg'}
company_list['zendesk'] = {'name':'Zendesk','description':"Zendesk, Inc. is a software development company based in San Francisco, California. The company provides a cloud-based customer service platform, also called Zendesk, that includes ticketing, self-service options, and customer support features.",'links':'https://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q769Vfw1&jvprefix=http%3a%2f%2fwww.zendesk.com&jvresize=https%3a%2f%2fwww.zendesk.com%2fframe-resize&page=Apply&j=ogCBZfwc', 'img':'http://ww1.prweb.com/prfiles/2008/09/08/275118/gI_Zendesklogo.JPG.jpg'}
company_list['appnexus'] = {'name':'AppNexus','description':"AppNexus is a technology company that provides trading solutions and powers marketplaces for Internet advertising. Our open, unified, and powerful programmatic platform empowers customers to more effectively buy and sell media, allowing them to innovate, differentiate, and transform their businesses.",'links':'http://hire.jobvite.com/CompanyJobs/Careers.aspx?k=JobListing&c=qbZ9VfwY&jvresize=http%3A%2F%2Fcareers.appnexus.com%2FFrameResize.html&j=oB1QZfwb%2CApply&v=1', 'img':'https://hirecamp-assets.s3.amazonaws.com/sites/50d39b0f7b4b510002000005/theme/images/logo_appnexus.png'}
company_list['lifesize'] = {'name':'Lifesize', 'description':"LifeSize, a division of Logitech, is a pioneer and world leader in high definition video collaboration. Designed to make video conferencing truly universal, our full range of open standards-based systems offer enterprise-class IT-friendly technologies that enable genuine human interaction over any distance.", 'links':"http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=q9Y9VfwV&page=Apply&j=omdOZfw6", 'img':"http://s3.techshout.com/images/lifesize-logo.jpg"}
company_list['medialets'] = {'name':'Medialets', 'description':"Medialets is a third-party ad serving and rich media ad platform that enables brands, agencies and publishers to more effectively create, deliver and measure mobile and tablet campaigns. Medialets' technology, which is built expressly for mobile, is supported by comprehensive services and a seamless workflow that transforms complex mobile ad executions into measurable and meaningful results.", 'links':"http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qCY9Vfwo&jvprefix=http%3a%2f%2fmedialets.com&jvresize=https%3a%2f%2fmedialets.com%2fjv-frame-resize.html&v=1&page=Apply&j=orM8Wfw1", 'img':"https://medialets.com/wp-content/uploads/2014/11/medialets_logo@2x.png"}
company_list['AppFolio'] = {'name':'AppFolio', 'description':"AppFolio Property Manager is a web-based property management software solution designed to help professional residential property managers focus on growing their business, not managing their software.", 'links':"http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qh79Vfwc&jvprefix=http%3a%2f%2fwww.appfolio.com&cs=9QE9Vfwi&jvresize=http%3a%2f%2fwww.appfolio.com%2fjobvite_frame_resize.html&page=Apply&j=osVGZfwM", 'img':"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSPih8XpJd_pdIUkNZeyARLTUKcyDvrUTaBvO--GfCknE54gbdR"}
company_list['Infinera'] = {'name':'Infinera', 'description':"Infinera Corporation provides optical networking systems based on photonic integration technology in the United States. Its digital transport node (DTN) system utilizes the photonic integrated circuit (PIC) technology to enable digital processing and management of data with the capability to generate wavelength division multiplexing wavelengths and to add, drop, switch, manage, protect, and restore network traffic digitally.", 'links':"http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qKW9Vfwu&jvprefix=http%3a%2f%2fwww.infinera.com&cs=9eVaVfwY&jvresize=http%3a%2f%2fhttp%3a%2f%2finfinera.boldfocus.com%2fcareer%2fFrameResize.html&page=Apply&j=ooKvZfwm", 'img':"http://tiaonline.multiview.com/userlogo/tiaonline/833526v1v1.jpg"}
company_list['InteractiveIntelligence'] = {'name':'InteractiveIntelligence', 'description':"Interactive Intelligence Inc. is a global provider of unified business communications solutions for contact center automation, enterprise IP telephony, and business process automation.", 'links':"http://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qqY9Vfwc&jvprefix=http%3a%2f%2fwww.inin.com&cs=9w4bVfwq&jvresize=http%3a%2f%2fwww.inin.com%2fCareers%2fDocuments%2fframeresize.htm&page=Apply&j=oHUSZfwc", 'img':"http://images.tmcnet.com/online-communities/callcenterinfo/images/test_banner.png"}
company_list['Spokeo'] = {'name': "Spokeo", 'description':"As a people search platform, Spokeo enables friends and family to reconnect, browsing of celebrity profiles, and discovery of information about your own digital footprint, by simply searching a name, home address, phone, email or username. Spokeo can also be used as a research tool for small businesses and non-profit companies.", 'links':"https://boards.greenhouse.io/spokeo/jobs/33554#app", 'img':"http://www.userlogos.org/files/logos/jumpordie/spokeo.png"}
company_list['Pinterest'] = {'name': "Pinterest", 'description':"Pinterest is a web and mobile application company that offers a visual discovery, collection, sharing, and storage tool. Users create and share the collections of visual bookmarks (boards). Boards are created through a user selecting an item, page, website, etc. and pinning it to an existing or newly created board.", 'links':"https://app.greenhouse.io/embed/job_app?token=34498&amp;t=null&amp;b=https://about.pinterest.com/en/careers/cloud-software-engineer-intern_34498", 'img':"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRzPyxpO1_6_8MlPVc2IOTbhDuZE_wv3d7VJWurONuxI9zO2rct"}
company_list['TubeMogul'] = {'name': "TubeMogul", 'description':"TubeMogul is a publicly traded enterprise software platform for digital video advertising. TubeMogul’s programmatic software platform leverages real-time bidding (RTB) technology to help major brands, advertising agencies, trading desks, and publishers advertise to global audiences using online video across multiple devices.", 'links':"https://boards.greenhouse.io/tubemogulinc/jobs/33121?#app", 'img':"http://plesstv.blogs.com/.a/6a00d8341c0d2f53ef017c31939346970b-800wi"}
company_list['Twilio'] = {'name': "Twilio", 'description':"Twilio is a cloud communications (IaaS) company based in San Francisco, California. Twilio allows software developers to programmatically make and receive phone calls and send and receive text messages using its web service APIs.", 'links':"https://boards.greenhouse.io/twilio/jobs/26688#app", 'img':"http://softwareandoutsourcing.files.wordpress.com/2012/01/twilio-logo.png"}
company_list['ThumbTack'] = {'name': "ThumbTack", 'description':"Thumbtack is a consumer service for finding and hiring local professionals, launched in December 2009. Thumbtack allows service providers and consumers to find each other and negotiate jobs online.", 'links':"https://boards.greenhouse.io/thumbtack/jobs/2570?#app", 'img':"http://lasvegasoutdoorkitchen.com/lvok/wp-content/uploads/2013/08/thumbtackLogo.jpg"}
company_list['SurveyMonkey'] = {'name': "SurveyMonkey", 'description':"SurveyMonkey provides free, customizable surveys, as well as a suite of paid back-end programs that include data analysis, sample selection, bias elimination, and data representation tools.", 'links':"https://boards.greenhouse.io/surveymonkey/jobs/30035?#app", 'img':"https://secure.surveymonkey.com/smassets/anonweb/13.2.26-anonweb-0132/assets/brandassets/logo_stacked.png"}
company_list['Blackbaud'] = {'name': "Blackbaud", 'description':"Blackbaud Inc. is a supplier of software and services specifically designed for nonprofit organizations. Its products focus on fundraising, website management, CRM, analytics, financial management, ticketing, and education administration.", 'links':"https://hire.jobvite.com/CompanyJobs/Careers.aspx?c=qWX9VfwH&jvprefix=https%3a%2f%2fwww.blackbaud.com&cs=95XaVfwR&jvresize=https%3a%2f%2fwww.blackbaud.com%2ffiles%2fcareers%2fFrameResize.html&nl=0&page=Apply&j=oWGJZfw4", 'img':"http://teamheller.com/wp-content/uploads/2014/03/blackbaud-logo.jpg"}
company_list['CodeAcademy'] = {'name': "CodeAcademy", 'description':"Codecademy is an online interactive platform that offers free coding classes in six different programming languages like Python, PHP, jQuery, JavaScript, and Ruby, as well as markup languages including HTML and CSS.", 'links':"https://jobs.lever.co/codecademy/865fcd20-1fcf-47ff-bbfc-67dccdb9322a/apply", 'img':"http://cdn.appstorm.net/web.appstorm.net/files/2011/10/codecademy_logo.png"}
company_list['ClearSlide'] = {'name': "ClearSlide", 'description':"ClearSlide is a SaaS-based Sales Engagement platform that lets users share content / sales materials via email links or their viewer’s link in a ‘Live Pitch’. ClearSlide is designed for sales and marketing teams, accessible primarily via an annual subscription model. Users can also sign up for a limited time free trial of the software with full access to all the features of a regular subscription.", 'links':"https://jobs.lever.co/clearslide/ba666e4f-221c-4b8e-bb7d-f435d0d1c105/apply", 'img':"http://mediaserver.pulse2.com/wp-content/uploads/2014/02/ClearSlide-Logo.png"}

company_list['OPower'] = {'name':'OPower', 'description':"Opower is a publicly held Software-as-a-Service company that provides cloud-based software to the utility industry and transforms the way utilities relate to their customers.", 'links':'https://app.greenhouse.io/embed/job_app?for=opower&token=34841&b=http://opower.com/careers/job-openings', 'img':"http://media.glassdoor.com/sqll/313448/opower-squarelogo-1373392289256.png"}
company_list['HomeJoy'] = {'name':'HomeJoy', 'description':"Homejoy is an online platform which connects customers with house cleaners. The company is based in San Francisco.", 'links':"https://app.greenhouse.io/embed/job_app?for=homejoy&token=21041&b=https://www.homejoy.com/job-listings", 'img':"https://www.homejoy.com/static/img/logo-200x200.png"}
company_list['MarinSoftware'] = {'name':"MarinSoftware", 'description':"Marin Software is a publicly traded company that provides advertisers and digital marketing agencies a web-based management platform to manage revenue acquisition through online advertising campaigns. Marin Software provides its customers a single application through which customers can manage paid search, display, mobile, and social marketing campaigns.", 'links':"https://app.greenhouse.io/embed/job_app?for=marinsoftware&token=28606&b=http://marinsoftware.ongig.com/form", 'img':'http://media.marketwire.com/attachments/201201/5267_marinsoft_logo_rgb.jpg'}
company_list['Qualtrics'] = {'name':'Qualtrics', 'description':"Qualtrics is a private research software company, based in Provo, Utah. The company was founded in 2002 by Scott M. Smith, Ryan Smith, Jared Smith and Stuart Orgill.", 'links':"https://boards.greenhouse.io/qualtrics/jobs/36397?gh_src=website#.VHBJTYeUsz4", 'img':"http://news.it.ufl.edu/wp-content/uploads/2012/08/Qualtrics.jpg"}
company_list['Airbnb'] = {'name':"Airbnb", 'description':"Airbnb is a website for people to rent out lodging. It has over 800,000 listings in 33,000 cities and 192 countries.", 'links':"https://app.greenhouse.io/embed/job_app?token=2492&amp;t=2492&amp;b=https://www.airbnb.com/jobs/departments/position/2492", 'img':"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRSUAhuZ6WQJq_H9P8R3351WAllCg13F55gFXryv_A-JDAMEzYD"}
company_list['KhanAcademy'] = {'name':"KhanAcademy", 'description':"Khan Academy is a non-profit educational organization created in 2006 by educator Salman Khan to provide a free, world-class education for anyone, anywhere. The organization produces micro lectures in the form of YouTube videos.", 'links':"https://boards.greenhouse.io/khanacademy/jobs/15827#app", 'img':"http://instructionaltechtalk.com/wp-content/uploads/2012/03/khan-academy-logo-jpg.jpg"}
company_list['RiotGames'] = {'name':"RiotGames", 'description':"Riot Games is an American video game publisher that was established in 2006. Their main office is based in Santa Monica, California.", 'img':"http://upload.wikimedia.org/wikipedia/en/2/23/RiotGamesLogo.jpg", "links":"https://boards.greenhouse.io/riotgames/jobs/10838#app"}