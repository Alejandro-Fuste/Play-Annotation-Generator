# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_92`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_92/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 184: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [43–57], lower_priority='Action_PassBlock' annotated_start=46, effective_Action_PassBlock_start=58.
> - Action 'Action_None' range [43-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-238] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-54] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-118] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-96] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [95-223] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-108] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [88-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-124] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-212] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-203] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-135] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-207] for track '33' has 1 frames without a visible bounding box.
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