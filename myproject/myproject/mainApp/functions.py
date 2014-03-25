import random
import uuid
from datetime import datetime,timedelta
from myproject.mainApp.models import User,Plan
import json;


def random_date(start,end):
    return start + timedelta(seconds=random.randint(0, int((end-start).total_seconds())))


def random_date_one_week():
    end = datetime.now()
    start = datetime.now()-timedelta(days=7)

    randDate = random_date(start,end)
    return randDate


def addUserRandom(number):
    '''
    adds random users
    '''

    family_names=['smith','johnson','williams','jones','brown','davis','miller','wilson','moore','taylor','anderson','thomas','jackson','white','harris','martin','thompson','garcia','martinez','robinson','clark','rodriguez','lewis','lee','walker','hall','allen','young','hernandez','king','wright','lopez','hill','scott','green','adams','baker','gonzalez','nelson','carter','mitchell','perez','roberts','turner','phillips','campbell','parker','evans','edwards','collins','stewart','sanchez','morris','rogers','reed','cook','morgan','bell','murphy','bailey','rivera','cooper','richardson','cox','howard','ward','torres','peterson','gray','ramirez','james','watson','brooks','kelly','sanders','price','bennett','wood','barnes','ross','henderson','coleman','jenkins','perry','powell','long','patterson','hughes','flores','washington','butler','simmons','foster','gonzales','bryant','alexander','russell','griffin','diaz','hayes','myers','ford','hamilton','graham','sullivan','wallace','woods','cole','west','jordan','owens','reynolds','fisher','ellis','harrison','gibson','mcdonald','cruz','marshall','ortiz','gomez','murray','freeman','wells','webb','simpson','stevens','tucker','porter','hunter','hicks','crawford','henry','boyd','mason','morales','kennedy','warren','dixon','ramos','reyes','burns','gordon','shaw','holmes','rice','robertson','hunt','black','daniels','palmer','mills','nichols','grant','knight','ferguson','rose','stone','hawkins','dunn','perkins','hudson','spencer','gardner','stephens','payne','pierce','berry','matthews','arnold','wagner','willis','ray','watkins','olson','carroll','duncan','snyder','hart','cunningham','bradley','lane','andrews','ruiz','harper','fox','riley','armstrong','carpenter','weaver','greene','lawrence','elliott','chavez','sims','austin','peters','kelley','franklin','lawson','fields','gutierrez','ryan','schmidt','carr','vasquez','castillo','wheeler','chapman','oliver','montgomery','richards','williamson','johnston','banks','meyer','bishop','mccoy','howell','alvarez','morrison','hansen','fernandez','garza','harvey','little','burton','stanley','nguyen','george','jacobs','reid','kim','fuller','lynch','dean','gilbert','garrett','romero','welch','larson','frazier','burke','hanson','day','mendoza','moreno','bowman','medina','fowler','brewer','hoffman','carlson','silva','pearson','holland','douglas','fleming','jensen','vargas','byrd','davidson','hopkins','may','terry','herrera','wade','soto','walters','curtis','neal','caldwell','lowe','jennings','barnett','graves','jimenez','horton','shelton','barrett','obrien','castro','sutton','gregory','mckinney','lucas','miles','craig','rodriquez','chambers','holt','lambert','fletcher','watts','bates','hale','rhodes','pena','beck','newman','haynes','mcdaniel','mendez','bush','vaughn','parks','dawson','santiago','norris','hardy','love','steele','curry','powers','schultz','barker','guzman','page','munoz','ball','keller','chandler','weber','leonard','walsh','lyons','ramsey','wolfe','schneider','mullins','benson','sharp','bowen','daniel','barber','cummings','hines','baldwin','griffith','valdez','hubbard','salazar','reeves','warner','stevenson','burgess','santos','tate','cross','garner','mann','mack','moss','thornton','dennis','mcgee','farmer','delgado','aguilar','vega','glover','manning','cohen','harmon','rodgers','robbins','newton','todd','blair','higgins','ingram','reese','cannon','strickland','townsend','potter','goodwin','walton','rowe','hampton','ortega','patton','swanson','joseph','francis','goodman','maldonado','yates','becker','erickson','hodges','rios','conner','adkins','webster','norman','malone','hammond','flowers','cobb','moody','quinn','blake','maxwell','pope','floyd','osborne','paul','mccarthy','guerrero','lindsey','estrada','sandoval','gibbs','tyler','gross','fitzgerald','stokes','doyle','sherman','saunders','wise','colon','gill','alvarado','greer','padilla','simon','waters','nunez','ballard','schwartz','mcbride','houston','christensen','klein','pratt','briggs','parsons','mclaughlin','zimmerman','french','buchanan','moran','copeland','roy','pittman','brady','mccormick','holloway','brock','poole','frank','logan','owen','bass','marsh','drake','wong','jefferson','park','morton','abbott','sparks','patrick','norton','huff','clayton','massey','lloyd','figueroa','carson','bowers','roberson','barton','tran','lamb','harrington','casey','boone','cortez','clarke','mathis','singleton','wilkins','cain','bryan','underwood','hogan','mckenzie','collier','luna','phelps','mcguire','allison','bridges','wilkerson','nash','summers','atkins','wilcox','pitts','conley','marquez','burnett','richard','cochran','chase','davenport','hood','gates','clay','ayala','sawyer','roman','vazquez','dickerson','hodge','acosta','flynn','espinoza','nicholson','monroe','wolf','morrow','kirk','randall','anthony','whitaker','oconnor','skinner','ware','molina','kirby','huffman','bradford','charles','gilmore','dominguez','oneal','bruce','lang','combs','kramer','heath','hancock','gallagher','gaines','shaffer','short','wiggins','mathews','mcclain','fischer','wall','small','melton','hensley','bond','dyer','cameron','grimes','contreras','christian','wyatt','baxter','snow','mosley','shepherd','larsen','hoover','beasley','glenn','petersen','whitehead','meyers','keith','garrison','vincent','shields','horn','savage','olsen','schroeder','hartman','woodard','mueller','kemp','deleon','booth','patel','calhoun','wiley','eaton','cline','navarro','harrell','lester','humphrey','parrish','duran','hutchinson','hess','dorsey','bullock','robles','beard','dalton','avila','vance','rich','blackwell','york','johns','blankenship','trevino','salinas','campos','pruitt','moses','callahan','golden','montoya','hardin','guerra','mcdowell','carey','stafford','gallegos','henson','wilkinson','booker','merritt','miranda','atkinson','orr','decker','hobbs','preston','tanner','knox','pacheco','stephenson','glass','rojas','serrano','marks','hickman','english','sweeney','strong','prince','mcclure','conway','walter','roth','maynard','farrell','lowery','hurst','nixon','weiss','trujillo','ellison','sloan','juarez','winters','mclean','randolph','leon','boyer','villarreal','mccall','gentry','carrillo','kent','ayers','lara','shannon','sexton','pace','hull','leblanc','browning','velasquez','leach','chang','house','sellers','herring','noble','foley','bartlett','mercado','landry','durham','walls','barr','mckee','bauer','rivers','everett','bradshaw','pugh','velez','rush','estes','dodson','morse','sheppard','weeks','camacho','bean','barron','livingston','middleton','spears','branch','blevins','chen','kerr','mcconnell','hatfield','harding','ashley','solis','herman','frost','giles','blackburn','william','pennington','woodward','finley','mcintosh','koch','best','solomon','mccullough','dudley','nolan','blanchard','rivas','brennan','mejia','kane','benton','joyce','buckley','haley','valentine','maddox','russo','mcknight','buck','moon','mcmillan','crosby','berg','dotson','mays','roach','church','chan','richmond','meadows','faulkner','oneill','knapp','kline','barry','ochoa','jacobson','gay','avery','hendricks','horne','shepard','hebert','cherry','cardenas','mcintyre','whitney','waller','holman','donaldson','cantu','terrell','morin','gillespie','fuentes','tillman','sanford','bentley','peck','key','salas','rollins','gamble','dickson','battle','santana','cabrera','cervantes','howe','hinton','hurley','spence','zamora','yang','mcneil','suarez','case','petty','gould','mcfarland','sampson','carver','bray','rosario','macdonald','stout','hester','melendez','dillon','farley','hopper','galloway','potts','bernard','joyner','stein','aguirre','osborn','mercer','bender','franco','rowland','sykes','benjamin','travis','pickett','crane','sears','mayo','dunlap','hayden','wilder','mckay','coffey','mccarty','ewing','cooley','vaughan','bonner','cotton','holder','stark','ferrell','cantrell','fulton','lynn','lott','calderon','rosa','pollard','hooper','burch','mullen','fry','riddle','levy','david','duke','odonnell','guy','michael','britt','frederick','daugherty','berger','dillard','alston','jarvis','frye','riggs','chaney','odom','duffy','fitzpatrick','valenzuela','merrill','mayer','alford','mcpherson','acevedo','donovan','barrera','albert','cote','reilly','compton','raymond','mooney','mcgowan','craft','cleveland','clemons','wynn','nielsen','baird','stanton','snider','rosales','bright','witt','stuart','hays','holden','rutledge','kinney','clements','castaneda','slater','hahn','emerson','conrad','burks','delaney','pate','lancaster','sweet','justice','tyson','sharpe','whitfield','talley','macias','irwin','burris','ratliff','mccray','madden','kaufman','beach','goff','cash','bolton','mcfadden','levine','good','byers','kirkland','kidd','workman','carney','dale','mcleod','holcomb','england','finch','head','burt','hendrix','sosa','haney','franks','sargent','nieves','downs','rasmussen','bird','hewitt','lindsay','le','foreman','valencia','oneil','delacruz','vinson','dejesus','hyde','forbes','gilliam','guthrie','wooten','huber','barlow','boyle','mcmahon','buckner','rocha','puckett','langley','knowles','cooke','velazquez','whitley','noel','vang']
    male_names = ['james','john','robert','michael','william','david','richard','charles','joseph','thomas','christopher','daniel','paul','mark','donald','george','kenneth','steven','edward','brian','ronald','anthony','kevin','jason','matthew','gary','timothy','jose','larry','jeffrey','frank','scott','eric','stephen','andrew','raymond','gregory','joshua','jerry','dennis','walter','patrick','peter','harold','douglas','henry','carl','arthur','ryan','roger','joe','juan','jack','albert','jonathan','justin','terry','gerald','keith','samuel','willie','ralph','lawrence','nicholas','roy','benjamin','bruce','brandon','adam','harry','fred','wayne','billy','steve','louis','jeremy','aaron','randy','howard','eugene','carlos','russell','bobby','victor','martin','ernest','phillip','todd','jesse','craig','alan','shawn','clarence','sean','philip','chris','johnny','earl','jimmy','antonio','danny','bryan','tony','luis','mike','stanley','leonard','nathan','dale','manuel','rodney','curtis','norman','allen','marvin','vincent','glenn','jeffery','travis','jeff','chad','jacob','lee','melvin','alfred','kyle','francis','bradley','jesus','herbert','frederick','ray','joel','edwin','don','eddie','ricky','troy','randall','barry','alexander','bernard','mario','leroy','francisco','marcus','micheal','theodore','clifford','miguel','oscar','jay','jim','tom','calvin','alex','jon','ronnie','bill','lloyd','tommy','leon','derek','warren','darrell','jerome','floyd','leo','alvin','tim','wesley','gordon','dean','greg','jorge','dustin','pedro','derrick','dan','lewis','zachary','corey','herman','maurice','vernon','roberto','clyde','glen','hector','shane','ricardo','sam','rick','lester','brent','ramon','charlie','tyler','gilbert','gene','marc','reginald','ruben','brett','angel','nathaniel','rafael','leslie','edgar','milton','raul','ben','chester','cecil','duane','franklin','andre','elmer','brad','gabriel','ron','mitchell','roland','arnold','harvey','jared','adrian','karl','cory','claude','erik','darryl','jamie','neil','jessie','christian','javier','fernando','clinton','ted','mathew','tyrone','darren','lonnie','lance','cody','julio','kelly','kurt','allan','nelson','guy','clayton','hugh','max','dwayne','dwight','armando','felix','jimmie','everett','jordan','ian','wallace','ken','bob','jaime','casey','alfredo','alberto','dave','ivan','johnnie','sidney','byron','julian','isaac','morris','clifton','willard','daryl','ross','virgil','andy','marshall','salvador','perry','kirk','sergio','marion','tracy','seth','kent','terrance','rene','eduardo','terrence','enrique','freddie','wade']
    female_names = ['mary','patricia','linda','barbara','elizabeth','jennifer','maria','susan','margaret','dorothy','lisa','nancy','karen','betty','helen','sandra','donna','carol','ruth','sharon','michelle','laura','sarah','kimberly','deborah','jessica','shirley','cynthia','angela','melissa','brenda','amy','anna','rebecca','virginia','kathleen','pamela','martha','debra','amanda','stephanie','carolyn','christine','marie','janet','catherine','frances','ann','joyce','diane','alice','julie','heather','teresa','doris','gloria','evelyn','jean','cheryl','mildred','katherine','joan','ashley','judith','rose','janice','kelly','nicole','judy','christina','kathy','theresa','beverly','denise','tammy','irene','jane','lori','rachel','marilyn','andrea','kathryn','louise','sara','anne','jacqueline','wanda','bonnie','julia','ruby','lois','tina','phyllis','norma','paula','diana','annie','lillian','emily','robin','peggy','crystal','gladys','rita','dawn','connie','florence','tracy','edna','tiffany','carmen','rosa','cindy','grace','wendy','victoria','edith','kim','sherry','sylvia','josephine','thelma','shannon','sheila','ethel','ellen','elaine','marjorie','carrie','charlotte','monica','esther','pauline','emma','juanita','anita','rhonda','hazel','amber','eva','debbie','april','leslie','clara','lucille','jamie','joanne','eleanor','valerie','danielle','megan','alicia','suzanne','michele','gail','bertha','darlene','veronica','jill','erin','geraldine','lauren','cathy','joann','lorraine','lynn','sally','regina','erica','beatrice','dolores','bernice','audrey','yvonne','annette','june','samantha','marion','dana','stacy','ana','renee','ida','vivian','roberta','holly','brittany','melanie','loretta','yolanda','jeanette','laurie','katie','kristen','vanessa','alma','sue','elsie','beth','jeanne','vicki','carla','tara','rosemary','eileen','terri','gertrude','lucy','tonya','ella','stacey','wilma','gina','kristin','jessie','natalie','agnes','vera','willie','charlene','bessie','delores','melinda','pearl','arlene','maureen','colleen','allison','tamara','joy','georgia','constance','lillie','claudia','jackie','marcia','tanya','nellie','minnie','marlene','heidi','glenda','lydia','viola','courtney','marian','stella','caroline','dora','jo','vickie','mattie','terry','maxine','irma','mabel','marsha','myrtle','lena','christy','deanna','patsy','hilda','gwendolyn','jennie','nora','margie','nina','cassandra','leah','penny','kay','priscilla','naomi','carole','brandy','olga','billie','dianne','tracey','leona','jenny','felicia','sonia','miriam','velma','becky','bobbie','violet','kristina','toni','misty','mae','shelly','daisy','ramona','sherri','erika','katrina','claire','lindsey','lindsay','geneva','guadalupe','belinda','margarita','sheryl','cora','faye','ada','natasha','sabrina','isabel','marguerite','hattie','harriet','molly','cecilia','kristi','brandi','blanche','sandy','rosie','joanna','iris','eunice','angie','inez','lynda','madeline','amelia','alberta','genevieve','monique','jodi','janie','maggie','kayla','sonya','jan','lee','kristine','candace','fannie','maryann','opal','alison','yvette','melody','luz','susie','olivia','flora','shelley','kristy','mamie','lula','lola','verna','beulah','antoinette','candice','juana','jeannette','pam','kelli','hannah','whitney','bridget','karla','celia','latoya','patty','shelia','gayle','della','vicky','lynne','sheri','marianne','kara','jacquelyn','erma','blanca','myra','leticia','pat','krista','roxanne','angelica','johnnie','robyn','francis','adrienne','rosalie','alexandra','brooke','bethany','sadie','bernadette','traci','jody','kendra','jasmine','nichole','rachael','chelsea','mable','ernestine','muriel','marcella','elena','krystal','angelina','nadine','kari','estelle','dianna','paulette','lora','mona','doreen','rosemarie','angel','desiree','antonia','hope','ginger','janis','betsy','christie','freda','mercedes','meredith','lynette','teri','cristina','eula','leigh','meghan','sophia','eloise','rochelle','gretchen','cecelia','raquel','henrietta','alyssa','jana','kelley','gwen','kerry','jenna','tricia','laverne','olive','alexis','tasha','silvia','elvira','casey','delia','sophie','kate','patti','lorena','kellie','sonja','lila','lana','darla','may','mindy','essie','mandy','lorene','elsa','josefina','jeannie','miranda','dixie','lucia','marta','faith','lela','johanna','shari','camille','tami','shawna','elisa','ebony','melba','ora','nettie','tabitha','ollie','jaime','winifred','kristie','marina','alisha','aimee','rena','myrna','marla','tammie','latasha','bonita','patrice','ronda','sherrie','addie','francine','deloris','stacie','adriana','cheri','shelby','abigail','celeste','jewel','cara','adele','rebekah','lucinda','dorthy','chris','effie','trina','reba','shawn','sallie','aurora','lenora','etta','lottie','kerri','trisha','nikki','estella','francisca','josie','tracie','marissa','karin','brittney','janelle','lourdes','laurel','helene','fern','elva','corinne','kelsey','ina','bettie','elisabeth','aida','caitlin','ingrid','iva','eugenia','christa','goldie','cassie','maude','jenifer','therese','frankie','dena','lorna','janette','latonya','candy','morgan','consuelo','tamika','rosetta','debora','cherie','polly','dina','jewell','fay','jillian','dorothea','nell','trudy','esperanza','patrica','kimberley','shanna','helena','carolina','cleo','stefanie','rosario','ola','janine','mollie','lupe','alisa','lou','maribel','susanne','bette','susana','elise','cecile','isabelle','lesley','jocelyn','paige','joni','rachelle','leola','daphne','alta','ester','petra','graciela','imogene','jolene','keisha','lacey','glenna','gabriela','keri','ursula','lizzie','kirsten','shana','adeline','mayra','jayne','jaclyn','gracie','sondra','carmela','marisa','rosalind','charity','tonia','beatriz','marisol','clarice','jeanine','sheena','angeline','frieda','lily','robbie','shauna','millie','claudette','cathleen','angelia','gabrielle','autumn','katharine','summer','jodie','staci','lea','christi','jimmie','justine','elma','luella','margret','dominique','socorro','rene','martina','margo','mavis','callie','bobbi','maritza','lucile','leanne','jeannine','deana','aileen','lorie','ladonna','willa','manuela','gale','selma','dolly','sybil','abby','lara','dale','ivy','dee','winnie','marcy','luisa','jeri','magdalena','ofelia','meagan','audra','matilda','leila','cornelia','bianca','simone','bettye','randi','virgie','latisha','barbra','georgina','eliza','leann','bridgette','rhoda','haley','adela','nola','bernadine','flossie','ila','greta','ruthie','nelda','minerva','lilly','terrie','letha','hilary','estela','valarie','brianna','rosalyn','earline','catalina','ava','mia','clarissa','lidia','corrine','alexandria','concepcion','tia','sharron','rae','dona','ericka','jami','elnora','chandra','lenore','neva','marylou','melisa','tabatha','serena','avis','allie','sofia','jeanie','odessa','nannie','harriett','loraine','penelope','milagros','emilia','benita','allyson','ashlee','tania','tommie','esmeralda','karina','eve','pearlie','zelma','malinda','noreen','tameka','saundra','hillary','amie','althea','rosalinda','jordan','lilia','alana','gay','clare','alejandra','elinor','michael','lorrie','jerri','darcy','earnestine','carmella','taylor','noemi','marcie','liza','annabelle','louisa','earlene','mallory','carlene','nita','selena','tanisha','katy','julianne','john','lakisha','edwina','maricela','margery','kenya','dollie','roxie','roslyn','kathrine','nanette','charmaine','lavonne','ilene','kris','tammi','suzette','corine','kaye','jerry','merle','chrystal','lina','deanne','lilian','juliana','aline','luann','kasey','maryanne','evangeline','colette','melva','lawanda','yesenia','nadia','madge','kathie','eddie','ophelia','valeria','nona','mitzi','mari','georgette','claudine','fran','alissa','roseann','lakeisha','susanna','reva','deidre','chasity','sheree','carly','james','elvia','alyce','deirdre','gena','briana','araceli','katelyn','rosanne','wendi','tessa','berta','marva','imelda','marietta','marci','leonor','arline','sasha','madelyn','janna','juliette','deena','aurelia','josefa','augusta','liliana','young','christian','lessie','amalia','savannah','anastasia','vilma','natalia','rosella','lynnette','corina','alfreda','leanna','carey','amparo','coleen','tamra','aisha','wilda','karyn','cherry','queen','maura','mai','evangelina','rosanna','hallie','erna','enid','mariana','lacy','juliet','jacklyn','freida','madeleine','mara','hester','cathryn','lelia','casandra','bridgett','angelita','jannie','dionne','annmarie','katina','beryl','phoebe','millicent','katheryn','diann','carissa','maryellen','liz','lauri','helga','gilda','adrian','rhea','marquita','hollie','tisha','tamera','angelique','francesca','britney','kaitlin','lolita','florine','rowena','reyna','twila','fanny','janell','ines','concetta','bertie','alba','brigitte','alyson','vonda','pansy','elba','noelle','letitia','kitty','deann','brandie','louella','leta','felecia','sharlene','lesa','beverley','robert','isabella','herminia','terra','celina']

    for i in range(number):
        familyname = random.choice(family_names)

        if random.random()<0.5:
            last_name = random.choice(male_names)
        else:
            last_name = random.choice(female_names)

        user_name = last_name+familyname
        user_email = user_name+'@randomuser.com'
        user_password = familyname+last_name
        user_points = -1.0
        user_avatar = ''
        user_last_creation = random_date_one_week()
        user_last_evaluation = random_date_one_week()

        user = User(
            name = user_name,
            email = user_email,
            password = user_password,
            points = user_points,
            avatar = user_avatar,
            last_creation = user_last_creation,
            last_evaluation = user_last_evaluation
        )

        user.save()

        print 'added %s' %user_name

