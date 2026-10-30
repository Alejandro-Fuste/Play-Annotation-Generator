# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_125`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [33-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-58] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [41-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-120] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-63] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '7' starts at frame 33, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [33-33] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [21-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-109] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-68] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-43] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-118] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-41] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-11] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-32] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-103] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-53] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-58] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-51] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-62] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-116] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [81-117] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-89] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-120] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-99] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-106] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-119] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-112] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '30' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.