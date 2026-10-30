# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_119`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_119/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 240: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [50-64] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-140] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-149] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-130] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-63] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-90] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-49] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 50, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [50-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-49] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-35] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-81] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-113] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [55-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 65, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [65-73] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-149] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-57] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-20] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-49] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-111] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-106] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-105] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-105] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-116] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.