# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_112`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_112/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 226: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '11' has invalid range: start=20, end=19. Clamping end to start.
> - Action 'Action_None' range [17-94] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [98-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-198] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-79] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-93] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-77] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-137] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-75] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-159] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [67-80] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [84-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [178-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [20-74] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-139] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [17-19] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-82] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-239] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [85-107] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [86-101] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-103] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-225] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-188] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-219] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-239] for track '27' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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