from pathlib import Path
import re

ROOT=Path('.')

SHELL=(ROOT/'index.html').read_text(encoding='utf-8')

sources=r'''window.BUNA_SOURCES={
  "review-2024":{title:"Coffee leaf phytochemicals, traditional uses and functional beverage research",year:2024,type:"Review",url:"https://doi.org/10.1016/j.jfca.2024.106570",note:"Background review for composition, traditional-use context and research gaps."},
  "barrier-cell-2024":{title:"Coffee leaf fractions and intestinal barrier dysfunction",year:2024,type:"Cell model",url:"https://doi.org/10.1016/j.fbio.2024.104639",note:"Cell co-culture study; laboratory evidence."},
  "uric-rat-2023":{title:"Coffee Leaf Tea Extracts Improve Hyperuricemia Nephropathy and Associated Gut Changes in Rats",year:2023,type:"Animal study",url:"https://doi.org/10.1021/acs.jafc.3c02797",note:"Rat disease model using coffee-leaf extracts."},
  "gut-mouse-2026":{title:"Polyphenol-Rich Coffee Leaf Extract and High-Fat-Diet Intestinal Barrier Dysfunction",year:2026,type:"Animal study",url:"https://doi.org/10.1021/acs.jafc.5c13455",note:"Mouse study using a polyphenol-rich extract."},
  "human-2025":{title:"Functional and relaxing properties of coffee leaf tea: an integrative food cognition approach",year:2025,type:"Human intervention",url:"https://doi.org/10.1016/j.afres.2025.101141",note:"Early human intervention using a defined coffee-leaf tea preparation."},
  "darktea-2026":{title:"Coffee Leaf Dark Tea Processed Using Pu-Erh-Style Pile Fermentation",year:2026,type:"Processing / in-vitro study",url:"https://doi.org/10.3390/foods15111980",note:"Processing, sensory and laboratory enzyme-assay work."},
  "chemo-2026":{title:"Traditional preparation and cultural significance of Chemo",year:2026,type:"Ethnographic study",url:"https://doi.org/10.1186/s13002-026-00863-y",note:"Mixed-methods study documenting Chemo preparation, context and reported meanings."},
  "engere-2026":{title:"Indigenous coffee leaf brew and Engere brewing practices and consumption patterns in South Ethiopia",year:2026,type:"Survey / ethnographic study",url:"https://doi.org/10.1007/s44187-026-00927-8",note:"Documents preparation, reported use and consumption patterns in Gofa Zone."},
  "kawa-2018":{title:"Kahwa Daun: Traditional Knowledge of a Coffee Leaf Herbal Tea from West Sumatera, Indonesia",year:2018,type:"Ethnographic / producer study",url:"https://doi.org/10.1016/j.jef.2018.11.005",note:"Survey, interviews and producer observations in West Sumatra; includes processing observations and measurements."},
  "safety-2022":{title:"Risk Assessment of Caffeine and Epigallocatechin Gallate in Coffee Leaf Tea",year:2022,type:"Safety review",url:"https://doi.org/10.3390/foods11030263",note:"Reviews caffeine and EGCG exposure for coffee-leaf tea products."},
  "eu-2020":{title:"Commission Implementing Regulation (EU) 2020/917",year:2020,type:"Regulatory",url:"https://eur-lex.europa.eu/eli/reg_impl/2020/917/oj",note:"EU authorisation/specification for a defined coffee-leaf infusion."},
  "eu-2023":{title:"Commission Implementing Regulation (EU) 2023/931",year:2023,type:"Regulatory",url:"https://eur-lex.europa.eu/eli/reg_impl/2023/931/oj",note:"Extends authorised uses in the EU."}
};
'''

