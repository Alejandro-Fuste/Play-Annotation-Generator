# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_40`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 82: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [14-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-32] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-108] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-44] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-54] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-119] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-43] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-58] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-120] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-86] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-97] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-88] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-98] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-40] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-120] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [14-24] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [14-75] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-119] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-87] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-32] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-79] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [53-57] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-105] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-82] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-112] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-119] for track '25' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.