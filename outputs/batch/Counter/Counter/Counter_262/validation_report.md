# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_262`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_262/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 526: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '4' (DE2) duration 92 frames exceeds threshold 90 frames [start=34, end=125].
> - Validation warning: Action 'Action_PullBlock' for track '11' (LG) duration 92 frames exceeds threshold 90 frames [start=34, end=125].
> - Validation warning: Action 'Action_DownBlock' for track '13' (C) duration 92 frames exceeds threshold 90 frames [start=34, end=125].
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [31–46], lower_priority='Action_DownBlock' annotated_start=34, effective_Action_DownBlock_start=47.
> - Action 'Action_None' range [31-66] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-169] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-145] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [152-181] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-70] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-70] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-157] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [34-54] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [56-125] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-141] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-194] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-208] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-53] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-56] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-101] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [34-49] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [53-58] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [60-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [47-56] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [66-105] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-135] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-141] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [35-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-141] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-193] for track '23' has 1 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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