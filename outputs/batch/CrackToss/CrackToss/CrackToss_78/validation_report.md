# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_78`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
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
> - Row 158: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 158: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=111, end=38. Clamping end to start.
> - Action 'Action_None' range [76-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-225] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [79-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-112] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-144] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-223] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [79-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-225] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-225] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-225] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-189] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-161] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-225] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [111-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [79-148] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-38] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-225] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-225] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-225] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-225] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-197] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-225] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-225] for track '29' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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