claims=r'''window.BUNA_CLAIMS={
  "leaf-to-cup":{type:"evidence context",level:"established",plain:"Dry-leaf composition and brewed-cup composition are different measurements.",detail:"Processing and brewing affect which compounds move into water; digestion and metabolism add later stages.",sources:["review-2024"]},
  "human-evidence-limited":{type:"evidence context",level:"established",plain:"Human evidence for coffee-leaf biological effects remains limited.",detail:"Much of the current literature is composition, laboratory, cell or animal work, with a smaller human evidence base.",sources:["human-2025","gut-mouse-2026","barrier-cell-2024"]},
  "engere-documented":{type:"documented tradition",level:"documented",plain:"Engere is documented in Gofa Zone as part of coffee-leaf beverage practice, including milk-combined preparation.",detail:"The 2026 study records household preparation and consumption patterns.",sources:["engere-2026"]},
  "engere-report":{type:"community report",level:"documented",plain:"Participants reported everyday and restorative roles for coffee-leaf brew and Engere.",detail:"These are reported uses and perceptions; the study did not establish clinical strength, medicinal or lactation effects.",sources:["engere-2026"]},
  "chemo-documented":{type:"documented tradition",level:"documented",plain:"Chemo is a documented coffee-leaf beverage tradition in southwestern Ethiopia.",detail:"The study records preparation, ingredients, social context and participant descriptions.",sources:["chemo-2026"]},
  "chemo-report":{type:"community report",level:"documented",plain:"Participants used words including warming, refreshing, invigorating and restorative when describing Chemo.",detail:"Those words document local meaning and experience rather than clinical outcomes.",sources:["chemo-2026"]},
  "kawa-documented":{type:"documented tradition",level:"documented",plain:"Kahwa/Kawa Daun is documented as a coffee-leaf beverage tradition in West Sumatra.",detail:"The 2018 study surveyed sellers and observed producers, recording several heat- and smoke-related processing methods.",sources:["kawa-2018"]},
  "kawa-variation":{type:"published observation",level:"documented",plain:"Observed Kawa Daun processing varied between producers.",detail:"Producer-specific observations are more precise than treating one method, wood type or duration as universal practice.",sources:["kawa-2018"]},
  "kuti-evidence-gap":{type:"evidence context",level:"limited",plain:"Kuti is associated in the Library source corpus with Harari coffee-leaf practice, while several detailed legacy claims lack a resolved primary-source basis.",detail:"Exact caffeine values, child-safety statements, fixed preparation rules and long historical chronologies are not used as admitted facts here.",sources:[]},
  "processing-actions":{type:"definition",level:"established",plain:"Processing describes actions carried out between harvest and the finished ingredient or cup.",detail:"Withering, bruising, rolling, fermentation, drying, roasting, smoking and brewing describe different actions or stages.",sources:["review-2024","darktea-2026"]},
  "processing-framework":{type:"project model",level:"project",plain:"Citane processing maps organise process questions and experiments.",detail:"Individual relationships may come from published research, documented tradition, field observation, interpretation or hypothesis.",sources:[]},
  "observation-mechanism":{type:"evidence context",level:"established",plain:"An observed colour, aroma or temperature does not by itself identify the underlying chemical mechanism.",detail:"Mechanistic statements depend on the measurements or research sources available for the specific process.",sources:[]},
  "chemistry-composition":{type:"published context",level:"established",plain:"Coffee leaves contain several compound families, including phenolic compounds, caffeine and mangiferin.",detail:"Amounts vary with material and process, and a dry-leaf value is not automatically the concentration in a beverage.",sources:["review-2024"]},
  "reactive-landscape-status":{type:"project model",level:"project",plain:"The Citane Reactive Landscape is a research-informed organising model.",detail:"Its named reservoirs, activation events and connections are a project framework unless a specific element is tied to published measurement.",sources:[]},
  "tool-provenance":{type:"evidence context",level:"project",plain:"Interactive relationships can carry source, scope, calculation and evidence-status information.",detail:"A visual connection may represent a measured relationship, an interpretation or a generated proposal.",sources:[]},
  "ai-status":{type:"generated output",level:"project",plain:"AI-generated material is a generated proposal unless it is explicitly tied to an admitted claim and source.",detail:"The shared knowledge registry supplies factual material; generated interpretation remains identifiable as generated material.",sources:[]},
  "sensory-language":{type:"definition",level:"established",plain:"Sensory descriptors record perception and are distinct from chemical or medical claims.",detail:"Compound associations can contribute to sensory explanation, but perception also depends on concentration, matrix, thresholds and the whole mixture.",sources:[]},
  "sensory-perception":{type:"evidence context",level:"established",plain:"Taste is not confined to fixed zones of the tongue.",detail:"Taste receptors are distributed across the oral cavity; simplified tongue maps are not used as the sensory model here.",sources:[]},
  "culinary-status":{type:"provenance",level:"established",plain:"Documented traditional preparations, recorded KoffyKraft trials, reconstructions and untested concepts have different provenance.",detail:"The provenance identifies where a preparation came from without implying that one category is superior to another.",sources:[]},
  "gut-preclinical":{type:"published result",level:"preclinical",plain:"Cell and animal studies make the gut barrier and microbiome an active research area for coffee leaf.",detail:"These studies do not establish a human gut-health effect from an ordinary cup.",sources:["barrier-cell-2024","uric-rat-2023","gut-mouse-2026"]},
  "metabolic-preclinical":{type:"published result",level:"preclinical",plain:"Coffee-leaf extracts and processed materials have produced metabolic signals in laboratory and animal studies.",detail:"These results do not establish that an ordinary infusion treats diabetes, cholesterol or obesity.",sources:["darktea-2026","gut-mouse-2026"]},
  "stress-human":{type:"published result",level:"early human",plain:"A 2025 human study reported sensory/emotional responses and a salivary-cortisol change after a defined coffee-leaf tea.",detail:"The study is an early human result and does not establish treatment for stress or anxiety.",sources:["human-2025"]},
  "safety-variability":{type:"safety context",level:"established",plain:"Exposure varies with the finished product, serving and preparation.",detail:"Caffeine and other relevant measurements can differ by material, process, extract strength and serving size.",sources:["safety-2022","eu-2020","eu-2023"]}
};
'''

