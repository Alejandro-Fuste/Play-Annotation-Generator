# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_83`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_83/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_KickBall' for track '0' starts at frame 55, but the player has no visible bounding box on this frame.
> - Action 'Action_KickBall' range [55-59] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-126] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-198] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [59-74] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-59] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-154] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [55-210] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '11' starts at frame 55, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [55-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-74] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-92] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-35] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-8] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-54] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [58-63] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-159] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-179] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-29] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-189] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-102] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-117] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-72] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-78] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-108] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-128] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-84] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-126] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-179] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-108] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-195] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-138] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '27' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.