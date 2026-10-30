# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_82`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 165: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [43-91] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_KickBall' range [43-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-84] for track '1' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-127] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-141] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-75] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-82] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-150] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-101] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-121] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-74] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-57] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-92] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-116] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-116] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-136] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' for track '10' starts at frame 47, but the player has no visible bounding box on this frame.
> - Action 'Action_BlockKick' range [47-47] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [53-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-103] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-128] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-81] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-78] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-105] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-53] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-20] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-34] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-27] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-136] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [84-96] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-143] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-150] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-102] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-98] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-150] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [115-150] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-150] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-150] for track '29' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.