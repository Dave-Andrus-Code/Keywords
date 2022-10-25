# UTILS
# Written by DMA on 2022-10-23
# Simple quality of life tools I use to expedite projects
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# --------------------------------------------------------------------------------------------------------------------------------

import numpy as np

def excerpt (line, word, numwords):
    s = line.split(' ')
    try:
        i = s.index(word) # find the keyword in the sentence
    except:
        i = s.index(word + 's') # find the plural keyword in the sentence
    i = i - numwords    # start a few words before the keyword
    excerpt = ''
    for x in range(i, i+(numwords*2)+1):
        try:
            excerpt = excerpt + s[x] + ' '
        except:
            #  Nothing; this protects against subscript out of range
            pass
    return excerpt


def strstrip (ostr):
    # strip all the extraneous characters except what is allowed
    # allowed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,;:-_=+\'\"!@#$%^&*()'
    allowed = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890-'
    strstrip = ''.join(l for l in ostr if l in allowed)
    return strstrip

def normal_dist(x , mean , sd):
    # Simple normal distribution formula
    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)
    return prob_density

# Word Lists

# Articles, prepositions, being, pronouns, auxilary verbs
ignore = [
    # artlces
    'a',
    'an',
    'the',
    # prepositions
    'aboard',
    'about',
    'above',
    'across',
    'after',
    'against',
    'along',
    'amid',
    'among',
    'anti',
    'around',
    'as',
    'at',
    'before',
    'behind',
    'below',
    'beneath',
    'beside',
    'besides',
    'between',
    'beyond',
    'but',
    'by',
    'concerning',
    'considering',
    'despite',
    'down',
    'during',
    'except',
    'excepting',
    'excluding',
    'following',
    'for',
    'from',
    'in',
    'inside',
    'into',
    'like',
    'minus',
    'near',
    'of',
    'off',
    'on',
    'onto',
    'opposite',
    'or',
    'outside',
    'over',
    'past',
    'per',
    'plus',
    'regarding',
    'round',
    'save',
    'since',
    'than',
    'through',
    'to',
    'toward',
    'towards',
    'under',
    'underneath',
    'unlike',
    'until',
    'up',
    'upon',
    'versus',
    'via',
    'with',
    'within',
    'without',
    'because',
    'although',
    'whereas',
    #conjunctions
    'but',
    'besides',
    'unlike',
    'therefore',
    'provided',
    'unless',
    'since',
    'so',
    'if',
    'yet',
    'for',
    'and',
    'nor',
    'so',
    'where',
    # state of being
    'am',
    'are',
    'is',
    'was',
    'were',
    'been',
    'being',
    # personal pronouns
    'i',
    'you',
    'he',
    'she',
    'it',
    'we',
    'you',
    'they',
    'me',
    'him',
    'her',
    'us',
    'them',
    'mine',
    'our',
    'ours',
    'its'
    'their'
    'theirs',
    #auxilary verbs
    'be',
    'am',
    'is',
    'are',
    'was',
    'were',
    'being',
    'been',
    # other
    'that',
    'this',
    'have'
]

