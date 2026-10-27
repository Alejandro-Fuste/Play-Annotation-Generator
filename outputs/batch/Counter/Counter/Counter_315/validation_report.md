# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_315`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_315/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 632: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [43–58], lower_priority='Action_DownBlock' annotated_start=46, effective_Action_DownBlock_start=59.
> - Action 'Action_None' range [43-89] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-236] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-152] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-226] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-109] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-121] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-219] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-166] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-223] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-124] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [97-110] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-122] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-213] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-111] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [46-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [59-89] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-96] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-218] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-219] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-158] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-229] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-155] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-193] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-228] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '34' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.