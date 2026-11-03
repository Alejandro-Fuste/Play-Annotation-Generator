# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_11`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_PassBlock' annotated_start=13, effective_Action_PassBlock_start=25.
> - Action 'Action_None' range [10-73] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [10-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-28] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-51] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-61] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-82] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-117] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-88] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-57] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-65] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-81] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-123] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-150] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [25-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [120-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [144-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-58] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-118] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' for track '12' starts at frame 68, but the player has no visible bounding box on this frame.
> - Action 'Action_ThrowPass' range [68-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-150] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-98] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [119-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-91] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [101-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-45] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-60] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-36] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-98] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-150] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [13-55] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-30] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-37] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-69] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [71-78] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-75] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-122] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-150] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-150] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.