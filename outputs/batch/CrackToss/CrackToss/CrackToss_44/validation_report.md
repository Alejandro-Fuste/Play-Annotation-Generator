# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_44`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 90: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [81-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-175] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [84-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [95-112] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-120] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [81-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-112] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-121] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-5] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [92-122] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-165] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-110] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-111] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-112] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-175] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [97-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-110] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-110] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-111] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-175] for track '26' has 2 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.