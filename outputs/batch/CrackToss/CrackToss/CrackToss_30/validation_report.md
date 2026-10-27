# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_30`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 298 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '0' (TE) duration 107 frames exceeds threshold 90 frames [start=34, end=140].
> - Segment 'Action_CrackBlock' for track '3' has invalid range: start=34, end=30. Clamping end to start.
> - Validation warning: Action 'Action_PullBlock' for track '9' (LT) duration 177 frames exceeds threshold 90 frames [start=34, end=210].
> - Action 'Action_PullBlock' range [34-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [92-98] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [126-140] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-114] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-259] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-208] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-287] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-70] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-281] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-146] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-174] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-298] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-136] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [34-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [154-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [158-172] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [176-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [182-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [204-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-283] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [31-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-164] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-280] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-298] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-46] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-281] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-277] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-298] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [31-54] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-56] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-144] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-96] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-148] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-253] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-247] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-267] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '29' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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