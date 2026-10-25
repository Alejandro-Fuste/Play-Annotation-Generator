# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_47`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [60–79], lower_priority='Action_RunBlock' annotated_start=66, effective_Action_RunBlock_start=80.
> - Action 'Action_None' range [198-233] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-195] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [66-115] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-221] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.