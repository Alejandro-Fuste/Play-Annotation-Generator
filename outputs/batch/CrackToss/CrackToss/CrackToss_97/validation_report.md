# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_97`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_97/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 196: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '10' (RB2) duration 93 frames exceeds threshold 90 frames [start=40, end=132].
> - Segment 'Action_Toss' for track '15' has invalid range: start=48, end=47. Clamping end to start.
> - Action 'Action_None' range [37-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-164] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [70-139] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [147-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-79] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-142] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-156] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-52] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [40-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-174] for track '11' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [37-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-134] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-175] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 42, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [42-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-24] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [40-129] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-175] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-74] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-97] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-107] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-175] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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