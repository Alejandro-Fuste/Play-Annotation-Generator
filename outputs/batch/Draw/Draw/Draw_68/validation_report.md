# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_68`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 15 |
| Player Tracks | 15 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [27–41], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=42.
> - Action 'Action_PassBlock' range [30-146] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [101-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [132-135] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [115-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-86] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-146] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [27-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-121] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [136-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-48] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [49-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [82-165] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [167-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '14' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.