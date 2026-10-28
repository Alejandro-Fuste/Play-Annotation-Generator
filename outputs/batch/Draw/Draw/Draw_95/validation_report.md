# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_95`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PassBlock' range [22-38] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [42-77] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-145] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-88] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-56] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-69] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-83] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-33] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-45] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-191] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-83] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [39-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [77-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [217-224] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-248] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-47] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-77] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-261] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-165] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-275] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [280-319] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-167] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-213] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-272] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-291] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-381] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [383-389] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-382] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-366] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-378] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '31' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.