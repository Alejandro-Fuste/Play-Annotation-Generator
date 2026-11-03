# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_153`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_153/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-57] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [16-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [16-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-136] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_RunOutRoute' range [16-65] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-131] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-148] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-97] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-174] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-60] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-107] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [109-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-46] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-173] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [178-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [11-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-55] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-47] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-46] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-138] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-71] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-79] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-157] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-83] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-88] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-94] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-98] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-105] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-78] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-101] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-116] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-124] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-148] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-168] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-180] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-140] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-148] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-174] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-147] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-147] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-180] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-180] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-163] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-174] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-177] for track '41' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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