terms=r'''window.BUNA_TERMS={
  "buna":{plain:"An umbrella name used by this Library for coffee-leaf beverage and food knowledge.",technical:"The name does not imply that every coffee-leaf tradition uses the word Buna."},
  "coffee-leaf":{plain:"A leaf from a Coffea plant.",technical:"Species, cultivar, leaf age, growing conditions and processing can affect composition and sensory character."},
  "infusion":{plain:"Leaf steeped in hot water without continued boiling.",technical:"Extraction by steeping; time, temperature, dose and particle size affect the beverage."},
  "decoction":{plain:"Leaf boiled directly in water, usually for longer than an infusion.",technical:"Extended wet extraction under boiling or near-boiling conditions."},
  "extraction":{plain:"Movement of soluble material from the leaf into a liquid.",technical:"Extraction depends on solvent, time, temperature, particle size, dose and the processed leaf matrix."},
  "withering":{plain:"A period in which fresh leaf loses some moisture before another processing step.",technical:"Controlled moisture reduction changes handling and can alter the environment for enzymatic reactions."},
  "oxidation":{plain:"Chemical change involving loss of electrons; in damaged plant tissue some oxidation is enzyme-mediated.",technical:"Oxidation is one class of reaction and is not a synonym for every colour or flavour change."},
  "fermentation":{plain:"Transformation involving microorganisms such as yeasts, bacteria or fungi.",technical:"Microbial metabolism under controlled or spontaneous conditions; resting or darkening alone does not identify fermentation."},
  "roasting":{plain:"Heating the leaf strongly enough to create toasted, browned or roasted character.",technical:"The reactions depend on temperature, time, moisture and composition; visual browning alone does not identify every reaction involved."},
  "smoke-drying":{plain:"Drying leaf in an environment where smoke is also present.",technical:"Heat, moisture loss and smoke exposure may occur together; their individual contributions depend on the method."},
  "maillard-reaction":{plain:"A group of heat-driven reactions between amino compounds and reducing sugars that can create colour and aroma.",technical:"Extent depends on temperature, time, moisture, pH and reactant availability."},
  "polyphenol":{plain:"A broad family of plant compounds containing multiple phenolic structures.",technical:"The term covers many compounds with different chemistry; total-polyphenol measures do not describe each compound separately."},
  "chlorogenic-acids":{plain:"A family of phenolic compounds found in coffee plants.",technical:"Often abbreviated CGAs; amounts vary with species, tissue, maturity and processing."},
  "mangiferin":{plain:"A xanthone-related plant compound reported in coffee leaves.",technical:"Presence in leaf material does not by itself establish concentration in a brewed serving or a human effect."},
  "caffeine":{plain:"A naturally occurring stimulant alkaloid present in coffee plants.",technical:"Coffee-leaf caffeine varies with material and preparation; beverage exposure depends on dose and extraction."},
  "volatile":{plain:"A compound that can readily enter the air and contribute to aroma.",technical:"Whether a volatile affects perception depends on concentration, threshold and the surrounding mixture."},
  "sensory-descriptor":{plain:"A word used to describe an aroma, taste, texture or finish that a person perceives.",technical:"A descriptor records perception; it is not automatically the name of the chemical responsible."},
  "astringency":{plain:"A drying or puckering mouth sensation.",technical:"Astringency is a tactile/oral sensation often associated with interactions between plant polyphenols and salivary proteins."},
  "mouthfeel":{plain:"The physical sensation of a drink in the mouth.",technical:"Includes body, viscosity, drying, coating and other tactile impressions."},
  "bioaccessibility":{plain:"How much of a compound becomes available from the food or drink during digestion.",technical:"The fraction released from the matrix and available for intestinal uptake after digestion."},
  "bioavailability":{plain:"How much reaches the body after absorption and metabolism.",technical:"The amount and chemical form reaching systemic circulation or a target tissue."},
  "microbiome":{plain:"The community of microorganisms living in an environment such as the gut.",technical:"Changes in composition or activity require context before they can be described as beneficial or harmful."},
  "in-vitro":{plain:"A study carried out outside a whole living organism, such as in a test tube or cell system.",technical:"Useful for controlled mechanisms and assays; direct human effects require separate evidence."},
  "preclinical":{plain:"Research carried out before or outside direct clinical testing in people.",technical:"Often includes cell, laboratory and animal studies."},
  "ethnography":{plain:"Research that documents people, practices, meanings and social context.",technical:"Ethnographic evidence can establish what people do or report without by itself establishing a clinical physiological effect."},
  "observation":{plain:"Something directly seen, measured, recorded or tasted in a particular setting.",technical:"Observation is separated from the explanation proposed for it."},
  "interpretation":{plain:"An explanation or meaning drawn from observations or sources.",technical:"Interpretation can be well supported while remaining distinct from direct measurement."},
  "hypothesis":{plain:"A proposed explanation or prediction that can be tested.",technical:"A hypothesis identifies a question for investigation rather than a settled result."},
  "evidence":{plain:"The information supporting a statement about what is known, reported, observed or uncertain.",technical:"The Library distinguishes human, animal, cell, laboratory, regulatory, documented-tradition, observation, interpretation and hypothesis evidence."},
  "dose":{plain:"The amount of a material or compound taken in one serving or over time.",technical:"Dose depends on product composition, serving size and frequency."},
  "exposure":{plain:"The amount of a compound that a person actually encounters from a product or serving.",technical:"Exposure can differ from dry-material concentration because preparation, absorption and metabolism intervene."}
};
'''

