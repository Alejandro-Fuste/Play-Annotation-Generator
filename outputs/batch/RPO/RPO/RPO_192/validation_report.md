# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_192`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_192/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (LT) duration 95 frames exceeds threshold 90 frames [start=58, end=152].
> - Validation warning: Action 'Action_ZoneBlock' for track '8' (LG) duration 95 frames exceeds threshold 90 frames [start=58, end=152].
> - Action 'Action_None' range [57-75] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-113] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-118] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-146] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [138-142] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [147-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-77] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-111] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-142] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-189] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 57, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [57-57] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-71] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-83] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-103] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-74] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-161] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-65] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-128] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-46] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-70] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-89] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-100] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-146] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-168] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-183] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-190] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-184] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-199] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-239] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-204] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-217] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-229] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.