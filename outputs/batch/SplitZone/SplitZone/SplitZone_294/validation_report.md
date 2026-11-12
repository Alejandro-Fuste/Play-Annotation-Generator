# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_294`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_294/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '6' has invalid range: start=85, end=62. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '20' has invalid range: start=85, end=63. Clamping end to start.
> - Action 'Action_None' range [27-139] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-144] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-74] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-110] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [113-205] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-83] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [86-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [31-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [83-84] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-65] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-62] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [64-233] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-66] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-74] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-223] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-166] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-77] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-179] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-203] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-203] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [27-36] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-50] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [53-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-86] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-234] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-56] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-63] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-75] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-181] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-232] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-75] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-86] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-110] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-224] for track '27' has 1 frames without a visible bounding box.
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