holds=r'''window.BUNA_HOLDS={
  "engere-zero-adverse":{status:"hold",legacy:["engere.html","engere-schoolbook-guide-part-1.html","engere-visual-pictogram-guide.html"],statement:"Engere has zero adverse events or is universally safe.",reason:"A household survey report is not a controlled safety trial."},
  "engere-milk-buffer":{status:"hold",legacy:["engere.html","engere-schoolbook-guide-part-1.html"],statement:"Milk protects the stomach or neutralises coffee-leaf physiological effects.",reason:"Mechanistic and clinical interpretation exceeds the ethnographic/survey source."},
  "engere-postpartum":{status:"hold",legacy:["engere-intro.html","engere-schoolbook-guide-part-2.html"],statement:"Engere is recommended for postpartum or lactating mothers.",reason:"Reported cultural use is distinct from a health recommendation."},
  "engere-child":{status:"hold",legacy:["engere-visual-pictogram-guide.html"],statement:"Engere is suitable or safe for children.",reason:"No child-safety trial is represented in the admitted source set."},
  "engere-raw-milk":{status:"hold",legacy:["engere-visual-pictogram-guide.html"],statement:"Fresh unpasteurised milk is the preferred public preparation instruction.",reason:"Ethnographic description and modern food-safety guidance are separate questions."},
  "kuti-caffeine-10":{status:"hold",legacy:["kuti-schoolbook-guide.html","kuti-visual-pictogram-guide.html"],statement:"Kuti contains about 10 mg/L caffeine as a general value.",reason:"Product, leaf state and preparation scope are unresolved."},
  "kuti-caffeine-return":{status:"hold",legacy:["kuti-schoolbook-guide.html"],statement:"Most caffeine returns from a senescing leaf to the tree.",reason:"Mechanism and magnitude are not established in the cited Kuti material."},
  "kuti-child-safe":{status:"hold",legacy:["kuti-schoolbook-guide.html","kuti-visual-pictogram-guide.html"],statement:"Kuti is safe for children.",reason:"Community use does not establish paediatric safety."},
  "kuti-centuries":{status:"hold",legacy:["kuti-intro.html","kuti-schoolbook-guide.html"],statement:"Kuti has been prepared unchanged for centuries.",reason:"Chronology and continuity require specific historical documentation."},
  "chemo-universal-spices":{status:"hold",legacy:["chemo-intro.html","chemo-recipe.html"],statement:"Every Chemo preparation uses all spices every time.",reason:"Universal wording requires exact source support."},
  "chemo-young-tips-best":{status:"hold",legacy:["chemo-schoolbook-guide.html","chemo-visual-pictogram-guide.html"],statement:"Young tender tips are the best Chemo leaf material.",reason:"A preference or chemical rationale has not been established as a universal rule."},
  "chemo-food-moderation":{status:"hold",legacy:["chemo-intro.html","chemo-recipe.html"],statement:"Food pairing moderates the physiological intensity of Chemo.",reason:"Cultural food pairing and physiological effect are different propositions."},
  "chemo-maillard":{status:"hold",legacy:["chemo.html","chemo-recipe.html"],statement:"The documented household roast necessarily produces a defined Maillard transformation with predictable sensory effects.",reason:"The reaction extent was not established by the ethnographic source."},
  "kawa-resistance":{status:"hold",legacy:["kawa-daun-schoolbook-guide.html","kawa-daun.html"],statement:"Kawa Daun was born from resistance to a colonial prohibition and survived an attempt to erase it.",reason:"Oral/community history and documentary colonial history require separate sourcing."},
  "kawa-cinnamon-universal":{status:"hold",legacy:["kawa-daun-recipe.html","kawa-daun-visual-pictogram-guide.html"],statement:"Cinnamon wood is the universal or preferred Kawa Daun fuel.",reason:"Producer-specific observations do not establish a universal tradition rule."},
  "kawa-smoke-chemistry":{status:"hold",legacy:["kawa-daun.html","kawa-daun-recipe.html"],statement:"Specific smoke volatiles are proven to enter Kawa Daun and cause its finished flavour.",reason:"Exposure is documented; finished-leaf causal chemistry requires direct measurement."},
  "grill-gaba":{status:"hold",legacy:["citane-hack-grill-wilted-leaves.html"],statement:"The grill-wilted trial produced a specific GABA concentration.",reason:"The field note did not contain an analytical GABA measurement for that batch."},
  "gas-maillard-complete":{status:"hold",legacy:["citane-hack-gas-flame-roasted-leaf.html"],statement:"Visible browning demonstrates that Maillard development is complete.",reason:"Appearance alone does not identify reaction completion."},
  "smoke-cell-threshold":{status:"hold",legacy:["cinnamon-smoke-trial.html"],statement:"A recorded leaf temperature around 41 C proves the leaf remained below a critical cell-destruction threshold.",reason:"The threshold and biological state were not measured in the trial."},
  "smoke-oxidation-colour":{status:"hold",legacy:["cinnamon-smoke-trial.html"],statement:"Leaf colour proves controlled oxidation or enzyme/microbial transformation.",reason:"Colour was observed; the proposed mechanism was not directly measured."},
  "sensory-tongue-map":{status:"hold",legacy:["buna-sensory-school.html"],statement:"Bitterness is perceived at the back of the tongue.",reason:"Fixed tongue-zone teaching is not an accurate model of taste receptor distribution."},
  "sensory-cooling-mint":{status:"hold",legacy:["buna-sensory-school.html","sensory-chemistry.html"],statement:"An unnamed coffee-leaf compound creates the same cooling mechanism as mint.",reason:"The compound and mechanism require identification and evidence."},
  "sensory-chilled-best":{status:"hold",legacy:["sensory-landscape-of-coffee-leaf.html"],statement:"Chilled service is generally the best-performing presentation and reduces bitterness/astringency.",reason:"A specific study or tasting condition cannot automatically be generalised to all preparations."},
  "culinary-fat-binding":{status:"hold",legacy:["buna-culinary.html","buna-culinary-elements.html"],statement:"Fat or milk binds coffee-leaf phenolics in a way that makes the cup gentler for people.",reason:"Food chemistry plausibility and a human tolerance effect are separate propositions."},
  "culinary-gaba-bitterness":{status:"hold",legacy:["buna-culinary-school.html"],statement:"GABA suppresses bitterness in the culinary system.",reason:"The hidden prompt carried a causal claim not established in the public evidence layer."},
  "ritual-functional-times":{status:"hold",legacy:["vocab/ritual-context.html"],statement:"Morning, work or night Buna categories have established caffeine, calming or functional effects.",reason:"These categories were editorial/project proposals rather than documented vocabulary or clinical evidence."},
  "terrain-canopy-mangiferin":{status:"hold",legacy:["citane-terrain-map.html"],statement:"Rubber-canopy light conditions predict specific mangiferin or ionone-precursor changes at Thumpassery.",reason:"Estate-specific chemistry was not measured for the mapped relationship."},
  "flavour-exact-oav":{status:"hold",legacy:["citane-flavour-landscape.html"],statement:"Exact odour activity values and process recommendations apply across coffee-leaf preparations.",reason:"Scope, matrix and provenance require relationship-level verification."},
  "visual-cortisol":{status:"hold",legacy:["buna-visual-guide.html"],statement:"Visual cortisol or emotion values represent measured clinical data.",reason:"The page identifies those numbers as simulations rather than clinical measurements."}
};
'''

for path,text in {
    'data/buna-sources.js':sources,
    'data/buna-claims.js':claims,
    'data/buna-terms.js':terms,
    'data/buna-holds.js':holds,
}.items():
    (ROOT/path).write_text(text,encoding='utf-8')