def addPlanRandom(number):
    users = User.objects.all()
    plans = Plan.objects.all()

    prefixes = ['a','acro','allo','an','ante','anti','auto','bi','co','contra','counter','de','di','dis','dys','epi','extra','hemi','hexa','hyper','hypo','ig','im','in','infra','inter','intra','ir','macro','mal','maxi','meso','micro','mid','mini','mono','multi','non','octo','over','pan','para','penta','peri','per','poly','post','pre','pro','proto','pseudo','quadri','quasi','re','self','semi','sub','super','supra','tetra','trans','tri','ultra','un','under','xeno']
    constellations = ['andromeda','antlia','apus','aquarius','aquila','ara','aries','auriga','bootes','caelum','camelopardalis','cancer','canesvenatici','canismajor','canisminor','capricornus','carina','cassiopeia','centaurus','cepheus','cetus','chamaeleon','circinus','columba','comaberenices','coronaaustrina','coronaborealis','corvus','crater','crux','cygnus','delphinus','dorado','draco','equuleus','eridanus','fornax','gemini','grus','hercules','horologium','hydra','hydrus','indus','lacerta','leo','leominor','lepus','libra','lupus','lynx','lyra','mensa','microscopium','monoceros','musca','norma','octans','ophiuchus','orion','pavo','pegasus','perseus','phoenix','pictor','pisces','piscis austrinus','puppis','pyxis','reticulum','sagitta','sagittarius','scorpius','sculptor','scutum','serpens','sextans','taurus','telescopium','triangulum','triangulumaustrale','tucana','ursa major','ursaminor','vela','virgo','volans','vulpecula']

    if len(plans)<1:
        #add initial plan
        number -= 1

        prefix = random.choice(prefixes)
        constellation = random.choice(constellations)

        geomData = {'site': [], 'woodFloor': [], 'concreteFloor': [], 'woodWall': [], 'concreteWall': [], 'glassWall': []}

        for i in range(5):
            geomData['site'].append([random.randint(0, 64), random.randint(0, 4)])
            geomData['woodFloor'].append([random.randint(0, 64), random.randint(0, 4)])
            geomData['concreteFloor'].append([random.randint(0, 64), random.randint(0, 4)])
            geomData['woodWall'].append([random.randint(0, 144), random.randint(0, 3)])
            geomData['concreteWall'].append([random.randint(0, 144), random.randint(0, 3)])
            geomData['glassWall'].append([random.randint(0, 144), random.randint(0, 3)])


        plan = Plan(
           name = prefix+constellation+str(1),
           initial_points = random.randint(1,100),
           additional_points = random.randint(1,100),
           creation_time = random_date_one_week(),
           geometry = json.dumps(geomData),
           image = '',
           similarity = -1,
           user = random.choice(users)
        )

        plan.save()
        print 'added %s' % prefix+constellation

        if number <1 :return

    for i in range(number):
        print len(plans)
        prefix = random.choice(prefixes)
        constellation =random .choice(constellations)

        geomData = {'site': [], 'woodFloor': [], 'concreteFloor': [], 'woodWall': [], 'concreteWall': [], 'glassWall': []}

        for i in range(5):
            geomData['site'].append([random.randint(0, 64), random.randint(0, 4)])
            geomData['woodFloor'].append([random.randint(0, 64), random.randint(0, 4)])
            geomData['concreteFloor'].append([random.randint(0, 64), random.randint(0, 4)])
            geomData['woodWall'].append([random.randint(0, 144), random.randint(0, 3)])
            geomData['concreteWall'].append([random.randint(0, 144), random.randint(0, 3)])
            geomData['glassWall'].append([random.randint(0, 144), random.randint(0, 3)])

        model_name = prefix+constellation+str(len(plans)+2)

        sim = random.uniform(0.001, 0.999)
        plans = Plan.objects.all() # will this change the parents??
        parent = random.choice(plans)

        plan = Plan(
            name = model_name,
            initial_points = parent.total_points() * sim,
            additional_points = random.randint(1, 100),
            creation_time = random_date_one_week(),
            geometry = geomData,
            image = '',
            similarity = sim,
            user = random.choice(users),
            relation = parent
        )

        plan.save()
        print 'added %s' % model_name
