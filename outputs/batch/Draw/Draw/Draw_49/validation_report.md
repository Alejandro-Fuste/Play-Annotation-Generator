# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_49`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 75 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [38–52], lower_priority='Action_PassBlock' annotated_start=41, effective_Action_PassBlock_start=53.
> - Action 'Action_None' range [38-239] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [38-92] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-226] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-211] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [87-223] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [226-235] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-112] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-120] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-191] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-90] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-149] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-185] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.