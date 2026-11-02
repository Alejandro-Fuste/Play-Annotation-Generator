# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_156`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_156/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [27–29], lower_priority='Action_ZoneBlock' annotated_start=29, effective_Action_ZoneBlock_start=30.
> - Action 'Action_ZoneBlock' range [29-84] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-96] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-75] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-64] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [47-54] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-109] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-85] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [88-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-87] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-45] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [27-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-39] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [29-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-106] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-70] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-83] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [86-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [27-44] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [11-42] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [45-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [51-54] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '15' starts at frame 55, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [55-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [55-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-112] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-78] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-88] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-75] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-177] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [75-120] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-103] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-119] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-124] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-159] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-207] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-165] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-141] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-199] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-166] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-174] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-166] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-210] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-178] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-193] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '41' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.