# Door Two becomes a threshold to four independent three-depth tradition paths.
content_path=ROOT/'data/buna-content.js'
content=content_path.read_text(encoding='utf-8')
start=content.index('"/traditions/":')
end=content.index('\n\n"/processing/":', start)
traditions=r'''"/traditions/":{title:"Living traditions",eye:"Door Two",lead:"Coffee leaves are prepared in distinct local traditions. Each path begins with a short introduction and opens into context and source detail.",question:"Which tradition would you like to visit?",body:`<section><div class="cards two"><a class="card" href="/traditions/engere/"><div class="kicker">Gofa Zone · South Ethiopia</div><h3>Engere</h3><p>Coffee-leaf beverage practice documented through household research, including milk-combined preparation.</p></a><a class="card" href="/traditions/kuti/"><div class="kicker">Harar · Ethiopia</div><h3>Kuti</h3><p>A Harari coffee-leaf tradition for which detailed modern source mapping remains more limited.</p></a><a class="card" href="/traditions/chemo/"><div class="kicker">Southwestern Ethiopia</div><h3>Chemo</h3><p>Coffee leaf prepared with herbs and spices in a documented household and social tradition.</p></a><a class="card" href="/traditions/kawa-daun/"><div class="kicker">West Sumatra · Indonesia</div><h3>Kawa Daun</h3><p>A coffee-leaf beverage with observed heat- and smoke-related processing methods.</p></a></div></section><section><h2>Tradition and evidence</h2><p>A tradition can document ingredients, methods, language, setting and reported experience. Physiological effects are a separate research question.</p></section>`},

"/traditions/engere/":{title:"Engere",eye:"Living Traditions · LOOK",lead:"Engere is documented in Gofa Zone, South Ethiopia, within a wider coffee-leaf beverage practice.",question:"What is Engere?",depth:"look",group:"engere",parent:{url:"/traditions/",label:"Living traditions"},claims:["engere-documented"],sources:["engere-2026"],body:`<section><p>The published study describes coffee-leaf beverages prepared in households and a milk-combined preparation called Engere. Ingredients and methods vary between households.</p><p>The study also records how people describe and use the beverage in everyday life. Those reports provide cultural and household context.</p><div class="callout"><strong>Source scope</strong>The source is well suited to preparation and reported-use questions. It is not a clinical trial of strength, lactation, treatment or child safety.</div></section>`},
"/traditions/engere/understand/":{title:"Engere in household life",eye:"Living Traditions · UNDERSTAND",lead:"The preparation makes more sense when ingredients, household setting and reported purpose are read together.",question:"What does the field study document?",depth:"understand",group:"engere",parent:{url:"/traditions/",label:"Living traditions"},claims:["engere-report"],sources:["engere-2026"],body:`<section><h2>Preparation</h2><p>Coffee leaf forms the base of the beverage. Milk is central to Engere, while spices and sweeteners can vary with household practice.</p><h2>Reported use</h2><p>Participants described everyday and restorative roles for coffee-leaf beverages. These descriptions record local experience and meaning.</p><h2>Modern preparation</h2><p>A modern reconstruction can reproduce documented ingredients and sequence while applying contemporary food-handling choices. That reconstruction has different provenance from the ethnographic description.</p></section>`},
"/traditions/engere/examine/":{title:"Engere evidence & sources",eye:"Living Traditions · EXAMINE",lead:"The advanced view separates study observations, participant reports and later interpretation.",question:"What can the Engere source establish?",depth:"examine",group:"engere",parent:{url:"/traditions/",label:"Living traditions"},claims:["engere-documented","engere-report"],sources:["engere-2026"],body:`<section><div class="table-wrap"><table><thead><tr><th>Question</th><th>Evidence available</th></tr></thead><tbody><tr><td>Where and how is the beverage prepared?</td><td>Household survey and community documentation.</td></tr><tr><td>How do participants describe its role?</td><td>Participant reports and consumption patterns.</td></tr><tr><td>Does milk create a clinical protective effect?</td><td>Not established by this study.</td></tr><tr><td>Is it proven safe for children or postpartum use?</td><td>Not established by this study.</td></tr></tbody></table></div></section>`},

"/traditions/kuti/":{title:"Kuti",eye:"Living Traditions · LOOK",lead:"Kuti is associated in the Library source corpus with Harari coffee-leaf practice in eastern Ethiopia.",question:"What is known at a basic level?",depth:"look",group:"kuti",parent:{url:"/traditions/",label:"Living traditions"},claims:["kuti-evidence-gap"],body:`<section><p>Accounts describe a coffee-leaf decoction associated with mature, yellowed or fallen leaf material and Harari household practice.</p><p>The present evidence base used here is less complete than the recent Engere, Chemo and Kawa Daun studies. Detailed caffeine values, child-safety statements and fixed recipe rules are therefore not included as general facts.</p></section>`},
"/traditions/kuti/understand/":{title:"Kuti in Harari context",eye:"Living Traditions · UNDERSTAND",lead:"Kuti belongs to a broader Harari coffee culture in which leaf, bean, husk, household practice and trade histories intersect.",question:"What context is useful for understanding Kuti?",depth:"understand",group:"kuti",parent:{url:"/traditions/",label:"Living traditions"},claims:["kuti-evidence-gap"],body:`<section><p>Legacy Buna material connects Kuti with Harar, household coffee practice and the use of mature or fallen leaves. It also contains stronger historical, caffeine and health statements whose source basis is not sufficiently resolved for public factual use.</p><p>This page therefore keeps the cultural identity and preparation category visible while leaving precise chronology, physiological explanations and safety claims to source-level research.</p></section>`},
"/traditions/kuti/examine/":{title:"Kuti evidence questions",eye:"Living Traditions · EXAMINE",lead:"The advanced Kuti view makes the evidence gaps visible rather than filling them with inherited certainty.",question:"Which details still depend on stronger source resolution?",depth:"examine",group:"kuti",parent:{url:"/traditions/",label:"Living traditions"},claims:["kuti-evidence-gap"],body:`<section><div class="table-wrap"><table><thead><tr><th>Topic</th><th>Current position</th></tr></thead><tbody><tr><td>Harari association</td><td>Retained as the core cultural identification in the source corpus.</td></tr><tr><td>Exact caffeine concentration</td><td>No general value admitted.</td></tr><tr><td>Caffeine movement during leaf senescence</td><td>No Kuti-specific mechanism admitted.</td></tr><tr><td>Use by children or nursing mothers</td><td>Community-use descriptions and safety evidence are treated separately.</td></tr><tr><td>Centuries of unchanged preparation</td><td>Requires historical documentation.</td></tr></tbody></table></div></section>`},

"/traditions/chemo/":{title:"Chemo",eye:"Living Traditions · LOOK",lead:"Chemo is a documented coffee-leaf beverage tradition from southwestern Ethiopia.",question:"What is Chemo?",depth:"look",group:"chemo",parent:{url:"/traditions/",label:"Living traditions"},claims:["chemo-documented"],sources:["chemo-2026"],body:`<section><p>Coffee leaf forms the base, with herbs and spices appearing in documented preparations. The study records household methods, social context and participant language around the beverage.</p><p>Preparation is not represented as one universal recipe because the study records variation.</p></section>`},
"/traditions/chemo/understand/":{title:"Chemo in context",eye:"Living Traditions · UNDERSTAND",lead:"Chemo combines leaf preparation with ingredients, hospitality and social meaning.",question:"What does the study add beyond a recipe?",depth:"understand",group:"chemo",parent:{url:"/traditions/",label:"Living traditions"},claims:["chemo-report"],sources:["chemo-2026"],body:`<section><h2>Ingredients</h2><p>The ethnographic record includes coffee leaf together with locally used herbs and spices. Individual botanical, sensory and medicinal associations are separate propositions and can be sourced independently.</p><h2>Social setting</h2><p>Participant descriptions place Chemo within household and social life. Words such as warming, refreshing, invigorating and restorative describe reported experience and meaning.</p><h2>Preparation variation</h2><p>The source records more than one leaf-preparation approach. Modern standardisation can be documented separately from the range observed in households.</p></section>`},
"/traditions/chemo/examine/":{title:"Chemo evidence & sources",eye:"Living Traditions · EXAMINE",lead:"The advanced view separates what the field study documents from chemical or health interpretations added later.",question:"Which propositions come directly from the ethnographic study?",depth:"examine",group:"chemo",parent:{url:"/traditions/",label:"Living traditions"},claims:["chemo-documented","chemo-report"],sources:["chemo-2026"],body:`<section><div class="table-wrap"><table><thead><tr><th>Evidence area</th><th>What it can describe</th></tr></thead><tbody><tr><td>Household methods</td><td>Observed or reported preparation categories and ingredients.</td></tr><tr><td>Participant language</td><td>Local descriptions, meanings and reported use.</td></tr><tr><td>Botanical chemistry</td><td>Requires plant- or compound-specific sources beyond the ethnography.</td></tr><tr><td>Clinical effects</td><td>Not established by the ethnographic design.</td></tr></tbody></table></div></section>`},

"/traditions/kawa-daun/":{title:"Kawa Daun",eye:"Living Traditions · LOOK",lead:"Kahwa or Kawa Daun is a documented coffee-leaf beverage tradition from West Sumatra, Indonesia.",question:"What distinguishes it?",depth:"look",group:"kawa",parent:{url:"/traditions/",label:"Living traditions"},claims:["kawa-documented"],sources:["kawa-2018"],body:`<section><p>The 2018 producer study records coffee leaves processed with heat and smoke in several ways before brewing. The beverage also has its own local material and serving context.</p><p>The observed methods were not identical between producers, so one producer's time, fuel or technique does not represent every Kawa Daun preparation.</p></section>`},
"/traditions/kawa-daun/understand/":{title:"Kawa Daun in West Sumatra",eye:"Living Traditions · UNDERSTAND",lead:"The tradition combines processing, local material culture, producer practice and historical context.",question:"What did the producer study observe?",depth:"understand",group:"kawa",parent:{url:"/traditions/",label:"Living traditions"},claims:["kawa-variation"],sources:["kawa-2018"],body:`<section><h2>Producer methods</h2><p>The study records several techniques involving heat, smoke and drying. Producer-specific observations include differences in handling and process duration.</p><h2>Material culture</h2><p>Storage and serving objects form part of the documented practice and help explain the beverage as more than a processing recipe.</p><h2>History</h2><p>Community history and colonial-era context appear in the wider Kawa Daun story. Oral/community accounts and documentary history are distinguishable evidence types.</p></section>`},
"/traditions/kawa-daun/examine/":{title:"Kawa Daun evidence & sources",eye:"Living Traditions · EXAMINE",lead:"The producer study supports process-level detail while preserving the scope of each observation.",question:"How broad is the evidence behind a Kawa Daun process statement?",depth:"examine",group:"kawa",parent:{url:"/traditions/",label:"Living traditions"},claims:["kawa-documented","kawa-variation"],sources:["kawa-2018"],body:`<section><p>The research period covered districts in West Sumatra and included seller interviews together with direct producer observations and moisture measurements. Findings tied to an observed producer remain producer-specific unless the study demonstrates a broader pattern.</p><div class="table-wrap"><table><thead><tr><th>Statement type</th><th>Scope</th></tr></thead><tbody><tr><td>Observed processing step</td><td>The producer or producers for whom it was recorded.</td></tr><tr><td>Moisture or yield measurement</td><td>The measured sample/method.</td></tr><tr><td>Historical account</td><td>The source type—community/oral or documentary—attached to that account.</td></tr><tr><td>Smoke chemistry explanation</td><td>Requires analytical or appropriately scoped food-chemistry evidence.</td></tr></tbody></table></div></section>`}'''
content=content[:start]+traditions+content[end:]

