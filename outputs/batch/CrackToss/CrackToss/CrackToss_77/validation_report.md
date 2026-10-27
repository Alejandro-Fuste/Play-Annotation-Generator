# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_77`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_77/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 155: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 156: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 156: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - Row 156: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_CrackBlock' range [93-132] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-225] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-130] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-212] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-212] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-225] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-171] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-209] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-215] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-223] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-197] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [93-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-225] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-172] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-225] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-225] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [122-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-182] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-225] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-225] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [122-168] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-201] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-147] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-225] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-225] for track '25' has 3 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.