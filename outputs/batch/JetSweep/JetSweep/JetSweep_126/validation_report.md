# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_126`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_126/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (RT) duration 108 frames exceeds threshold 90 frames [start=16, end=123].
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [15–26], lower_priority='Action_ZoneBlock' annotated_start=16, effective_Action_ZoneBlock_start=27.
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 96 frames exceeds threshold 90 frames [start=16, end=111].
> - Validation warning: Action 'Action_LeadBlock' for track '12' (RB) duration 108 frames exceeds threshold 90 frames [start=16, end=123].
> - Validation warning: Action 'Action_ZoneBlock' for track '14' (RG) duration 108 frames exceeds threshold 90 frames [start=16, end=123].
> - Action 'Action_None' range [15-73] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-47] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-95] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-180] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-38] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [16-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [56-60] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [62-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-24] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-20] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-105] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [113-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-143] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [7-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [45-72] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [76-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-111] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-89] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-180] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-134] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-154] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-165] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.