# Replace generic group definition with family groups.
content=content.replace(' traditions:{label:"Door Two · Living traditions",look:"/traditions/",understand:"/traditions/understand/",examine:"/traditions/examine/"},', ''' engere:{label:"Engere",look:"/traditions/engere/",understand:"/traditions/engere/understand/",examine:"/traditions/engere/examine/"},
 kuti:{label:"Kuti",look:"/traditions/kuti/",understand:"/traditions/kuti/understand/",examine:"/traditions/kuti/examine/"},
 chemo:{label:"Chemo",look:"/traditions/chemo/",understand:"/traditions/chemo/understand/",examine:"/traditions/chemo/examine/"},
 kawa:{label:"Kawa Daun",look:"/traditions/kawa-daun/",understand:"/traditions/kawa-daun/understand/",examine:"/traditions/kawa-daun/examine/"},''')
content_path.write_text(content,encoding='utf-8')

# Create canonical tradition route shells.
trad_routes=[
'/traditions/engere/','/traditions/engere/understand/','/traditions/engere/examine/',
'/traditions/kuti/','/traditions/kuti/understand/','/traditions/kuti/examine/',
'/traditions/chemo/','/traditions/chemo/understand/','/traditions/chemo/examine/',
'/traditions/kawa-daun/','/traditions/kawa-daun/understand/','/traditions/kawa-daun/examine/'
]
for route in trad_routes:
    d=ROOT/route.strip('/')
    d.mkdir(parents=True,exist_ok=True)
    (d/'index.html').write_text(SHELL,encoding='utf-8')

