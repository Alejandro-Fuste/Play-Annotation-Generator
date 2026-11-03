# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_27`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_27/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 142 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 30: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [12–24], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=25.
> - Action 'Action_None' range [12-34] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-58] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-108] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-135] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-173] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-34] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-52] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-58] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-68] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-71] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-89] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-122] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [129-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SellOut' range [54-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [77-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-80] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-37] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-40] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-58] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-86] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-45] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-55] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-66] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-110] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-164] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-121] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-177] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-58] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-84] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-188] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-198] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-34] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-200] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-210] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [12-42] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-34] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-58] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-182] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [12-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [12-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [15-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [56-58] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-34] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-79] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [84-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-124] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-71] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-87] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-164] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-193] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-140] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-158] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '36' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.