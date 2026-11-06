# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_50`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 131 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [1-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-345] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-204] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-359] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-83] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-264] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-272] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [287-295] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_Tackle' range [301-302] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [308-325] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [73-101] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-34] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-47] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-325] for track '9' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [1-129] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-21] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-48] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-54] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-178] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-196] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-328] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-344] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-131] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-268] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-278] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-359] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-126] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-157] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-67] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-141] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-156] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-60] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-194] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-100] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-127] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-172] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [238-342] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-10] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-20] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-28] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-47] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-141] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [40-54] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-58] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-134] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-147] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-141] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-193] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-240] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-220] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-216] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-273] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [277-339] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-316] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [326-331] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-314] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-264] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-338] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-359] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-302] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-344] for track '39' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.