# Breadcrumbs can include an explicit parent such as Living traditions.
app_path=ROOT/'assets/buna-v2.js'
app=app_path.read_text(encoding='utf-8')
old='''  const bits=[`<a href="/">Library</a>`];\n  if(page.group&&path!==G[page.group].look) bits.push(`<a href="${G[page.group].look}">${h(G[page.group].label)}</a>`);\n  bits.push(`<span aria-current="page">${h(page.title)}</span>`);'''
new='''  const bits=[`<a href="/">Library</a>`];\n  if(page.parent) bits.push(`<a href="${page.parent.url}">${h(page.parent.label)}</a>`);\n  if(page.group&&path!==G[page.group].look) bits.push(`<a href="${G[page.group].look}">${h(G[page.group].label)}</a>`);\n  bits.push(`<span aria-current="page">${h(page.title)}</span>`);'''
if old not in app:
    raise SystemExit('breadcrumb pattern not found')
app=app.replace(old,new)
app=app.replace('<section><h2>Evidence position</h2>','<section><h2>Evidence notes</h2>')
app_path.write_text(app,encoding='utf-8')

# Redirect every former tradition page to its specific depth path.
redir_path=ROOT/'_redirects'
r=redir_path.read_text(encoding='utf-8')
replacements={
'/engere-intro.html /traditions/ 301':'/engere-intro.html /traditions/engere/ 301',
'/engere.html /traditions/understand/ 301':'/engere.html /traditions/engere/understand/ 301',
'/engere-deep.html /traditions/examine/ 301':'/engere-deep.html /traditions/engere/examine/ 301',
'/engere-recipe.html /traditions/understand/ 301':'/engere-recipe.html /traditions/engere/understand/ 301',
'/engere-people-work-context.html /traditions/understand/ 301':'/engere-people-work-context.html /traditions/engere/understand/ 301',
'/engere-schoolbook-guide-part-1.html /traditions/examine/ 301':'/engere-schoolbook-guide-part-1.html /traditions/engere/examine/ 301',
'/engere-schoolbook-guide-part-2.html /traditions/examine/ 301':'/engere-schoolbook-guide-part-2.html /traditions/engere/examine/ 301',
'/engere-visual-pictogram-guide.html /traditions/examine/ 301':'/engere-visual-pictogram-guide.html /traditions/engere/examine/ 301',
'/kuti-intro.html /traditions/ 301':'/kuti-intro.html /traditions/kuti/ 301',
'/kuti.html /traditions/understand/ 301':'/kuti.html /traditions/kuti/understand/ 301',
'/kuti-deep.html /traditions/examine/ 301':'/kuti-deep.html /traditions/kuti/examine/ 301',
'/kuti-recipe.html /traditions/understand/ 301':'/kuti-recipe.html /traditions/kuti/understand/ 301',
'/kuti-schoolbook-guide.html /traditions/examine/ 301':'/kuti-schoolbook-guide.html /traditions/kuti/examine/ 301',
'/kuti-visual-pictogram-guide.html /traditions/examine/ 301':'/kuti-visual-pictogram-guide.html /traditions/kuti/examine/ 301',
'/chemo-intro.html /traditions/ 301':'/chemo-intro.html /traditions/chemo/ 301',
'/chemo.html /traditions/understand/ 301':'/chemo.html /traditions/chemo/understand/ 301',
'/chemo-deep.html /traditions/examine/ 301':'/chemo-deep.html /traditions/chemo/examine/ 301',
'/chemo-recipe.html /traditions/understand/ 301':'/chemo-recipe.html /traditions/chemo/understand/ 301',
'/chemo-plants.html /traditions/understand/ 301':'/chemo-plants.html /traditions/chemo/understand/ 301',
'/chemo-schoolbook-guide.html /traditions/examine/ 301':'/chemo-schoolbook-guide.html /traditions/chemo/examine/ 301',
'/chemo-visual-pictogram-guide.html /traditions/examine/ 301':'/chemo-visual-pictogram-guide.html /traditions/chemo/examine/ 301',
'/kawa-daun-intro.html /traditions/ 301':'/kawa-daun-intro.html /traditions/kawa-daun/ 301',
'/kawa-daun.html /traditions/understand/ 301':'/kawa-daun.html /traditions/kawa-daun/understand/ 301',
'/kawa-daun-deep.html /traditions/examine/ 301':'/kawa-daun-deep.html /traditions/kawa-daun/examine/ 301',
'/kawa-daun-recipe.html /traditions/understand/ 301':'/kawa-daun-recipe.html /traditions/kawa-daun/understand/ 301',
'/kawa-daun-schoolbook-guide.html /traditions/examine/ 301':'/kawa-daun-schoolbook-guide.html /traditions/kawa-daun/examine/ 301',
'/kawa-daun-visual-pictogram-guide.html /traditions/examine/ 301':'/kawa-daun-visual-pictogram-guide.html /traditions/kawa-daun/examine/ 301',
'/vocab/ritual-context.html /traditions/understand/ 301':'/vocab/ritual-context.html /traditions/ 301'
}
for a,b in replacements.items():
    r=r.replace(a,b)