# nouns that end in an S
snouns = [
    'business ', 
    'process ', 
    'class ', 
    'basis ', 
    'series ', 
    'news ', 
    'success ', 
    'analysis ', 
    'loss ', 
    'press ', 
    'access ', 
    'species ', 
    'glass ', 
    'status ', 
    'progress ', 
    'gas ', 
    'crisis ', 
    'congress ', 
    'emphasis ', 
    'bus ', 
    'address ', 
    'cross ', 
    'jones ', 
    'grass ', 
    'dress ', 
    'stress ', 
    'lewis ', 
    'focus ', 
    'mass ', 
    'awareness ', 
    'illness ', 
    'earnings ', 
    'darkness ', 
    'boss ', 
    'economics ', 
    'princess ', 
    'tennis ', 
    'consciousness ', 
    'louis ', 
    'effectiveness ', 
    'mathematics ', 
    'harris ', 
    'mess ', 
    'ross ', 
    'jews ', 
    'consensus ', 
    'morris ', 
    'excess ', 
    'witness ', 
    'diagnosis ', 
    'weakness ', 
    'ms ', 
    'hypothesis ', 
    'happiness ', 
    'chaos ', 
    'fitness ', 
    'virus ', 
    'distress ', 
    'brass ', 
    'stimulus ', 
    'goodness ', 
    'bonus ', 
    'bias ', 
    'les ', 
    'surplus ', 
    'thesis ', 
    'synthesis ', 
    'sickness ', 
    'willingness ', 
    'corps ', 
    'apparatus ', 
    'collins ', 
    'canvas ', 
    'mistress ', 
    'actress ', 
    'genius ', 
    'axis ', 
    'census ', 
    'colitis ', 
    'texas ', 
    'jacques ', 
    'chorus ', 
    'dealings ', 
    'lotus ', 
    'iris ', 
    'travis ', 
    'hastings ', 
    'moss ', 
    'duchess ', 
    'madness ', 
    'fuss ', 
    'sadness ', 
    'debris ', 
    'corpus ', 
    'circus ', 
    'thickness ', 
    'fairness ', 
    'kindness ', 
    'bitterness ', 
    'wilderness ', 
    'dickens ', 
    'hepatitis ', 
    'nucleus ', 
    'diabetes ', 
    'impetus ', 
    'radius ', 
    'campus ', 
    'chess ', 
    'ps ', 
    'saunders ', 
    'syllabus ', 
    'readiness ', 
    'genesis ', 
    'compass ', 
    'loneliness ', 
    'competitiveness ', 
    'goddess ', 
    'seriousness ', 
    'bypass ', 
    'venus ', 
    'jess ', 
    'binoculars ', 
    'penis ', 
    'usefulness ', 
    'countess ', 
    'oesophagus ', 
    'fortress ', 
    'siemens ', 
    'openness ', 
    'arthritis ', 
    'mattress ', 
    'psychoanalysis ', 
    'ethos ', 
    'locus ', 
    'forgiveness ', 
    'exodus ', 
    'cannabis ', 
    'lass ', 
    'tallis ', 
    'richness ', 
    'gis ', 
    'burgess ', 
    'brightness ', 
    'reasonableness ', 
    'bliss ', 
    'empress ', 
    'hostess ', 
    'genus ', 
    'tenderness ', 
    'blackness ', 
    'tuberculosis ', 
    'gloss ', 
    'knickers ', 
    'stillness ', 
    'homelessness ', 
    'harness ', 
    'gastritis ', 
    'pancreatitis ', 
    'closeness ', 
    'chassis ', 
    'faeces ', 
    'unhappiness ', 
    'nervousness ', 
    'hardness ', 
    'aerobics ', 
    'emptiness ', 
    'marquis ', 
    'asbestos ', 
    'ass ', 
    'sweetness ', 
    'cleanliness ', 
    'fungus ', 
    'blindness ', 
    'os ', 
    'sharpness ', 
    'bollocks ', 
    'fibrosis ', 
    'greatness ', 
    'terminus ', 
    'es ', 
    'tiredness ', 
    'prospectus ', 
    'unwillingness ', 
    'prowess ', 
    'oesophagitis ', 
    'pathogenesis ', 
    'waitress ', 
    'attractiveness ', 
    'syphilis ', 
    'highness ', 
    'atlas ', 
    'piss ', 
    'prognosis ', 
    'hypnosis ', 
    'underclass ', 
    'headmistress ', 
    'softness ', 
    'minibus ', 
    'likeness ', 
    'modulus ', 
    'baroness ', 
    'onus ', 
    'uniqueness ', 
    'fullness ', 
    'politeness ', 
    'rendezvous ', 
    'stiffness ', 
    'meningitis ', 
    'helplessness ', 
    'mucus ', 
    'appropriateness ', 
    'metropolis ', 
    'recess ', 
    'eagerness ', 
    'coldness ', 
    'trespass ', 
    'foetus ', 
    'friendliness ', 
    'ness ', 
    'freshness ', 
    'gentleness ', 
    'paralysis ', 
    'thesaurus ', 
    'cholangitis ', 
    'selfishness ', 
    'tardis ', 
    'distinctiveness ', 
    'completeness ', 
    'airbus ', 
    'hiss ', 
    'pelvis ', 
    'toss ', 
    'deixis ', 
    'psychosis ', 
    'antithesis ', 
    'phosphorus ', 
    'pancreas ', 
    'duress ', 
    'judas ', 
    'heiress ', 
    'biomass ', 
    'droppings ', 
    'lightness ', 
    'correctness ', 
    'remoteness ', 
    'cypress ', 
    'shyness ', 
    'righteousness ', 
    'toughness ', 
    'carelessness ', 
    'nightdress ', 
    'holiness ', 
    'governess ', 
    'deafness ', 
    'sclerosis ', 
    'octopus ', 
    'assertiveness ', 
    'hopelessness ', 
    'pons ', 
    'bronchitis ', 
    'jacobs ', 
    'responsiveness ', 
    'photosynthesis ', 
    'pegasus ', 
    'cirrhosis ', 
    'marquess ', 
    'weariness ', 
    'buttress ', 
    'wickedness ', 
    'recklessness ', 
    'mavis ', 
    'fondness ', 
    'drunkenness ', 
    'ras ', 
    'slowness ', 
    'whiteness ', 
    'firmness ', 
    'uterus ', 
    'idleness ', 
    'missus ', 
    'unfairness ', 
    'self-consciousness ', 
    'celsius ', 
    'indebtedness ', 
    'underpants ', 
    'tetanus ', 
    'smoothness ', 
    'aegis ', 
    'abyss ', 
    'anus ', 
    'tectonics ', 
    'bedclothes ', 
    'harshness ', 
    'powerlessness ', 
    'restlessness ', 
    'carcass ', 
    'strangeness ', 
    'patois ', 
    'coolness ', 
    'electrophoresis ', 
    'nakedness ', 
    'neurosis ', 
    'vagueness ', 
    'omnibus ', 
    'detritus ', 
    'fetus ', 
    'wholeness ', 
    'quietness ', 
    'directness ', 
    'ugliness ', 
    'tass ', 
    'dryness ', 
    'madras ', 
    'tightness ', 
    'calculus ', 
    'caress ', 
    'dampness ', 
    'cheerfulness ', 
    'nexus ', 
    'isis ', 
    'dialysis ', 
    'res ', 
    'opus ', 
    'herpes ', 
    'thoroughness ', 
    'forceps ', 
    'majlis ', 
    'ascites ', 
    'necrosis ', 
    'thrombosis ', 
    'dais ', 
    'asparagus ', 
    'jus ', 
    'pathos ', 
    'sis ', 
    'frankness ', 
    'hiatus ', 
    'self-awareness ', 
    'thermodynamics ', 
    'ruthlessness ', 
    'nearness ', 
    'watercress ', 
    'eyewitness ', 
    'fibreglass ', 
    'metamorphosis ', 
    'preparedness ', 
    'laziness ', 
    'rightness ', 
    'facies ', 
    'praxis ', 
    'narrowness ', 
    'macroeconomics ', 
    'permissiveness ', 
    'manageress ', 
    'rudeness ', 
    'doldrums ', 
    'cleverness ', 
    'parvis ', 
    'rhinoceros ', 
    'pres ', 
    'geophysics ', 
    'osteoporosis ', 
    'truss ', 
    'unconsciousness ', 
    'redness ', 
    'trellis ', 
    'stenosis ', 
    'prioress ', 
    'synopsis ', 
    'boldness ', 
    'dizziness ', 
    'showbusiness ', 
    'incubus ', 
    'awkwardness ', 
    'caucus ', 
    'discus ', 
    'stylus ', 
    'numbness ', 
    'cystitis ', 
    'soundness ', 
    'nothingness ', 
    'unpleasantness ', 
    'cost-effectiveness ', 
    'gallows ', 
    'pus ', 
    'hippocampus ', 
    'stasis ', 
    'suppleness ', 
    'alms ', 
    'tripos ', 
    'uneasiness ', 
    'alertness ', 
    'acropolis ', 
    'clematis ', 
    'inventiveness ', 
    'poetics ', 
    'argus ', 
    'nimbus ', 
    'lawlessness ', 
    'clitoris ', 
    'backwardness ', 
    'sepsis ', 
    'endometriosis ', 
    'foolishness ', 
    'roughness ', 
    'otherness ', 
    'calmness ', 
    'stratus ', 
    'rabies ', 
    'eugenics ', 
    'cactus ', 
    'lexis ', 
    'vastness ', 
    'camus ', 
    'steelworks ', 
    'heaviness ', 
    'ineffectiveness ', 
    'epidermis ', 
    'fracas ', 
    'thrombolysis ', 
    'cress ', 
    'lateness ', 
    'lysis ', 
    'econometrics ', 
    'aeronautics ', 
    'anastomosis ', 
    'ergonomics ', 
    'thymus ', 
    'eye-witness ', 
    'togetherness ', 
    'chrysalis ', 
    'aggressiveness ', 
    'sinus ', 
    'neatness ', 
    'suddenness ', 
    'sarcophagus ', 
    'corydoras ', 
    'agonistes ', 
    'stubbornness ', 
    'cheapness ', 
    'ordinariness ', 
    'ironworks ', 
    'dungarees ', 
    'wetness ', 
    'aerobatics ', 
    'plexus ', 
    'avionics ', 
    'explicitness ', 
    'mayoress ', 
    'albatross ', 
    'thermos ', 
    'peristalsis ', 
    'floss ', 
    'mandamus ', 
    'sameness ', 
    'naturalness ', 
    'urethritis ', 
    'johannes ', 
    'toxoplasmosis ', 
    'wildness ', 
    'morass ', 
    'pouchitis ', 
    'apoptosis ', 
    'gasworks ', 
    'nemesis ', 
    'thinness ', 
    'bolus ', 
    'stickiness ', 
    'marchioness ', 
    'forgetfulness ', 
    'robustness ', 
    'priestess ', 
    'gramps ', 
    'maleness ', 
    'regress ', 
    'meanness ', 
    'tinnitus ', 
    'enteritis ', 
    'rhesus ', 
    'cytomegalovirus ', 
    'oneness ', 
    'dullness ', 
    'sociolinguistics ', 
    'wariness ', 
    'walrus ', 
    'handedness ', 
    'drowsiness ', 
    'nastiness ', 
    'unreasonableness ', 
    'separateness ', 
    'osmosis ', 
    'newness ', 
    'appendicitis ', 
    'smallness ', 
    'gauss ', 
    'stewardess ', 
    'underclothes ', 
    'faithfulness ', 
    'shortness ', 
    'tbs ', 
    'civitas ', 
    'bacillus ', 
    'loudness ', 
    'greyness ', 
    'cohesiveness ', 
    'narcissus ', 
    'duodenitis ', 
    'eros ', 
    'papyrus ', 
    'symbiosis ', 
    'homesickness ', 
    'expressiveness ', 
    'abbess ', 
    'comprehensiveness ', 
    'tidiness ', 
    'astrophysics ', 
    'soreness ', 
    'hubris ', 
    'amniocentesis ', 
    'crocus ', 
    'wakefulness ', 
    'papillomavirus ', 
    'prophylaxis ', 
    'apotheosis ', 
    'atherosclerosis ', 
    'joss ', 
    'secateurs ', 
    'humus ', 
    'dimness ', 
    'abacus ', 
    'lomas ', 
    'randomness ', 
    'challis ', 
    'cumulus ', 
    'dermatitis ', 
    'exegesis ', 
    'ess ', 
    'casualness ', 
    'spaciousness ', 
    'representativeness ', 
    'meaningfulness ', 
    'hydrolysis ', 
    'polyposis ', 
    'caddis ', 
    'goss ', 
    'subclass ', 
    'flatness ', 
    'beaux-arts ', 
    'lupus ', 
    'paratuberculosis ', 
    'headdress ', 
    'colossus ', 
    'arbitrariness ', 
    'aloofness ', 
    'puss ', 
    'liveliness ', 
    'airworthiness ', 
    'humerus ', 
    'prettiness ', 
    'trolleybus ', 
    'litmus ', 
    'lioness ', 
    'habitus ', 
    'shrewdness ', 
    'subspecies ', 
    'creditworthiness ', 
    'amicus ', 
    'badlands ', 
    'veritas ', 
    'tigress ', 
    'abscess ', 
    'torus ', 
    'hibiscus ', 
    'scabies ', 
    'fineness ', 
    'baldness ', 
    'bleakness ', 
    'earnestness ', 
    'playfulness ', 
    'sinfulness ', 
    'metastasis ', 
    'semi-darkness ', 
    'eucalyptus ', 
    'self-righteousness ', 
    'chamois ', 
    'silliness ', 
    'breathlessness ', 
    'candidiasis ', 
    'phallus ', 
    'polis ', 
    'precis ', 
    'haves ', 
    'endoprosthesis ', 
    'smugness ', 
    'stats ', 
    'cosiness ', 
    'typhus ', 
    'carcinogenesis ', 
    'oddness ', 
    'dross ', 
    'catharsis ', 
    'resourcefulness ', 
    'possessiveness ', 
    'parthenogenesis ', 
    'single-mindedness ', 
    'greenness ', 
    'catalysis ', 
    'exclusiveness ', 
    'premiss ', 
    'arras ', 
    'hols ', 
    'animus ', 
    'clumsiness ', 
    'diagenesis ', 
    'relatedness ', 
    'deaconess ', 
    'loveliness ', 
    'mutagenesis ', 
    'rumpus ', 
    'canvass ', 
    'parenthesis ', 
    'blankness ', 
    'informatics ', 
    'decisiveness ', 
    'thoughtfulness ', 
    'incompleteness ', 
    'plexiglass ', 
    'defensiveness ', 
    'looking-glass ', 
    'ellipsis ', 
    'britches ', 
    'liss ', 
    'bluntness ', 
    'unevenness ', 
    'mantis ', 
    'photolysis ', 
    'chablis ', 
    'orderliness ', 
    'neighbourliness ', 
    'niceness ', 
    'persuasiveness ', 
    'femaleness ', 
    'inappropriateness ', 
    'all-comers ', 
    'sheerness ', 
    'hippopotamus ', 
    'vividness ', 
    'genuineness ', 
    'truthfulness ', 
    'blueness ', 
    'electrolysis ', 
    'awfulness ', 
    'psoriasis ', 
    'foss ', 
    'vas ', 
    'destructiveness ', 
    'sorceress ', 
    'swiftness ', 
    'roundness ', 
    'underpass ', 
    'watchfulness ', 
    'testis ', 
    'biogas ', 
    'jodhpurs ', 
    'pettiness ', 
    'isthmus ', 
    'tas ', 
    'ibis ', 
    'temptress ', 
    'nous ', 
    'undies ', 
    'wretchedness ', 
    'uselessness ', 
    'catechesis ', 
    'gladness ', 
    'timeliness ', 
    'colobus ', 
    'hysteresis ', 
    'fierceness ', 
    'foulness ', 
    'agribusiness ', 
    'tyrannosaurus ', 
    'hollowness ', 
    'blandness ', 
    'ingress ', 
    'timelessness ', 
    'lameness ', 
    'cholestasis ', 
    'thrombus ', 
    'have-nots ', 
    'coarseness ', 
    'cyclops ', 
    'paediatrics ', 
    'amyloidosis ', 
    'compactness ', 
    'quickness ', 
    'worthlessness ', 
    'modus ', 
    'meiosis ', 
    'mastitis ', 
    'adenovirus ', 
    'banns ', 
    'oestrus ', 
    'civvies ', 
    'fancy-dress ', 
    'vindictiveness ', 
    'cirrus ', 
    'murderess ', 
    'gastroenteritis ', 
    'literariness ', 
    'childishness ', 
    'childlessness ', 
    'cryptosporidiosis ', 
    'ranunculus ', 
    'proboscis ', 
    'cholecystitis ', 
    'keenness ', 
    'plainness ', 
    'meta-analysis ', 
    'abruptness ', 
    'peritonitis ', 
    'ramus ', 
    'barrenness ', 
    'sarcoidosis ', 
    'jakes ', 
    'slackness ', 
    'protectiveness ', 
    'enuresis ', 
    'godliness ', 
    'steadiness ', 
    'kouros ', 
    'naughtiness ', 
    'ripeness ', 
    'battledress ', 
    'hoarseness ', 
    'necropolis ', 
    'demographics ', 
    'self-analysis ', 
    'pretentiousness ', 
    'worthiness ', 
    'masterclass ', 
    'waterbus ', 
    'calvados ', 
    'allsorts ', 
    'busyness ', 
    'proctitis ', 
    'callousness ', 
    'unfaithfulness ', 
    'badness ', 
    'gonococcus ', 
    'portcullis ', 
    'nautilus ', 
    'buss ', 
    'hermeneutics ', 
    'craziness ', 
    'platypus ', 
    'culottes ', 
    'youthfulness ', 
    'rebus ', 
    'manliness ', 
    'steadfastness ', 
    'primus ', 
    'loess ', 
    'sureness ', 
    'acidosis ', 
    'sleepiness ', 
    'untidiness ', 
    'biosynthesis ', 
    'grimness ', 
    'lias ', 
    'otitis ', 
    'viciousness ', 
    'shallowness ', 
    'schnapps ', 
    'steepness ', 
    'telesales ', 
    'mos ', 
    'embryogenesis ', 
    'sus ', 
    'encephalitis ', 
    'pylorus ', 
    'poliovirus ', 
    'crispness ', 
    'avis ', 
    'hardiness ', 
    'short-sightedness ', 
    'paratroops ', 
    'unsteadiness ', 
    'kindliness ', 
    'staphylococcus ', 
    'amaryllis ', 
    'gubbins ', 
    'hypothalamus ', 
    'patroness ', 
    'maquis ', 
    'attentiveness ', 
    'poliomyelitis ', 
    'fastidiousness ', 
    'palmas ', 
    'energetics ', 
    'proprietress ', 
    'unfitness ', 
    'helpfulness ', 
    'distinctness ', 
    'slimness ', 
    'mildness ', 
    'covetousness ', 
    'cybernetics ', 
    'bis ', 
    'financials ', 
    'gravitas ', 
    'claes ', 
    'paleness ', 
    'fatness ', 
    'backwoods ', 
    'wistfulness ', 
    'peacefulness ', 
    'wrongness ', 
    'weirdness ', 
    'therapeutics ', 
    'feebleness ', 
    'seasickness ', 
    'starkness ', 
    'magnetics ', 
    'meaninglessness ', 
    'pyrotechnics ', 
    'unexpectedness ', 
    'smithereens ', 
    'sloppiness ', 
    'worldliness ', 
    'academicals ', 
    'pointlessness ', 
    'fundus ', 
    'orthopaedics ', 
    'pneumocystis ', 
    'viscountess ', 
    'sleeplessness ', 
    'sourness ', 
    'brittleness ', 
    'pervasiveness ', 
    'thoughtlessness ', 
    'cess ', 
    'lawfulness ', 
    'shabbiness ', 
    'tear-gas ', 
    'teargas ', 
    'rickets ', 
    'elevenses ', 
    'aloneness ', 
    'letterpress ', 
    'fastness ', 
    'mimesis ', 
    'actus ', 
    'cassis ', 
    'haemostasis ', 
    'homeostasis ', 
    'falseness ', 
    'wilfulness ', 
    'negus ', 
    'proteus ', 
    'tonsillitis ', 
    'morphogenesis ', 
    'cantharus ', 
    'citrus ', 
    'aureus ', 
    'plumpness ', 
    'exactness ', 
    'weightlessness ', 
    'shamus ', 
    'mitosis ', 
    'grossness ', 
    'pleasantness ', 
    'seamstress ', 
    'fruitfulness ', 
    'pastis ', 
    'meekness ', 
    'indecisiveness ', 
    'thankfulness ', 
    'astuteness ', 
    'evenness ', 
    'backstairs ', 
    'amess ', 
    'impulsiveness ', 
    'pinus ', 
    'deadness ', 
    'turps ', 
    'telesis ', 
    'sapiens ', 
    'rawness ', 
    'pes ', 
    'graciousness ', 
    'methanogenesis ', 
    'psycholinguistics ', 
    'eurythmics ', 
    'gneiss ', 
    'deviousness ', 
    'poetess ', 
    'microeconomics ', 
    'atmospherics ', 
    'agrostis ', 
    'giddiness ', 
    'connectedness ', 
    'pertussis ', 
    'nightclothes ', 
    'looseness ', 
    'brashness ', 
    'sacredness ', 
    'dreariness ', 
    'rhinitis ', 
    'rhombus ', 
    'coyness ', 
    'sluggishness ', 
    'stuffiness ', 
    'halitosis ', 
    'drabness ', 
    'yonks ', 
    'triceps ', 
    'tamas ', 
    'brontosaurus ', 
    'strictness ', 
    'landmass ', 
    'amanuensis ', 
    'obviousness ', 
    'trustworthiness ', 
    'ficus ', 
    'kinematics ', 
    'thalamus ', 
    'polyneuritis ', 
    'microdialysis ', 
    'epos ', 
    'forensics ', 
    'unworthiness ', 
    'definiteness ', 
    'cunnilingus ', 
    'earlies ', 
    'rictus ', 
    'pseudomonas ', 
    'grampus ', 
    'schoolmistress ', 
    'tarsus ', 
    'clearness ', 
    'egress ', 
    'motocross ', 
    'baculovirus ', 
    'hoss ', 
    'osteoarthritis ', 
    'mirabilis ', 
    'classlessness ', 
    'riskiness ', 
    'ileitis ', 
    'mindedness ', 
    'forcefulness ', 
    'bathos ', 
    'sundress ', 
    'retinitis ', 
    'bloody-mindedness ', 
    'coitus ', 
    'shepherdess ', 
    'singleness ', 
    'coveralls ', 
    'chilliness ', 
    'sexiness ', 
    'amplexus ', 
    'alumnus ', 
    'skewness ', 
    'hypobiosis ', 
    'francais ', 
    'streptococcus ', 
    'pais ', 
    'smartness ', 
    'faintness ', 
    'deerness ', 
    'receptiveness ', 
    'deftness ', 
    'promptness ', 
    'aimlessness ', 
    'vicus ', 
    'wholesomeness ', 
    'criss-cross ', 
    'postmistress ', 
    'polyanthus ', 
    'edginess ', 
    'waywardness ', 
    'asbestosis ', 
    'authoress ', 
    'ignoramus ', 
    'inwardness ', 
    'unselfishness ', 
    'progressiveness ', 
    'beastliness ', 
    'precariousness ', 
    'digitalis ', 
    'rashness ', 
    'selflessness ', 
    'ichthus ', 
    'knowingness ', 
    'humanness ', 
    'schistosomiasis ', 
    'acquisitiveness ', 
    'porteous '
]

    
