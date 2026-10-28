# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_53`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 109 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [40–55], lower_priority='Action_PassBlock' annotated_start=43, effective_Action_PassBlock_start=56.
> - Action 'Action_None' range [40-104] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-111] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-116] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-169] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-147] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-96] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [105-111] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [115-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [198-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-131] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '9' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [40-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-190] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-133] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-168] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-103] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [44-83] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [85-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-181] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-83] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-95] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-170] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [174-177] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [40-55] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [43-53] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-89] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-133] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-147] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-71] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-84] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-79] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-117] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-188] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-115] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-171] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-147] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-159] for track '31' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.