# Former generic depth URLs are compatibility redirects, not canonical pages.
if '/traditions/understand/' not in r:
    r += '\n/traditions/understand/ /traditions/ 301\n/traditions/examine/ /traditions/ 301\n'
redir_path.write_text(r,encoding='utf-8')

# Remove now noncanonical generic route files if present.
for rel in ['traditions/understand/index.html','traditions/examine/index.html']:
    p=ROOT/rel
    if p.exists(): p.unlink()

# Generate a complete legacy HTML accounting map from redirect rules.
redirect_map={}
for line in r.splitlines():
    parts=line.strip().split()
    if len(parts)>=2 and parts[0].endswith('.html'):
        redirect_map[parts[0].lstrip('/')]=parts[1]
legacy={}
canonical_indexes={str(p.relative_to(ROOT)).replace('\\','/') for p in ROOT.glob('**/index.html')}
for p in sorted(ROOT.rglob('*.html')):
    rel=str(p.relative_to(ROOT)).replace('\\','/')
    if rel in canonical_indexes and (rel=='index.html' or rel.startswith(('foundation/','catalogue/','sources/','cup/','traditions/','processing/','chemistry/','tools/','sensory/','culinary/','vocabulary/','biology/'))):
        continue
    if rel in redirect_map:
        legacy[rel]={"status":"redirect","to":redirect_map[rel]}
    else:
        legacy[rel]={"status":"archive"}
lines=['window.BUNA_LEGACY_MAP={']
items=[]
for k,v in legacy.items():
    if v['status']=='redirect': items.append(f'  {k!r}:{{status:"redirect",to:{v["to"]!r}}}')
    else: items.append(f'  {k!r}:{{status:"archive"}}')
lines.append(',\n'.join(items)); lines.append('};\n')
(ROOT/'data/buna-legacy-map.js').write_text('\n'.join(lines),encoding='utf-8')

# Update the v2 audit for the new canonical route set and held-claim/legacy coverage.
audit=ROOT/'scripts/audit_rebuild_v2.py'
a=audit.read_text(encoding='utf-8')
a=a.replace("'/traditions/','/traditions/understand/','/traditions/examine/',", "'/traditions/',\n'/traditions/engere/','/traditions/engere/understand/','/traditions/engere/examine/',\n'/traditions/kuti/','/traditions/kuti/understand/','/traditions/kuti/examine/',\n'/traditions/chemo/','/traditions/chemo/understand/','/traditions/chemo/examine/',\n'/traditions/kawa-daun/','/traditions/kawa-daun/understand/','/traditions/kawa-daun/examine/',")
a=a.replace("'data/buna-sources.js','data/buna-terms.js']", "'data/buna-sources.js','data/buna-terms.js','data/buna-holds.js','data/buna-legacy-map.js']")
# Redirect validation permits compatibility source URLs to redirect to a canonical route.
insert='''\n# Every held claim remains non-public and records its legacy provenance.\nholds=(ROOT/'data/buna-holds.js').read_text()\nfor hid,block in re.findall(r'"([^"]+)":\\{(.*?)\\}(?:,|\\n)', holds, flags=re.S):\n    if 'status:"hold"' not in block: errors.append(f'Hold record missing hold status: {hid}')\n    if 'legacy:[' not in block: errors.append(f'Hold record missing legacy provenance: {hid}')\n    if hid in content: errors.append(f'Held claim referenced by public content: {hid}')\n\n# Every legacy HTML file is explicitly accounted for as redirect or archive.\nlegacy_map=(ROOT/'data/buna-legacy-map.js').read_text()\nlegacy_names=set(re.findall(r"^  '([^']+)':\\{status:", legacy_map, flags=re.M))\ncanonical_index_paths={str(p.relative_to(ROOT)).replace('\\\\','/') for p in ROOT.rglob('index.html')}\nfor p in ROOT.rglob('*.html'):\n    rel=str(p.relative_to(ROOT)).replace('\\\\','/')\n    if rel in canonical_index_paths and (rel=='index.html' or rel.startswith(('foundation/','catalogue/','sources/','cup/','traditions/','processing/','chemistry/','tools/','sensory/','culinary/','vocabulary/','biology/'))):\n        continue\n    if rel not in legacy_names: errors.append(f'Legacy HTML not classified: {rel}')\n'''
marker="print(f'canonical_routes={len(routes)} expected={len(expected)} redirects={len([x for x in redirects if x.strip()])}')"
a=a.replace(marker,insert+'\n'+marker)
audit.write_text(a,encoding='utf-8')

# Record completion semantics internally; this text is never public runtime content.
(ROOT/'governance/ITEM_5_7_MIGRATION_RECORD.md').write_text('''# Items 5 and 7 — Migration Record\n\nThis record distinguishes public migration from scientific validation.\n\n## Item 5 — shared message/evidence engine\n\nImplemented stores:\n- admitted claims: `data/buna-claims.js`\n- sources: `data/buna-sources.js`\n- terms: `data/buna-terms.js`\n- held legacy propositions: `data/buna-holds.js`\n- legacy page accounting: `data/buna-legacy-map.js`\n\nHeld propositions are preserved but cannot be referenced by canonical public content.\n\n## Item 7 — content migration\n\nThe canonical public routes contain ordinary-reader LOOK, UNDERSTAND and EXAMINE material. Door Two now gives Engere, Kuti, Chemo and Kawa Daun independent three-depth paths. Legacy HTML is explicitly classified as redirect or archive.\n\nCompletion here means content has a canonical destination or an explicit hold/archive state. It does not mean every held proposition has been scientifically validated. Source-level validity closure remains a separate work order.\n''',encoding='utf-8')

print('message engine and Door Two content migration written')
