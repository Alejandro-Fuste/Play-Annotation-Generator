# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_125`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 127 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (LT) duration 116 frames exceeds threshold 90 frames [start=34, end=149].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (C) duration 116 frames exceeds threshold 90 frames [start=34, end=149].
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [31–39], lower_priority='Action_ZoneBlock' annotated_start=34, effective_Action_ZoneBlock_start=40.
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 116 frames exceeds threshold 90 frames [start=34, end=149].
> - Action 'Action_None' range [31-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-177] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-194] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-74] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-124] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-206] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-114] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-159] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-109] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [31-57] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [53-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [80-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [112-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-36] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [38-39] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [43-44] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [40-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [60-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [137-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-52] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-117] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-72] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-96] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [99-107] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-174] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-105] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-117] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-112] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-147] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-153] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-203] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-204] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '44' has 1 frames without a visible bounding box.
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
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.