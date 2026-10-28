# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_51`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_51/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [46–62], lower_priority='Action_PassBlock' annotated_start=49, effective_Action_PassBlock_start=63.
> - Action 'Action_None' range [46-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-190] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-198] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-136] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-299] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-263] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-182] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-195] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-246] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-299] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-139] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-160] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-151] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-248] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [66-152] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [154-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [171-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-189] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [49-85] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-127] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-191] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-190] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-199] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-299] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-271] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '35' has 1 frames without a visible bounding box.
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